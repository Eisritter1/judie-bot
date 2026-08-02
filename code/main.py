# DISCORD LIBRARIES
import discord
from discord import app_commands
from discord.ext import commands, tasks
# EXTERNAL LIBRARIES
import sqlite3,os,traceback
from dotenv import load_dotenv
from itertools import cycle
# JUDIE LIBRARIES
from OiaLt import OiaLt, help_oialt
from Nsfw import Nsfw
from Eternum import Eternum, help_eternum
from AccountManager import AccountManager
from Utilities import HelperClass, check_channel
from BotConfig import BotConfig
from Timekeeper import Timekeeper

#region Bot config
intents = discord.Intents().default()
intents.guilds = True

client = commands.Bot(command_prefix="-", help_command=None, case_insensitive=True, intents=intents)
client.config = BotConfig(client)
client.db_path = "main.sqlite"
load_dotenv()
TOKEN = os.getenv("TOKEN")
GUILD = discord.Object(id=os.getenv("GUILD"))

status = cycle(
    ["-help", "-help misc", "-help oialt", "-help eternum", "-help nsfw", "-ogf", "-oharem", "-stabbyclan", "-theboys",
     "-potentialLis", "-ocollections", "-oprotectors", "-nsfw", "-egf", "-eharem", "-homies", "-sidegirls",
     "-creatures", "-eprotectors", "-ecollections"])
#endregion


@client.event
async def on_ready():
    """
    A function called as soon as the bot is loaded up.

    Initializes all the cogs and creates/edits the database
    """
    await client.config.load()
    HelperClass.init(client)
    await Timekeeper.init(client)
    await createAndUpdateDatabase()
    changeGameActivity.start()

    await AccountManager.setup(client)
    await OiaLt.setup(client)
    await Nsfw.setup(client)
    await Eternum.setup(client)

    # sync the command tree to the server in question
    client.tree.clear_commands(guild=None)
    await client.tree.sync()
    try: 
        synced = await client.tree.sync(guild=client.config.guild)
        print(f"Successfully synchronised {len(synced)} commands to guild with ID {client.config.guild.id}.")
    except Exception as e:
        print(f"Error synchronising commands tree: {e}")

    print("Hello there!")


@tasks.loop(seconds=7)
async def changeGameActivity():
    """
    A looping function that changes the activity status of the bot to "playing" a random command.
    """
    await client.change_presence(activity=discord.Game(next(status)))


@client.tree.command(name="gm", description="Sends a good morning render featuring Lauren.", guild=GUILD)
async def gm(interaction: discord.Interaction):
    """
    Sends a beautiful legacy good morning render of Lauren.
    """
    image = discord.File(f"./GreetingImages/gm.png", filename="gm.png")
    await interaction.response.send_message(file=image)


@client.tree.command(name="gn", description="Sends a good night render featuring Judie.", guild=GUILD)
async def gn(interaction: discord.Interaction):
    """
    Sends a beautiful legacy good night render of Judie.
    """
    image = discord.File(f"./GreetingImages/gn.png", filename="gn.png")
    await interaction.response.send_message(file=image)


