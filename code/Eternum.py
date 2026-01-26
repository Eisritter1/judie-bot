# DISCORD.PY
from gc import collect
import discord
from discord import Embed, File
from discord.ext import commands, tasks
from discord.ext.commands import CooldownMapping, Cooldown, BucketType
# OTHER LIBRARIES
import os
import random
import sqlite3
from time import sleep
# OWN LIBRARIES
from Utilities import Collections, HelperClass, Results, Effects, check_channel, get_cols
from CharacterCard import CharacterCard
from AccountManager import AccountManager, check_user
from EgfCharacters import EgfCharacters


class Eternum(commands.Cog):
    """
    Judie's Eternum GF game cog.
    ----------------------------------
    Members:
        - activate() - initialize data following config data,
        - buildCharacterEmbed(CharacterCard, Results, discord.ext.Context, int) - builds the egf embed for a given character card,
        - updateDatabase(int, CharacterCard, sqlite3.Connection, sqlite3.Connection.Cursor) -> Results - performs alterations to the database following a gf pull,
        - egf(ctx) - attempts to pull a random character from the game Eternum for the user,
        - eharem(ctx) - provides an overview of the user's progress in the Eternum Harem collection,
        - homies(ctx) - provides an overview of the user's progress in the Eternum Homies collection,
        - sidedishes(ctx) - provides an overview of the user's progress in the Eternum Side Girl collection,
        - creatures(ctx) - provides an overview of the user's progress in the Eternum Pets collection,
        - eprotectors(ctx) - provides an overview of the user's coverage on the Eternum Insurance Policy(tm),
        - ecollections(ctx) - provides an overview of the user's progress in all Eternum collections,
        - errorGf(ctx, error) - catches errors that come up in the -egf command.
    """
    def __init__(self, client):
        self.client = client
        self.accountManager = self.client.accountManager
        client.CogsToActivate.append(self)
        self.characterList = EgfCharacters()
        self.characters = self.characterList.characters
        self.botSpamChannel = None

    # Development Start 17/08/2022; Version 1.0.

    def activate(self):
        """
        Initializes client data for the gf game - setting channel IDs, cooldown time etc. 

        Required for proper functioning; Required to run only after BotConfig.load() was called.
        """
        command = self.client.get_command("egf")
        cd = Cooldown(rate=1, per=self.client.config.cooldown)
        command._buckets = CooldownMapping(cd, type=BucketType.user)
        self.botSpamChannel = self.client.config.botSpamChannel
        print("successfully activated Eternum cog.")

    # HELPER FUNCTIONS - checkUser in AccountManager // createEmbed in Utilities/HelperFunctions

    async def buildCharacterEmbed(self, character: CharacterCard, results: Results, ctx, n: int = -1):
        """
        Builds and sends the egf embed using info from the provided CharacterCard.
        ---------------------------------------------------------------------------------------------------
        Parameters:
            - character : CharacterCard - the character whose card is to be built,
            - results : Results - a struct used to determine what happened to be displayed,
            - ctx : discord.ext.Context - discord context object for user info,
            - n : int - the index of chosen picture; chooses a random picture if n = -1 (defaults to -1).
        ---------------------------------------------------------------------------------------------------
        """
        if not character:
            print("Error: Missing character object.")

        embed = ""
        image = ""
        text = ""
        footer = ""
        effect_description = ""
        aliases = f"*a.k.a. {character.aliases}*"
        color = HelperClass.eternumBlue

        number = n if (n > 0 and n <= character.picNumber) else random.randint(1, character.picNumber)
        filepath = f"./EternumGfGameImages/{character.filename}_{number}.webp"

        # error message & early exit if file unrecognized.
        if not os.path.exists(filepath):
            print(f"Error: file {filepath} not found.")
            await ctx.send(f"Error building embed for character {character}: Couldn't find image no. {number}")
            return

        collection = character.collection

        # This needs to include Pyramid Head :PepeBruh:
        if collection == Collections.NONE:

            # average joes
            if not character.effects in [Effects.HAREM_KILLER, Effects.HOMIE_KILLER, Effects.SIDE_GIRL_KIDNAPPER, Effects.CREATURE_STOMPER]:
                text = f"{random.choice(character.quotes)}"
                effect_description = f"{str(collection)} - {str(character.effects)}"
                footer = f"Better luck next time, {str(ctx.author.display_name)}!"
            # villains:
            else:
                if character.name == "Thanatos":
                    if results.protected:
                        text = f"Calypso managed to evacuate {results.victim} before Thanatos could kill her! {HelperClass.annieYay}"
                        effect_description = f"{str(character.effects)} (denied) {HelperClass.novaGun}"
                        color = HelperClass.red
                        footer = f"You won't be this lucky next time, {str(ctx.author.display_name)}..."
                        filepath = f"./EternumGfGameImages/{character.filename}_denied.webp"
                    else:
                        effect_description = f"{str(character.effects)} {HelperClass.alexAngry}"
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
                        effect_description = f"{str(character.effects)} (denied) {HelperClass.novaGun}"
                        color = HelperClass.red
                        footer = "*groans*"
                        filepath = f"./EternumGfGameImages/{character.filename}_denied.webp"
                    else:
                        effect_description = f"{str(character.effects)} {HelperClass.alexAngry}"
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
                        effect_description = f"{str(character.effects)} (denied) {HelperClass.novaGun}"
                        color = HelperClass.red
                        footer = f"You messed with the wrong guy, cocksucker ({str(ctx.author.display_name)})!"
                        filepath = f"./EternumGfGameImages/{character.filename}_denied.webp"
                    else:
                        if results.victim != "Nobody":
                            text = f"Oh no! Axel kidnapped {results.victim} from your side girl harem, {str(ctx.author.display_name)}! {HelperClass.pepeCry2}"
                            effect_description = f"{str(character.effects)} {HelperClass.alexAngry}"
                        else:
                            text = f"Axel didn't find anyone to kidnap... Lucky you I guess, {str(ctx.author.display_name)}."
                            effect_description = f"{str(character.effects)} {HelperClass.alexAngry}"
                        color = HelperClass.black
                        footer = random.choice(character.quotes)

                elif character.name == "Golem":
                    if results.protected:
                        text = f"Pyramid Head managed to kill the troll before it could get its feet on " \
                               f"{str(ctx.author.display_name)}'s {results.victim}! {HelperClass.annieYay}"
                        effect_description = f"{str(character.effects)} (denied) {HelperClass.novaGun}"
                        color = HelperClass.red
                        footer = "*groans*"
                        filepath = f"./EternumGfGameImages/{character.filename}_denied.webp"
                    else:
                        if results.victim != "Nobody":
                            text = f"The golem stomped {results.victim} to death. They are no longer in your creatures " \
                                   f"group, {str(ctx.author.display_name)}! {HelperClass.pepeCry2}"
                            effect_description = f"{str(character.effects)} {HelperClass.alexAngry}"
                        else:
                            text = f"The golem didn't find anyone to trample on... Lucky you I guess, {str(ctx.author.display_name)}."
                            effect_description = f"{str(character.effects)} {HelperClass.alexAngry}"
                        color = HelperClass.black
                        footer = random.choice(character.quotes)
            if character.name == "Pyramid Head":
                color = HelperClass.blue

        # Collectibles
        else:
            text = f"{random.choice(character.quotes)}"
            effect_description = (
                f"{collection} "
                f"{'(duplicate) ' + HelperClass.annieCry if results.duplicate else '(new) ' + HelperClass.daliaParty}"
                f" - {character.effects}"
            )

            color = collection.color()
            footer = f"So close! Maybe next time, {str(ctx.author.display_name)}..." \
                if results.duplicate \
                else f"New {collection.member_desc()}, {str(ctx.author.display_name)}!"

        if not effect_description.strip() or not aliases.strip():
            print(f"Error: Embed fields for {character} (victim: {results.victim}, x2: {results.duplicate}, shield:"
                  f"{results.protected}) are empty.")

        image = discord.File(filepath, filename="gf.webp")

        if not image:
            print(f"Error: No image attached to embed of {character}.")

        embed = await HelperClass.createEmbed(title=character.name, text=text, color=color, footer=footer)
        embed.add_field(name=effect_description, value=aliases)
        embed.set_image(url="attachment://gf.webp")
        await ctx.send(file=image, embed=embed)

    async def updateDatabase(self, uid: int, character: CharacterCard, db, cursor) -> Results:
        """
        Performs all alterations to the database following a character draw.
        --------------------------------------------------------------------------------------------------------------------------------------------
        Parameters:
            - uid : int - the user's discord ID,
            - character : CharacterCard - the character prompting the database update,
            - db : sqlite3.connection - an existing connection to the database (DevNote 15/07/2025 - might want to make connection local to here),
            - cursor : sqlite3.Connection.Cursor - a cursor to perform SQL actions on the given database.
        --------------------------------------------------------------------------------------------------------------------------------------------
        Returns:
            - Results: A struct containing information whether the character obtained was a duplicate entry, protected from a villain, or what victim it chose as a villain.
        """
        try:
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
        except Exception as e:
            print(f"[Error Updating database] {e}")
            return None

        return Results(duplicate=duplicateCharacter, protected=protected, victim=victim)

    # COMMANDS

    @commands.command(aliases=['gfe', 'eternum gf', 'gf eternum'])
    @commands.check(check_channel)
    @check_user()
    async def egf(self, ctx):
        """
        The main command for the egf.
        ------------------------------------------------
        Parameters:
            - ctx : discord.ext.Context - discord-provided context to the command prompt.
        """
        db = sqlite3.connect("main.sqlite")
        cursor = db.cursor()
        discordID = str(ctx.author.id)
        
        uid = await self.accountManager.getUserID(discordID=discordID, cursor=cursor)
        # choose random character
        gf = random.choice(self.characters)
        # update database accordingly
        results = await self.updateDatabase(uid=uid, character=gf, cursor=cursor, db=db)
        if not results:
            await ctx.send(f"Sorry! I encountered an error updating the database for user {ctx.author.mention} with character {gf.name}.\n"\
                "Please contact @eisritter for further information & support.")
            return;
        # create according embed --> self.buildCharacterEmbed
        await self.buildCharacterEmbed(character=gf, results=results, ctx=ctx)

        db.commit()
        cursor.close()
        db.close()


    @commands.command()
    @commands.check(check_channel)
    @check_user()
    async def testegf(self, ctx):
        """
        The main testing command for the egf.
        ------------------------------------------------
        Parameters:
            - ctx : discord.ext.Context - discord-provided context to the command prompt.
        """

        db = sqlite3.connect("main.sqlite")
        cursor = db.cursor()
        discordID = str(ctx.author.id)
        for char in self.characters:
            for i in range(char.picNumber):
                print(f"Assessing character {char.name} for image {i+1}/{char.picNumber}")
                uid = await self.accountManager.getUserID(discordID=discordID, cursor=cursor)
                # choose random character
                gf = char #random.choice(self.characters)
                # update database accordingly
                results = await self.updateDatabase(uid=uid, character=gf, cursor=cursor, db=db)
                # create according embed --> self.buildCharacterEmbed
                await self.buildCharacterEmbed(character=gf, results=results, ctx=ctx, n=i+1)
                sleep(3)
        db.commit()
        cursor.close()
        db.close()


    async def collectionOverview(self, author, collection: Collections):
        db = sqlite3.connect("main.sqlite")
        cursor = db.cursor()
        discordID = str(author.id)
        user_name = str(author.display_name)

        #   search thru 'eternum_harem' table for entries
        uid = await self.accountManager.getUserID(discordID=discordID, cursor=cursor)

        count = 0
        members = []
        missing = []
        
        table = collection.table()
        cols = await get_cols(table_name=table, blacklist=collection.blacklist())
        total = len(cols)
        for c in cols:
            cursor.execute("SELECT %s FROM %s WHERE user_id=?" % (c, table), [uid])
            res = cursor.fetchone()
            if not res or res[0] == "NONE":
                missing.append(self.characterList.searchNameWithFilename(c))
            else:
                members.append(res[0])
                count += 1

        #   compile entries to list
        haremlist = "\n".join(members)
        missinglist = "\n".join(missing)

        c_title = "Eternum Harem" if collection == Collections.HAREM else str(collection)
        embed_title = f"{c_title} of **{user_name}**:"

        if haremlist == "":
            haremlist = f"You haven't collected anyone for your {str(collection)} yet..."

        if missinglist == "":
            missinglist = f"You have completed the {str(collection)}! {HelperClass.daliaParty}"
        #   build embed with categories 'got x/y' + names & 'missing z/y' + names --> + emotes?
        embed = discord.Embed(title=embed_title, color=collection.color())
        embed.add_field(name=f"Claimed ({count}/{total}):", value=haremlist)
        embed.add_field(name=f"Missing ({total - count}/{total}):", value=missinglist)

        cursor.close()
        db.close()

        return embed

    async def getMembers(self, author, collection: Collections) -> tuple:
        db = sqlite3.connect("main.sqlite")
        cursor = db.cursor()
        discordID = str(author.id)

        #   search thru 'eternum_harem' table for entries
        uid = await self.accountManager.getUserID(discordID=discordID, cursor=cursor)

        count = 0
        members = []
        
        table = collection.table()
        cols = await get_cols(table_name=table, blacklist=collection.blacklist())
        total = len(cols)
        for c in cols:
            cursor.execute("SELECT %s FROM %s WHERE user_id=?" % (c, table), [uid])
            res = cursor.fetchone()
            if res and res[0] != "NONE":
                members.append(res[0])
                count += 1

        cursor.close()
        db.close()

        return (members, (count, total))

    # There's work to do...
    @commands.command(aliases=['hareme', 'eternum harem', 'harem eternum'])
    @commands.check(check_channel)
    @check_user()
    async def eharem(self, ctx):
        """
        Provides an overview of a user's progress in collecting the eternum harem.
        ------------------------------------------------
        Parameters:
            - ctx : discord.ext.Context - discord-provided context to the command prompt.
        """
        await ctx.send(embed=await self.collectionOverview(ctx.author, Collections.HAREM))

    @commands.command(aliases=['thehomies', 'the homies', 'da homies', 'ehomies'])
    @commands.check(check_channel)
    @check_user()
    async def homies(self, ctx):
        """
        Provides an overview of a user's progress in collecting the eternum homies.
        ------------------------------------------------
        Parameters:
            - ctx : discord.ext.Context - discord-provided context to the command prompt.
        """
        await ctx.send(embed=await self.collectionOverview(ctx.author, Collections.THE_HOMIES))


    @commands.command(aliases=['sidegirls', 'sidechicks', 'esidegirls', 'epotentiallis'])
    @commands.check(check_channel)
    @check_user()
    async def sidedishes(self, ctx):
        """
        Provides an overview of a user's progress in collecting the eternum side girls.
        ------------------------------------------------
        Parameters:
            - ctx : discord.ext.Context - discord-provided context to the command prompt.
        """
        await ctx.send(embed=await self.collectionOverview(ctx.author, Collections.SIDE_DISHES))

    @commands.command(aliases=['pets'])
    @commands.check(check_channel)
    @check_user()
    async def creatures(self, ctx):
        """
        Provides an overview of a user's progress in collecting the eternum pets.
        DevNote 15/07/2025: might migrate to pets(ctx) instead - keep creatures as an alias or do a shell command like -gf.
        ------------------------------------------------
        Parameters:
            - ctx : discord.ext.Context - discord-provided context to the command prompt.
        """
        await ctx.send(embed=await self.collectionOverview(ctx.author, Collections.CREATURES))

    @commands.command()
    @commands.check(check_channel)
    @check_user()
    async def eprotectors(self, ctx):
        """
        Provides an overview of a user's progress in collecting the eternum protectors.
        ------------------------------------------------
        Parameters:
            - ctx : discord.ext.Context - discord-provided context to the command prompt.
        """
        db = sqlite3.connect("main.sqlite")
        cursor = db.cursor()
        discordID = str(ctx.author.id)
        user_name = str(ctx.author.display_name)

            
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

        cursor.close()
        db.close()


    @commands.command(aliases=['eternum collections', 'collectionsE', 'collections eternum'])
    @commands.check(check_channel)
    @check_user()
    async def eCollections(self, ctx):
        """
        Provides an overview of a user's progress in all eternum collections.
        ------------------------------------------------
        Parameters:
            - ctx : discord.ext.Context - discord-provided context to the command prompt.
        """
        db = sqlite3.connect("main.sqlite")
        cursor = db.cursor()
        discordID = str(ctx.author.id)
        user_name = str(ctx.author.display_name)

        embed_title = f"Eternum Collections of **{user_name}**:"
        embed = discord.Embed(title=embed_title, color=HelperClass.eternumBlue)


        # HAREM
        h_list, h_vals = await self.getMembers(ctx.author, Collections.HAREM)

        haremlist = "\n".join(h_list)

        if haremlist == "":
            haremlist = "You haven't collected anyone for your harem yet..."
        embed.add_field(name=f"Harem: ({h_vals[0]}/{h_vals[1]}):", value=haremlist)


        # HOMIES
        ho_list, ho_vals = await self.getMembers(ctx.author, Collections.HAREM)

        homielist = "\n".join(ho_list)

        if homielist == "":
            homielist = "You haven't collected any of the homies yet..."

        embed.add_field(name=f"Homies: ({ho_vals[0]}/{ho_vals[1]}):", value=homielist)


        # SIDE GIRLS
        s_list, s_vals = await self.getMembers(ctx.author, Collections.SIDE_DISHES)
        
        sideslist = "\n".join(s_list)

        if sideslist == "":
            sideslist = "You haven't collected any of the side girls yet..."
        embed.add_field(name=f"Side Girls: ({s_vals[0]}/{s_vals[1]}):", value=sideslist)

        # CREATURES
        c_list, c_vals = await self.getMembers(ctx.author, Collections.CREATURES)
        
        petlist = "\n".join(c_list)

        if petlist == "":
            petlist = "You haven't collected any of the side girls yet..."
        embed.add_field(name=f"Creatures: ({c_vals[0]}/{c_vals[1]}):", value=petlist)

        # Protectors

        members = []
        uid = await self.accountManager.getUserID(discordID=discordID, cursor=cursor)
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

        cursor.close()
        db.close()

    # ERROR MESSAGES

    @egf.error
    @commands.check(check_channel)
    @check_user()
    async def errorEgf(self, ctx, error):
        """
        Catches various errors in running the -egf command; Mostly cooldown infractions.
        ------------------------------------------------
        Parameters:
            - ctx : discord.ext.Context - discord-provided context to the command prompt,
            - error : str (?) - the error object to tell what the hell just happened.
        """
        # if cooldown not done send last gf from table 'eternum'
        db = sqlite3.connect("main.sqlite")
        cursor = db.cursor()

        discordID = str(ctx.author.id)
        uid = await self.accountManager.getUserID(discordID=discordID, cursor=cursor)
        
        if isinstance(error, commands.CommandOnCooldown):

            time = error.retry_after
            hours = int(time // 3600)
            minutes = int((time % 3600) // 60)
            seconds = int((time % 3600) % 60)

            description = f"You still have {hours}h {minutes} mins and {seconds}s until your next draw!"

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
        db.close()


def setup(client):
    client.add_cog(Eternum(client))
