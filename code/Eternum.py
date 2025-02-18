# DISCORD.PY
import discord
from discord import Embed, File
from discord.ext import commands, tasks
from discord.ext.commands import cooldown, BucketType
# OTHER HELPING
import os
import random
import sqlite3
# OWN HELPING
from Utilities import Collections, HelperClass, Results, Effects
from CharacterCard import CharacterCard
from AccountManager import AccountManager
from EgfCharacters import EgfCharacters


class Eternum(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.characterList = EgfCharacters()
        self.characters = self.characterList.characters
        self.botSpamChannels = []
        self.botSpamChannels.append(779873459756335104)
        self.botSpamChannels.append(929419591573188608)
        self.HelperClass = HelperClass()
        self.accountManager = AccountManager(self.client)

    # Development Start 17/08/2022; Version 1.0.

    # CD: 20H = 72k seconds
    cooldowntime = 72000

    # HELPER FUNCTIONS - checkUser in AccountManager // createEmbed in Utilities/HelperFunctions

    async def buildCharacterEmbed(self, character: CharacterCard, results: Results, ctx, n: int = -1):
        if not character:
            print("Error: Missing character object.")

        embed = ""
        image = ""
        text = ""
        footer = ""
        field_name = ""
        field_value = ""
        color = HelperClass.eternumBlue

        number = random.randint(1, character.picNumber) if n == -1 else n
        filepath = f"./EternumGfGameImages/{character.filename}_{number}.webp"

        collection = character.collection

        if collection == Collections.NONE:
            text = f"{random.choice(character.quotes)}"
            field_name = f"{str(collection)} - {str(character.effects)}"
            field_value = f"*a.k.a. {character.aliases}*"
            footer = f"Better luck next time, {str(ctx.author.display_name)}!"

            if character.effects in [Effects.HAREM_KILLER, Effects.HOMIE_KILLER, Effects.SIDE_GIRL_KIDNAPPER,
                                     Effects.CREATURE_STOMPER]:

                if character.name == "Thanatos":
                    if results.protected:
                        text = f"Calypso managed to evacuate {results.victim} before Thanatos could kill her! {HelperClass.annieYay}"
                        field_name = f"{str(character.effects)} (denied) {HelperClass.novaGun}"
                        field_value = f"*a.k.a. {character.aliases}*"
                        color = HelperClass.red
                        footer = f"You won't be this lucky next time, {str(ctx.author.display_name)}..."
                        filepath = f"./EternumGfGameImages/{character.filename}_denied.webp"
                    else:
                        field_name = f"{str(character.effects)} {HelperClass.alexAngry}"
                        field_value = f"*a.k.a. {character.aliases}*"
                        if results.victim != "Nobody":
                            text = f"Thanatos killed {results.victim}. She is no longer in your harem, " \
                                   f"{str(ctx.author.display_name)}! {HelperClass.pepeCry2}"
                        else:
                            text = f"Thanatos didn't find anyone to kill... Lucky you I guess, {str(ctx.author.display_name)}."
                        color = HelperClass.black
                        footer = random.choice(character.quotes)

                elif character.name == "Troll":
                    if results.protected:
                        text = f"Dalia managed to kill the troll before it could get its hands on {str(ctx.author.display_name)}'s" \
                               f" {results.victim}! {HelperClass.annieYay}"
                        field_name = f"{str(character.effects)} (denied) {HelperClass.novaGun}"
                        field_value = f"*a.k.a. {character.aliases}*"
                        color = HelperClass.red
                        footer = "*groans*"
                        filepath = f"./EternumGfGameImages/{character.filename}_denied.webp"
                    else:
                        field_name = f"{str(character.effects)} {HelperClass.alexAngry}"
                        field_value = f"*a.k.a. {character.aliases}*"
                        if results.victim != "Nobody":
                            text = f"The troll killed {results.victim}. They are no longer in your homie group, " \
                                   f"{str(ctx.author.display_name)}! {HelperClass.pepeCry2}"
                        else:
                            text = f"The troll didn't find anyone to kill... Lucky you I guess, {str(ctx.author.display_name)}"
                        color = HelperClass.black
                        footer = random.choice(character.quotes)

                elif character.name == "Axel Bardot":
                    if results.protected:
                        text = f"Orion punched Axel the second he noticed him harassing {results.victim}! {HelperClass.annieYay}"
                        field_name = f"{str(character.effects)} (denied) {HelperClass.novaGun}"
                        field_value = f"*a.k.a. {character.aliases}*"
                        color = HelperClass.red
                        footer = f"You messed with the wrong guy, cocksucker ({str(ctx.author.display_name)})!"
                        filepath = f"./EternumGfGameImages/{character.filename}_denied.webp"
                    else:
                        if results.victim != "Nobody":
                            text = f"Oh no! Axel kidnapped {results.victim} from your side girl harem, {str(ctx.author.display_name)}! {HelperClass.pepeCry2}"
                            field_name = f"{str(character.effects)} {HelperClass.alexAngry}"
                            field_value = f"*a.k.a. {character.aliases}*"
                        else:
                            text = f"Axel didn't find anyone to kidnap... Lucky you I guess, {str(ctx.author.display_name)}."
                            field_name = f"{str(character.effects)} {HelperClass.alexAngry}"
                            field_value = f"*a.k.a. {character.aliases}*"
                        color = HelperClass.black
                        footer = random.choice(character.quotes)

                elif character.name == "Golem":
                    if results.protected:
                        text = f"Pyramid Head managed to kill the troll before it could get its feet on " \
                               f"{str(ctx.author.display_name)}'s {results.victim}! {HelperClass.annieYay}"
                        field_name = f"{str(character.effects)} (denied) {HelperClass.novaGun}"
                        field_value = f"*a.k.a. {character.aliases}*"
                        color = HelperClass.red
                        footer = "*groans*"
                        filepath = f"./EternumGfGameImages/{character.filename}_denied.webp"
                    else:
                        if results.victim != "Nobody":
                            text = f"The golem stomped {results.victim} to death. They are no longer in your creatures " \
                                   f"group, {str(ctx.author.display_name)}! {HelperClass.pepeCry2}"
                            field_name = f"{str(character.effects)} {HelperClass.alexAngry}"
                            field_value = f"*a.k.a. {character.aliases}*"
                        else:
                            text = f"The golem didn't find anyone to trample on... Lucky you I guess, {str(ctx.author.display_name)}."
                            field_name = f"{str(character.effects)} {HelperClass.alexAngry}"
                            field_value = f"*a.k.a. {character.aliases}*"
                        color = HelperClass.black
                        footer = random.choice(character.quotes)

        else:
            if collection == Collections.HAREM:
                color = HelperClass.pink
                if not results.duplicate:
                    text = f"{random.choice(character.quotes)}"
                    field_name = f"{str(collection)} (new) {HelperClass.daliaParty} - {str(character.effects)}"
                    field_value = f"*a.k.a. {character.aliases}*"
                    footer = f"New harem member {str(ctx.author.display_name)}!"
                else:
                    text = f"{random.choice(character.quotes)}"
                    field_name = f"{str(collection)} (duplicate) {HelperClass.annieCry} - {str(character.effects)}"
                    field_value = f"*a.k.a. {character.aliases}*"
                    footer = f"So close! Maybe next time, {str(ctx.author.display_name)}..."

            elif collection == Collections.SIDE_DISHES:
                color = HelperClass.purple
                if not results.duplicate:
                    text = f"{random.choice(character.quotes)}"
                    field_name = f"{str(collection)} (new) {HelperClass.daliaParty} - {str(character.effects)}"
                    field_value = f"*a.k.a. {character.aliases}*"
                    footer = f"New side chick {str(ctx.author.display_name)}!"
                else:
                    text = f"{random.choice(character.quotes)}"
                    field_name = f"{str(collection)} (duplicate) {HelperClass.annieCry} - {str(character.effects)}"
                    field_value = f"*a.k.a. {character.aliases}*"
                    footer = f"So close! Maybe next time, {str(ctx.author.display_name)}..."

            elif collection == Collections.THE_HOMIES:
                color = HelperClass.yellow
                if not results.duplicate:
                    text = f"{random.choice(character.quotes)}"
                    field_name = f"{str(collection)} (new) {HelperClass.daliaParty} - {str(character.effects)}"
                    field_value = f"*a.k.a. {character.aliases}*"
                    footer = f"New homie {str(ctx.author.display_name)}!"
                else:
                    text = f"{random.choice(character.quotes)}"
                    field_name = f"{str(collection)} (duplicate) {HelperClass.annieCry} - {str(character.effects)}"
                    field_value = f"*a.k.a. {character.aliases}*"
                    footer = f"So close! Maybe next time, {str(ctx.author.display_name)}..."

            elif collection == Collections.CREATURES:
                color = HelperClass.green
                if not results.duplicate:
                    text = f"{random.choice(character.quotes)}"
                    field_name = f"{str(collection)} (new) {HelperClass.daliaParty} - {str(character.effects)}"
                    field_value = f"*a.k.a. {character.aliases}*"
                    footer = f"New creature {str(ctx.author.display_name)}!"
                else:
                    text = f"{random.choice(character.quotes)}"
                    field_name = f"{str(collection)} (duplicate) {HelperClass.annieCry} - {str(character.effects)}"
                    field_value = f"*a.k.a. {character.aliases}*"
                    footer = f"So close! Maybe next time, {str(ctx.author.display_name)}..."

        if not os.path.exists(filepath):
            print(f"Error: file {filepath} not found.")
            return

        if not field_name.strip() or not field_value.strip():
            print(f"Error: Embed fields for {character} (victim: {results.victim}, x2: {results.duplicate}, shield:"
                  f"{results.protected}) are empty.")

        image = discord.File(filepath, filename="gf.webp")

        if not image:
            print(f"Error: No image attached to embed of {character} []")

        embed = await self.HelperClass.createEmbed(title=character.name, text=text, color=color, footer=footer)
        embed.add_field(name=field_name, value=field_value)
        embed.set_image(url="attachment://gf.webp")
        await ctx.send(file=image, embed=embed)

    async def updateDatabase(self, uid: int, character: CharacterCard, db, cursor):
        duplicateCharacter = False
        protected = False
        victim = None

        cursor.execute("UPDATE eternum SET last_gf = ? WHERE user_id = ?", [character.name, uid])

        if character.collection == Collections.HAREM:
            cursor.execute("SELECT %s FROM eternum_harem WHERE user_id=?" % character.filename, (uid,))
            duplicate = cursor.fetchone()
            if duplicate[0] == "NONE":
                cursor.execute("UPDATE eternum_harem SET %s = ? WHERE user_id=?" % character.filename,
                               [character.name, uid])
            else:
                duplicateCharacter = True
            cursor.execute("UPDATE eternum_harem SET last_girl=? WHERE user_id=?", [character.filename, uid])

        elif character.collection == Collections.SIDE_DISHES:
            cursor.execute("SELECT %s FROM side_girls WHERE user_id=?" % character.filename, [uid])
            duplicate = cursor.fetchone()
            if duplicate[0] == "NONE":
                cursor.execute("UPDATE side_girls SET %s = ? WHERE user_id=?" % character.filename,
                               [character.name, uid])
            else:
                duplicateCharacter = True
            cursor.execute("UPDATE side_girls SET last_affair=? WHERE user_id=?", [character.filename, uid])

        elif character.collection == Collections.THE_HOMIES:
            cursor.execute("SELECT %s FROM homies WHERE user_id=?" % character.filename, [uid])
            duplicate = cursor.fetchone()
            if duplicate[0] == "NONE":
                cursor.execute("UPDATE homies SET %s = ? WHERE user_id=?" % character.filename, [character.name, uid])
            else:
                duplicateCharacter = True
            cursor.execute("UPDATE homies SET last_homie=? WHERE user_id=?", [character.filename, uid])

        elif character.collection == Collections.CREATURES:
            cursor.execute("SELECT %s FROM creatures WHERE user_id=?" % character.filename, [uid])
            duplicate = cursor.fetchone()
            if duplicate[0] == "NONE":
                cursor.execute("UPDATE creatures SET %s = ? WHERE user_id=?" % character.filename,
                               [character.name, uid])
            else:
                duplicateCharacter = True
            cursor.execute("UPDATE creatures SET last_creature=? WHERE user_id=?", [character.filename, uid])

        if character.effects == Effects.HAREM_KILLER:

            cursor.execute("SELECT alex FROM eternum_harem WHERE user_id=?", [uid])
            alex = cursor.fetchone()

            if alex[0] == 'Alexandra Bardot':
                victim = alex[0]
            else:
                cursor.execute("SELECT nova FROM eternum_harem WHERE user_id=?", [uid])
                nova = cursor.fetchone()
                if nova[0] == 'Nova Johnson':
                    victim = nova[0]
                else:
                    cursor.execute("SELECT last_girl FROM eternum_harem WHERE user_id=?", [uid])
                    lastgf = cursor.fetchone()
                    if lastgf[0] in ['annie', 'dalia', 'luna', 'nancy', 'penny']:
                        for i in range(len(self.characters)):
                            if self.characters[i].filename == lastgf[0]:
                                victim = self.characters[i].name
                    else:
                        victim = "Nobody"

            cursor.execute("SELECT calypso FROM eternum WHERE user_id=?", [uid])
            protection = cursor.fetchone()

            if protection[0] == 0 and victim != "Nobody":
                for i in range(len(self.characters)):
                    if self.characters[i].name == victim:
                        column = self.characters[i].filename
                        cursor.execute("UPDATE eternum_harem SET %s = 'NONE' WHERE user_id=?" % column, [uid])

                cursor.execute("UPDATE eternum_harem SET last_girl='NONE' WHERE user_id=?", [uid])

            else:
                if victim != "Nobody":
                    cursor.execute("UPDATE eternum SET calypso=0 WHERE user_id=?", [uid])
                    protected = True

        if character.effects == Effects.SIDE_GIRL_KIDNAPPER:
            cursor.execute("SELECT last_affair FROM side_girls WHERE user_id=?", [uid])
            lastgf = cursor.fetchone()
            if lastgf[0] in ['bluefoxmaiden', 'calypso', 'eva', 'idriel', 'maat', 'redfoxmaiden', 'wenlin']:
                for i in range(len(self.characters)):
                    if self.characters[i].filename == lastgf[0]:
                        victim = self.characters[i].name
            else:
                victim = "Nobody"

            cursor.execute("SELECT orion FROM eternum WHERE user_id=?", [uid])
            protection = cursor.fetchone()

            if protection[0] == 0 and victim != "Nobody":
                for i in range(len(self.characters)):
                    if self.characters[i].name == victim:
                        column = self.characters[i].filename
                        cursor.execute("UPDATE side_girls SET %s='NONE' WHERE user_id=?" % column, [uid])

                cursor.execute("UPDATE side_girls SET last_affair='NONE' WHERE user_id=?", [uid])

            else:
                if victim != "Nobody":
                    cursor.execute("UPDATE eternum SET orion=0 WHERE user_id=?", [uid])
                    protected = True

        if character.effects == Effects.HOMIE_KILLER:
            cursor.execute("SELECT jerry FROM homies WHERE user_id=?", [uid])
            jerry = cursor.fetchone()

            if jerry[0] == 'Jerry':
                victim = jerry[0]
            else:
                cursor.execute("SELECT last_homie FROM homies WHERE user_id=?", [uid])
                lastgf = cursor.fetchone()
                if lastgf[0] in ['chang', 'orion', 'chopchop', 'hernandez', 'micaela', 'noah', 'raul']:
                    for i in range(len(self.characters)):
                        if self.characters[i].filename == lastgf[0]:
                            victim = self.characters[i].name
                else:
                    victim = "Nobody"

            cursor.execute("SELECT dalia FROM eternum WHERE user_id=?", [uid])
            protection = cursor.fetchone()

            if protection[0] == 0 and victim != "Nobody":
                for i in range(len(self.characters)):
                    if self.characters[i].name == victim:
                        column = self.characters[i].filename
                        cursor.execute("UPDATE homies SET %s='NONE' WHERE user_id=?" % column, [uid])

                    cursor.execute("UPDATE homies SET last_homie='NONE' WHERE user_id=?", [uid])

            else:
                if victim != "Nobody":
                    cursor.execute("UPDATE eternum SET dalia=0 WHERE user_id=?", [uid])
                    protected = True

        if character.effects == Effects.CREATURE_STOMPER:
            cursor.execute("SELECT kermit FROM creatures WHERE user_id=?", [uid])
            kermit = cursor.fetchone()

            if kermit[0] == 'Kermit':
                victim = kermit[0]
            else:
                cursor.execute("SELECT last_creature FROM creatures WHERE user_id=?", [uid])
                lastgf = cursor.fetchone()
                if lastgf[0] in ['carolyn', 'igor', 'mauricec', 'mauriceg', 'mauricet', 'pancho']:
                    for i in range(len(self.characters)):
                        if self.characters[i].filename == lastgf[0]:
                            victim = self.characters[i].name
                else:
                    victim = "Nobody"

            cursor.execute("SELECT pyramid_head FROM eternum WHERE user_id=?", [uid])
            protection = cursor.fetchone()

            if protection[0] == 0 and victim != "Nobody":
                for i in range(len(self.characters)):
                    if self.characters[i].name == victim:
                        column = self.characters[i].filename
                        cursor.execute("UPDATE creatures SET %s='NONE' WHERE user_id=?" % column, [uid])

                    cursor.execute("UPDATE creatures SET last_creature='NONE' WHERE user_id=?", [uid])

            else:
                if victim != "Nobody":
                    cursor.execute("UPDATE eternum SET pyramid_head=0 WHERE user_id=?", [uid])
                    protected = True

        if character.effects == Effects.HAREM_SAVIOUR:
            cursor.execute("SELECT calypso FROM eternum WHERE user_id=?", [uid])
            duplicate = cursor.fetchone()
            if duplicate[0] == 0:
                cursor.execute("UPDATE eternum SET calypso=1 WHERE user_id =?", [uid])

        if character.effects == Effects.SIDE_GIRL_SAVIOUR:
            cursor.execute("SELECT orion FROM eternum WHERE user_id=?", [uid])
            duplicate = cursor.fetchone()
            if duplicate[0] == 0:
                cursor.execute("UPDATE eternum SET orion=1 WHERE user_id =?", [uid])

        if character.effects == Effects.HOMIE_SAVIOUR:
            cursor.execute("SELECT dalia FROM eternum WHERE user_id=?", [uid])
            duplicate = cursor.fetchone()
            if duplicate[0] == 0:
                cursor.execute("UPDATE eternum SET dalia=1 WHERE user_id =?", [uid])

        if character.effects == Effects.CREATURE_SAVIOUR:
            cursor.execute("SELECT pyramid_head FROM eternum WHERE user_id=?", [uid])
            duplicate = cursor.fetchone()
            if duplicate[0] == 0:
                cursor.execute("UPDATE eternum SET pyramid_head=1 WHERE user_id =?", [uid])

        db.commit()

        return Results(duplicate=duplicateCharacter, protected=protected, victim=victim)

    # COMMANDS

    @commands.command(aliases=['gfe', 'eternum gf', 'gf eternum'])
    @commands.cooldown(1, cooldowntime, commands.BucketType.user)
    async def egf(self, ctx):
        db = sqlite3.connect("main.sqlite")
        cursor = db.cursor()
        discordID = str(ctx.author.id)
        channelId = ctx.channel.id

        if channelId not in self.botSpamChannels:
            embed = discord.Embed(title="Wrong channel!",
                                  description=f"Please take this to {self.client.get_channel(self.botSpamChannels[0]).mention}",
                                  color=HelperClass.orange)
            ctx.command.reset_cooldown(ctx)
            await ctx.send(embed=embed)
        else:
            checkUser = await self.accountManager.checkUser(discord_id=discordID, cursor=cursor)
            if checkUser == "register":
                embed = await self.HelperClass.createEmbed(title=f"Error #404 - User {str(ctx.author.display_name)} not registered!",
                                                           text="Please register before playing! (-register)",
                                                           footer="Contact Eisritter#6969 if you encounter any issues!")
                await ctx.send(embed=embed)
                ctx.command.reset_cooldown(ctx)
            elif checkUser == "update":
                embed = await self.HelperClass.createEmbed(title=f"Error - User {str(ctx.author.display_name)} is not up to date!",
                                                           text="Please update to the newest stand with -update!",
                                                           footer="Contact Eisritter#6969 if you encounter any issues!")
                await ctx.send(embed=embed)
                ctx.command.reset_cooldown(ctx)
            else:
                uid = await self.accountManager.getUserID(discordID=discordID, cursor=cursor)
                # choose random character
                gf = random.choice(self.characters)
                # update database accordingly
                results = await self.updateDatabase(uid=uid, character=gf, cursor=cursor, db=db)
                #   create according embed --> self.buildCharacterEmbed
                await self.buildCharacterEmbed(character=gf, results=results, ctx=ctx)

            db.commit()
            cursor.close()

    @commands.command(aliases=['hareme', 'eternum harem', 'harem eternum'])
    async def eharem(self, ctx):
        db = sqlite3.connect("main.sqlite")
        cursor = db.cursor()
        discordID = str(ctx.author.id)
        user_name = str(ctx.author.display_name)
        count = 0
        channelId = ctx.channel.id

        if channelId not in self.botSpamChannels:
            embed = discord.Embed(title="Wrong channel!",
                                  description=f"Please take this to {self.client.get_channel(self.botSpamChannels[0]).mention}",
                                  color=HelperClass.orange)
            await ctx.send(embed=embed)
        else:
            # check if user registered & up to date
            checkUser = await self.accountManager.checkUser(discord_id=discordID, cursor=cursor)
            # if no build error embed
            if checkUser == "register":
                embed = await self.HelperClass.createEmbed(title=f"Error #404 - User {str(ctx.author.display_name)} not registered!",
                                                           text="Please register before playing! (-register)",
                                                           footer="Contact Eisritter#6969 if you encounter any issues!")
                await ctx.send(embed=embed)
            elif checkUser == "update":
                embed = await self.HelperClass.createEmbed(title=f"Error - User {str(ctx.author.display_name)} is not up to date!",
                                                           text="Please update to the newest stand with -update!",
                                                           footer="Contact Eisritter#6969 if you encounter any issues!")
                await ctx.send(embed=embed)
            # if yes:
            else:
                #   search thru 'eternum_harem' table for entries
                uid = await self.accountManager.getUserID(discordID=discordID, cursor=cursor)
                members = []
                missing = []
                cursor.execute(
                    "SELECT alex, annie, dalia, luna, nancy, nova, penny FROM eternum_harem WHERE user_id=?", [uid])
                yesno = cursor.fetchone()
                for i in yesno:
                    if i != 'NONE':
                        count = count + 1
                        members.append(i)
                for j in members:
                    if j == "NONE":
                        members.remove(j)
                        count = count - 1

                if "Alexandra Bardot" not in members:
                    missing.append("Alexandra Bardot")
                if "Annie Winters" not in members:
                    missing.append("Annie Winters")
                if "Dalia Carter" not in members:
                    missing.append("Dalia Carter")
                if "Luna Hernandez" not in members:
                    missing.append("Luna Hernandez")
                if "Nancy Carter" not in members:
                    missing.append("Nancy Carter")
                if "Nova Johnson" not in members:
                    missing.append("Nova Johnson")
                if "Penelope Carter" not in members:
                    missing.append("Penelope Carter")

                #   compile entries to list
                haremlist = "\n".join(members)
                missinglist = "\n".join(missing)

                embed_title = f"Eternum Harem of **{user_name}**:"

                if haremlist == "":
                    haremlist = "You haven't collected anyone for your harem yet..."

                if missinglist == "":
                    missinglist = f"You have completed the harem! {HelperClass.daliaParty}"
                #   build embed (color pink) with categories 'got x/y' + names & 'missing z/y' + names --> + emotes?
                embed = discord.Embed(title=embed_title, color=HelperClass.pink)
                embed.add_field(name=f"Claimed ({count}/7):", value=haremlist)
                embed.add_field(name=f"Missing ({7 - count}/7):", value=missinglist)
                await ctx.send(embed=embed)

    @commands.command(aliases=['thehomies', 'the homies', 'da homies', 'ehomies'])
    async def homies(self, ctx):
        db = sqlite3.connect("main.sqlite")
        cursor = db.cursor()
        discordID = str(ctx.author.id)
        user_name = str(ctx.author.display_name)
        count = 0
        channelId = ctx.channel.id

        if channelId not in self.botSpamChannels:
            embed = discord.Embed(title="Wrong channel!",
                                  description=f"Please take this to {self.client.get_channel(self.botSpamChannels[0]).mention}",
                                  color=HelperClass.orange)
            await ctx.send(embed=embed)
        else:
            # check if user registered & up to date
            checkUser = await self.accountManager.checkUser(discord_id=discordID, cursor=cursor)
            # if no build error embed
            if checkUser == "register":
                embed = await self.HelperClass.createEmbed(title=f"Error #404 - User {str(ctx.author.display_name)} not registered!",
                                                           text="Please register before playing! (-register)",
                                                           footer="Contact Eisritter#6969 if you encounter any issues!")
                await ctx.send(embed=embed)
            elif checkUser == "update":
                embed = await self.HelperClass.createEmbed(title=f"Error - User {str(ctx.author.display_name)} is not up to date!",
                                                           text="Please update to the newest stand with -update!",
                                                           footer="Contact Eisritter#6969 if you encounter any issues!")
                await ctx.send(embed=embed)
            # if yes:
            else:
                #   search thru 'homies' table for entries
                uid = await self.accountManager.getUserID(discordID=discordID, cursor=cursor)
                members = []
                missing = []
                cursor.execute(
                    "SELECT chang, chopchop, victor, jerry, micaela, noah, orion, raul FROM homies WHERE user_id=?",
                    [uid])
                yesno = cursor.fetchone()
                for i in yesno:
                    if i != 'NONE':
                        count = count + 1
                        members.append(i)
                for j in members:
                    if j == "NONE":
                        members.remove(j)
                        count = count - 1

                if "Chang Wong" not in members:
                    missing.append("Chang Wong")
                if "Chop-Chop" not in members:
                    missing.append("Chop-Chop")
                if "Victor Hernandez" not in members:
                    missing.append("Mr. Hernandez")
                if "Jerry" not in members:
                    missing.append("Jerry")
                if "Micaela Garcia" not in members:
                    missing.append("Micaela Garcia")
                if "Noah" not in members:
                    missing.append("Noah")
                if "Orion Richards" not in members:
                    missing.append("Orion Richards")
                if "Raul" not in members:
                    missing.append("Raul")

                #   compile entries to list
                homielist = "\n".join(members)
                missinglist = "\n".join(missing)

                embed_title = f"Homies of **{user_name}**:"

                if homielist == "":
                    homielist = "You haven't collected any of the homies yet..."

                if missinglist == "":
                    missinglist = f"You have assembled all the homies! {HelperClass.daliaParty}"
                #   build embed (color pink) with categories 'got x/y' + names & 'missing z/y' + names --> + emotes?
                embed = discord.Embed(title=embed_title, color=HelperClass.yellow)
                embed.add_field(name=f"Claimed ({count}/8):", value=homielist)
                embed.add_field(name=f"Missing ({8 - count}/8):", value=missinglist)
                await ctx.send(embed=embed)

    @commands.command(aliases=['sidegirls', 'sidechicks', 'esidegirls', 'epotentiallis'])
    async def sidedishes(self, ctx):
        db = sqlite3.connect("main.sqlite")
        cursor = db.cursor()
        discordID = str(ctx.author.id)
        user_name = str(ctx.author.display_name)
        count = 0
        channelId = ctx.channel.id

        if channelId not in self.botSpamChannels:
            embed = discord.Embed(title="Wrong channel!",
                                  description=f"Please take this to {self.client.get_channel(self.botSpamChannels[0]).mention}",
                                  color=HelperClass.orange)
            await ctx.send(embed=embed)
        else:
            # check if user registered & up to date
            checkUser = await self.accountManager.checkUser(discord_id=discordID, cursor=cursor)
            # if no build error embed
            if checkUser == "register":
                embed = await self.HelperClass.createEmbed(title=f"Error #404 - User {str(ctx.author.display_name)} not registered!",
                                                           text="Please register before playing! (-register)",
                                                           footer="Contact Eisritter#6969 if you encounter any issues!")
                await ctx.send(embed=embed)
            elif checkUser == "update":
                embed = await self.HelperClass.createEmbed(title=f"Error - User {str(ctx.author.display_name)} is not up to date!",
                                                           text="Please update to the newest stand with -update!",
                                                           footer="Contact Eisritter#6969 if you encounter any issues!")
                await ctx.send(embed=embed)
            # if yes:
            else:
                #   search thru 'homies' table for entries
                uid = await self.accountManager.getUserID(discordID=discordID, cursor=cursor)
                members = []
                missing = []
                cursor.execute(
                    "SELECT bluefoxmaiden, calypso, eva, idriel, maat, redfoxmaiden, wenlin FROM side_girls WHERE user_id=?",
                    [uid])
                yesno = cursor.fetchone()
                for i in yesno:
                    if i != 'NONE':
                        count = count + 1
                        members.append(i)
                for j in members:
                    if j == "NONE":
                        members.remove(j)
                        count = count - 1

                if "Blue Fox Maiden" not in members:
                    missing.append("Blue Fox Maiden")
                if "Calypso" not in members:
                    missing.append("Calypso")
                if "Eva" not in members:
                    missing.append("Eva")
                if "Idriel" not in members:
                    missing.append("Idriel")
                if "Maat" not in members:
                    missing.append("Maat")
                if "Red Fox Maiden" not in members:
                    missing.append("Red Fox Maiden")
                if "Wenlin" not in members:
                    missing.append("Wenlin")

                #   compile entries to list
                sideslist = "\n".join(members)
                missinglist = "\n".join(missing)

                embed_title = f"Eternum Side Girls of **{user_name}**:"

                if sideslist == "":
                    sideslist = "You haven't collected any of the side girls yet..."

                if missinglist == "":
                    missinglist = f"You have assembled all the side girls! {HelperClass.daliaParty}"
                #   build embed (color pink) with categories 'got x/y' + names & 'missing z/y' + names --> + emotes?
                embed = discord.Embed(title=embed_title, color=HelperClass.purple)
                embed.add_field(name=f"Claimed ({count}/7):", value=sideslist)
                embed.add_field(name=f"Missing ({7 - count}/7):", value=missinglist)
                await ctx.send(embed=embed)

    @commands.command()
    async def creatures(self, ctx):
        db = sqlite3.connect("main.sqlite")
        cursor = db.cursor()
        discordID = str(ctx.author.id)
        user_name = str(ctx.author.display_name)
        count = 0
        channelId = ctx.channel.id

        if channelId not in self.botSpamChannels:
            embed = discord.Embed(title="Wrong channel!",
                                  description=f"Please take this to {self.client.get_channel(self.botSpamChannels[0]).mention}",
                                  color=HelperClass.orange)
            await ctx.send(embed=embed)
        else:
            # check if user registered & up to date
            checkUser = await self.accountManager.checkUser(discord_id=discordID, cursor=cursor)
            # if no build error embed
            if checkUser == "register":
                embed = await self.HelperClass.createEmbed(title=f"Error #404 - User {str(ctx.author.display_name)} not registered!",
                                                           text="Please register before playing! (-register)",
                                                           footer="Contact Eisritter#6969 if you encounter any issues!")
                await ctx.send(embed=embed)
            elif checkUser == "update":
                embed = await self.HelperClass.createEmbed(title=f"Error - User {str(ctx.author.display_name)} is not up to date!",
                                                           text="Please update to the newest stand with -update!",
                                                           footer="Contact Eisritter#6969 if you encounter any issues!")
                await ctx.send(embed=embed)
            # if yes:
            else:
                #   search thru 'homies' table for entries
                uid = await self.accountManager.getUserID(discordID=discordID, cursor=cursor)
                members = []
                missing = []
                cursor.execute(
                    "SELECT carolyn, igor, kermit, mauricec, mauriceg, mauricet, pancho FROM creatures WHERE user_id=?",
                    [uid])
                yesno = cursor.fetchone()
                for i in yesno:
                    if i != 'NONE':
                        count = count + 1
                        members.append(i)
                for j in members:
                    if j == "NONE":
                        members.remove(j)
                        count = count - 1

                if "Carolyn" not in members:
                    missing.append("Carolyn")
                if "Igor" not in members:
                    missing.append("Igor")
                if "Kermit" not in members:
                    missing.append("Kermit")
                if "Maurice (cat)" not in members:
                    missing.append("Maurice (cat)")
                if "Maurice (goat)" not in members:
                    missing.append("Maurice (goat)")
                if "Maurice (toucan)" not in members:
                    missing.append("Maurice (toucan)")
                if "Pancho" not in members:
                    missing.append("Pancho")

                #   compile entries to list
                creaturelist = "\n".join(members)
                missinglist = "\n".join(missing)

                embed_title = f"Eternum Creatures of **{user_name}**:"

                if creaturelist == "":
                    creaturelist = "You haven't collected any of the creatures yet..."

                if missinglist == "":
                    missinglist = f"You have assembled all of eternum's creatures! {HelperClass.daliaParty}"
                #   build embed (color pink) with categories 'got x/y' + names & 'missing z/y' + names --> + emotes?
                embed = discord.Embed(title=embed_title, color=HelperClass.green)
                embed.add_field(name=f"Claimed ({count}/7):", value=creaturelist)
                embed.add_field(name=f"Missing ({7 - count}/7):", value=missinglist)
                await ctx.send(embed=embed)

    @commands.command()
    async def eprotectors(self, ctx):
        db = sqlite3.connect("main.sqlite")
        cursor = db.cursor()
        discordID = str(ctx.author.id)
        user_name = str(ctx.author.display_name)
        channelId = ctx.channel.id

        if channelId not in self.botSpamChannels:
            embed = discord.Embed(title="Wrong channel!",
                                  description=f"Please take this to {self.client.get_channel(self.botSpamChannels[0]).mention}",
                                  color=HelperClass.orange)
            await ctx.send(embed=embed)
        else:
            # check if user registered & up to date
            checkUser = await self.accountManager.checkUser(discord_id=discordID, cursor=cursor)
            # if no build error embed
            if checkUser == "register":
                embed = await self.HelperClass.createEmbed(title=f"Error #404 - User {str(ctx.author.display_name)} not registered!",
                                                           text="Please register before playing! (-register)",
                                                           footer="Contact Eisritter#6969 if you encounter any issues!")
                await ctx.send(embed=embed)
            elif checkUser == "update":
                embed = await self.HelperClass.createEmbed(title=f"Error - User {str(ctx.author.display_name)} is not up to date!",
                                                           text="Please update to the newest stand with -update!",
                                                           footer="Contact Eisritter#6969 if you encounter any issues!")
                await ctx.send(embed=embed)
            # if yes:
            else:
                #   search thru 'eternum_harem' table for entries
                uid = await self.accountManager.getUserID(discordID=discordID, cursor=cursor)
                members = []
                cursor.execute("SELECT orion, calypso, dalia, pyramid_head FROM eternum WHERE user_id = ?", [uid])
                yesno = cursor.fetchone()
                sides = "**Side Girls:**\nOrion: :x:"
                if yesno[0] == 1:
                    sides = "**Side Girls:**\nOrion: ✅"
                members.append(sides)

                harem = "**Harem:**\nCalypso: :x:"
                if yesno[1] == 1:
                    harem = "**Harem:**\nCalypso: ✅"
                members.append(harem)

                homies = "**Homies:**\nDalia: :x:"
                if yesno[2] == 1:
                    homies = "**Homies:**\nDalia: ✅"
                members.append(homies)

                creatures = "**Creatures:**\nPyramid Head: :x:"
                if yesno[3] == 1:
                    creatures = "**Creatures:**\nPyramid Head: ✅"
                members.append(creatures)

                #   compile entries to list
                protectorlist = "\n".join(members)

                embed_title = f"Eternum Protectors of **{user_name}**:"
                #   build embed (color pink) with categories 'got x/y' + names & 'missing z/y' + names --> + emotes?
                embed = discord.Embed(title=embed_title, description=protectorlist, color=HelperClass.blue)
                await ctx.send(embed=embed)

    @commands.command(aliases=['eternum collections', 'collectionsE', 'collections eternum'])
    async def eCollections(self, ctx):
        db = sqlite3.connect("main.sqlite")
        cursor = db.cursor()
        discordID = str(ctx.author.id)
        user_name = str(ctx.author.display_name)
        haremcount = 0
        homiecount = 0
        sidescount = 0
        creaturecount = 0
        channelId = ctx.channel.id

        if channelId not in self.botSpamChannels:
            embed = discord.Embed(title="Wrong channel!",
                                  description=f"Please take this to {self.client.get_channel(self.botSpamChannels[0]).mention}",
                                  color=HelperClass.orange)
            await ctx.send(embed=embed)
        else:
            # check if user registered & up to date
            checkUser = await self.accountManager.checkUser(discord_id=discordID, cursor=cursor)
            # if no build error embed
            if checkUser == "register":
                embed = await self.HelperClass.createEmbed(title=f"Error #404 - User {str(ctx.author.display_name)} not registered!",
                                                           text="Please register before playing! (-register)",
                                                           footer="Contact Eisritter#6969 if you encounter any issues!")
                await ctx.send(embed=embed)
            elif checkUser == "update":
                embed = await self.HelperClass.createEmbed(title=f"Error - User {str(ctx.author.display_name)} is not up to date!",
                                                           text="Please update to the newest stand with -update!",
                                                           footer="Contact Eisritter#6969 if you encounter any issues!")
                await ctx.send(embed=embed)
            # if yes:
            else:
                embed_title = f"Eternum Collections of **{user_name}**:"
                embed = discord.Embed(title=embed_title, color=HelperClass.eternumBlue)

                #   search thru tables for entries
                uid = await self.accountManager.getUserID(discordID=discordID, cursor=cursor)
                members = []

                cursor.execute(
                    "SELECT alex, annie, dalia, luna, nancy, nova, penny FROM eternum_harem WHERE user_id=?", [uid])
                yesno = cursor.fetchone()
                for i in yesno:
                    if i != 'NONE':
                        haremcount = haremcount + 1
                        members.append(i)
                for j in members:
                    if j == "NONE":
                        members.remove(j)
                        haremcount = haremcount - 1

                #   compile entries to list
                haremlist = "\n".join(members)

                if haremlist == "":
                    haremlist = "You haven't collected anyone for your harem yet..."
                embed.add_field(name=f"Harem: ({haremcount}/7):", value=haremlist)

                members = []

                cursor.execute(
                    "SELECT chang, chopchop, victor, jerry, micaela, noah, orion, raul FROM homies WHERE user_id=?",
                    [uid])
                yesno = cursor.fetchone()
                for i in yesno:
                    if i != 'NONE':
                        homiecount = homiecount + 1
                        members.append(i)
                for j in members:
                    if j == "NONE":
                        members.remove(j)
                        homiecount = homiecount - 1

                #   compile entries to list
                homielist = "\n".join(members)

                if homielist == "":
                    homielist = "You haven't collected any of the homies yet..."

                embed.add_field(name=f"Homies: ({homiecount}/8):", value=homielist)

                members = []

                # SIDE GIRLS
                cursor.execute(
                    "SELECT bluefoxmaiden, calypso, eva, idriel, maat, redfoxmaiden, wenlin FROM side_girls WHERE user_id=?",
                    [uid])
                yesno = cursor.fetchone()
                for i in yesno:
                    if i != 'NONE':
                        sidescount = sidescount + 1
                        members.append(i)
                for j in members:
                    if j == "NONE":
                        members.remove(j)
                        sidescount = sidescount - 1

                # compile entries to list
                sideslist = "\n".join(members)

                if sideslist == "":
                    sideslist = "You haven't collected any of the side girls yet..."
                embed.add_field(name=f"Side Girls: ({sidescount}/7):", value=sideslist)

                # Creatures

                members = []

                cursor.execute(
                    "SELECT carolyn, igor, kermit, mauricec, mauriceg, mauricet, pancho FROM creatures WHERE user_id=?",
                    [uid])
                yesno = cursor.fetchone()
                for i in yesno:
                    if i != 'NONE':
                        creaturecount = creaturecount + 1
                        members.append(i)
                for j in members:
                    if j == "NONE":
                        members.remove(j)
                        creaturecount = creaturecount - 1

                #   compile entries to list
                creaturelist = "\n".join(members)

                if creaturelist == "":
                    creaturelist = "You haven't collected any of the creatures yet..."
                embed.add_field(name=f"Creatures: ({creaturecount}/7):", value=creaturelist)

                # Protectors

                members = []
                cursor.execute("SELECT orion, calypso, dalia, pyramid_head FROM eternum WHERE user_id = ?", [uid])
                yesno = cursor.fetchone()
                sides = "Side Girls:  :x:"
                if yesno[0] == 1:
                    sides = "Side Girls:  ✅"
                members.append(sides)

                harem = "Harem:  :x:"
                if yesno[1] == 1:
                    harem = "Harem:  ✅"
                members.append(harem)

                homies = "Homies:  :x:"
                if yesno[2] == 1:
                    homies = "Homies:  ✅"
                members.append(homies)

                creatures = "Creatures:  :x:"
                if yesno[3] == 1:
                    creatures = "Creatures:  ✅"
                members.append(creatures)

                #   compile entries to list
                protectorlist = "\n".join(members)

                embed.add_field(name="Protections:", value=protectorlist)

                await ctx.send(embed=embed)

    # ERROR MESSAGES

    @egf.error
    async def errorEgf(self, ctx, error):
        # if cooldown not done send last gf from table 'eternum'
        db = sqlite3.connect("main.sqlite")
        cursor = db.cursor()

        discordID = str(ctx.author.id)
        uid = await self.accountManager.getUserID(discordID=discordID, cursor=cursor)
        checkUser = await self.accountManager.checkUser(discord_id=discordID, cursor=cursor)
        channelId = ctx.channel.id

        if channelId not in self.botSpamChannels:
            embed = discord.Embed(title="Wrong channel!",
                                  description=f"Please take this to {self.client.get_channel(self.botSpamChannels[0]).mention}",
                                  color=HelperClass.orange)
            await ctx.send(embed=embed)
        elif isinstance(error, commands.CommandOnCooldown):

            time = error.retry_after
            hours = int(time // 3600)
            minutes = int((time % 3600) // 60)
            seconds = int((time % 3600) % 60)

            description = f"You still have {hours}h {minutes} mins and {seconds}s until your next draw!"

            if checkUser == "register":
                embed = await self.HelperClass.createEmbed(title=f"Error #404 - User {str(ctx.author.display_name)} not registered!",
                                                           text="Please register before playing! (-register)",
                                                           footer="Contact Eisritter#6969 if you encounter any issues!")
                await ctx.send(embed=embed)
                ctx.command.reset_cooldown(ctx)

            elif checkUser == "update":
                embed = await self.HelperClass.createEmbed(title=f"Error - User {str(ctx.author.display_name)} is not up to date!",
                                                           text="Please update to the newest stand with -update!",
                                                           footer="Contact Eisritter#6969 if you encounter any issues!")
                await ctx.send(embed=embed)
                ctx.command.reset_cooldown(ctx)
            else:
                cursor.execute("SELECT last_gf FROM eternum WHERE user_id=?", [uid])
                lastGf = cursor.fetchone()
                gf = ""
                field_name = ""
                field_value = ""
                field2_name = ""
                field2_value = ""
                number = 0
                if lastGf is None:
                    title = "This is awkward..."
                    field_name = "Your last pull is... No one?"
                    field_value = "How could that happen..."
                    footer = "Might as well contact Eisritter#6969, sumn ain't right"

                else:
                    for i in range(len(self.characters)):
                        if self.characters[i].name == lastGf[0]:
                            gf = self.characters[i]

                    title = "Slow down dude!"
                    field_name = gf.name
                    field_value = f"The last pull you made was {gf.name}"
                    field2_name = f"{str(gf.collection)} - {str(gf.effects)}"
                    field2_value = f"a.k.a. *{gf.aliases}*"
                    footer = "retry later mate..."

                embed = discord.Embed(title=title, description=description, color=HelperClass.eternumBlue)
                embed.set_footer(text=footer)

                embed.add_field(name=field_name, value=field_value, inline=True)
                embed.add_field(name=field2_name, value=field2_value, inline=False)
                if lastGf is not None:
                    number = random.randint(1, gf.picNumber)
                    image = discord.File(f"./EternumGfGameImages/{gf.filename}_{number}.webp", filename="gf.webp")
                else:
                    image = discord.File("./EternumGfGameImages/None.webp", filename="gf.webp")
                embed.set_image(url="attachment://gf.webp")
                await ctx.send(file=image, embed=embed)

            cursor.close()


def setup(client):
    client.add_cog(Eternum(client))
