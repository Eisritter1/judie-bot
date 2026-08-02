# DISCORD LIBRARIES
import discord
from discord import app_commands
from discord.ext import commands
from discord.ext.commands import Bot
# EXTERNAL LIBRARIES
import enum, os
import sqlite3
from dotenv import load_dotenv
# JUDIE LIBRARIES
from Utilities import HelperClass, check_channel
from AccountManagementViews import DeleteAccView, GiveCharacterView


class RoleHierarchy(enum.Enum):
    MEMBER = 0
    MASTER_BOTTER = 1
    MODERATOR = 2
    DEV = 3

    def to_hierarchy(role_id):
        client = AccountManager.static_client
        if client is None:
            print("Invalid client")
            return RoleHierarchy.MEMBER

        if int(role_id) == int(client.config.admin_role):
            return RoleHierarchy.DEV
        
        if int(role_id) == int(client.config.mod_role):
            return RoleHierarchy.MODERATOR

        if int(role_id) == int(client.config.maintainer_role):
            return RoleHierarchy.MASTER_BOTTER
        
        return RoleHierarchy.MEMBER

    def compareTo(self, other) -> bool:
        """
        Checks whether a role passes the priority check over the other role.\n
        Should absolutely be used as roleToCheck.check(expectedPriority)!\n
        checking the other way around may cause issues (access granting for inverse priority, 
        e.g. member check against admin, admin prio > member)

        @params
            - other: RoleHierarchy - a RoleHierarchy priority level the 'self' priority is to be checked against.
            Using any other object will automatically fail the test.
        """

        if isinstance(other, RoleHierarchy):
            # case universal access (no access restriction, or server admin)
            if other == RoleHierarchy.MEMBER or self == RoleHierarchy.DEV:
                return True

            if self == RoleHierarchy.MEMBER:
                return False                # only true if other == MEMBER -> see case above, hence no way to get access.

            # Master Botter lowest above Member -> only true if other == role
            if self == RoleHierarchy.MASTER_BOTTER:
                return other == RoleHierarchy.MASTER_BOTTER

            # Moderator 2nd highest -> only false if admin-only
            if self == RoleHierarchy.MODERATOR:
                return other != RoleHierarchy.DEV
        else:
            print("Invalid comparison object.")

def check_user(expectFail: bool = False):
    """
    Checks whether a user is registered to the system or not

    Parameters:
        - interaction: discord.Interaction
            the context provided with the message to check
        - expectFail: bool - False by default
            a bool representing whether the command was called with
            the expectation of it failing (changes error message)

    Returns:
        bool: success of the check operation; 
            True = success (user is registered)
    """
    async def predicate(interaction: discord.Interaction):
        return await AccountManager.verifyUser(interaction.user.id, interaction, expectFail)
    return app_commands.check(predicate)


def check_permission(expected_role: RoleHierarchy) -> bool:
    """
    """
    async def predicate(interaction: discord.Interaction):
        expected_priority = expected_role
        try:
            author = interaction.user
        except:
            print(f"[Error] Invalid type of author presented to permission checker. Expecting 'discord.member.Member', got {type(author)}")
            await interaction.response.send_message(f"Error checking permissions for user", ephemeral=True)
            return False

        highest_role = None
        for role in author.roles:
            user_priority = RoleHierarchy.to_hierarchy(role.id)
            if highest_role is None or user_priority.compareTo(highest_role):
                highest_role = user_priority

            # if any role passes the access priority check, return success
            if user_priority.compareTo(expected_priority):
                (f"User access granted")
                return True

        # if no role passes the access priority check, return failure.
        await interaction.response.send_message(f"Insufficient permissions (Internal role: {highest_role}) to use this command (expecting {expected_role} or higher).", ephemeral=True)
        return False
    return app_commands.check(predicate)
        

load_dotenv()
GUILD = discord.Object(id=os.getenv("GUILD"))

