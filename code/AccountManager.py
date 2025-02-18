import discord
from discord import Embed, File
from discord.ext import commands, tasks
from discord.ext.commands import cooldown, BucketType
import random
import sqlite3
from Utilities import HelperClass


class AccountManager(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.helperClass = HelperClass()

    msgID = ""
    deleteMsg = ""
    userThatWantsToDelete = ""

    # HELPER FUNCTIONS

    async def getUserID(self, discordID, cursor):

        cursor.execute("SELECT user_id FROM users WHERE discord_id=?", [discordID])
        uID = cursor.fetchone()
        if uID is not None:
            return uID[0]
        else:
            return uID

    # update to 0.5 check
    async def checkUser(self, discord_id: str, cursor):

        cursor.execute("SELECT user_id FROM users WHERE discord_id = ?", [discord_id])
        userIDCheck = cursor.fetchone()

        if userIDCheck is None:
            return "register"
        else:
            userID = userIDCheck[0]
            cursor.execute("SELECT pancho FROM creatures WHERE user_id = ?", [userID])
            panchoCheck = cursor.fetchone()
            pancho = None
            if panchoCheck is not None:
                pancho = panchoCheck[0]

            if pancho == "Xenomorph":
                return "update"
            else:
                return "good"

    # COMMANDS & RELATED

    @commands.command()
    async def register(self, ctx):
        db = sqlite3.connect("main.sqlite")
        cursor = db.cursor()
        discordID = str(ctx.author.id)

        title = ""
        text = ""
        footer = ""

        userCheck = await self.checkUser(discord_id=discordID, cursor=cursor)
        # check user registration --> checkUser()
        # if good send error message --> good to go
        if userCheck != "register":
            title = f"{str(ctx.author)[:-5]} is already registered."
            text = "If you can't access the games, try updating (-update)!"
            footer = "Please enjoy!"
        # if register:
        else:
            cursor.execute("INSERT INTO users (discord_id) VALUES (?)", [discordID])
            uID = await self.getUserID(discordID, cursor)
            cursor.execute("INSERT INTO oialt (user_id) VALUES (?)", [uID])
            cursor.execute("INSERT INTO oialt_harem (user_id) VALUES (?)", [uID])
            cursor.execute("INSERT INTO stabby_mikes (user_id) VALUES (?)", [uID])
            cursor.execute("INSERT INTO the_boys (user_id) VALUES (?)", [uID])
            cursor.execute("INSERT INTO li_potential (user_id) VALUES (?)", [uID])
            cursor.execute("INSERT INTO eternum (user_id) VALUES (?)", [uID])
            cursor.execute("INSERT INTO eternum_harem (user_id) VALUES (?)", [uID])
            cursor.execute("INSERT INTO homies (user_id) VALUES (?)", [uID])
            cursor.execute("INSERT INTO side_girls (user_id) VALUES (?)", [uID])
            cursor.execute("INSERT INTO creatures (user_id) VALUES (?)", [uID])

            title = "Great Success!"
            text = f"user {ctx.author.mention} was successfully registered to the database!"
            footer = "Welcome aboard!"
            db.commit()

        embed = await HelperClass.createEmbed(self=self.helperClass, title=title, text=text, footer=footer)
        await ctx.send(embed=embed)

    @commands.command()
    async def deleteacc(self, ctx):
        db = sqlite3.connect("main.sqlite")
        cursor = db.cursor()
        discordID = str(ctx.author.id)
        uid = await self.getUserID(discordID=discordID, cursor=cursor)
        user_name = str(ctx.author)

        if uid is not None:
            msg = await ctx.send("Are you sure you want to delete **all** your data?"
                                 "\nThis action is irreversible! (React to the checkmark to confirm.)")
            self.deleteMsg = ctx.message
            self.msgID = msg.id
            self.userThatWantsToDelete = ctx.author
            await msg.add_reaction('✅')
        else:
            cursor.execute("SELECT user_id FROM usersnew WHERE discord_id=?", [discordID])
            oldID = cursor.fetchone()
            if oldID is not None:
                msg = await ctx.send("Are you sure you want to delete **all** your data?"
                                     "\nThis action is irreversible! (React to the checkmark to confirm.)")
                self.deleteMsg = ctx.message
                self.msgID = msg.id
                self.userThatWantsToDelete = ctx.author
                await msg.add_reaction('✅')
            else:
                await ctx.send(f"User {user_name[:-5]} is not in our database I'm afraid...")
        db.commit()

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        # If no message marked for deletion, ignore
        if isinstance(self.deleteMsg, str):
            return

        db = sqlite3.connect("main.sqlite")
        cursor = db.cursor()
        discordID = str(self.deleteMsg.author.id)
        uid = await self.getUserID(discordID=discordID, cursor=cursor)
        oldID = None
        if uid is None:
            cursor.execute("SELECT user_id FROM usersnew WHERE discord_id = ?", [discordID])
            oldIDList = cursor.fetchone()
            oldID = oldIDList[0]
        user_name = str(self.deleteMsg.author)
        channel = self.client.get_channel(self.deleteMsg.channel.id)

        if self.msgID == payload.message_id:
            if self.userThatWantsToDelete.id == payload.user_id:
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
                await self.deleteMsg.add_reaction('✅')

                db.commit()

                self.deleteMsg = ""
                self.userThatWantsToDelete = ""
                self.msgID = ""

    @commands.command()
    async def update(self, ctx):
        db = sqlite3.connect("main.sqlite")
        cursor = db.cursor()
        discordID = str(ctx.author.id)
        user_name = str(ctx.author)

        user = await self.checkUser(discordID, cursor)

        title = ""
        description = ""
        footer = ""

        if user == 'good':
            title = f"No update needed..."
            description = f"User {user_name} is already up to date!"
            footer = "Enjoy the gf game!"
        elif user == 'update':
            # update to 0.5 content
            userID = await self.getUserID(discordID, cursor)

            # rename entries in xenomorph column to "Pancho"
            cursor.execute("UPDATE creatures SET pancho = 'Pancho' WHERE user_id = ?", [userID])

            title = "Great Success!"
            description = "You've successfully updated to Judie v2.1!"
            footer = "Have fun!"
            await ctx.message.add_reaction('✅')
        else:
            # build error embed that user needs to register
            title = f"Error #404 - User {str(ctx.author)} not registered!"
            description = "Please register before playing! (-register)"
            footer = "Contact Eisritter#6969 if you encounter any issues!"

        embed = await self.helperClass.createEmbed(title=title, text=description, footer=footer)
        await ctx.send(embed=embed)

        db.commit()

    async def forceDelete(self, uid):
        db = sqlite3.connect("main.sqlite")
        cursor = db.cursor()

        # check if user in DB
        cursor.execute("SELECT * FROM users WHERE user_id = ?", [uid])
        if cursor.fetchone():
            # if so delete all related entries
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

        db.commit()
        cursor.close()
        db.close()


def setup(client):
    client.add_cog(AccountManager(client))
