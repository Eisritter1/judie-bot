# DISCORD.PY
import discord
from discord import app_commands
from discord.ext import commands
# OTHER LIBRARIES
import os
import random
import sqlite3
from dotenv import load_dotenv
from types import SimpleNamespace
# OWN LIBRARIES
from EgfCharacters import EgfCharacters
from EgfUtils import Collections, Results, Effects, CharacterCard, Villain
from Utilities import HelperClass, check_channel, get_cols
from AccountManager import AccountManager, check_user
from Timekeeper import check_cooldown, CommandOnCooldownError

load_dotenv()
GUILD = discord.Object(id=os.getenv("GUILD"))

async def help_eternum(interaction: discord.Interaction):
    field_names = []
    field_values = []

    title = "Judie's Eternum gf game!"
    description = "Here are the commands to use the eternum gf game:"

    field_names.append("/egf")
    field_values.append("pull a random gf from the eternum universe! (20hr cooldown)")

    field_names.append("/eternum_collections")
    field_values.append("get an overview of all your eternum collections!")

    field_names.append("/eternum_harem")
    field_values.append(
        "check your progress in the harem collection\n--> Contains **Alex, Annie, Calypso, Dalia, Luna, Nancy, Nova & Penny**")

    field_names.append("/eternum_homies")
    field_values.append(
        "check your progress in the homie collection\n--> Contains **Chang, Chop Chop, Mr. Hernandez, Jerry, Micaela, Noah, Orion & Raul**")

    field_names.append("/eternum_side_girls")
    field_values.append(
        "check your progress in the side girl collection\n--> Contains **Blue Fox Maiden, Eva, Idriel, Lorelei, Maat, Red Fox Maiden & Wenlin**")

    field_names.append("/eternum_pets")
    field_values.append(
        "check your progress in the creatures collection\n--> Contains **Carolyn, Igor, Kermit, Maurice, Maurice, Maurice, Pancho**")

    field_names.append("/eternum_protectors")
    field_values.append("Check your protections against various villains!\n--> Contains **Orion, Calypso, Dalia &"
                        " Pyramid Head**")

    field_names.append("__Further info__")
    field_values.append("For any other kind of information, feel free to contact **eisritter**!")

    embed = discord.Embed(title=title, description=description, color=HelperClass.eternumBlue)
    embed.set_footer(text="WARNING: All of Judie's features contain spoilers to players who are not up to the current version" \
             " of Eternum.")

    for i in range(0, len(field_names)):
        embed.add_field(name=field_names[i], value=field_values[i], inline=False)

    await interaction.response.send_message(embed=embed)


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
        self.characterList = EgfCharacters()
        self.characters = self.characterList.characters
        self.botSpamChannel = None
        self.db_path = client.db_path

    # Development Start 17/08/2022; Version 1.0.

    # HELPER FUNCTIONS - checkUser in AccountManager // createEmbed in Utilities/HelperFunctions

    async def buildCharacterEmbed(self, character: CharacterCard, results: Results, interaction: discord.Interaction, n: int = -1) -> bool:
        """
        Builds and sends the egf embed using info from the provided CharacterCard.
        ---------------------------------------------------------------------------------------------------
        Parameters:
            - character : CharacterCard - the character whose card is to be built,
            - results : Results - a struct used to determine what happened to be displayed,
            - ctx : discord.ext.Context - discord context object for user info,
            - n : int - the index of chosen picture; chooses a random picture if n=-1 (defaults to -1).
        ---------------------------------------------------------------------------------------------------
        """
        if not character:
            print("Error: Missing character object.")
            return False

        # variable initialization
        author=str(interaction.user.display_name)

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
            await interaction.response.send_message(f"Error building embed for character {character.name}: Couldn't find image no. {number}", ephemeral=True)
            return False

        collection = character.collection

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
            footer = f"So close! Maybe next time, {author}..." \
                if results.duplicate \
                else f"New {collection.member_desc()}, {author}!"

        if not effect_description.strip() or not aliases.strip():
            print(f"Error: Embed fields for {character.name} (victim: {results.victim}, x2: {results.duplicate}, shield:"
                  f"{results.protected}) are empty.")
            return False

        image = discord.File(filepath, filename="gf.webp")

        if not image:
            print(f"Error: No image attached to embed of {character}.")

        embed = await HelperClass.createEmbed(title=character.name, text=text, color=color, footer=footer)
        embed.add_field(name=effect_description, value=aliases)
        embed.set_image(url="attachment://gf.webp")
        await interaction.response.send_message(file=image, embed=embed)
        return True


    async def updateDatabase(self, uid: int, character: CharacterCard) -> Results:
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
        db = sqlite3.connect(self.db_path)
        cursor = db.cursor()

        try:
            duplicateCharacter = False
            protected = False
            victim = "Nobody"

            cursor.execute("UPDATE eternum SET last_gf = ? WHERE user_id = ?", [character.name, uid])

            # early exit if not interesting
            if character.collection == Collections.NONE and character.effects == Effects.NONE:
                db.commit()
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

            cursor.close()
            db.close()
            return None

        cursor.close()
        db.close()
        return Results(duplicate=duplicateCharacter, protected=protected, victim=victim)


    async def collectionOverview(self, author: discord.User, collection: Collections):
        discordID = str(author.id)
        user_name = str(author.display_name)

        members, missing, count, total = await self.getCollectionProgress(discordID, collection)

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

        return embed


    async def getCollectionProgress(self, discordID, collection: Collections) -> tuple[list]:
        db = sqlite3.connect(self.db_path)
        cursor = db.cursor()

        #   search thru 'eternum_harem' table for entries
        uid = await self.accountManager.getUserID(discordID=discordID)

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
                missing.append(await self.characterList.searchNameWithFilename(c))
            else:
                members.append(await self.characterList.searchNameWithFilename(c))
                count += 1

        cursor.close()
        db.close()
        
        return (members, missing, count, total)


    async def getMembers(self, author, collection: Collections) -> tuple:
        db = sqlite3.connect(self.db_path)
        cursor = db.cursor()
        discordID = str(author.id)

        uid = await self.accountManager.getUserID(discordID=discordID)

        count = 0
        members = []
        
        table = collection.table()
        cols = await get_cols(table_name=table, blacklist=collection.blacklist())
        total = len(cols)
        for c in cols:
            cursor.execute("SELECT %s FROM %s WHERE user_id=?" % (c, table), [uid])
            res = cursor.fetchone()
            if res and res[0] != 0:
                members.append(await self.characterList.searchNameWithFilename(c))
                count += 1

        cursor.close()
        db.close()

        return (members, (count, total))


    async def resolveUser(self, uid: str, interaction: discord.Interaction):

        user = SimpleNamespace(id=-1, display_name="Dummy#0001")
        if uid != "None":
            uid = await AccountManager.receiveDiscordIDFromInput(interaction, uid)
            if uid == -1:
                return interaction.user

            if uid == interaction.user.id:
                user = interaction.user
            else:
                user.id = uid
                user.display_name = f"User {uid}"
        else:
            user = interaction.user

        return user


    # DISCORD COMMANDS (no intricate logic here, all wrapping the logic above to discord callable! for testing reasons :D)

    @app_commands.guilds(GUILD)
    @app_commands.command(name="egf", description="Draw an Eternum character to be your partner for the day.")
    @app_commands.check(check_channel)
    @check_cooldown()
    @check_user()
    async def egf(self, interaction: discord.Interaction):
        """
        The main command for the egf.
        ------------------------------------------------
        Parameters:
            - ctx : discord.ext.Context - discord-provided context to the command prompt.
        """
        discordID = str(interaction.user.id)
        
        uid = await self.accountManager.getUserID(discordID=discordID)
        # choose pseudo-random character
        gf = random.choice(self.characters)
        # update database accordingly
        results = await self.updateDatabase(uid=uid, character=gf)
        if not results:
            await interaction.response.send_message(f"Sorry! I encountered an error updating the database for user {interaction.user.mention} with character {gf.name}.\n"\
                "Please contact @eisritter for further information & support.", ephemeral=True)
            return;
        # create according embed --> self.buildCharacterEmbed
        await self.buildCharacterEmbed(character=gf, results=results, interaction=interaction)

        
    @app_commands.guilds(GUILD)
    @app_commands.command(name="eternum_harem", description="View a user's progress on the Eternum harem collection (ex eharem). Defaults to your User ID")
    @commands.check(check_channel)
    async def eharem(self, interaction: discord.Interaction, uid: str="None"):
        """
        Provides an overview of a user's progress in collecting the eternum harem.
        ------------------------------------------------
        Parameters:
            - ctx : discord.ext.Context - discord-provided context to the command prompt.
        """
        user = await self.resolveUser(uid, interaction)

        # check whether the user is registered.
        if not await AccountManager.verifyUser(discord_id=user.id, interaction=interaction, expectFail=False):
            return

        # if user is registered, proceed.
        await interaction.response.send_message(embed=await self.collectionOverview(user, Collections.HAREM))
        
    @app_commands.guilds(GUILD)
    @app_commands.command(name="eternum_homies", description="View a user's progress on the Eternum homies collection (ex ehomies). Defaults to your User ID")
    @commands.check(check_channel)
    async def homies(self, interaction: discord.Interaction, uid: str="None"):
        """
        Provides an overview of a user's progress in collecting the eternum homies.
        ------------------------------------------------
        Parameters:
            - ctx : discord.ext.Context - discord-provided context to the command prompt.
        """
        user = await self.resolveUser(uid, interaction)

        # check whether the user is registered.
        if not await AccountManager.verifyUser(discord_id=user.id, interaction=interaction, expectFail=False):
            return

        # if user is registered, proceed.
        await interaction.response.send_message(embed=await self.collectionOverview(interaction.user, Collections.THE_HOMIES))
        
    @app_commands.guilds(GUILD)
    @app_commands.command(name="eternum_side_girls", description="View a user's progress on the Eternum side girls collection (ex sidegirls). Defaults to your User ID")
    @commands.check(check_channel)
    async def sidegirls(self, interaction: discord.Interaction, uid: str="None"):
        """
        Provides an overview of a user's progress in collecting the eternum side girls.
        ------------------------------------------------
        Parameters:
            - ctx : discord.ext.Context - discord-provided context to the command prompt.
        """
        user = await self.resolveUser(uid, interaction)

        # check whether the user is registered.
        if not await AccountManager.verifyUser(discord_id=user.id, interaction=interaction, expectFail=False):
            return

        # if user is registered, proceed.
        await interaction.response.send_message(embed=await self.collectionOverview(interaction.user, Collections.SIDE_DISHES))

    @app_commands.guilds(GUILD)
    @app_commands.command(name="eternum_pets", description="View a user's progress on the Eternum pets collection (ex creatures). Defaults to your User ID")
    @commands.check(check_channel)
    async def creatures(self, interaction: discord.Interaction, uid: str="None"):
        """
        Provides an overview of a user's progress in collecting the eternum pets.
        DevNote 15/07/2025: might migrate to pets(ctx) instead - keep creatures as an alias or do a shell command like -gf.
        ------------------------------------------------
        Parameters:
            - ctx : discord.ext.Context - discord-provided context to the command prompt.
        """
        user = await self.resolveUser(uid, interaction)

        # check whether the user is registered.
        if not await AccountManager.verifyUser(discord_id=user.id, interaction=interaction, expectFail=False):
            return

        # if user is registered, proceed.
        await interaction.response.send_message(embed=await self.collectionOverview(interaction.user, Collections.CREATURES))

    @app_commands.guilds(GUILD)
    @app_commands.command(name="eternum_protectors", description="View a user's Eternum protection racket (ex eprotectors). Defaults to your User ID")
    @commands.check(check_channel)
    async def eprotectors(self, interaction: discord.Interaction, uid: str="None"):
        """
        Provides an overview of a user's progress in collecting the eternum protectors.
        ------------------------------------------------
        Parameters:
            - ctx : discord.ext.Context - discord-provided context to the command prompt.
        """
        user = await self.resolveUser(uid, interaction)

        # check whether the user is registered.
        if not await AccountManager.verifyUser(discord_id=user.id, interaction=interaction, expectFail=False):
            return

        # if user is registered, proceed.
        db = sqlite3.connect(self.db_path)
        cursor = db.cursor()
        discordID = str(user.id)
        user_name = str(user.display_name)

            
        #   search thru 'eternum_harem' table for entries
        uid = await self.accountManager.getUserID(discordID=discordID)
        members = []
        cursor.execute("SELECT orion, calypso, dalia, pyramid_head FROM eternum WHERE user_id = ?", [uid])
        yesno = cursor.fetchone()
        sides = f"**Side Girls:**\nOrion: {'✅' if yesno[0] == 1 else ':x:'}"
        members.append(sides)

        harem = f"**Harem:**\nCalypso: {'✅' if yesno[1] == 1 else ':x:'}"
        members.append(harem)
        
        homies = f"**Homies:**\nDalia: {'✅' if yesno[2] == 1 else ':x:'}"
        members.append(homies)

        creatures = f"**Creatures:**\nPyramid Head: {'✅' if yesno[3] == 1 else ':x:'}"
        members.append(creatures)

        #   compile entries to list
        protectorlist = "\n".join(members)

        embed_title = f"Eternum Protectors of **{user_name}**:"
        #   build embed (color blue) with categories 'got x/y' + names & 'missing z/y' + names --> + emotes?
        embed = discord.Embed(title=embed_title, description=protectorlist, color=HelperClass.blue)
        await interaction.response.send_message(embed=embed)

        cursor.close()
        db.close()


    @app_commands.guilds(GUILD)
    @app_commands.command(name="eternum_collections", description="View a user's Eternum collections portfolio (ex ecollections). Defaults to your User ID.")
    @commands.check(check_channel)
    async def eCollections(self, interaction: discord.Interaction, uid: str="None"):
        """
        Provides an overview of a user's progress in all eternum collections.
        ------------------------------------------------
        Parameters:
            - ctx : discord.ext.Context - discord-provided context to the command prompt.
        """
        user = await self.resolveUser(uid, interaction)

        # check whether the user is registered.
        if not await AccountManager.verifyUser(discord_id=user.id, interaction=interaction, expectFail=False):
            return

        # if user is registered, proceed.
        db = sqlite3.connect(self.db_path)
        cursor = db.cursor()
        discordID = str(user.id)
        user_name = str(user.display_name)

        embed_title = f"Eternum Collections of **{user_name}**:"
        embed = discord.Embed(title=embed_title, color=HelperClass.eternumBlue)


        # HAREM
        h_list, h_vals = await self.getMembers(user, Collections.HAREM)

        haremlist = "\n".join(h_list)

        if haremlist == "":
            haremlist = "You haven't collected anyone for your harem yet..."
        embed.add_field(name=f"Harem: ({h_vals[0]}/{h_vals[1]}):", value=haremlist)


        # HOMIES
        ho_list, ho_vals = await self.getMembers(user, Collections.THE_HOMIES)

        homielist = "\n".join(ho_list)

        if homielist == "":
            homielist = "You haven't collected any of the homies yet..."

        embed.add_field(name=f"Homies: ({ho_vals[0]}/{ho_vals[1]}):", value=homielist)


        # SIDE GIRLS
        s_list, s_vals = await self.getMembers(user, Collections.SIDE_DISHES)
        
        sideslist = "\n".join(s_list)

        if sideslist == "":
            sideslist = "You haven't collected any of the side girls yet..."
        embed.add_field(name=f"Side Girls: ({s_vals[0]}/{s_vals[1]}):", value=sideslist)

        # CREATURES
        c_list, c_vals = await self.getMembers(user, Collections.CREATURES)
        
        petlist = "\n".join(c_list)

        if petlist == "":
            petlist = "You haven't collected any of the side girls yet..."
        embed.add_field(name=f"Creatures: ({c_vals[0]}/{c_vals[1]}):", value=petlist)

        # Protectors

        members = []
        uid = await self.accountManager.getUserID(discordID=discordID)
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

        await interaction.response.send_message(embed=embed)

        cursor.close()
        db.close()

    # ERROR MESSAGES

    @egf.error
    @commands.check(check_channel)
    @check_user()
    async def errorEgf(self, interaction: discord.Interaction, error: app_commands.AppCommandError):
        """
        Catches various errors in running the -egf command; Mostly cooldown infractions.
        ------------------------------------------------
        Parameters:
            - ctx : discord.ext.Context - discord-provided context to the command prompt,
            - error : str (?) - the error object to tell what the hell just happened.
        """
        # if cooldown not done send last gf from table 'eternum'
        db = sqlite3.connect(self.db_path)
        cursor = db.cursor()

        discordID = str(interaction.user.id)
        
        if isinstance(error, CommandOnCooldownError):
            uid = await self.accountManager.getUserID(discordID=discordID)

            time = error.retry_after

            description = f"You still have {time.get_time()} until your next draw!"

            cursor.execute("SELECT last_gf FROM eternum WHERE user_id=?", [uid])
            lastGf = cursor.fetchone()
            gf = ""
            field_name = ""
            field_value = ""
            field2_name = ""
            field2_value = ""
            number = 0
            if lastGf is None or lastGf[0] is None:
                title = "This is awkward..."
                field_name = "Your last pull is... No one?"
                field_value = "How could that happen..."
                footer = "Might as well contact eisritter, sumn ain't right"

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
            if lastGf is not None or lastGf[0] is not None:
                number = random.randint(1, gf.picNumber)
                image = discord.File(f"./EternumGfGameImages/{gf.filename}_{number}.webp", filename="gf.webp")
            else:
                image = discord.File("./EternumGfGameImages/None.webp", filename="gf.webp")
            embed.set_image(url="attachment://gf.webp")
            await interaction.response.send_message(file=image, embed=embed, ephemeral=True)

        elif not interaction.response.is_done():
            await interaction.response.send_message(f"Unexpected error drawing egf: {error}", ephemeral=True)

        cursor.close()
        db.close()


    async def setup(client):
        cog = Eternum(client)
        await client.add_cog(cog)
        cog.botSpamChannel = cog.client.config.botSpamChannel
        print("successfully activated Eternum cog.")
