# DISCORD.PY
import discord
from discord import Embed, File
from discord.ext import commands, tasks
from discord.ext.commands import CooldownMapping, Cooldown, BucketType
# OTHER LIBRARIES
import random
import sqlite3
# OWN LIBRARIES
from Utilities import HelperClass, OgfCollections, OgfEffects, OgfResults, TimeObject, check_channel
from AccountManager import AccountManager, check_user
from CharacterCard import OgfCharacterCard
from OgfCharacters import OgfCharacters


# Help function
async def help_oialt(ctx):
    field_names = []
    field_values = []

    title = "Judie's OiaLt gf game!"
    description = "Here are the commands to use the oialt gf system!"

    field_names.append("-ogf (oialt gf)")
    field_values.append("pull a random gf from the OiaLt world! (20h cooldown!)")

    field_names.append("-ocollections (oialt collections)")
    field_values.append("Get an overview of all your oialt collections!")

    field_names.append("-oharem (oialt harem)")
    field_values.append(
        "check your progress in the LI collection!\n--> Contains **Judie, Lauren, Messy Hair Lauren, " \
        "Carla, Iris, Aiko, Jasmine & Rebecca**.")

    field_names.append("-stabbyclan")
    field_values.append(
        "check your progress in the stabby mike collection!\n--> Contains **Stabby Police, Hitman Mike, " \
        "Anastasia, Yakuza Mike, Priest Mike & Mike the Exterminator**.")

    field_names.append("-theboys")
    field_values.append(
        "check your progress in the boys collection!\n--> Contains **MC, Tom, Fit Jack, Oliver, Asmodeus & " \
        "Hiromi**.")

    field_names.append("-potentialLIs")
    field_values.append(
        "check your progress in the potential LI collection!\n--> Contains **Ava, Lilith, Fit Jack's "
        "Groupie, Train Conductor, Shop Girl & Stone Elephant**.")

    field_names.append("-oprotectors (oialt protectors)")
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

    await ctx.send(embed=embed)

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
        client.CogsToActivate.append(self)
        self.characterList = OgfCharacters()
        self.characters = self.characterList.characters
        self.accountManager = AccountManager(self.client)
        self.botSpamChannel = None


    def activate(self):
        """
        Initializes client data for the gf game - setting channel IDs, cooldown time etc. 

        Required for proper functioning; Required to run only after BotConfig.load() was called.
        """
        command = self.client.get_command("ogf")
        cd = Cooldown(rate=1, per=self.client.config.cooldown)
        command._buckets = CooldownMapping(cd, type=BucketType.user)
        self.botSpamChannel = self.client.config.botSpamChannel
        print("successfully activated OiaLt cog.")

    # HELPER FUNCTIONS - checkUser in AccountManager // createEmbed in Utilities/HelperClass

    async def displayLastGF(self, ctx, time):
        """
        Shows the last character obtained by a character as cooldown reminder.
        -------------------------------------------------------------------------
        Parameters:
            - ctx : discord.ext.Context - discord-provided context to the command prompt.
            - time : int - time in seconds left until the cooldown runs out.
        """
        timer = TimeObject(time)
        description = f"You still have {timer.hours}h {timer.minutes} mins and {timer.seconds}s until your next draw!"
        db = sqlite3.connect("main.sqlite")
        cursor = db.cursor()
        discordID = str(ctx.author.id)

        uid = await self.accountManager.getUserID(discordID=discordID, cursor=cursor)

        # Get last obtained character
        cursor.execute("SELECT last_gf FROM oialt WHERE user_id=?", [uid])
        lastGf = cursor.fetchone()
        if lastGf is not None:
            name = self.characterList.GetFilename(lastGf[0])
        else:
            name = "None"

        if lastGf is not None:
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
        await ctx.send(file=image, embed=embed)

        cursor.close()
        db.close()

    @commands.command(aliases=["oialt gf", "gfo", "gf oialt"])
    @commands.check(check_channel)
    @check_user()
    async def ogf(self, ctx):
        """
        Draws a random character from the OiaLt game - cooldown 20h for public deployment.
        -------------------------------------------------------------------------
        Parameters:
            - ctx : discord.ext.Context - discord-provided context to the command prompt.
        """
        db = sqlite3.connect("main.sqlite")
        cursor = db.cursor()
        discordID = str(ctx.author.id)

        # Get UID
        uid = await self.accountManager.getUserID(discordID, cursor)
        # Choose a random character
        gf = random.choice(self.characters)
        # Update the DB
        results = await self.updateDatabase(uid, gf)
        # Build and send Embed
        await self.createAndSendEmbed(ctx, character=gf, results=results)
            
        cursor.close()
        db.close()

    async def createAndSendEmbed(self, ctx, character: OgfCharacterCard, results: OgfResults):
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
        duplicateText = "" if collection == OgfCollections.NONE and effect == OgfEffects.NONE else f"(New) {HelperClass.daliaParty}" if not results.duplicate else f"(duplicate) {HelperClass.annieCry}"
        collection_field_name = f"{str(collection)} {duplicateText}"
        collection_field_value = ""
        effect_field_name = str(effect)
        effect_field_value = effect.Describe()

        # <editor-fold desc="Non-collectibles">
        if collection == OgfCollections.NONE:
            text = f"Congrats, {ctx.author.mention}...? Your companion for the day is {character.name}."
            collection_field_value = "A character that doesn't belong into any collection."

            # Special case - Spiderman (includes author username in footer)
            if character.name == "Spiderman":
                displayname = ctx.author.display_name
                footer = f"Hey, is there a {displayname}? I have a pizza for {displayname}!"
        # </editor-fold>
        # <editor-fold desc="Harem">
        elif collection == OgfCollections.HAREM:
            text = f"Congratulations {ctx.author.mention}! Your gf for the day is {character.name}!"
            collection_field_value = f"A wild {character.name} has spawned in your harem!" if not results.duplicate \
                else f"Tough luck! {character.name} is already in your harem!"
        # </editor-fold>
        # <editor-fold desc="Stabby Clan">
        elif collection == OgfCollections.STABBIES:
            text = f"Congratulations {ctx.author.mention}! Your protector for the day is {character.name}!"
            collection_field_value = f"A new recruit for the stabby clan!" if not results.duplicate \
                else f"Tough luck! {character.name} is already part of your bodyguard staff!"
        # </editor-fold>
        # <editor-fold desc="The Boys">
        elif collection == OgfCollections.BOYS:
            text = f"Congratulations {ctx.author.mention}! Your homie for the day is {character.name}!"
            collection_field_value = f"Let's fucking goo! {character.name} joined the squad!" if not results.duplicate \
                else f"Tough luck! {character.name} is already chilling with you!"
        # </editor-fold>
        # <editor-fold desc="Potential LI's">
        elif collection == OgfCollections.POTENTIALS:
            text = f"Congrats {ctx.author.mention}! Your gf for the day is {character.name}!"
            collection_field_value = f"{character.name} has joined the gang! Might consider asking her out? :wink:" if not results.duplicate \
                else f"Tough luck! {character.name} has already expressed her interest in you!"

            if ctx.author.display_name == "frostkanra":
                text = "Well, well, well... if this were real life, a creator-createe relationship wouldn't be so " \
                       "acceptable now, would it...?"
        # </editor-fold>

        # <editor-fold desc="Orochi">
        if effect == OgfEffects.HAREM_BUYER:
            text = f"Yikes! Your company for the day is {character.name}. Good luck {ctx.author.mention} (You'll need it!)"
            if results.protected:
                collection_field_name = f"Bid for {results.victim} refused."
                collection_field_value = f"GODDAMN IT, WHY AREN'T YOU LAUGHING OROCHI??!"
            else:
                collection_field_name = "**OH NO**"
                collection_field_value = f"Orochi offered a deal for {results.victim} you couldn't refuse..." if \
                    results.victim != "Nobody" else f"Must have been the wind..."
        # </editor-fold>
        # <editor-fold desc="Astaroth">
        if effect == OgfEffects.STABBY_KILLER:
            text = f"Yikes! Your company for the day is {character.name}. Good luck {ctx.author.mention} (You'll need it!)"
            if results.protected:
                collection_field_name = f"That was close..."
                collection_field_value = f"The MC managed to body Astaroth before he could kill {results.victim}!"
            else:
                collection_field_name = "**OH SHIT**"
                collection_field_value = f"Astaroth shot {results.victim} dead. R.I.P." if \
                    results.victim != "Nobody" else f"Must have been the wind..."
        # </editor-fold>
        # <editor-fold desc="Azazel">
        if effect == OgfEffects.BOYS_KILLER:
            text = f"Yikes! Your company for the day is {character.name}. Good luck {ctx.author.mention} (You'll need it!)"
            if results.protected:
                collection_field_name = f"That was close..."
                collection_field_value = f"Watch {results.victim}'s back, buddy."
            else:
                collection_field_name = "**OH SHIT**"
                collection_field_value = f"Azazel put {results.victim} to sleep forever! R.I.P." if \
                    results.victim != "Nobody" else f"Must have been the wind..."
        # </editor-fold>
        # <editor-fold desc="Monster Lilith">
        if effect == OgfEffects.POTENTIAL_MUTATOR:
            text = f"Yikes! Your company for the day is {character.name}. Good luck {ctx.author.mention} (You'll need it!)"
            if results.protected:
                collection_field_name = f"That was close..."
                collection_field_value = f"93 managed to turn the monster's gaze away from {results.victim}!"
            else:
                collection_field_name = "**OH SHIT**"
                collection_field_value = f"{results.victim} just turned into a living set of spare ribs in front of you!" if \
                    results.victim != "Nobody" else f"Must have been the wind..."
        # </editor-fold>


        # <editor-fold desc="Embed compilation and sending">
        embed = await HelperClass.createEmbed(title=character.name, text=text, footer=footer)

        embed.add_field(name=collection_field_name, value=collection_field_value, inline=True)
        embed.add_field(name=effect_field_name, value=effect_field_value, inline=True)

        image = discord.File(f"./gfGameImages/{character.filename}.webp", filename="gf.webp")
        embed.set_image(url="attachment://gf.webp")
        await ctx.send(file=image, embed=embed)
        # </editor-fold>

    async def updateDatabase(self, uid: int, character: OgfCharacterCard) -> OgfResults:
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
        # <editor-fold desc="Setup">
        # Setup: DB connections
        db = sqlite3.connect("main.sqlite")
        cursor = db.cursor()

        # Setup: Results variables
        duplicate = False
        target = None
        protected = False
        # </editor-fold>

        # Update last obtained character
        cursor.execute("UPDATE oialt SET last_gf=? WHERE user_id=?", [character.name, uid])

        # <editor-fold desc="Collections">
        # Switch Collections:
        # <editor-fold desc="Harem">
        if character.collection == OgfCollections.HAREM:
            # Update collection's last obtained
            cursor.execute("UPDATE oialt_harem SET last_li=? WHERE user_id=?", [character.filename, uid])

            # Check if already in collection
            cursor.execute("SELECT %s FROM oialt_harem WHERE user_id=?" % character.filename, [uid])
            check = cursor.fetchone()
            # If not, add to collection
            if check[0] == "NONE":
                cursor.execute("UPDATE oialt_harem SET %s=? WHERE user_id=?" % character.filename,
                               [character.name, uid])
            # Else mark as duplicate
            else:
                duplicate = True
        # </editor-fold>
        # <editor-fold desc="Stabby Mikes">
        elif character.collection == OgfCollections.STABBIES:
            # Update collection's last obtained
            cursor.execute("UPDATE stabby_mikes SET last_mike=? WHERE user_id=?", [character.filename, uid])

            # Check if already in collection
            cursor.execute("SELECT %s FROM stabby_mikes WHERE user_id=?" % character.filename, [uid])
            check = cursor.fetchone()
            # If not, add to collection
            if check[0] == "NONE":
                cursor.execute("UPDATE stabby_mikes SET %s=? WHERE user_id=?" % character.filename,
                               [character.name, uid])
            # Else mark as duplicate
            else:
                duplicate = True
        # </editor-fold>
        # <editor-fold desc="The Boys">
        elif character.collection == OgfCollections.BOYS:
            # Update Collection's last obtained
            cursor.execute("UPDATE the_boys SET last_boi=? WHERE user_id=?", [character.filename, uid])

            # Check if already in collection
            cursor.execute("SELECT %s FROM the_boys WHERE user_id=?" % character.filename, [uid])
            check = cursor.fetchone()
            # If not, add to collection
            if check[0] == "NONE":
                cursor.execute("UPDATE the_boys SET %s=? WHERE user_id=?" % character.filename, [character.name, uid])
            # Else mark as duplicate
            else:
                duplicate = True
        # </editor-fold>
        # <editor-fold desc="Potential LI's">
        elif character.collection == OgfCollections.POTENTIALS:
            # Update Collection's last obtained
            cursor.execute("UPDATE li_potential SET last_potential_li=? WHERE user_id=?", [character.filename, uid])

            # Check if already in collection
            cursor.execute("SELECT %s FROM li_potential WHERE user_id=?" % character.filename, [uid])
            check = cursor.fetchone()
            # If not, add to collection
            if check[0] == "NONE":
                cursor.execute("UPDATE li_potential SET %s=? WHERE user_id=?" % character.filename,
                               [character.name, uid])
            # Else mark as duplicate
            else:
                duplicate = True
        # </editor-fold>
        # </editor-fold>

        # <editor-fold desc="Effects">
        # <editor-fold desc="Saviours">
        if character.effect in [OgfEffects.HAREM_SAVER, OgfEffects.STABBY_SAVER, OgfEffects.BOYS_SAVER, OgfEffects.POTENTIAL_SAVER]:
            # Check if protection is already obtained
            cursor.execute("SELECT %s FROM oialt WHERE user_id=?" % character.filename, [uid])
            check = cursor.fetchone()
            # If not, add to user
            if check[0] == 0:
                cursor.execute("UPDATE oialt SET %s=1 WHERE user_id=?" % character.filename, [uid])
            # else mark as duplicate
            else:
                duplicate = True
        # </editor-fold>
        # <editor-fold desc="Orochi - Lauren > MH Lauren > Any // Funtime">
        elif character.effect == OgfEffects.HAREM_BUYER:
            # <editor-fold desc="Target Hunt">
            # Hunt for target - Lauren > MH Lauren > last LI -> if none, no victim.
            cursor.execute("SELECT lauren FROM oialt_harem WHERE user_id=?", [uid])
            victim = cursor.fetchone()
            if victim[0] == 'NONE':
                cursor.execute("SELECT messy_hair_lauren FROM oialt_harem WHERE user_id=?", [uid])
                victim = cursor.fetchone()
                if victim[0] == 'NONE':
                    cursor.execute("SELECT last_li FROM oialt_harem WHERE user_id=?", [uid])
                    victim = cursor.fetchone()

            # Set target name - Full name, or 'Nobody' if no victim.
            target = self.characterList.GetName(victim[0]) if victim[0] not in ['NONE', None] else "Nobody"
            if target is None:  # None returned when nothing is found in GetName
                target = victim[0]
            # </editor-fold>
            # <editor-fold desc="Target handling">
            # If target resolved, check for protection [Funtime]
            if target != "Nobody":
                cursor.execute("SELECT funtime FROM oialt WHERE user_id=?", [uid])
                protection = cursor.fetchone()
                # If protection, discard it and deny the aggressor
                if protection[0] != 0:
                    cursor.execute("UPDATE oialt SET funtime=0 WHERE user_id=?", [uid])
                    protected = True
                # Else remove target from collection
                else:
                    filename = self.characterList.GetFilename(target)
                    try:
                        cursor.execute("UPDATE oialt_harem SET %s='NONE' WHERE user_id=?" % filename, [uid])
                    except Exception as e:
                        print(e)
                    cursor.execute("UPDATE oialt_harem SET last_li='NONE' WHERE user_id=?", [uid])

            # If no target, fail
            # </editor-fold>
        # </editor-fold>
        # <editor-fold desc="Astaroth - Father Mitchell > Any // MC">
        elif character.effect == OgfEffects.STABBY_KILLER:
            # <editor-fold desc="Target Hunt">
            # Hunt for target - Father Mitchell > Last Mike -> If none, no victim
            cursor.execute("SELECT priest FROM stabby_mikes WHERE user_id=?", [uid])
            victim = cursor.fetchone()
            if victim[0] == 'NONE':
                cursor.execute("SELECT last_mike FROM stabby_mikes WHERE user_id=?", [uid])
                victim = cursor.fetchone()

            # Set target name - Full name, or 'Nobody' if no victim.
            target = self.characterList.GetName(victim[0]) if victim[0] not in ['NONE', None] else "Nobody"
            if target is None:      # None returned when nothing is found in GetName
                target = victim[0]

            # </editor-fold>
            # <editor-fold desc="Target Handling">
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
                    filename = self.characterList.GetFilename(target)
                    try:
                        cursor.execute("UPDATE stabby_mikes SET %s='NONE' WHERE user_id=?" % filename, [uid])
                    except Exception as e:
                        print(e)
                    cursor.execute("UPDATE stabby_mikes SET last_mike='NONE' WHERE user_id=?", [uid])
            # If no target, fail
            # </editor-fold>
        # </editor-fold>
        # <editor-fold desc="Azazel - MC > Any // Aiko">
        elif character.effect == OgfEffects.BOYS_KILLER:
            # <editor-fold desc="Target Hunt">
            # Hunt for target - MC > Last Homie -> If none, no victim
            cursor.execute("SELECT mc FROM the_boys WHERE user_id=?", [uid])
            victim = cursor.fetchone()
            if victim[0] == 'NONE':
                cursor.execute("SELECT last_boi FROM the_boys WHERE user_id=?", [uid])
                victim = cursor.fetchone()

            # Set target name - Full name, or 'Nobody' if no victim.
            target = self.characterList.GetName(victim[0]) if victim[0] not in ['NONE', None] else "Nobody"
            if target is None:  # None returned when nothing is found in GetName
                target = victim[0]
            # </editor-fold>
            # <editor-fold desc="Target Handling">
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
                    filename = self.characterList.GetFilename(target)
                    try:
                        cursor.execute("UPDATE the_boys SET %s='NONE' WHERE user_id=?" % filename, [uid])
                    except Exception as e:
                        print(e)
                    cursor.execute("UPDATE the_boys SET last_boi='NONE' WHERE user_id=?", [uid])
            # If no target, fail
            # </editor-fold>
        # </editor-fold>
        # <editor-fold desc="Monster Lilith - Lilith > Any // 93">
        elif character.effect == OgfEffects.POTENTIAL_MUTATOR:
            # <editor-fold desc="Target Hunt">
            # Hunt for target - Lilith > Last Potential LI -> If none, no victim
            cursor.execute("SELECT lilith FROM li_potential WHERE user_id=?", [uid])
            victim = cursor.fetchone()
            if victim[0] == 'NONE':
                cursor.execute("SELECT last_potential_li FROM li_potential WHERE user_id=?", [uid])
                victim = cursor.fetchone()

            # Set target name - Full name, or 'Nobody' if no victim.
            target = self.characterList.GetName(victim[0]) if victim[0] not in ['NONE', None] else "Nobody"
            if target is None:  # None returned when nothing is found in GetName
                target = victim[0]

            # </editor-fold>
            # <editor-fold desc="Target Handling">
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
                    filename = self.characterList.GetFilename(target)
                    try:
                        cursor.execute("UPDATE li_potential SET %s='NONE' WHERE user_id=?" % filename, [uid])
                    except Exception as e:
                        print(e)
                    cursor.execute("UPDATE li_potential SET last_potential_li='NONE' WHERE user_id=?", [uid])
                # If no target, fail
                # </editor-fold>
        # </editor-fold>
        # </editor-fold>

        db.commit()
        cursor.close()
        db.close()
        return OgfResults(duplicate=duplicate, victim=target, protected=protected)


    @commands.command()
    @commands.check(check_channel)
    @check_user()
    async def oharem(self, ctx):
        """
        Provides an overview of a user's progress in collecting the OiaLt harem.
        ------------------------------------------------
        Parameters:
            - ctx : discord.ext.Context - discord-provided context to the command prompt.
        """
        db = sqlite3.connect("main.sqlite")
        cursor = db.cursor()
        discordID = str(ctx.author.id)
        uid = await self.accountManager.getUserID(discordID=discordID, cursor=cursor)
        user_name = str(ctx.author.display_name)
        count = 0

        members = []
        missing = ["Aiko", "Carla", "Iris", "Jasmine", "Judie", "Lauren", "Messy Hair Lauren", "Rebecca"]
        cursor.execute(
            "SELECT judie, lauren, messy_hair_lauren, carla, iris, aiko, jasmine, rebecca FROM oialt_harem WHERE user_id=?",
            [uid])
        yesno = cursor.fetchone()
        for i in yesno:
            if i != 'NONE':
                count = count + 1
                members.append(i)

        for i in missing:
            if i in members:
                missing.remove(i)

        haremlist = "\n".join(members)
        missinglist = "\n".join(missing)

        if haremlist == "":
            haremlist = "You haven't collected anyone for your harem yet..."

        if missinglist == "":
            missinglist = "You have completed the collection, congrats!"

        embed_title = f"OiaLt Harem of **{user_name}**:"
        embed = discord.Embed(title=embed_title, color=HelperClass.orange)
        embed.add_field(name=f"Claimed ({count}/8):", value=haremlist)
        embed.add_field(name=f"Missing ({8 - count}/8):", value=missinglist)
        await ctx.send(embed=embed)

        cursor.close()
        db.close()

    @commands.command()
    @commands.check(check_channel)
    @check_user()
    async def stabbyclan(self, ctx):
        """
        Provides an overview of a user's progress in collecting the clan of Stabby Mike personas.
        ------------------------------------------------
        Parameters:
            - ctx : discord.ext.Context - discord-provided context to the command prompt.
        """
        db = sqlite3.connect("main.sqlite")
        cursor = db.cursor()
        discordID = str(ctx.author.id)
        uid = await self.accountManager.getUserID(discordID=discordID, cursor=cursor)
        user_name = str(ctx.author.display_name)
        count = 0

        members = []
        cursor.execute(
            "SELECT police, hitman, yakuza, priest, exterminator, anastasia FROM stabby_mikes WHERE user_id=?",
            [uid])
        yesno = cursor.fetchone()
        for i in yesno:
            if i != 'NONE':
                count = count + 1
                members.append(i)

        mikes = ", ".join(members)

        if mikes == "":
            mikes = "You haven't collected anyone for your clan yet..."

        embed_title = f"Stabby Clan of {user_name}:"
        embed = discord.Embed(title=embed_title, description=mikes, color=0xFFA800)
        embed.set_footer(text=f"Progress: {count} / 6")
        await ctx.send(embed=embed)

        cursor.close()
        db.close()

    @commands.command()
    @commands.check(check_channel)
    @check_user()
    async def theboys(self, ctx):
        """
        Provides an overview of a user's progress in collecting the OiaLt homies.
        ------------------------------------------------
        Parameters:
            - ctx : discord.ext.Context - discord-provided context to the command prompt.
        """
        db = sqlite3.connect("main.sqlite")
        cursor = db.cursor()
        discordID = str(ctx.author.id)
        uid = await self.accountManager.getUserID(discordID=discordID, cursor=cursor)
        user_name = str(ctx.author.display_name)
        count = 0

        members = []
        cursor.execute("SELECT mc, tom, oliver, fit_jack, asmodeus, hiromi FROM the_boys WHERE user_id=?",
                        [uid])
        yesno = cursor.fetchone()
        for i in yesno:
            if i != 'NONE':
                count = count + 1
                members.append(i)

        bois = ", ".join(members)

        if bois == "":
            bois = "You haven't collected anyone for your boys yet..."

        embed_title = f"The OiaLt Boys of {user_name}:"
        embed = discord.Embed(title=embed_title, description=bois, color=0xFFA800)
        embed.set_footer(text=f"Progress: {count} / 6")
        await ctx.send(embed=embed)

        cursor.close()
        db.close()

    @commands.command()
    @commands.check(check_channel)
    @check_user()
    async def potentialLis(self, ctx):
        """
        Provides an overview of a user's progress in collecting the OiaLt side girls.
        ------------------------------------------------
        Parameters:
            - ctx : discord.ext.Context - discord-provided context to the command prompt.
        """
        db = sqlite3.connect("main.sqlite")
        cursor = db.cursor()
        discordID = str(ctx.author.id)
        uid = await self.accountManager.getUserID(discordID=discordID, cursor=cursor)
        user_name = str(ctx.author.display_name)
        count = 0

        members = []
        cursor.execute(
            "SELECT ava, lilith, fit_jack_groupie, train_conductor, shop_girl, stone_elephant FROM li_potential WHERE user_id=?",
            [uid])
        yesno = cursor.fetchone()
        for i in yesno:
            if i != 'NONE':
                count = count + 1
                members.append(i)

        potentials = ", ".join(members)

        if potentials == "":
            potentials = "You haven't collected anyone for your potential LI's yet..."

        embed_title = f"Potential OiaLt LI's of {user_name}:"
        embed = discord.Embed(title=embed_title, description=potentials, color=0xFFA800)
        embed.set_footer(text=f"Progress: {count} / 6")
        await ctx.send(embed=embed)

        cursor.close()
        db.close()

    @commands.command(aliases=["protectorso", "oprotections", "oprotection", "protectionso", "protectiono"])
    @commands.check(check_channel)
    @check_user()
    async def oprotectors(self, ctx):
        """
        Provides an overview of a user's progress in collecting the OiaLt protectors.
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
        cursor.execute("SELECT funtime, mc, aiko, nine_three FROM oialt WHERE user_id = ?", [uid])
        yesno = cursor.fetchone()
        harem = "**Harem:**\nFuntime: :x:"
        if yesno[0] == 1:
            harem = "**Harem:**\nFuntime: ✅"
        members.append(harem)

        mikes = "**Stabby Clan:**\nMC: :x:"
        if yesno[1] == 1:
            mikes = "**Stabby Clan:**\nMC: ✅"
        members.append(mikes)

        theboys = "**The Boys:**\nAiko: :x:"
        if yesno[2] == 1:
            theboys = "**The Boys:**\nAiko: ✅"
        members.append(theboys)

        potentialLis = "**Potential LI's:**\n93: :x:"
        if yesno[3] == 1:
            potentialLis = "**Potential LI's:**\n93: ✅"
        members.append(potentialLis)

        #   compile entries to list
        protectorlist = "\n".join(members)

        embed_title = f"OiaLt Protectors of **{user_name}**:"
        #   build embed (color pink) with categories 'got x/y' + names & 'missing z/y' + names --> + emotes?
        embed = discord.Embed(title=embed_title, description=protectorlist, color=HelperClass.orange)
        await ctx.send(embed=embed)

        cursor.close()
        db.close()

    @commands.command(aliases=['oialt collections', 'collectionso', 'collections oialt'])
    @commands.check(check_channel)
    @check_user()
    async def oCollections(self, ctx):
        """
        Provides an overview of a user's progress in all OiaLt collections.
        ------------------------------------------------
        Parameters:
            - ctx : discord.ext.Context - discord-provided context to the command prompt.
        """
        db = sqlite3.connect("main.sqlite")
        cursor = db.cursor()
        discordID = str(ctx.author.id)
        user_name = str(ctx.author.display_name)
        haremcount = 0
        homiecount = 0
        mikecount = 0
        potentialscount = 0

        embed_title = f"OiaLt Collections of **{user_name}**:"
        embed = discord.Embed(title=embed_title, color=HelperClass.orange)

        #   search thru tables for entries
        uid = await self.accountManager.getUserID(discordID=discordID, cursor=cursor)
        members = []

        # HAREM
        cursor.execute(
            "SELECT judie, lauren, messy_hair_lauren, carla, iris, aiko, jasmine, rebecca FROM oialt_harem WHERE user_id=?", [uid])
        yesno = cursor.fetchone()
        for i in yesno:
            if i != 'NONE':
                haremcount = haremcount + 1
                members.append(i)

        #   compile entries to list
        haremlist = "\n".join(members)

        if haremlist == "":
            haremlist = "You haven't collected anyone for your harem yet..."
        embed.add_field(name=f"Harem: ({haremcount}/8):", value=haremlist)

        members = []

        # THE BOYS
        cursor.execute(
            "SELECT mc, tom, oliver, fit_jack, asmodeus, hiromi FROM the_boys WHERE user_id=?", [uid])
        yesno = cursor.fetchone()
        for i in yesno:
            if i != 'NONE':
                homiecount = homiecount + 1
                members.append(i)

        #   compile entries to list
        homielist = "\n".join(members)

        if homielist == "":
            homielist = "You haven't collected any of the boys yet..."

        embed.add_field(name=f"The Boys: ({homiecount}/6):", value=homielist)

        members = []

        # STABBY CLAN
        cursor.execute(
            "SELECT police, hitman, yakuza, priest, exterminator, anastasia FROM stabby_mikes WHERE user_id=?",
            [uid])
        yesno = cursor.fetchone()
        for i in yesno:
            if i != 'NONE':
                mikecount = mikecount + 1
                members.append(i)

        # compile entries to list
        mikelist = "\n".join(members)

        if mikelist == "":
            mikelist = "You haven't collected any Mike yet..."
        embed.add_field(name=f"Stabby Clan: ({mikecount}/6):", value=mikelist)

        # POTENTIAL LI'S

        members = []

        cursor.execute(
            "SELECT ava, lilith, fit_jack_groupie, train_conductor, shop_girl, stone_elephant FROM li_potential WHERE user_id=?",
            [uid])
        yesno = cursor.fetchone()
        for i in yesno:
            if i != 'NONE':
                potentialscount = potentialscount + 1
                members.append(i)

        #   compile entries to list
        potentialslist = "\n".join(members)

        if potentialslist == "":
            potentialslist = "You haven't collected any of the potential LI's yet..."
        embed.add_field(name=f"Potential LI's: ({potentialscount}/6):", value=potentialslist)

        # Protectors

        members = []
        cursor.execute("SELECT funtime, mc, aiko, nine_three FROM oialt WHERE user_id = ?", [uid])
        yesno = cursor.fetchone()
        harem = "**Harem:**\nFuntime: :x:"
        if yesno[0] == 1:
            harem = "**Harem:**\nFuntime: ✅"
        members.append(harem)

        mikes = "**Stabby Clan:**\nMC: :x:"
        if yesno[1] == 1:
            mikes = "**Stabby Clan:**\nMC: ✅"
        members.append(mikes)

        theboys = "**The Boys:**\nAiko: :x:"
        if yesno[2] == 1:
            theboys = "**The Boys:**\nAiko: ✅"
        members.append(theboys)

        potentialLis = "**Potential LI's:**\n93: :x:"
        if yesno[3] == 1:
            potentialLis = "**Potential LI's:**\n93: ✅"
        members.append(potentialLis)

        #   compile entries to list
        protectorlist = "\n".join(members)

        embed.add_field(name="Protections:", value=protectorlist)

        await ctx.send(embed=embed)

        cursor.close()
        db.close()

    @ogf.error
    @commands.check(check_channel)
    @check_user()
    async def errorGF(self, ctx, error):
        """
        Handles errors coming up from faulty use of the -egf command.
        ------------------------------------------------
        Parameters:
            - ctx : discord.ext.Context - discord-provided context to the command prompt.
            - error : str (?) - details of the error.
        """
        if isinstance(error, commands.CommandOnCooldown):
            await self.displayLastGF(ctx, error.retry_after)


# Does this code ever get reached??
def setup(client):
    client.add_cog(OiaLt(client))
