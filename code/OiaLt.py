# DISCORD.PY
import discord
from discord import app_commands
from discord.ext import commands
# OTHER LIBRARIES
import os, random, sqlite3
from dotenv import load_dotenv
# OWN LIBRARIES
from OgfCharacters import OgfCharacters
from OgfUtils import Collections, Effects, Results, CharacterCard
from Utilities import HelperClass, check_channel, get_cols
from AccountManager import AccountManager, check_user
from Timekeeper import check_cooldown, TimeObject, CommandOnCooldownError


load_dotenv()
GUILD = discord.Object(id=os.getenv("GUILD"))

# Help function
async def help_oialt(interaction: discord.Interaction):
    field_names = []
    field_values = []

    title = "Judie's OiaLt gf game!"
    description = "Here are the commands to use the oialt gf system!"

    field_names.append("/ogf")
    field_values.append("pull a random gf from the OiaLt world! (20h cooldown!)")

    field_names.append("/oialt_collections")
    field_values.append("Get an overview of all your oialt collections!")

    field_names.append("/oialt_harem")
    field_values.append(
        "check your progress in the LI collection!\n--> Contains **Judie, Lauren, Messy Hair Lauren, " \
        "Carla, Iris, Aiko, Jasmine & Rebecca**.")

    field_names.append("/oialt_stabby_clan")
    field_values.append(
        "check your progress in the stabby mike collection!\n--> Contains **Stabby Police, Hitman Mike, " \
        "Anastasia, Yakuza Mike, Priest Mike & Mike the Exterminator**.")

    field_names.append("/oialt_homies")
    field_values.append(
        "check your progress in the boys collection!\n--> Contains **MC, Tom, Fit Jack, Oliver, Asmodeus & " \
        "Hiromi**.")

    field_names.append("/oialt_side_girls")
    field_values.append(
        "check your progress in the potential LI collection!\n--> Contains **Ava, Lilith, Fit Jack's "
        "Groupie, Train Conductor, Shop Girl & Stone Elephant**.")

    field_names.append("/oialt_protectors")
    field_values.append("Check your protections against the different villains!\n--> Contains **Funtime, MC, Aiko "
                        "and 93**.")

    field_names.append("__Further info__")
    field_values.append("For any other kind of information, feel free to contact **eisritter**!")

    footer = "WARNING: All of Judie's features contain spoilers to players who are not up to the current version" \
             " of Eternum."

    embed = discord.Embed(title=title, description=description, color=HelperClass.orange)
    embed.set_footer(text=footer)

    for i in range(0, len(field_names)):
        embed.add_field(name=field_names[i], value=field_values[i], inline=False)

    await interaction.response.send_message(embed=embed)

