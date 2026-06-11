# DISCORD LIBRARIES
import discord
from discord import Embed, File
from discord.ext import commands, tasks
from discord.ext.commands import cooldown, BucketType
# EXTERNAL LIBRARIES
import random, enum
import sqlite3
# JUDIE LIBRARIES
from Utilities import HelperClass, check_channel


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
        - ctx: discord.ext.commands.Context
            the context provided with the message to check
        - expectFail: bool - False by default
            a bool representing whether the command was called with
            the expectation of it failing (changes error message)

    Returns:
        bool: success of the check operation; 
            True = success (user is registered)
    """
    async def predicate(ctx):
        db = sqlite3.connect("main.sqlite")
        cursor = db.cursor()
        cursor.execute("SELECT user_id FROM users WHERE discord_id = ?", [ctx.author.id])
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
                title=f"Error #404 - User {str(ctx.author.display_name)} not registered!",
                text="Please register before playing! (-register)",
                footer="Contact eisritter if you encounter any issues!"
            )
        else:
            embed = await HelperClass.createEmbed(
                title=f"Error - User {str(ctx.author.display_name)} is already registered!",
                text="If this is not the case, please contact **eisritter**!",
                footer="Enjoy your time!"
            )
        await ctx.send(embed=embed)
        print(f"[REGISTRATION ERROR] User registration state does not match expectation.")
    return commands.check(predicate)


def check_deployment(_type: str):
    """
        Supported types by default: 'DEBUG', 'BUILD'. 
        Any unsupported value will automatically lead to failure.
    """
    async def predicate(ctx):
        client = ctx.bot
        return client.config.deployment == _type
    return commands.check(predicate)


def check_permission(expected_role: RoleHierarchy) -> bool:
    """
    """
    async def predicate(ctx):
        expected_priority = expected_role
        try:
            author = ctx.author
            print(f"Evaluating access of user {ctx.author.display_name}.")
        except:
            print(f"[Error] Invalid type of author presented to permission checker. Expecting 'discord.member.Member', got {type(ctx.author)}")
            await ctx.send(f"Error checking permissions for user")
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
        await ctx.send(f"Insufficient permissions (Internal role: {highest_role}) to use this command (expecting {expected_role} or higher).")
        return False
    return commands.check(predicate)
        

class AccountManager(commands.Cog):
    static_client = None
    """A stop-gap for the permissions system. Please use the [AccountManager-instance].client variable for all intents and purposes."""

    def __init__(self, client):
        self.client = client
        client.accountManager = self
        AccountManager.static_client = client

    deletionPromptMsgIDs = {}
    """
    A dictionary linking users to the bot's prompt to confirm data deletion.
    """
    deleteRequestMessages = {}
    """
    A dictionary linking users to their message requesting data deletion.
    """

    # HELPER FUNCTIONS

    async def getUserID(self, discordID, cursor):
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
        cursor.execute("SELECT user_id FROM users WHERE discord_id=?", [discordID])
        uID = cursor.fetchone()
        return uID if uID is None else uID[0]

    # COMMANDS & RELATED

    @commands.command()
    @commands.check(check_channel)
    @check_user(expectFail=True)
    async def register(self, ctx):
        """
        Registers a user to the database.

        Parameters:
            - ctx: discord.ext.commands.Context
                the context provided with the message to check

        Returns:
            Nothing, why are you looking? It's a command.
        """

        db = sqlite3.connect("main.sqlite")
        cursor = db.cursor()
        discordID = str(ctx.author.id)

        cursor.execute("INSERT INTO users (discord_id) VALUES (?)", [discordID])
        uID = await self.getUserID(discordID, cursor)
        tables = [ 
            "oialt", "oialt_harem", "stabby_mikes", "the_boys", "li_potential", 
            "eternum", "eternum_harem", "homies", "side_girls", "creatures"
        ]

        for table in tables:
            cursor.execute("INSERT INTO %s (user_id) VALUES (?)" % table, [uID])

        db.commit()

        embed = await HelperClass.createEmbed(
            title="Great Success!", 
            text=f"user {ctx.author.mention} was successfully registered to the database!", 
            footer="Welcome aboard!"
            )
        await ctx.send(embed=embed)

        cursor.close()
        db.close()

    @commands.command()
    @commands.check(check_channel)
    @check_user()
    async def deleteacc(self, ctx):
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
        discordID = str(ctx.author.id)

        uid = await self.getUserID(discordID=discordID, cursor=cursor)

        if uid is not None:
            msg = await ctx.message.reply("Are you sure you want to delete **all** your data?"
                                          "\nThis action is irreversible! (React to the checkmark to confirm. Ignore to cancel)")
            self.deleteRequestMessages.update({ctx.author: ctx.message})
            self.deletionPromptMsgIDs.update({msg.id: ctx.author})
            await msg.add_reaction('✅')

            # Add scheduling of timeout event here

        cursor.close()
        db.close()

    async def removeUserFromDB(self, ctx, discord_id):
        db = sqlite3.connect("main.sqlite")
        cursor = db.cursor()

        uid = await self.getUserID(discord_id, cursor)
        if uid is None:
            await ctx.send(f"User {discord_id} is not registered!")
            return

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

        await ctx.send(f"Successfully removed user {discord_id} from Judie's database!")

        cursor.close()
        db.close()

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        """
        A function called when any reaction is added to any message within the bot's scope.
        ---
        Used to confirm the deletion of user accounts. 
        Worthwile warning, ANY reaction would trigger this, the only counter is to ignore the request if the user changed their mind.
        """
        # If no message marked for deletion, ignore
        if len(self.deleteRequestMessages) == 0:
            return

        if payload.message_id in self.deletionPromptMsgIDs.keys():
            db = sqlite3.connect("main.sqlite")
            cursor = db.cursor()
            author = self.deletionPromptMsgIDs.get(payload.message_id)

            if author.id == payload.user_id:
                discordID = str(author.id)

                uid = await self.getUserID(discordID=discordID, cursor=cursor)
                user_name = str(author.display_name)
                request_message = self.deleteRequestMessages.get(author);
                channel = self.client.get_channel(request_message.channel.id)


                tables = ['users', 'oialt', 'oialt_harem', 'stabby_mikes', 'the_boys', 'li_potential', 
                          'eternum', 'eternum_harem', 'homies', 'side_girls', 'creatures']
                for table in tables:
                    cursor.execute("DELETE FROM %s WHERE user_id = ?" % table, [uid])

                await channel.send(f"User {user_name} has been successfully removed from the database."
                                   f" Have a great time! :wave:")
                await request_message.add_reaction('✅')

                db.commit()

                self.deleteRequestMessages.pop(author)
                self.deletionPromptMsgIDs.pop(payload.message_id)

            cursor.close()
            db.close()

    @commands.command()
    @commands.check(check_channel)
    @commands.check(check_permission)
    @check_permission(RoleHierarchy.MODERATOR)
    async def portProgress(self, ctx, oldUserID, newUserID):
        pass

    @commands.command()
    async def update(self, ctx):
        """
        Relic from times where the dev didn't know anything about SQL;
        Does nothing but send an easter egg message now :D
        """
        await ctx.send("This command is now obsolete :)")

    @commands.command()
    @commands.check(check_permission)
    @check_permission(RoleHierarchy.MODERATOR)          # Command available to master botter and higher in the hierarchy.
    async def forceDelete(self, ctx, discord_id):
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
            await self.removeUserFromDB(ctx, discord_id)
        except:
            await ctx.send("Unsafe input, please only supply discord ID's as integers to this command!")


def setup(client):
    client.add_cog(AccountManager(client))