class AccountManager(commands.Cog):
    static_client = None
    """A stop-gap for the permissions system. Please use the [AccountManager-instance].client variable for all intents and purposes."""

    def __init__(self, client):
        self.client: Bot = client
        client.accountManager = self
        AccountManager.static_client = client
        self.db_path = client.db_path

    tables = [ 
        "oialt", "oialt_harem", "stabby_mikes", "the_boys", "li_potential", 
        "eternum", "eternum_harem", "homies", "side_girls", "creatures"
    ]
    """
    A list of all table names in judie's database (except users).
    """

    # HELPER FUNCTIONS

    async def getUserID(self, discordID: str):
        """
        Fetches a user's ID in the database paired to their discord ID.

        Parameters:
            - discordID: int
                the user's discord ID
            - cursor: sqlite3.Connection.Cursor
                a database cursor object connected to the active DB

        Returns:
            int: user's ID if any is found
            None if no uID found
        """
        db = sqlite3.connect(self.db_path)
        cursor = db.cursor()

        cursor.execute("SELECT user_id FROM users WHERE discord_id=?", [discordID])
        uID = cursor.fetchone()

        cursor.close()
        db.close()
        return uID if uID is None else uID[0]

    async def removeUserFromDB(self, discord_id: int) -> bool:
        db = sqlite3.connect("main.sqlite")
        cursor = db.cursor()

        uid = await self.getUserID(discord_id)
        if uid is None:
            return False

        # check if user in DB
        cursor.execute("SELECT * FROM users WHERE user_id = ?", [uid])
        if cursor.fetchone():
            # if so delete all related entries
            for table in AccountManager.tables:
                cursor.execute("DELETE FROM %s WHERE user_id = ?" % table, [uid])
            
            cursor.execute("DELETE FROM users WHERE discord_id=?", [discord_id])    
            db.commit()

        print(f"[DELETION_NOTICE] User {discord_id} removed from DB!")

        cursor.close()
        db.close()
        return True

    async def transferProgress(self, source_uid, target_uid) -> bool:
        db = sqlite3.connect("main.sqlite")
        cursor = db.cursor()

        try:
            for table in AccountManager.tables:
                print(f"Inspecting table {table}.")

                cursor.execute("PRAGMA table_info(%s)" % table)
                results = cursor.fetchall()
                columns = [row[1] for row in results]
                print(columns)

                # get entries for both users
                cursor.execute("SELECT * FROM %s WHERE user_id=?" % table, [source_uid])
                source = cursor.fetchone()
                print(f"Source: {source}")

                cursor.execute("SELECT * FROM %s WHERE user_id=?" % table, [target_uid])
                target = cursor.fetchone()
                print(f"Target: {target}")

                # for table structured [uid, [values], last_collectible], ignore the first and last.
                values = [target[0]]
                for i in range(1, len(source)-1):
                    val = bool(source[i]) or bool(target[i])        # fair merge: A OR B -> any of A or B True => A|B = True
                    values.append(val)
                    print(f"{table}, {columns[i]}, {val}, {target_uid}")
                    cursor.execute("UPDATE %s SET %s=? WHERE user_id=?" % (table, columns[i]), [int(val), target_uid])

                print(f"Output: {values}")


                print("--------------------")

        except Exception as e:
            print(f"[Error migrating table {table} from {source_uid} to {target_uid}]: {e}")
            return False
        
        db.commit()

        cursor.close()
        db.close()
        return True

    async def receiveDiscordIDFromInput(interaction: discord.Interaction, id: str) -> int:
        output = -1
        try:
            output = int(id)
        except Exception as e:
            output = -1
            await interaction.response.send_message(f"[Error] Invalid input. Please input a number corresponding to a discord ID.", ephemeral=True)

        return output

    async def verifyUser(discord_id: int, interaction: discord.Interaction, expectFail: bool) -> bool:
        db = sqlite3.connect("main.sqlite")
        cursor = db.cursor()
        cursor.execute("SELECT user_id FROM users WHERE discord_id = ?", [discord_id])
        userIDCheck = cursor.fetchone()
        cursor.close()
        db.close()

        is_registered = userIDCheck is not None

        # XOR operation. if expect failure you want not_registered, otherwise you don't want not_registered.
        if is_registered ^ expectFail:
            return True  # allow command to run

        # Optional: Send feedback before raising error
        if not is_registered and not expectFail:
            embed = await HelperClass.createEmbed(
                title=f"Error #404 - User {str(interaction.user.display_name) if discord_id == interaction.user.id else discord_id} not registered!",
                text="Please register before playing! (-register)",
                footer="Contact eisritter if you encounter any issues!"
            )
        else:
            embed = await HelperClass.createEmbed(
                title=f"Error - User {str(interaction.user.display_name) if discord_id == interaction.user.id else discord_id} is already registered!",
                text="If this is not the case, please contact **eisritter**!",
                footer="Enjoy your time!"
            )
        await interaction.response.send_message(embed=embed)
        print(f"[REGISTRATION ERROR] User registration state does not match expectation.")
        return False
            

    # COMMANDS & RELATED

    @app_commands.guilds(GUILD)
    @app_commands.command(name="register", description="Sign up for Judie's systems! Only necessary for using egf and ogf.")
    @app_commands.check(check_channel)
    @check_user(expectFail=True)
    async def register(self, interaction: discord.Interaction):
        """
        Registers a user to the database.

        Parameters:
            - ctx: discord.ext.commands.Context
                the context provided with the message to check

        Returns:
            Nothing, why are you looking? It's a command.
        """

        db = sqlite3.connect(self.db_path)
        cursor = db.cursor()
        discordID = str(interaction.user.id)

        cursor.execute("INSERT INTO users (discord_id) VALUES (?)", [discordID])
        db.commit()

        uID = await self.getUserID(discordID)

        for table in AccountManager.tables:
            print(f"Inserting into table {table} value {uID}.")
            cursor.execute("INSERT INTO %s (user_id) VALUES (?)" % table, [uID])

        db.commit()

        embed = await HelperClass.createEmbed(
            title="Great Success!", 
            text=f"user {interaction.user.mention} was successfully registered to the database!", 
            footer="Welcome aboard!"
            )
        await interaction.response.send_message(embed=embed)

        cursor.close()
        db.close()

    @app_commands.guilds(GUILD)
    @app_commands.command(name="delete_account", description="Request the deletion of your account and its associated data. Irreversible action once completed.")
    @app_commands.check(check_channel)
    @check_user()
    async def deleteacc(self, interaction: discord.Interaction):
        """
        Requests deletion of an account.

        Parameters:
            - ctx: discord.ext.commands.Context
                the context provided with the message to check

        Returns:
            Nothing, why are you looking? This is a command.
        """
        discordID = str(interaction.user.id)

        uid = await self.getUserID(discordID=discordID)

        if uid is not None:
            view = DeleteAccView(interaction.user, self)
            embed = discord.Embed(
                title=f"Request to delete {interaction.user.display_name}'s account.", 
                description="__**This action is irreversible!**__ (Press 'CONFIRM' to proceed, or 'CANCEL' to cancel." \
                    "\nThis message will time out after 3 minutes.)",
                color=HelperClass.eternumBlue
            )
            await interaction.response.send_message(embed=embed, view=view)
            view.message = await interaction.original_response()


    @app_commands.guilds(GUILD)
    @app_commands.command(name="port_progress", description="Transfer a user's progress to another user's database, preserving existing progress.")
    @app_commands.check(check_channel)
    @app_commands.check(check_permission)
    @check_permission(RoleHierarchy.MASTER_BOTTER)
    async def port_progress(self, interaction: discord.Interaction, source_user_id: str, target_user_id: str):
        source_user_duid = await AccountManager.receiveDiscordIDFromInput(interaction, source_user_id)
        # return if value invalid (error msg in function already.)
        if source_user_duid == -1:
            return

        target_user_duid = await AccountManager.receiveDiscordIDFromInput(interaction, target_user_id)
        # return if value invalid (error msg in function already.)
        if target_user_duid == -1:
            return
        
        # make sure both users are registered & get their uids.
        # exit early if either user isn't registered.
        if source_user_duid == target_user_duid:
            await interaction.response.send_message(f"[Error] Attempting to migrate progress to and from the same user.", ephemeral=True)
            return

        source_uid = await self.getUserID(source_user_duid)
        if source_uid is None:
            await interaction.response.send_message(f"[Error] Source user {source_user_id} is not registered to Judie's DB.", ephemeral=True)
            return

        target_uid = await self.getUserID(target_user_duid)
        if target_uid is None:
            await interaction.response.send_message(f"[Error] Target user {target_user_id} is not registered to Judie's DB.", ephemeral=True)
            return
        
        # feed the uids to transferProgress.
        success = await self.transferProgress(source_uid, target_uid)

        title = "Success!" if success else "Error!"
        desc = f"Successfully transferred progress from user {source_user_id} to {target_user_id}." if success \
            else f"An unexpected error occurred transferring progress from user {source_user_id} to {target_user_id}."
        await interaction.response.send_message(embed=discord.Embed(title=title, description=desc, color=HelperClass.eternumBlue))


    @app_commands.guilds(GUILD)
    @app_commands.command(name="give_character", description="Grants a user a specific collectible 'free of charge'.")
    @app_commands.check(check_channel)
    @app_commands.check(check_permission)
    @check_permission(RoleHierarchy.MASTER_BOTTER)
    async def give_character(self, interaction: discord.Interaction, discord_id: str):
        discordID = await AccountManager.receiveDiscordIDFromInput(interaction, discord_id)

        uid = await self.getUserID(discordID=discordID)

        if uid is not None:
            user = await self.client.fetch_user(discordID)

            view = GiveCharacterView(user)
            embed = discord.Embed(
                title=f"Selecting a character to give to  {user.display_name}.", 
                description="Select the game of the character you want to grant:",
                color=HelperClass.eternumBlue
            )
            await interaction.response.send_message(embed=embed, view=view)
            view.message = await interaction.original_response()

    async def setup(client):
        await client.add_cog(AccountManager(client))
        