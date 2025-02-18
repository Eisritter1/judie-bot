import discord
import random
import sqlite3
import os
from discord import Embed, File
from discord.ext import commands, tasks
from discord.ext.commands import cooldown, BucketType
from dotenv import load_dotenv
from itertools import cycle
from OiaLt import OiaLt
from Nsfw import Nsfw
from Eternum import Eternum
from AccountManager import AccountManager

client = commands.Bot(command_prefix="-", help_command=None, case_insensitive=True, intents=discord.Intents.all())
load_dotenv()
TOKEN = os.getenv("TOKEN")

extensions = [OiaLt(client), Nsfw(client), Eternum(client), AccountManager(client)]
status = cycle(
    ["-help", "-help misc", "-help oialt", "-help eternum", "-help nsfw", "-ogf", "-oharem", "-stabbyclan", "-theboys",
     "-potentialLis", "-ocollections", "-oprotectors", "-nsfw", "-egf", "-eharem", "-homies", "-sidegirls",
     "-creatures", "-eprotectors", "-ecollections"])


@client.event
async def on_ready():
    for extension in extensions:
        try:
            await client.add_cog(extension)
            print(f"loaded extension {extension}!")
        except Exception as error:
            print('{} cannot be loaded. [{}]'.format(extension, error))
    await createDatabase()
    changeGameActivity.start()
    print("Hello there!")


@tasks.loop(seconds=7)
async def changeGameActivity():
    await client.change_presence(activity=discord.Game(next(status)))


@client.command()
async def gm(ctx):
    image = discord.File(f"./GreetingImages/gm.png", filename="gm.png")
    await ctx.send(file=image)


@client.command()
async def gn(ctx):
    image = discord.File(f"./GreetingImages/gn.png", filename="gn.png")
    await ctx.send(file=image)


@client.command()
async def gf(ctx):
    await ctx.send("Command was updated! You're probably looking for **-ogf**!\n-help oialt for the specific commands!")


