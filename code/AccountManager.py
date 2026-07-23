# DISCORD LIBRARIES
import discord
from discord import app_commands
from discord.ext import commands
# EXTERNAL LIBRARIES
import enum, os
import sqlite3
from dotenv import load_dotenv
# JUDIE LIBRARIES
from Utilities import HelperClass, check_channel
from AccountManagementViews import DeleteAccView


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

        if int(role_id) == int(client.config.cari_role):
            return RoleHierarchy.DEV
        
        if int(role_id) == int(client.config.mod_role):
            return RoleHierarchy.MODERATOR

        if int(role_id) == int(client.config.botter_role):
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
        db = sqlite3.connect("main.sqlite")
        cursor = db.cursor()
        cursor.execute("SELECT user_id FROM users WHERE discord_id = ?", [interaction.user.id])
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
                title=f"Error #404 - User {str(interaction.user.display_name)} not registered!",
                text="Please register before playing! (-register)",
                footer="Contact eisritter if you encounter any issues!"
            )
        else:
            embed = await HelperClass.createEmbed(
                title=f"Error - User {str(interaction.user.display_name)} is already registered!",
                text="If this is not the case, please contact **eisritter**!",
                footer="Enjoy your time!"
            )
        await interaction.response.send_message(embed=embed)
        print(f"[REGISTRATION ERROR] User registration state does not match expectation.")
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
        self.client = client
        client.accountManager = self
        AccountManager.static_client = client
        self.db_path = client.db_path

    deletionPromptMsgIDs = {}
    """
    A dictionary linking users to the bot's prompt to confirm data deletion.
    """
    deleteRequestMessages = {}
    """
    A dictionary linking users to their message requesting data deletion.
    """

    # HELPER FUNCTIONS

    async def getUserID(self, discordID):
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
        uID = await self.getUserID(discordID)
        tables = [ 
            "oialt", "oialt_harem", "stabby_mikes", "the_boys", "li_potential", 
            "eternum", "eternum_harem", "homies", "side_girls", "creatures"
        ]

        for table in tables:
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

        db = sqlite3.connect("main.sqlite")
        cursor = db.cursor()
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

        cursor.close()
        db.close()

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
            tables = [ 
                "oialt", "oialt_harem", "stabby_mikes", "the_boys", "li_potential", 
                "eternum", "eternum_harem", "homies", "side_girls", "creatures", "users"
            ]

            for table in tables:
                cursor.execute("DELETE FROM %s WHERE user_id = ?" % table, [uid])
            db.commit()

        print(f"[DELETION_NOTICE] User {discord_id} removed from DB!")

        cursor.close()
        db.close()
        return True

    @app_commands.guilds(GUILD)
    @app_commands.command(name="port_progress", description="Transfer a user's progress to another user's database, preserving existing progress.")
    @app_commands.check(check_channel)
    @app_commands.check(check_permission)
    @check_permission(RoleHierarchy.MODERATOR)
    async def port_progress(self, interaction: discord.Interaction, old_user_id: int, new_user_id: int):
        pass

    @app_commands.guilds(GUILD)
    @app_commands.command(name="force_delete", description="Forcibly removes a registered user from the database. Command available to moderators only.")
    @app_commands.check(check_permission)
    @check_permission(RoleHierarchy.MODERATOR)          # Command available to master botter and higher in the hierarchy.
    async def force_delete(self, interaction: discord.Interaction, discord_id: int):
        """
        [MOD ONLY] Deletes the data of a given user

        Parameters:
            - uid: int
                the user ID of the user whose data is to be obliterated.

        Returns:
            Nothing.
        """
        # SQL Injection prevention: Only accept discord_ids that can be converted to integers. 
        # invalid ctx would just result in a regular error.
        try:
            int(discord_id)
            success = await self.removeUserFromDB(interaction, discord_id)
            title = "Success!" if success else "Error!"
            description = f"Deleted account of user {discord_id}." if success else f"User {discord_id} is not registered to Judie's DB!"
            await interaction.response.send_message(embed=discord.Embed(title=title, description=description, color=HelperClass.eternumBlue))
        except:
            await interaction.response.send_message("Unsafe input, please only supply discord ID's as integers to this command!")


def setup(client):
    client.add_cog(AccountManager(client))