@client.tree.command(name="help", description="Helps understand how to use Judie's commands. example keywords: oialt, eternum, nsfw, general.", guild=GUILD)
@commands.check(check_channel)
async def help(interaction: discord.Interaction, plugin: str=None):
    """
    :TheyAskedForHaremAgain:
    Supposed to help people around; Is a massive mess of spaghetti code here. But yeah provides an overview of Judie's commands

    Parameters:
        - plugin: str - defaults to None
            The name of a specific section the user wants help for (from a variety of keywords)
    """
    title = "Judie's commands!"
    description = "Which category would you like to get the help commands from?\nJudie supports the following modules:"

    field_names = []
    field_values = []

    # default
    if plugin is None or plugin.lower() not in [
            "eternum", "oialt", "once in a lifetime", "nsfw", "general", "miscellaneous", "misc", "gen", "account", "accounts"
        ]:
        field_names.append("__OiaLt__")
        field_values.append("Commands for the classic Gf game! (-help OiaLt)")

        field_names.append("__Eternum__")
        field_values.append("Commands for the brand new Eternum GF game! (-help Eternum)")

        field_names.append("__Nsfw__")
        field_values.append("Commands for our lewds plugin! (-help Nsfw)")

        field_names.append("__General Commands__")
        field_values.append("Account Management & Miscellaneous Commands! (-help General)")
    #

    # Oialt
    elif plugin.lower() == "oialt" or plugin.lower() == "once in a lifetime":
        await help_oialt(interaction)
        return

    # NSFW
    elif plugin.lower() == "nsfw":
        title = "Judie's lewd stash!"
        description = "Please use in appropriate channels!"

        field_names.append("/nsfw [name]")
        field_values.append("Shows a random lewd including the character whose name you added!\n:warning: __Please use"
                            " this command in a channel marked **nsfw**__\nIf you don't add a name"
                            " it will choose a random lewd across all OiaLt and Eternum options!\n\n*Supported options:"
                            " Aiko, Carla, Iris, Jasmine, Judie, Lauren, Rebecca, Alex, Annie, Calypso, Dalia, Eva,"
                            " FoxMaidens (:warning: putting a space won't recognize it as fox maidens!), Lorelei, Luna, Maat, "
                            "Nancy, Nova, Penny, Wenlin, OiaLt, Eternum*")

    # Misc
    elif plugin.lower() in ["general", "miscellaneous", "misc", "gen", "account", "accounts"]:
        title = "Miscellaneous commands!"
        description = "Account management and a few other commands :)"

        field_names.append("-gm")
        field_values.append("Sends a good morning greeting to the fellas on discord!")

        field_names.append("-gn")
        field_values.append("Sends a good night wish to the fellas on discord!")

        field_names.append("-register")
        field_values.append("Register to the Judie Bot database! Required to play both gf games.\n"
                            "We only store your discord ID to track your collections :)")

        field_names.append("-deleteacc")
        field_values.append(
            "Delete all your entries to the database. *Please note that this action is __irreversible__.*")

    # eternum
    elif plugin.lower() == "eternum":
        await help_eternum(interaction)
        return

    field_names.append("__Further info__")
    field_values.append("For any other kind of information, feel free to contact **eisritter**!")

    footer = "WARNING: All of Judie's features contain spoilers to players who are not up to the current version" \
             " of Eternum."

    embed = discord.Embed(title=title, description=description, color=HelperClass.orange)
    embed.set_footer(text=footer)

    for i in range(0, len(field_names)):
        embed.add_field(name=field_names[i], value=field_values[i], inline=False)

    await interaction.response.send_message(embed=embed)

    
@client.tree.command(name="timers", description="Returns an overview of the time left until you can use the gf commands again.", guild=GUILD)
@commands.check(check_channel)
async def timers(interaction: discord.Interaction):
    """
    Provides an overview of the time left until a user can draw a gf in the gf games again.
    """
    ogf = client.tree.get_command("ogf", guild=GUILD)
    egf = client.tree.get_command("egf", guild=GUILD)
    
    dummy = discord.Object(id=interaction.id)
    dummy.author = interaction.user

    ogfTime = await Timekeeper.read_timer(ogf, interaction.user)
    ogfText = f"**-ogf**: you __can__ draw now!" if ogfTime.is_empty() \
        else f"**-ogf**: you can try again in {ogfTime.get_time()}"

    egfTime = await Timekeeper.read_timer(egf, interaction.user)
    egfText = f"**-egf**: you __can__ draw now!" if egfTime.is_empty()\
       else f"**-egf**: you can try again in {egfTime.get_time()}"

    embed = await HelperClass.createEmbed(title=f"Cooldown overview for {interaction.user.display_name}:", text=f"{ogfText}\n{egfText}")
    await interaction.response.send_message(embed=embed)