@client.command()
async def help(ctx, plugin=None):
    title = "Judie's commands!"
    description = "Which category would you like to get the help commands from?\nJudie supports the following modules:"

    field_names = []
    field_values = []

    # <editor-fold desc="Oialt">
    if plugin.lower() == "oialt" or plugin.lower() == "once in a lifetime":
        title = "Judie's OiaLt gf game!"
        description = "Here are the commands to use the oialt gf system!"

        field_names.append("-ogf (oialt gf)")
        field_values.append("pull a random gf from the OiaLt world! (23h cooldown!)")

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
    # </editor-fold>

    # <editor-fold desc="NSFW Commands">
    elif plugin.lower() in ["nsfw", "not safe for work"]:
        title = "Judie's lewd stash!"
        description = "Please use in appropriate channels!"

        field_names.append("-nsfw [name]")
        field_values.append("Shows a random lewd including the character whose name you added!\n:warning: __Please use"
                            " this command in a channel marked **nsfw**__\nIf you don't add a name"
                            " it will choose a random lewd across all OiaLt and Eternum options!\n\n*Supported options:"
                            " Aiko, Carla, Iris, Jasmine, Judie, Lauren, Rebecca, Alex, Annie, Calypso, Dalia, Eva,"
                            " FoxMaidens (:warning: putting a space won't recognize it as fox maidens!), Luna, Maat, "
                            "Nancy, Nova, Penny, Wenlin, OiaLt, Eternum*")
    # </editor-fold>

    # <editor-fold desc="Misc">
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

        field_names.append("-update")
        field_values.append("Update your account to Judie v2.0 (last updated September 2022)!")

        field_names.append("-deleteacc")
        field_values.append(
            "Delete all your entries to the database. *Please note that this action is __irreversible__.*")
    # </editor-fold>

    # <editor-fold desc="Eternum">
    elif plugin.lower() == "eternum":
        title = "Judie's Eternum gf game!"
        description = "Here are the commands to use the eternum gf game:"

        field_names.append("-egf (eternum gf)")
        field_values.append("pull a random gf from the eternum universe! (23hr cooldown)")

        field_names.append("-eCollections (eternum collections)")
        field_values.append("get an overview of all your eternum collections!")

        field_names.append("-eharem (eternum harem)")
        field_values.append(
            "check your progress in the harem collection\n--> Contains **Alex, Annie, Dalia, Luna, Nancy, Nova & Penny**")

        field_names.append("-homies (the homies)")
        field_values.append(
            "check your progress in the homie collection\n--> Contains **Chang, Chop Chop, Mr. Hernandez, Jerry, Micaela, Noah, Orion & Raul**")

        field_names.append("-sidegirls")
        field_values.append(
            "check your progress in the side girl collection\n--> Contains **Blue Fox Maiden, Calypso, Eva, Idriel, Maat, Red Fox Maiden & Wenlin**")

        field_names.append("-creatures")
        field_values.append(
            "check your progress in the creatures collection\n--> Contains **Carolyn, Igor, Kermit, Maurice, Maurice, Maurice, Pancho**")

        field_names.append("-eprotectors")
        field_values.append("Check your protections against various villains!\n--> Contains **Orion, Calypso, Dalia &"
                            " Pyramid Head**")
    # </editor-fold>

    # <editor-fold desc="Main Command">
    else:
        field_names.append("__OiaLt__")
        field_values.append("Commands for the classic Gf game! (-help OiaLt)")

        field_names.append("__Eternum__")
        field_values.append("Commands for the brand new Eternum GF game! (-help Eternum)")

        field_names.append("__Nsfw__")
        field_values.append("Commands for our lewds plugin! (-help Nsfw)")

        field_names.append("__General Commands__")
        field_values.append("Account Management & Miscellaneous Commands! (-help General)")
    # </editor-fold>

    field_names.append("__Further info__")
    field_values.append("For any other kind of information, feel free to contact **eisritter**!")

    footer = "WARNING: All of Judie's features contain spoilers to players who are not up to the current version" \
             " of Eternum."

    embed = discord.Embed(title=title, description=description, color=0xFFA800)
    embed.set_footer(text=footer)

    for i in range(0, len(field_names)):
        embed.add_field(name=field_names[i], value=field_values[i], inline=False)

    await ctx.send(embed=embed)


async def createDatabase():
    db = sqlite3.connect("main.sqlite")
    cursor = db.cursor()

    # <editor-fold desc="Users">
    cursor.execute("""
            CREATE TABLE if NOT EXISTS users(
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            discord_id TEXT
            )
            """)
    # </editor-fold>

    # <editor-fold desc="Oialt">
    # <editor-fold desc="Overview: oialt">
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
    # </editor-fold>

    # <editor-fold desc="Harem: oialt_harem">
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
    # </editor-fold>

    # <editor-fold desc="Stabby Clan: stabby_mikes">
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
    # </editor-fold>

    # <editor-fold desc="The Boys: the_boys">
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
    # </editor-fold>

    # <editor-fold desc="Potential LI's: li_potential">
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
    # </editor-fold>
    # </editor-fold>

    # <editor-fold desc="Eternum">
    # <editor-fold desc="Overview: eternum">
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
    # </editor-fold>

    # <editor-fold desc="Harem: eternum_harem">
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
    # </editor-fold>

    # <editor-fold desc="The homies: homies">
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
    # </editor-fold>

    # <editor-fold desc="Side Girls: side_girls">
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
    # </editor-fold>

    # <editor-fold desc="Pets: creatures">
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
    # </editor-fold>
    # </editor-fold>

    # <editor-fold desc="Patch 2.5.1: Update Chang full name">
    try:
        cursor.execute("UPDATE homies SET chang=? WHERE chang=?", ["Chang Wong", "Chang Zhong"])
    except Exception as e:
        print(e)
    # </editor-fold>

    db.commit()
    cursor.close()


if __name__ == '__main__':
    client.run(TOKEN)