class OiaLt(commands.Cog):
    """
    Judie's OiaLt GF game cog.
    -------------------------------------
    Members:
        - activate(): Initializes the cog's variables according to config data.
        - 
    """
    def __init__(self, client):
        self.client = client
        self.characterList = OgfCharacters()
        self.characters = self.characterList.characters
        self.accountManager = AccountManager(self.client)
        self.botSpamChannel = None
        self.db_path = client.db_path
        

    # HELPER FUNCTIONS - checkUser in AccountManager // createEmbed in Utilities/HelperClass

    async def displayLastGF(self, interaction: discord.Interaction, time: TimeObject):
        """
        Shows the last character obtained by a character as cooldown reminder.
        -------------------------------------------------------------------------
        Parameters:
            - ctx : discord.ext.Context - discord-provided context to the command prompt.
            - time : int - time in seconds left until the cooldown runs out.
        """
        description = f"You still have {time.get_time()} until your next draw!"
        db = sqlite3.connect("main.sqlite")
        cursor = db.cursor()
        discordID = str(interaction.user.id)

        uid = await self.accountManager.getUserID(discordID=discordID)

        # Get last obtained character
        cursor.execute("SELECT last_gf FROM oialt WHERE user_id=?", [uid])
        lastGf = cursor.fetchone()
        if lastGf is not None and lastGf[0] is not None:
            name = (await self.characterList.getCharacter(lastGf[0])).filename
        else:
            name = "None"

        if name != "None":
            title = "Slow down dude!"
            field_name = lastGf[0]
            field_value = f"The last pull you made was {field_name}"
            footer = "retry later mate..."
        else:
            title = "This is awkward..."
            field_name = "Your last pull is... No one?"
            field_value = "How could that happen..."
            footer = "Might as well contact Eisritter#6969, sumn ain't right"

        embed = discord.Embed(title=title, description=description, color=HelperClass.orange)
        embed.set_footer(text=footer)

        embed.add_field(name=field_name, value=field_value, inline=True)

        image = discord.File(f"./gfGameImages/{name}.webp", filename="gf.webp")
        embed.set_image(url="attachment://gf.webp")
        await interaction.response.send_message(file=image, embed=embed, ephemeral=True)

        cursor.close()
        db.close()


    async def createAndSendEmbed(self, interaction: discord.Interaction, character: CharacterCard, results: Results):
        """
        Creates and sends an embed using the provided character information.
        -------------------------------------------------------------------------
        Parameters:
            - ctx : discord.ext.Context - discord-provided context to the command prompt.
            - character : OgfCharacterCard - the card of the character to display.
            - results : OgfResults - A struct containing context of the consequences of the character draw.
        """
        if not character:
            print("Error: Missing character object.")

        collection = character.collection
        effect = character.effect

        embed = ""
        image = ""
        text = ""
        footer = character.footer
        duplicateText = "" if collection == Collections.NONE and effect == Effects.NONE else f"(New) {HelperClass.daliaParty}" if not results.duplicate else f"(duplicate) {HelperClass.annieCry}"
        collection_field_name = f"{str(collection)} {duplicateText}"
        collection_field_value = ""
        effect_field_name = str(effect)
        effect_field_value = effect.Describe()

        # non-collectibles
        if collection == Collections.NONE:
            text = f"Congrats, {interaction.user.mention}...? Your companion for the day is {character.name}."
            collection_field_value = "A character that doesn't belong into any collection."

            # Special case - Spiderman (includes author username in footer)
            if character.name == "Spiderman":
                displayname = interaction.user.display_name
                footer = f"Hey, is there a {displayname}? I have a pizza for {displayname}!"
       
        #region Harem
        elif collection == Collections.HAREM:
            text = f"Congratulations {interaction.user.mention}! Your gf for the day is {character.name}!"
            collection_field_value = f"A wild {character.name} has spawned in your harem!" if not results.duplicate \
                else f"Tough luck! {character.name} is already in your harem!"
        #endregion
        #region Stabby Clan
        elif collection == Collections.STABBIES:
            text = f"Congratulations {interaction.user.mention}! Your protector for the day is {character.name}!"
            collection_field_value = f"A new recruit for the stabby clan!" if not results.duplicate \
                else f"Tough luck! {character.name} is already part of your bodyguard staff!"
        #endregion
        #region The Boys
        elif collection == Collections.BOYS:
            text = f"Congratulations {interaction.user.mention}! Your homie for the day is {character.name}!"
            collection_field_value = f"Let's fucking goo! {character.name} joined the squad!" if not results.duplicate \
                else f"Tough luck! {character.name} is already chilling with you!"
        #endregion
        #region Potential LI's
        elif collection == Collections.POTENTIALS:
            text = f"Congrats {interaction.user.mention}! Your gf for the day is {character.name}!"
            collection_field_value = f"{character.name} has joined the gang! Might consider asking her out? :wink:" if not results.duplicate \
                else f"Tough luck! {character.name} has already expressed her interest in you!"

            if interaction.user.name == "frostkanra":
                text = "Well, well, well... if this were real life, a creator-createe relationship wouldn't be so " \
                       "acceptable now, would it...?"
        #endregion

        #region Orochi
        if effect == Effects.HAREM_BUYER:
            text = f"Yikes! Your company for the day is {character.name}. Good luck {interaction.user.mention} (You'll need it!)"
            if results.protected:
                collection_field_name = f"Bid for {results.victim} refused."
                collection_field_value = f"GODDAMN IT, WHY AREN'T YOU LAUGHING OROCHI??!"
            else:
                collection_field_name = "**OH NO**"
                collection_field_value = f"Orochi offered a deal for {results.victim} you couldn't refuse..." if \
                    results.victim != "Nobody" else f"Must have been the wind..."
        #endregion
        #region Astaroth
        if effect == Effects.STABBY_KILLER:
            text = f"Yikes! Your company for the day is {character.name}. Good luck {interaction.user.mention} (You'll need it!)"
            if results.protected:
                collection_field_name = f"That was close..."
                collection_field_value = f"The MC managed to body Astaroth before he could kill {results.victim}!"
            else:
                collection_field_name = "**OH SHIT**"
                collection_field_value = f"Astaroth shot {results.victim} dead. R.I.P." if \
                    results.victim != "Nobody" else f"Must have been the wind..."
        #endregion
        #region Azazel
        if effect == Effects.BOYS_KILLER:
            text = f"Yikes! Your company for the day is {character.name}. Good luck {interaction.user.mention} (You'll need it!)"
            if results.protected:
                collection_field_name = f"That was close..."
                collection_field_value = f"Watch {results.victim}'s back, buddy."
            else:
                collection_field_name = "**OH SHIT**"
                collection_field_value = f"Azazel put {results.victim} to sleep forever! R.I.P." if \
                    results.victim != "Nobody" else f"Must have been the wind..."
        #endregion
        #region Monster Lilith
        if effect == Effects.POTENTIAL_MUTATOR:
            text = f"Yikes! Your company for the day is {character.name}. Good luck {interaction.user.mention} (You'll need it!)"
            if results.protected:
                collection_field_name = f"That was close..."
                collection_field_value = f"93 managed to turn the monster's gaze away from {results.victim}!"
            else:
                collection_field_name = "**OH SHIT**"
                collection_field_value = f"{results.victim} just turned into a living set of spare ribs in front of you!" if \
                    results.victim != "Nobody" else f"Must have been the wind..."
        #endregion


        #region Embed compilation and sending
        embed = await HelperClass.createEmbed(title=character.name, text=text, footer=footer)

        embed.add_field(name=collection_field_name, value=collection_field_value, inline=True)
        embed.add_field(name=effect_field_name, value=effect_field_value, inline=True)

        image = discord.File(f"./gfGameImages/{character.filename}.webp", filename="gf.webp")
        embed.set_image(url="attachment://gf.webp")
        await interaction.response.send_message(file=image, embed=embed)
        #endregion


    async def updateDatabase(self, uid: int, character: CharacterCard) -> Results:
        """
        Performs the changes to the database following a character's drawing.
        -------------------------------------------------------------------------
        Parameters:
            - uid : int - the user's ID in the database system.
            - character : OgfCharacterCard - the character drawn.
        -------------------------------------------------------------------------
        Returns:
            - OgfResults: A struct containing context around the draw - duplicate collectible, protected against a villain, and chosen victim.
        """
        # Setup: DB connections
        db = sqlite3.connect("main.sqlite")
        cursor = db.cursor()

        # Setup: Results variables
        duplicate = False
        target = None
        protected = False

        # Update last obtained character
        cursor.execute("UPDATE oialt SET last_gf=? WHERE user_id=?", [character.name, uid])

        # Switch Collections:
        if character.collection == Collections.HAREM:
            # Update collection's last obtained
            cursor.execute("UPDATE oialt_harem SET last_li=? WHERE user_id=?", [character.filename, uid])

            # Check if already in collection
            cursor.execute("SELECT %s FROM oialt_harem WHERE user_id=?" % character.filename, [uid])
            check = cursor.fetchone()
            # If not, add to collection
            if not check[0]:
                cursor.execute("UPDATE oialt_harem SET %s=1 WHERE user_id=?" % character.filename, [uid])
            # Else mark as duplicate
            else:
                duplicate = True
        
        elif character.collection == Collections.STABBIES:
            # Update collection's last obtained
            cursor.execute("UPDATE stabby_mikes SET last_mike=? WHERE user_id=?", [character.filename, uid])

            # Check if already in collection
            cursor.execute("SELECT %s FROM stabby_mikes WHERE user_id=?" % character.filename, [uid])
            check = cursor.fetchone()
            # If not, add to collection
            if not check[0]:
                cursor.execute("UPDATE stabby_mikes SET %s=1 WHERE user_id=?" % character.filename, [uid])
            # Else mark as duplicate
            else:
                duplicate = True
        
        elif character.collection == Collections.BOYS:
            # Update Collection's last obtained
            cursor.execute("UPDATE the_boys SET last_boi=? WHERE user_id=?", [character.filename, uid])

            # Check if already in collection
            cursor.execute("SELECT %s FROM the_boys WHERE user_id=?" % character.filename, [uid])
            check = cursor.fetchone()
            # If not, add to collection
            if not check[0]:
                cursor.execute("UPDATE the_boys SET %s=1 WHERE user_id=?" % character.filename, [uid])
            # Else mark as duplicate
            else:
                duplicate = True
        
        elif character.collection == Collections.POTENTIALS:
            # Update Collection's last obtained
            cursor.execute("UPDATE li_potential SET last_potential_li=? WHERE user_id=?", [character.filename, uid])

            # Check if already in collection
            cursor.execute("SELECT %s FROM li_potential WHERE user_id=?" % character.filename, [uid])
            check = cursor.fetchone()
            # If not, add to collection
            if not check[0]:
                cursor.execute("UPDATE li_potential SET %s=1 WHERE user_id=?" % character.filename, [uid])
            # Else mark as duplicate
            else:
                duplicate = True
        
        # Switch Effectors:
        if character.effect in [Effects.HAREM_SAVER, Effects.STABBY_SAVER, Effects.BOYS_SAVER, Effects.POTENTIAL_SAVER]:
            # Check if protection is already obtained
            cursor.execute("SELECT %s FROM oialt WHERE user_id=?" % character.filename, [uid])
            check = cursor.fetchone()
            # If not, add to user
            if not check[0]:
                cursor.execute("UPDATE oialt SET %s=1 WHERE user_id=?" % character.filename, [uid])
            # else mark as duplicate
            else:
                duplicate = True
        
        elif character.effect == Effects.HAREM_BUYER:
            # Hunt for target - Lauren > Messy Hair Lauren > Last LI -> If none, no victim
            cursor.execute("SELECT lauren FROM oialt_harem WHERE user_id=?", [uid])
            lauren = cursor.fetchone()

            if lauren[0]:
                target = "Lauren"
            else:
                cursor.execute("SELECT messy_hair_lauren FROM oialt_harem WHERE user_id=?", [uid])
                mhlauren = cursor.fetchone()
                if mhlauren[0]:
                    target = "Messy Hair Lauren"
                else:
                    cursor.execute("SELECT last_li FROM oialt_harem WHERE user_id=?", [uid])
                    lastgf = cursor.fetchone()

                    if lastgf[0] in Collections.HAREM.members():
                        target = (await self.characterList.getCharacterWithFilename(lastgf[0])).name
                    else:
                        target = "Nobody"

            # If target resolved, check for protection [Funtime]
            if target != "Nobody":
                cursor.execute("SELECT funtime FROM oialt WHERE user_id=?", [uid])
                protection = cursor.fetchone()

                # If protection, discard it and deny the aggressor
                if protection[0]:
                    cursor.execute("UPDATE oialt SET funtime=0 WHERE user_id=?", [uid])
                    protected = True
                # Else remove target from collection
                else:
                    filename = (await self.characterList.getCharacter(target)).filename
                    try:
                        cursor.execute("UPDATE oialt_harem SET %s=0 WHERE user_id=?" % filename, [uid])
                    except Exception as e:
                        print(e)
                    cursor.execute("UPDATE oialt_harem SET last_li='NONE' WHERE user_id=?", [uid])

            # If no target, fail

        elif character.effect == Effects.STABBY_KILLER:
            # Hunt for target - Father Mitchell > Last Mike -> If none, no victim
            cursor.execute("SELECT priest FROM stabby_mikes WHERE user_id=?", [uid])
            victim = cursor.fetchone()

            if victim[0]:
                target = "Father Mitchell"
            else:
                cursor.execute("SELECT last_mike FROM stabby_mikes WHERE user_id=?", [uid])
                victim = cursor.fetchone()
                if victim[0] in Collections.STABBIES.members():
                    target = (await self.characterList.getCharacterWithFilename(victim[0])).name
                else:
                    target = "Nobody"

            # If target resolved check for protection [MC]
            if target != "Nobody":
                cursor.execute("SELECT mc FROM oialt WHERE user_id=?", [uid])
                protection = cursor.fetchone()
                # If protection - discard and deny aggressor
                if protection[0] != 0:
                    cursor.execute("UPDATE oialt SET mc=0 WHERE user_id=?", [uid])
                    protected = True
                # Else remove collectible from collection
                else:
                    filename = (await self.characterList.getCharacter(target)).filename
                    try:
                        cursor.execute("UPDATE stabby_mikes SET %s=0 WHERE user_id=?" % filename, [uid])
                    except Exception as e:
                        print(e)
                    cursor.execute("UPDATE stabby_mikes SET last_mike='NONE' WHERE user_id=?", [uid])
            # If no target, fail
            
        elif character.effect == Effects.BOYS_KILLER:
            # Hunt for target - MC > Last Homie -> If none, no victim
            cursor.execute("SELECT mc FROM the_boys WHERE user_id=?", [uid])
            victim = cursor.fetchone()
            if victim[0]:
                target = "MC"
            else:
                cursor.execute("SELECT last_boi FROM the_boys WHERE user_id=?", [uid])
                victim = cursor.fetchone()
                if victim[0] in Collections.BOYS.members():
                    target = (await self.characterList.getCharacterWithFilename(victim[0])).name
                else:
                    target = "Nobody"

            
            # If target resolved check for protection [MC]
            if target != "Nobody":
                cursor.execute("SELECT aiko FROM oialt WHERE user_id=?", [uid])
                protection = cursor.fetchone()
                # If protection - discard and deny aggressor
                if protection[0] != 0:
                    cursor.execute("UPDATE oialt SET aiko=0 WHERE user_id=?", [uid])
                    protected = True
                # Else remove collectible from collection
                else:
                    filename = (await self.characterList.getCharacter(target)).filename
                    try:
                        cursor.execute("UPDATE the_boys SET %s=0 WHERE user_id=?" % filename, [uid])
                    except Exception as e:
                        print(e)
                    cursor.execute("UPDATE the_boys SET last_boi='NONE' WHERE user_id=?", [uid])
            # If no target, fail
            
        elif character.effect == Effects.POTENTIAL_MUTATOR:
            # Hunt for target - Lilith > Last Potential LI -> If none, no victim
            cursor.execute("SELECT lilith FROM li_potential WHERE user_id=?", [uid])
            victim = cursor.fetchone()
            if victim[0] == 'NONE':
                cursor.execute("SELECT last_potential_li FROM li_potential WHERE user_id=?", [uid])
                victim = cursor.fetchone()

            cursor.execute("SELECT lilith FROM li_potential WHERE user_id=?", [uid])
            victim = cursor.fetchone()
            if victim[0]:
                target = "Lilith"
            else:
                cursor.execute("SELECT last_potential_li FROM li_potential WHERE user_id=?", [uid])
                victim = cursor.fetchone()
                if victim[0] in Collections.POTENTIALS.members():
                    target = (await self.characterList.getCharacterWithFilename(victim[0])).name
                else:
                    target = "Nobody"

            
            # If target resolved check for protection [93]
            if target != "Nobody":
                cursor.execute("SELECT nine_three FROM oialt WHERE user_id=?", [uid])
                protection = cursor.fetchone()
                # If protection - discard and deny aggressor
                if protection[0] != 0:
                    cursor.execute("UPDATE oialt SET nine_three=0 WHERE user_id=?", [uid])
                    protected = True
                # Else remove collectible from collection
                else:
                    filename = (await self.characterList.getCharacter(target)).filename
                    try:
                        cursor.execute("UPDATE li_potential SET %s=0 WHERE user_id=?" % filename, [uid])
                    except Exception as e:
                        print(e)
                    cursor.execute("UPDATE li_potential SET last_potential_li='NONE' WHERE user_id=?", [uid])
            # If no target, fail

        db.commit()
        cursor.close()
        db.close()
        return Results(duplicate=duplicate, victim=target, protected=protected)


    async def collectionOverview(self, author: discord.User, collection: Collections) -> discord.Embed:
        discordID = str(author.id)
        user_name = str(author.display_name)

        members, missing, count, total = await self.getCollectionProgress(discordID, collection)

        #   compile entries to list
        haremlist = "\n".join(members)
        missinglist = "\n".join(missing)

        c_title = "OiaLt Harem" if collection == Collections.HAREM else str(collection)
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


    async def resolveUser(self, uid: str, interaction: discord.Interaction):

        user = None
        if uid != "None":
            uid = await AccountManager.receiveDiscordIDFromInput(interaction, uid)
            if uid == -1:
                return interaction.user

            if uid == interaction.user.id:
                user = interaction.user
            else:
                user = await interaction.client.fetch_user(int(uid))
        else:
            user = interaction.user

        return user


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


    # COMMANDS

    @app_commands.guilds(GUILD)
    @app_commands.command(name="ogf", description="Draw a OiaLt character to be your partner for the day.")
    @commands.check(check_channel)
    @check_cooldown()
    @check_user()
    async def ogf(self, interaction: discord.Interaction):
        """
        Draws a random character from the OiaLt game - cooldown 20h for public deployment.
        -------------------------------------------------------------------------
        Parameters:
            - ctx : discord.ext.Context - discord-provided context to the command prompt.
        """
        db = sqlite3.connect("main.sqlite")
        cursor = db.cursor()
        discordID = str(interaction.user.id)

        # Get UID
        uid = await self.accountManager.getUserID(discordID)
        # Choose a random character
        gf = random.choice(self.characters)
        # Update the DB
        results = await self.updateDatabase(uid, gf)
        # Build and send Embed
        await self.createAndSendEmbed(interaction, character=gf, results=results)
            
        cursor.close()
        db.close()

    @app_commands.guilds(GUILD)
    @app_commands.command(name="oialt_harem", description="View a user's progress on the OiaLt harem collection (ex oharem). Defaults to your User ID")
    @commands.check(check_channel)
    async def oharem(self, interaction: discord.Interaction, uid: str="None"):
        """
        Provides an overview of a user's progress in collecting the OiaLt harem.
        ------------------------------------------------
        Parameters:
            - interaction : discord.Interaction - discord-provided context to the command prompt.
        """
        user = await self.resolveUser(uid, interaction)

        # check whether the user is registered.
        if not await AccountManager.verifyUser(discord_id=user.id, interaction=interaction, expectFail=False):
            return

        # if user is registered, proceed.
        await interaction.response.send_message(embed=await self.collectionOverview(user, Collections.HAREM))

    @app_commands.guilds(GUILD)
    @app_commands.command(name="oialt_stabby_clan", description="View a user's progress on the OiaLt stabby clan collection (ex stabbyclan). Defaults to your User ID")
    @commands.check(check_channel)
    async def stabbyclan(self, interaction: discord.Interaction, uid: str="None"):
        """
        Provides an overview of a user's progress in collecting the clan of Stabby Mike personas.
        ------------------------------------------------
        Parameters:
            - ctx : discord.ext.Context - discord-provided context to the command prompt.
        """
        user = await self.resolveUser(uid, interaction)

        # check whether the user is registered.
        if not await AccountManager.verifyUser(discord_id=user.id, interaction=interaction, expectFail=False):
            return

        # if user is registered, proceed.
        await interaction.response.send_message(embed=await self.collectionOverview(user, Collections.STABBIES))

    @app_commands.guilds(GUILD)
    @app_commands.command(name="oialt_homies", description="View a user's progress on the OiaLt homies collection (ex theboys). Defaults to your User ID")
    @commands.check(check_channel)
    async def theboys(self, interaction: discord.Interaction, uid: str="None"):
        """
        Provides an overview of a user's progress in collecting the OiaLt homies.
        ------------------------------------------------
        Parameters:
            - interaction : discord.Interaction - discord-provided context to the command prompt.
        """
        user = await self.resolveUser(uid, interaction)

        # check whether the user is registered.
        if not await AccountManager.verifyUser(discord_id=user.id, interaction=interaction, expectFail=False):
            return

        # if user is registered, proceed.
        await interaction.response.send_message(embed=await self.collectionOverview(user, Collections.BOYS))

    @app_commands.guilds(GUILD)
    @app_commands.command(name="oialt_side_girls", description="View a user's progress on the OiaLt side girls collection (ex potentiallis) Defaults to your User ID")
    @commands.check(check_channel)
    async def potentialLis(self, interaction: discord.Interaction, uid: str="None"):
        """
        Provides an overview of a user's progress in collecting the OiaLt side girls.
        ------------------------------------------------
        Parameters:
            - interaction : discord.Interaction - discord-provided context to the command prompt.
        """
        user = await self.resolveUser(uid, interaction)

        # check whether the user is registered.
        if not await AccountManager.verifyUser(discord_id=user.id, interaction=interaction, expectFail=False):
            return

        # if user is registered, proceed.
        await interaction.response.send_message(embed=await self.collectionOverview(user, Collections.POTENTIALS))

    @app_commands.guilds(GUILD)
    @app_commands.command(name="oialt_protectors", description="View a user's OiaLt protection racket (ex oprotectors). Defaults to your User ID")
    @commands.check(check_channel)
    @check_user()
    async def oprotectors(self, interaction: discord.Interaction, uid: str="None"):
        """
        Provides an overview of a user's progress in collecting the OiaLt protectors.
        ------------------------------------------------
        Parameters:
            - ctx : discord.ext.Context - discord-provided context to the command prompt.
        """
        user = await self.resolveUser(uid, interaction)

        # check whether the user is registered.
        if not await AccountManager.verifyUser(discord_id=user.id, interaction=interaction, expectFail=False):
            return

        db = sqlite3.connect(self.db_path)
        cursor = db.cursor()
        discordID = str(user.id)
        user_name = str(user.display_name)

        #   search thru 'eternum_harem' table for entries
        uid = await self.accountManager.getUserID(discordID=discordID)
        members = []
        cursor.execute("SELECT funtime, mc, aiko, nine_three FROM oialt WHERE user_id = ?", [uid])
        yesno = cursor.fetchone()
        harem = f"**Harem:**\nFuntime: {'✅' if yesno[0] == 1 else ':x:'}"
        members.append(harem)

        mikes = f"**Stabby Clan:**\nMC: {'✅' if yesno[1] == 1 else ':x:'}"
        members.append(mikes)

        theboys = f"**The Boys:**\nAiko: {'✅' if yesno[2] == 1 else ':x:'}"
        members.append(theboys)

        potentialLis = f"**Potential LI's:**\n93: {'✅' if yesno[3] == 1 else ':x:'}"
        members.append(potentialLis)

        #   compile entries to list
        protectorlist = "\n".join(members)

        embed_title = f"OiaLt Protectors of **{user_name}**:"
        #   build embed (color blue) with categories 'got x/y' + names & 'missing z/y' + names --> + emotes?
        embed = discord.Embed(title=embed_title, description=protectorlist, color=HelperClass.orange)
        await interaction.response.send_message(embed=embed)

        cursor.close()
        db.close()

    @app_commands.guilds(GUILD)
    @app_commands.command(name="oialt_collections", description="View a user's OiaLt collections portfolio (ex ocollections). Defaults to your User ID.")
    @commands.check(check_channel)
    async def oCollections(self, interaction: discord.Interaction, uid: str="None"):
        """
        Provides an overview of a user's progress in all OiaLt collections.
        ------------------------------------------------
        Parameters:
            - ctx : discord.ext.Context - discord-provided context to the command prompt.
        """

        user = await self.resolveUser(uid, interaction)

        # check whether the user is registered.
        if not await AccountManager.verifyUser(discord_id=user.id, interaction=interaction, expectFail=False):
            return
        
        await interaction.response.defer()

        # if user is registered, proceed.
        db = sqlite3.connect(self.db_path)
        cursor = db.cursor()
        discordID = str(user.id)
        user_name = str(user.display_name)

        embed_title = f"Eternum Collections of **{user_name}**:"
        embed = discord.Embed(title=embed_title, color=HelperClass.orange)

        # HAREM
        h_list, h_vals = await self.getMembers(user, Collections.HAREM)

        haremlist = "\n".join(h_list)

        if haremlist == "":
            haremlist = "You haven't collected anyone for your harem yet..."
        embed.add_field(name=f"Harem: ({h_vals[0]}/{h_vals[1]}):", value=haremlist)

        # THE BOYS
        mikes_list, mikes_vals = await self.getMembers(user, Collections.BOYS)

        mikeslist = "\n".join(mikes_list)

        if mikeslist == "":
            mikeslist = "You haven't collected any of the boys yet..."

        embed.add_field(name=f"The Boys: ({mikes_vals[0]}/{mikes_vals[1]}):", value=mikeslist)

        # STABBY CLAN
        mikes_list, mikes_vals = await self.getMembers(user, Collections.STABBIES)

        mikeslist = "\n".join(mikes_list)

        if mikeslist == "":
            mikeslist = "You haven't collected any of the Mikes yet..."

        embed.add_field(name=f"Stabby Mikes: ({mikes_vals[0]}/{mikes_vals[1]}):", value=mikeslist)

        # POTENTIAL LI'S
        s_list, s_vals = await self.getMembers(user, Collections.POTENTIALS)
        
        sideslist = "\n".join(s_list)

        if sideslist == "":
            sideslist = "You haven't collected any of the potential LI's yet..."
        embed.add_field(name=f"Potential LI's': ({s_vals[0]}/{s_vals[1]}):", value=sideslist)

        # Protectors

        members = []
        uid = await self.accountManager.getUserID(discordID=discordID)
        cursor.execute("SELECT funtime, mc, aiko, nine_three FROM oialt WHERE user_id = ?", [uid])
        yesno = cursor.fetchone()
        harem = f"**Harem:**\nFuntime: {'✅' if yesno[0] == 1 else ':x:'}"
        members.append(harem)

        mikes = f"**Stabby Clan:**\nMC: {'✅' if yesno[1] == 1 else ':x:'}"
        members.append(mikes)
        
        theboys = f"**The Boys:**\nAiko: {'✅' if yesno[2] == 1 else ':x:'}"
        members.append(theboys)

        potentialLis = f"**Potential LI's:**\n93: {'✅' if yesno[3] == 1 else ':x:'}"
        members.append(potentialLis)

        #   compile entries to list
        protectorlist = "\n".join(members)

        embed.add_field(name="Protections:", value=protectorlist)

        await interaction.followup.send(embed=embed)

        cursor.close()
        db.close()

    @ogf.error
    @commands.check(check_channel)
    @check_user()
    async def errorGF(self, interaction: discord.Interaction, error: app_commands.AppCommandError):
        """
        Handles errors coming up from faulty use of the -egf command.
        ------------------------------------------------
        Parameters:
            - ctx : discord.ext.Context - discord-provided context to the command prompt.
            - error : str (?) - details of the error.
        """
        if isinstance(error, CommandOnCooldownError):
            await self.displayLastGF(interaction, error.retry_after)
        else:
            await interaction.response.send_message(f"Unexpected error drawing ogf: {error}", ephemeral=True)


    async def setup(client):
        cog = OiaLt(client)
        await client.add_cog(cog)
        cog.botSpamChannel = cog.client.config.botSpamChannel
        print("successfully activated OiaLt cog.")