async def column_is_integer(cursor, table: str, column: str) -> bool:
    cursor.execute(f"PRAGMA table_info({table})")
    for row in cursor.fetchall():
        if row[1] == column:  # row[1] = column name, row[2] = declared type
            return row[2].upper() == "INTEGER"
    return False


async def createAndUpdateDatabase():
    """
    Defines the structure of the Judie Bot Database and updates the database's contents afterwards.
    """

    db = sqlite3.connect(client.db_path)
    cursor = db.cursor()

    print("Checking DB Integrity")

    #region users
    cursor.execute("""
            CREATE TABLE if NOT EXISTS users(
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            discord_id TEXT
            )
            """)
    #endregion

#region Oialt
    #region Overview: oialt
    cursor.execute("""
            CREATE TABLE if NOT EXISTS oialt(
            user_id INTEGER,
            funtime INTEGER DEFAULT 0,
            mc INTEGER DEFAULT 0,
            aiko INTEGER DEFAULT 0,
            nine_three INTEGER DEFAULT 0,
            last_gf TEXT
            )
            """)
    #endregion

    #region Harem: oialt_harem
    cursor.execute("""
                        CREATE TABLE IF NOT EXISTS oialt_harem(
                        user_id INTEGER,
                        judie TEXT DEFAULT NONE,
                        lauren TEXT DEFAULT NONE,
                        messy_hair_lauren TEXT DEFAULT NONE,
                        carla TEXT DEFAULT NONE,
                        iris TEXT DEFAULT NONE,
                        aiko TEXT DEFAULT NONE,
                        jasmine TEXT DEFAULT NONE,
                        rebecca TEXT DEFAULT NONE,
                        last_li TEXT
                        )
                        """)
    #endregion

    #region Stabby Clan: stabby_mikes
    cursor.execute("""
                        CREATE TABLE IF NOT EXISTS stabby_mikes(
                        user_id INTEGER,
                        police TEXT DEFAULT NONE,
                        hitman TEXT DEFAULT NONE,
                        yakuza TEXT DEFAULT NONE,
                        priest TEXT DEFAULT NONE,
                        exterminator TEXT DEFAULT NONE,
                        anastasia TEXT DEFAULT NONE,
                        last_mike TEXT
                        )
                        """)
    #endregion

    #region The Boys: the_boys
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS the_boys(
                    user_id INTEGER,
                    mc TEXT DEFAULT NONE,
                    tom TEXT DEFAULT NONE,
                    oliver TEXT DEFAULT NONE,
                    fit_jack TEXT DEFAULT NONE,
                    asmodeus TEXT DEFAULT NONE,
                    hiromi TEXT DEFAULT NONE,
                    last_boi TEXT
                    )
                    """)
    #endregion

    #region Potential LI's: li_potential
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS li_potential(
                    user_id INTEGER,
                    ava TEXT DEFAULT NONE,
                    lilith TEXT DEFAULT NONE,
                    fit_jack_groupie TEXT DEFAULT NONE,
                    train_conductor TEXT DEFAULT NONE,
                    shop_girl TEXT DEFAULT NONE,
                    stone_elephant TEXT DEFAULT NONE,
                    last_potential_li TEXT
                    )
                    """)
    #endregion
#endregion

