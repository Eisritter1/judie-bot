# DISCORD LIBRARIES
import discord
from discord.ext import commands, tasks
# EXTERNAL LIBRARIES
import sqlite3
import os
from dotenv import load_dotenv
from itertools import cycle
# JUDIE LIBRARIES
from OiaLt import OiaLt, help_oialt
from Nsfw import Nsfw
from Eternum import Eternum, help_eternum
from AccountManager import AccountManager
from Utilities import HelperClass, TimeObject, check_channel
from BotConfig import BotConfig

#region Bot config
client = commands.Bot(command_prefix="-", help_command=None, case_insensitive=True, intents=discord.Intents.all())
client.config = BotConfig(client)
client.CogsToActivate = []
load_dotenv()
TOKEN = os.getenv("TOKEN")

extensions = [AccountManager(client), OiaLt(client), Nsfw(client), Eternum(client)]
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
    for extension in extensions:
        try:
            await client.add_cog(extension)
            print(f"loaded extension {extension}!")
        except Exception as error:
            print('{} cannot be loaded. [{}]'.format(extension, error))
    
    await client.config.load()
    HelperClass.init(client)
    await createDatabase()
    changeGameActivity.start()

    for cog in client.CogsToActivate:
        if hasattr(cog, "activate"):
            cog.activate()

    print("Hello there!")


@tasks.loop(seconds=7)
async def changeGameActivity():
    """
    A looping function that changes the activity status of the bot to "playing" a random command.
    """
    await client.change_presence(activity=discord.Game(next(status)))


@client.command()
async def gm(ctx):
    """
    Sends a beautiful legacy good morning render of Lauren.
    """
    image = discord.File(f"./GreetingImages/gm.png", filename="gm.png")
    await ctx.send(file=image)


@client.command()
async def gn(ctx):
    """
    Sends a beautiful legacy good night render of Judie.
    """
    image = discord.File(f"./GreetingImages/gn.png", filename="gn.png")
    await ctx.send(file=image)


@client.command()
@commands.check(check_channel)
async def gf(ctx):
    """
    Obsolete command; All it does now is send an easter egg message :D
    """
    await ctx.send("Command was updated! You're probably looking for **-ogf**!\n-help oialt for the specific commands!")


@client.command()
@commands.check(check_channel)
async def help(ctx, plugin=None):
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
        help_oialt(ctx)

    # NSFW
    elif plugin.lower() == "nsfw":
        title = "Judie's lewd stash!"
        description = "Please use in appropriate channels!"

        field_names.append("-nsfw [name]")
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
        help_eternum(ctx)

    field_names.append("__Further info__")
    field_values.append("For any other kind of information, feel free to contact **eisritter**!")

    footer = "WARNING: All of Judie's features contain spoilers to players who are not up to the current version" \
             " of Eternum."

    embed = discord.Embed(title=title, description=description, color=HelperClass.orange)
    embed.set_footer(text=footer)

    for i in range(0, len(field_names)):
        embed.add_field(name=field_names[i], value=field_values[i], inline=False)

    await ctx.send(embed=embed)


# find a way to prevent/reset cooldowns if TimeInSecs == 0
@client.command()
@commands.check(check_channel)
async def timers(ctx):
    """
    Provides an overview of the time left until a user can draw a gf in the gf games again.
    """
    ogf = client.get_command("ogf")
    egf = client.get_command("egf")

    ogfTimeInSecs = ogf._buckets.get_bucket(ctx.message).get_retry_after()
    ogfTime = None if ogfTimeInSecs == None else TimeObject(ogfTimeInSecs)
    ogfText = f"**-ogf**: you __can__ draw now!" if ogfTimeInSecs == 0 else f"**-ogf**: you can try again in {ogfTime.hours:02}:{ogfTime.minutes:02}:{ogfTime.seconds:02}"

    egfTimeInSecs = egf._buckets.get_bucket(ctx.message).get_retry_after()
    egfTime = None if egfTimeInSecs == None else TimeObject(egfTimeInSecs)
    egfText = f"**-egf**: you __can__ draw now!" if egfTimeInSecs == 0 else f"**-egf**: you can try again in {egfTime.hours:02}:{egfTime.minutes:02}:{egfTime.seconds:02}"

    embed = await HelperClass.createEmbed(title=f"Cooldown overview for {ctx.author.display_name}:", text=f"{ogfText}\n{egfText}")
    await ctx.send(embed=embed)
    


async def createDatabase():
    """
    Defines the structure of the Judie Bot Database and updates the database's contents afterwards.
    """

    db = sqlite3.connect("main.sqlite")
    cursor = db.cursor()

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
    # on Next Deployment: add column Calypso
    cursor.execute("""
                CREATE TABLE IF NOT EXISTS eternum_harem(
                user_id INTEGER,
                alex TEXT DEFAULT NONE,
                annie TEXT DEFAULT NONE,
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
    # On Next Deployment: Rename column calypso to lorelei
    cursor.execute("""
                CREATE TABLE IF NOT EXISTS side_girls(
                user_id INTEGER,
                bluefoxmaiden TEXT DEFAULT NONE,
                calypso TEXT DEFAULT NONE,
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
#endregion

    #region DB update code
    # SQLite extra guides because I'll forget otherwise:
        # if EXISTS not supported in ALTER TABLE statements
        # UPDATE [table_name]
        # DROP COLUMN not supported as an ALTER TABLE function
    try:
        # SQL here
        cursor.execute("""
            ALTER TABLE eternum_harem ADD COLUMN calypso TEXT DEFAULT NONE
        """)
    except Exception as e:
        print(f"[Add new column calypso] {e}")

    try:
        cursor.execute("""
            UPDATE eternum_harem 
            SET calypso = (
                SELECT side_girls.calypso
                FROM side_girls
                WHERE eternum_harem.user_id = side_girls.user_id
            ) WHERE EXISTS (
                SELECT 1
                FROM side_girls
                WHERE eternum_harem.user_id = side_girls.user_id
            )
        """)
    except Exception as e:
        print(f"[Transfer Calypso values to Harem] {e}")

    try:
        cursor.execute("""
            ALTER TABLE side_girls RENAME COLUMN calypso TO lorelei
        """)
    except Exception as e:
        print(f"[Rename old column calypso to lorelei] {e}")

    try:
        cursor.execute("""
            UPDATE side_girls SET lorelei = 'NONE'
        """)
    except Exception as e:
        print(f"[Reset lorelei column] {e}")
    #endregion

    db.commit()
    cursor.close()
    db.close()


if __name__ == '__main__':
    client.run(TOKEN)
