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
from CharacterCard import CharacterCard, Villain
from AccountManager import AccountManager, check_deployment, check_user
from EgfCharacters import EgfCharacters

async def help_eternum(ctx):
    field_names = []
    field_values = []

    title = "Judie's Eternum gf game!"
    description = "Here are the commands to use the eternum gf game:"

    field_names.append("-egf (eternum gf)")
    field_values.append("pull a random gf from the eternum universe! (20hr cooldown)")

    field_names.append("-eCollections (eternum collections)")
    field_values.append("get an overview of all your eternum collections!")

    field_names.append("-eharem (eternum harem)")
    field_values.append(
        "check your progress in the harem collection\n--> Contains **Alex, Annie, Calypso, Dalia, Luna, Nancy, Nova & Penny**")

    field_names.append("-homies (the homies)")
    field_values.append(
        "check your progress in the homie collection\n--> Contains **Chang, Chop Chop, Mr. Hernandez, Jerry, Micaela, Noah, Orion & Raul**")

    field_names.append("-sidegirls")
    field_values.append(
        "check your progress in the side girl collection\n--> Contains **Blue Fox Maiden, Eva, Idriel, Lorelei, Maat, Red Fox Maiden & Wenlin**")

    field_names.append("-creatures")
    field_values.append(
        "check your progress in the creatures collection\n--> Contains **Carolyn, Igor, Kermit, Maurice, Maurice, Maurice, Pancho**")

    field_names.append("-eprotectors")
    field_values.append("Check your protections against various villains!\n--> Contains **Orion, Calypso, Dalia &"
                        " Pyramid Head**")

    field_names.append("__Further info__")
    field_values.append("For any other kind of information, feel free to contact **eisritter**!")

    footer = "WARNING: All of Judie's features contain spoilers to players who are not up to the current version" \
             " of Eternum."

    embed = discord.Embed(title=title, description=description, color=HelperClass.orange)
    embed.set_footer(text=footer)

    for i in range(0, len(field_names)):
        embed.add_field(name=field_names[i], value=field_values[i], inline=False)

    await ctx.send(embed=embed)


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
            return

        # variable initialization
        author=str(ctx.author.display_name)

        embed = ""
        image = ""
        text = ""
        footer = ""
        effect_description = ""
        aliases = "*No aliases*" if character.aliases == "no aliases" else f"*a.k.a. {character.aliases}*"
        color = HelperClass.eternumBlue

        number = n if (n > 0 and n <= character.picNumber) else random.randint(1, character.picNumber)
        filepath = f"./EternumGfGameImages/{character.filename}_{number}.webp"

        # error message & early exit if file unrecognized.
        if not os.path.exists(filepath):
            print(f"Error: file {filepath} not found.")
            await ctx.send(f"Error building embed for character {character.name}: Couldn't find image no. {number}")
            return

        collection = character.collection

        # This needs to include Pyramid Head :PepeBruh:
        if collection == Collections.NONE:

            # villains
            if isinstance(character, Villain):
                # case: villain was denied
                if results.protected:
                    text = f"{character.protected_message(victim=results.victim, author=author)} {HelperClass.annieYay}"
                    effect_description = f"{str(character.effects)} (denied) {HelperClass.novaGun}"
                    color = HelperClass.red
                    footer = character.get_footer(author=author)
                    filepath = f"./EternumGfGameImages/{character.filename}_denied.webp"
                # case: villain unchecked
                else:
                    if results.victim != "Nobody":
                        text = f"{character.kill_message(victim=results.victim, author=author)} {HelperClass.pepeCry2}"
                        effect_description = f"{str(character.effects)} {HelperClass.alexAngry}"
                    else:
                        text = character.empty_message(author=author)
                        effect_description = f"{str(character.effects)} {HelperClass.alexAngry}"
                    color = HelperClass.black
                    footer = random.choice(character.quotes)
            # pyramid head (only non-collectible protector so far...)
            # average joe schmoes
            else:
                if character.name == "Pyramid Head":
                    color = HelperClass.blue
                text = f"{random.choice(character.quotes)}"
                effect_description = f"{str(collection)} - {str(character.effects)}"
                footer = f"Better luck next time, {author}!"

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
            print(f"Error: Embed fields for {character.name} (victim: {results.victim}, x2: {results.duplicate}, shield:"
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
            victim = "Nobody"

            cursor.execute("UPDATE eternum SET last_gf = ? WHERE user_id = ?", [character.name, uid])

            # early exit if not interesting
            if character.collection == Collections.NONE and character.effects == Effects.NONE:
                return Results(duplicate=duplicateCharacter, protected=protected, victim=victim)

            # character collection update
            if character.collection is not Collections.NONE:
                # get collection table and last_item column names
                table = character.collection.table()
                last = character.collection.lastColName()

                # check for duplication. Is duplicate if value @ table == 1 else 0 => 1st result[0] to bool.
                cursor.execute("SELECT %s FROM %s WHERE user_id=?" % (character.filename, table), [uid])
                duplicate = bool(cursor.fetchone()[0])
                if not duplicate:
                    cursor.execute("UPDATE %s SET %s=1 WHERE user_id=?" % (table, character.filename), [uid])
                else:
                    duplicateCharacter = True
                
                # update last_item_collected value
                cursor.execute("UPDATE %s SET %s=? WHERE user_id=?" % (table, last), [character.filename, uid])

            # character effect update
            protected, victim = character.effects.action()(cursor, uid, self.characters)

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
        # choose pseudo-random character
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
    # command should be unavailable to main bot.
    @check_deployment("DEBUG")
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
                gf = char
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
            if not res or res[0] == 0:
                missing.append(self.characterList.searchNameWithFilename(c))
            else:
                members.append(self.characterList.searchNameWithFilename(c))
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
            if res and res[0] != 0:
                members.append(self.characterList.searchNameWithFilename(c))
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
        ho_list, ho_vals = await self.getMembers(ctx.author, Collections.THE_HOMIES)

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