#region Eternum
    #region Overview: eternum
    cursor.execute("""
            CREATE TABLE if NOT EXISTS eternum(
            user_id INTEGER,
            orion INTEGER DEFAULT 0,
            calypso INTEGER DEFAULT 0,
            dalia INTEGER DEFAULT 0,
            pyramid_head INTEGER DEFAULT 0,
            last_gf TEXT
            )
            """)
    #endregion

    #region Harem: eternum_harem
    cursor.execute("""
                CREATE TABLE IF NOT EXISTS eternum_harem(
                user_id INTEGER,
                alex TEXT DEFAULT NONE,
                annie TEXT DEFAULT NONE,
                calypso TEXT DEFAULT NONE,
                dalia TEXT DEFAULT NONE,
                luna TEXT DEFAULT NONE,
                nancy TEXT DEFAULT NONE,
                nova TEXT DEFAULT NONE,
                penny TEXT DEFAULT NONE,
                last_girl TEXT
                )
                """)
    #endregion

    #region The homies: homies
    cursor.execute("""
                CREATE TABLE IF NOT EXISTS homies(
                user_id INTEGER,
                chang TEXT DEFAULT NONE,
                chopchop TEXT DEFAULT NONE,
                victor TEXT DEFAULT NONE,
                jerry TEXT DEFAULT NONE,
                micaela TEXT DEFAULT NONE,
                noah TEXT DEFAULT NONE,
                orion TEXT DEFAULT NONE,
                raul TEXT DEFAULT NONE,
                last_homie TEXT
                )
                """)
    #endregion

    #region Side Girls: side_girls
    cursor.execute("""
                CREATE TABLE IF NOT EXISTS side_girls(
                user_id INTEGER,
                bluefoxmaiden TEXT DEFAULT NONE,
                lorelei TEXT DEFAULT NONE,
                eva TEXT DEFAULT NONE,
                idriel TEXT DEFAULT NONE,
                maat TEXT DEFAULT NONE,
                redfoxmaiden TEXT DEFAULT NONE,
                wenlin TEXT DEFAULT NONE,
                last_affair TEXT
                )
                """)
    #endregion

    #region Pets: creatures
    cursor.execute("""
                CREATE TABLE if NOT EXISTS creatures(
                user_id INTEGER,
                carolyn TEXT DEFAULT NONE,
                igor TEXT DEFAULT NONE,
                kermit TEXT DEFAULT NONE,
                mauricec TEXT DEFAULT NONE,
                mauriceg TEXT DEFAULT NONE,
                mauricet TEXT DEFAULT NONE,
                pancho TEXT DEFAULT NONE,
                last_creature TEXT
                )
                """)
    #endregion

    db.commit()
