# DISCORD LIBRARIES
import discord
from discord import Embed, File
from discord.ext import commands, tasks
from discord.ext.commands import cooldown, BucketType
# EXTERNAL LIBRARIES
import random
import sqlite3
# JUDIE LIBRARIES
from Utilities import HelperClass, check_channel


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

        if (is_registered and not expectFail) or (not is_registered and expectFail):
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

        raise commands.CheckFailure("User registration state does not match expectation.")
    return commands.check(predicate)


class AccountManager(commands.Cog):
    def __init__(self, client):
        self.client = client

    deletionPromptMsgIDs = {}
    """
    A dictionary linking users to the bot's prompt to confirm data deletion.
    """
    deleteRequestMessages = {}
    """
    A dictionary linking users to their message requesting data deletion.
    """
    usersRequestingDeletion = []
    """
    A list of users having requested deletion of their data.
    """

    # HELPER FUNCTIONS

    async def getUserID(discordID, cursor):
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
            self.deletionPromptMsgIDs.update({ctx.author: msg.id})
            self.usersRequestingDeletion.append(ctx.author)
            await msg.add_reaction('✅')

            # Add scheduling of timeout event here

        cursor.close()
        db.close()

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        # If no message marked for deletion, ignore
        if isinstance(self.deleteRequestMessages, str):
            return

        db = sqlite3.connect("main.sqlite")
        cursor = db.cursor()
        discordID = str(self.deleteRequestMessages.author.id)
        uid = await self.getUserID(discordID=discordID, cursor=cursor)
        oldID = None
        if uid is None:
            cursor.execute("SELECT user_id FROM usersnew WHERE discord_id = ?", [discordID])
            oldIDList = cursor.fetchone()
            oldID = oldIDList[0]
        user_name = str(self.deleteRequestMessages.author)
        channel = self.client.get_channel(self.deleteRequestMessages.channel.id)

        if self.deletionPromptMsgIDs == payload.message_id:
            if self.usersRequestingDeletion.id == payload.user_id:
                if uid is not None:
                    cursor.execute("DELETE FROM users WHERE user_id = ?", [uid])
                    cursor.execute("DELETE FROM oialt WHERE user_id=?", [uid])
                    cursor.execute("DELETE FROM oialt_harem WHERE user_id = ?", [uid])
                    cursor.execute("DELETE FROM stabby_mikes WHERE user_id = ?", [uid])
                    cursor.execute("DELETE FROM the_boys WHERE user_id = ?", [uid])
                    cursor.execute("DELETE FROM li_potential WHERE user_id = ?", [uid])
                    cursor.execute("DELETE FROM eternum WHERE user_id=?", [uid])
                    cursor.execute("DELETE FROM eternum_harem WHERE user_id=?", [uid])
                    cursor.execute("DELETE FROM homies WHERE user_id=?", [uid])
                    cursor.execute("DELETE FROM side_girls WHERE user_id=?", [uid])
                    cursor.execute("DELETE FROM creatures WHERE user_id=?", [uid])
                else:
                    cursor.execute("DELETE FROM usersnew WHERE user_id=?", [oldID])
                    cursor.execute("DELETE FROM harem_new WHERE user_id=?", [oldID])
                    cursor.execute("DELETE FROM stabby_clan WHERE user_id=?", [oldID])
                    cursor.execute("DELETE FROM the_boys_new WHERE user_id=?", [oldID])
                    cursor.execute("DELETE FROM li_potential_new WHERE user_id=?", [oldID])

                await channel.send(f"User {user_name} has been successfully removed from the database."
                                   f" Have a great time! :wave:")
                await self.deleteRequestMessages.add_reaction('✅')

                db.commit()

                self.deleteRequestMessages = ""
                self.usersRequestingDeletion = ""
                self.deletionPromptMsgIDs = ""

    @commands.command()
    async def update(self, ctx):
        """
        Relic from times where the dev didn't know anything about SQL;
        Does nothing but send an easter egg message now :D
        """
        await ctx.send("This command is now obsolete :)")

    async def forceDelete(self, uid):
        """
        [MOD ONLY] Deletes the data of a given user

        Parameters:
            - uid: int
                the user ID of the user whose data is to be obliterated.

        Returns:
            Nothing.
        """
        db = sqlite3.connect("main.sqlite")
        cursor = db.cursor()

        # check if user in DB
        cursor.execute("SELECT * FROM users WHERE user_id = ?", [uid])
        if cursor.fetchone():
            # if so delete all related entries
            tables = [ 
                "oialt", "oialt_harem", "stabby_mikes", "the_boys", "li_potential", 
                "eternum", "eternum_harem", "homies", "side_girls", "creatures"
            ]

            for table in tables:
                cursor.execute("DELETE FROM %s WHERE user_id = ?" % table, [uid])
            db.commit()

        cursor.close()
        db.close()


def setup(client):
    client.add_cog(AccountManager(client))