#endregion

    #region DB update code
    # SQLite extra guides because I'll forget otherwise:
        # if EXISTS not supported in ALTER TABLE statements
        # UPDATE [table_name]
        # DROP COLUMN not supported as an ALTER TABLE function
    print("Performing Database Updates.")

    #region table oialt_harem to integer
    try:
        if not await column_is_integer(cursor, "oialt_harem", "judie"):
            # create a temp table with the new type
            cursor.execute("""
                CREATE TABLE oharem_temp(
                    user_id INTEGER,
                    judie INTEGER DEFAULT 0,
                    lauren INTEGER DEFAULT 0,
                    messy_hair_lauren INTEGER DEFAULT 0,
                    carla INTEGER DEFAULT 0,
                    iris INTEGER DEFAULT 0,
                    aiko INTEGER DEFAULT 0,
                    jasmine INTEGER DEFAULT 0,
                    rebecca INTEGER DEFAULT 0,
                    last_li TEXT
                )
            """)

            # insert values derived from 'old' table
            cursor.execute("""
                INSERT INTO oharem_temp (user_id, judie, lauren, messy_hair_lauren, carla, iris, aiko, jasmine, rebecca, last_li)
                SELECT
                    user_id,
                    CASE WHEN COALESCE(judie, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                    CASE WHEN COALESCE(lauren, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                    CASE WHEN COALESCE(messy_hair_lauren, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                    CASE WHEN COALESCE(carla, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                    CASE WHEN COALESCE(iris, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                    CASE WHEN COALESCE(aiko, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                    CASE WHEN COALESCE(jasmine, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                    CASE WHEN COALESCE(rebecca, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                    last_li
                FROM oialt_harem
            """)

            # drop old table
            cursor.execute("DROP TABLE oialt_harem")

            # rename 'new' table to oialt_harem
            cursor.execute("ALTER TABLE oharem_temp RENAME TO oialt_harem")

            db.commit()

    except Exception as e:
        print(f"[oialt_harem to int] {e}")
        traceback.print_exc()
    #endregion

    #region table stabby_mikes to integer
    try:
        if not await column_is_integer(cursor, "stabby_mikes", "police"):
            # create a temp table with the new type
            cursor.execute("""
                CREATE TABLE mikes_temp(
                    user_id INTEGER,
                    police INTEGER DEFAULT 0,
                    hitman INTEGER DEFAULT 0,
                    yakuza INTEGER DEFAULT 0,
                    priest INTEGER DEFAULT 0,
                    exterminator INTEGER DEFAULT 0,
                    anastasia INTEGER DEFAULT 0,
                    last_mike TEXT
                )
            """)

            # insert values derived from 'old' table
            cursor.execute("""
                INSERT INTO mikes_temp (user_id, police, hitman, yakuza, priest, exterminator, anastasia, last_mike)
                SELECT
                    user_id,
                    CASE WHEN COALESCE(police, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                    CASE WHEN COALESCE(hitman, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                    CASE WHEN COALESCE(yakuza, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                    CASE WHEN COALESCE(priest, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                    CASE WHEN COALESCE(exterminator, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                    CASE WHEN COALESCE(anastasia, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                    last_mike
                FROM stabby_mikes
            """)

            # drop old table
            cursor.execute("DROP TABLE stabby_mikes")

            # rename 'new' table to oialt_harem
            cursor.execute("ALTER TABLE mikes_temp RENAME TO stabby_mikes")

            db.commit()

    except Exception as e:
        print(f"[stabby_mikes to int] {e}")
        traceback.print_exc()
    #endregion

    #region table the_boys to integer
    try:
        if not await column_is_integer(cursor, "the_boys", "mc"):
            # create a temp table with the new type
            cursor.execute("""
                CREATE TABLE boys_temp(
                    user_id INTEGER,
                    mc INTEGER DEFAULT 0,
                    tom INTEGER DEFAULT 0,
                    oliver INTEGER DEFAULT 0,
                    fit_jack INTEGER DEFAULT 0,
                    asmodeus INTEGER DEFAULT 0,
                    hiromi INTEGER DEFAULT 0,
                    last_boi TEXT
                )
            """)

            # insert values derived from 'old' table
            cursor.execute("""
                INSERT INTO boys_temp (user_id, mc, tom, oliver, fit_jack, asmodeus, hiromi, last_boi)
                SELECT
                    user_id,
                    CASE WHEN COALESCE(mc, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                    CASE WHEN COALESCE(tom, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                    CASE WHEN COALESCE(oliver, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                    CASE WHEN COALESCE(fit_jack, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                    CASE WHEN COALESCE(asmodeus, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                    CASE WHEN COALESCE(hiromi, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                    last_boi
                FROM the_boys
            """)

            # drop old table
            cursor.execute("DROP TABLE the_boys")

            # rename 'new' table to oialt_harem
            cursor.execute("ALTER TABLE boys_temp RENAME TO the_boys")

            db.commit()

    except Exception as e:
        print(f"[the_boys to int] {e}")
        traceback.print_exc()
    #endregion

    #region table li_potential to integer
    try:
        if not await column_is_integer(cursor, "li_potential", "ava"):
            # create a temp table with the new type
            cursor.execute("""
                CREATE TABLE potlis_temp(
                    user_id INTEGER,
                    ava INTEGER DEFAULT 0,
                    lilith INTEGER DEFAULT 0,
                    fit_jack_groupie INTEGER DEFAULT 0,
                    train_conductor INTEGER DEFAULT 0,
                    shop_girl INTEGER DEFAULT 0,
                    stone_elephant INTEGER DEFAULT 0,
                    last_potential_li TEXT
                )
            """)

            # insert values derived from 'old' table
            cursor.execute("""
                INSERT INTO potlis_temp (user_id, ava, lilith, fit_jack_groupie, train_conductor, shop_girl, stone_elephant, last_potential_li)
                SELECT
                    user_id,
                    CASE WHEN COALESCE(ava, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                    CASE WHEN COALESCE(lilith, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                    CASE WHEN COALESCE(fit_jack_groupie, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                    CASE WHEN COALESCE(train_conductor, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                    CASE WHEN COALESCE(shop_girl, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                    CASE WHEN COALESCE(stone_elephant, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                    last_potential_li
                FROM li_potential
            """)

            # drop old table
            cursor.execute("DROP TABLE li_potential")

            # rename 'new' table to oialt_harem
            cursor.execute("ALTER TABLE potlis_temp RENAME TO li_potential")

            db.commit()

    except Exception as e:
        print(f"[li_potential to int] {e}")
        traceback.print_exc()
    #endregion

    #region table eternum_harem to integer
    try:
        if not await column_is_integer(cursor, "eternum_harem", "alex"):
            # create a temp table with the new type
            cursor.execute("""
                CREATE TABLE eharem_temp(
                    user_id INTEGER,
                    alex INTEGER DEFAULT 0,
                    annie INTEGER DEFAULT 0,
                    calypso INTEGER DEFAULT 0,
                    dalia INTEGER DEFAULT 0,
                    luna INTEGER DEFAULT 0,
                    nancy INTEGER DEFAULT 0,
                    nova INTEGER DEFAULT 0,
                    penny INTEGER DEFAULT 0,
                    last_girl TEXT
                )
            """)

            # insert values derived from 'old' table
            cursor.execute("""
                INSERT INTO eharem_temp (user_id, alex, annie, calypso, dalia, luna, nancy, nova, penny, last_girl)
                SELECT
                    user_id,
                    CASE WHEN COALESCE(alex, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                    CASE WHEN COALESCE(annie, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                    CASE WHEN COALESCE(calypso, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                    CASE WHEN COALESCE(dalia, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                    CASE WHEN COALESCE(luna, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                    CASE WHEN COALESCE(nancy, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                    CASE WHEN COALESCE(nova, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                    CASE WHEN COALESCE(penny, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                    last_girl
                FROM eternum_harem
            """)

            # drop old table
            cursor.execute("DROP TABLE eternum_harem")

            # rename 'new' table to oialt_harem
            cursor.execute("ALTER TABLE eharem_temp RENAME TO eternum_harem")

            db.commit()

    except Exception as e:
        print(f"[eternum_harem to int] {e}")
        traceback.print_exc()
    #endregion

    #region table homies to integer
    try:
        if not await column_is_integer(cursor, "homies", "chang"):
            # create a temp table with the new type
            cursor.execute("""
                CREATE TABLE homies_temp(
                    user_id INTEGER,
                    chang INTEGER DEFAULT 0,
                    chopchop INTEGER DEFAULT 0,
                    victor INTEGER DEFAULT 0,
                    jerry INTEGER DEFAULT 0,
                    micaela INTEGER DEFAULT 0,
                    noah INTEGER DEFAULT 0,
                    orion INTEGER DEFAULT 0,
                    raul INTEGER DEFAULT 0,
                    last_homie TEXT
                )
            """)

            # insert values derived from 'old' table
            cursor.execute("""
                INSERT INTO homies_temp (user_id, chang, chopchop, victor, jerry, micaela, noah, orion, raul, last_homie)
                SELECT
                    user_id,
                    CASE WHEN COALESCE(chang, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                    CASE WHEN COALESCE(chopchop, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                    CASE WHEN COALESCE(victor, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                    CASE WHEN COALESCE(jerry, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                    CASE WHEN COALESCE(micaela, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                    CASE WHEN COALESCE(noah, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                    CASE WHEN COALESCE(orion, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                    CASE WHEN COALESCE(raul, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                    last_homie
                FROM homies
            """)

            # drop old table
            cursor.execute("DROP TABLE homies")

            # rename 'new' table to oialt_harem
            cursor.execute("ALTER TABLE homies_temp RENAME TO homies")

            db.commit()

    except Exception as e:
        print(f"[homies to int] {e}")
        traceback.print_exc()
    #endregion

    #region table side_girls to integer
    try:
        if not await column_is_integer(cursor, "side_girls", "bluefoxmaiden"):
            # create a temp table with the new type
            cursor.execute("""
                CREATE TABLE sides_temp(
                    user_id INTEGER,
                    bluefoxmaiden INTEGER DEFAULT 0,
                    lorelei INTEGER DEFAULT 0,
                    eva INTEGER DEFAULT 0,
                    idriel INTEGER DEFAULT 0,
                    maat INTEGER DEFAULT 0,
                    redfoxmaiden INTEGER DEFAULT 0,
                    wenlin INTEGER DEFAULT 0,
                    last_affair TEXT
                )
            """)

            # insert values derived from 'old' table
            cursor.execute("""
                INSERT INTO sides_temp (user_id, bluefoxmaiden, lorelei, eva, idriel, maat, redfoxmaiden, wenlin, last_affair)
                SELECT
                    user_id,
                    CASE WHEN COALESCE(bluefoxmaiden, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                    CASE WHEN COALESCE(lorelei, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                    CASE WHEN COALESCE(eva, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                    CASE WHEN COALESCE(idriel, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                    CASE WHEN COALESCE(maat, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                    CASE WHEN COALESCE(redfoxmaiden, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                    CASE WHEN COALESCE(wenlin, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                    last_affair
                FROM side_girls
            """)

            # drop old table
            cursor.execute("DROP TABLE side_girls")

            # rename 'new' table to oialt_harem
            cursor.execute("ALTER TABLE sides_temp RENAME TO side_girls")

            db.commit()

    except Exception as e:
        print(f"[side_girls to int] {e}")
        traceback.print_exc()
    #endregion

    #region table creatures to integer
    try:
        if not await column_is_integer(cursor, "creatures", "carolyn"):
            # create a temp table with the new type
            cursor.execute("""
                CREATE TABLE pets_temp(
                    user_id INTEGER,
                    carolyn INTEGER DEFAULT 0,
                    igor INTEGER DEFAULT 0,
                    kermit INTEGER DEFAULT 0,
                    mauricec INTEGER DEFAULT 0,
                    mauriceg INTEGER DEFAULT 0,
                    mauricet INTEGER DEFAULT 0,
                    pancho INTEGER DEFAULT 0,
                    last_creature TEXT
                )
            """)

            # insert values derived from 'old' table
            cursor.execute("""
                INSERT INTO pets_temp (user_id, carolyn, igor, kermit, mauricec, mauriceg, mauricet, pancho, last_creature)
                SELECT
                    user_id,
                    CASE WHEN COALESCE(carolyn, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                    CASE WHEN COALESCE(igor, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                    CASE WHEN COALESCE(kermit, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                    CASE WHEN COALESCE(mauricec, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                    CASE WHEN COALESCE(mauriceg, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                    CASE WHEN COALESCE(mauricet, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                    CASE WHEN COALESCE(pancho, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                    last_creature
                FROM creatures
            """)

            # drop old table
            cursor.execute("DROP TABLE creatures")

            # rename 'new' table to oialt_harem
            cursor.execute("ALTER TABLE pets_temp RENAME TO creatures")

            db.commit()

    except Exception as e:
        print(f"[creatures to int] {e}")
        traceback.print_exc()
    #endregion

    #endregion

    db.commit()
    cursor.close()
    db.close()


if __name__ == '__main__':
    client.run(TOKEN)
