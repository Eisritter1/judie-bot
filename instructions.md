# Judie Bot Deployment & Modder's Guide!

Hi! If you're reading this, you are probably wondering how you can add Judie to your servers, and/or how you can add some cool features you came up with yourself!

A quick disclaimer before we begin. Deploying and extending Judie by yourself is an task you undertake at your own risk, on your own resources. The official developers (maintainers of the 'main' Judie repository linked in her bio) do not provide any hardware for hosting the bot, nor are they responsible for any custom code or additions (and any consequences thereof) you make in forks or own deployments of the bot, that is not embedded in code on the official repository.


## Assumptions & Guidelines
- Anyone wishing to deploy Judie for their own server should be at least somewhat literate in **python programming**, and potentially **SQL** for deeper-lying changes (it is generally shady to use code you don't understand!).
- For 24/7 runtime users need to find and deploy their own resources. This is just software that runs when executed and stops with any shutdown if you run it on your PC. Since cooldowns are now persistent, you do not need constant runtime if the bot will be used in a smaller group.
- It is recommended to use an IDE for this endeavour. The project is set up for Visual Studio (not VS Code), which has a free community version.
- Some information needed for the bot to work requires you to enable __developer mode__ on discord, at `settings > Developer > Developer Mode`.

That being said, let's dive in!

## Contents:
1. [Home Deployment Guide](#1-home-deployment-guide) 
1.A) [Set up a discord bot](#a-set-up-a-discord-bot)
1.B) [Set up the code project](#b-set-up-the-code-project)
1.C) [Set up the .env file](#c-set-up-the-env-file) 
1.D) [Set up the bot's config values](#d-set-up-the-bots-configuration)
2. [Modder's Guide](#2-modders-guide)
2.A) [Adding a custom, non-collectible character](#a-adding-a-custom-character-to-the-gf-games-non-collectible)
2.B) [Adding a character to an existing collection](#b-adding-a-character-to-an-existing-collection)
2.C) [Adding a new collection](#c-adding-a-new-collection)
2.D) [Other additions](#d-other-additions)

# 1. Home Deployment Guide

This section describes the process for you to download Judie's code, and add her to your servers without changing any functionalities in code.

## A) Set up a discord bot:
Before diving into the code, first you need to set up the discord side of things. It's kinda like setting up a discord account for your bot, but it is strictly forbidden to add a bot to regular user accounts, we have to do this via discord's dev portal, for which you should be able to register with your normal discord account.

- Go to the [Discord Developers Portal](https://discord.com/developers/applications) and __create a new application__ on the top right.
- You can customise your bot to your liking there. As noted in the next sections you will need to add a few emoji in the `Emojis` tab on the left
- Head to the `Bot` tab, and view your **Token**. Copy it and save it for later in a blank txt file. **This token allows ANYONE WHO KNOWS ITS VALUE to connect __AS THIS BOT__.** It is *very important you don't share this value* with anyone you don't trust. The token is a very long sequence of seemingly random letters and numbers.
- If you are deploying Judie to a small community (under 10.000 members) you can just check on all intents. If you do this, follow the instructions in all caps on `main.py` when you have set up the code project. In general it is easier for a private server to just give the bot admin permissions and all intents, but if you want to (understandably) micromanage permissions, the most important are:
> - OAuth2 Permissions: bot
> - Bot Permissions: See Channels, Send Messages, Use External Emoji [, Role Management for if auto-role assignment gets added]
> - Bot Privileged Intents: None required, BUT if you want to use Judie with the prefix again, you at least need to add the Message Content Privileged Intent enabled. Note that Discord will demand explanations if your server has more than 10.000 members, and will deny you the request for keeping the intents on, unless you change Judie's behaviour radically.
- Then you can invite your bot to your server by generating an invite link in the OAuth2 tab.

## B) Set up the code project:
Now that we have the front-facing part set up, we can dive into making the bot work! 
Please note this is drafted from my experience working on Windows 10/11. I have no idea how to replicate some of these steps on MacOS, or Linux. 

- To access the code, you can either just clone the repository (linked in Judie's bio, or in #links), or download it as a .zip file and extract it to wherever you want to have it.
- For the bot to work, the code needs to be run on a machine. If you don't need 24/7 uptime, your PC should do, otherwise you have to rent a server, or set your local device up as one.
> For server renting, I use Google Cloud because it reliably guaranteed 24/7, uninterrupted runtime, which costs ~US$10 per month. This is no longer necessary since cooldowns are no longer dependent on runtime, so models like Replit's might be more viable now, assuming they still provide their service for free. There are plenty of alternatives as well I am sure, at varying degrees of reliability.
- The machine needs to have **Python** installed. I worked with version __3.9.4__ in development, so make sure the version is either that or later. You can check your version by opening a Command-Line Interface (CLI) by typing cmd in your start menu, then typing `python --version` and pressing enter.
- Next, you will need to install the dependencies for the project. 
> **PLEASE NOTE THAT THIS INSTRUCTION, IF UNCHECKED, MAY RESULT IN THE INSTALLATION OF MALWARE IF MALICIOUS PACKAGES ARE INCLUDED. REVIEW THE CONTENTS OF requirements.txt BEFORE RUNNING THIS INSTRUCTION, AND NEVER INSTALL PACKAGES YOU DO NOT TRUST.**
Open the CLI again in the project folder (on windows, you can right-click in the file explorer, and select "Open in Terminal"), then type and run `pip install -r requirements.txt`. This process may take a while, and automatically installs all packages listed in the file `requirements.txt`.
- Once the pre-requisites are installed, you can open your IDE in the code folder. If you use VisualStudio as recommended, you can just open the `code.sln` file. If not, you should be able to delete the `.sln` file and set up your project manually.

## C) Set up the .env file
Once you have the project set up, we can take a short minute to set up the environment variables. These are sensitive values that could result in people usurping your bot if shown to someone you do not trust. Never publish this file, or any of its contents.

- Navigate in your file explorer to the project's `code` folder, and create an empty text file, which you can name whatever you want.
- Open the text file, and type in `TOKEN=`, then paste in the Token value you saved in step 1.A) here. Make sure there is no whitespace.
- On Discord, go to the server you want to add Judie in / have added her into already. Right-click the server icon, then select "Copy server ID" all the way at the bottom. If you do not see this option beneath "Leave server", go to settings and enable developer mode before retrying.
- In a new line, type in `GUILD=`, then paste in the ID you just copied, again without any whitespace.
- save the text file and close the window.
- Ensure that file types are visible in your explorer, by navigating to `View > Show`, then checking on `File name extensions`.
- rename the text file to .env, making sure to __overwrite the file type__. The file should ask you whether you are sure you want to change the file type, which you will confirm.
> If the name change did not trigger the confirmation window, or if it is still called `.env.txt`, the renaming went wrong. Try again.

## D) Set up the bot's configuration:
In summary, so far we have our discord bot created, a machine with python and project dependencies installed, and the environment variables safely stored where they need to be. 
If you try running the code, it should compile, but throw an error and exit, stating there is "No config found for bot with user ID" and a bunch of numbers. If it doesn't compile, try to fix the errors, or reach out to me @eisritter on discord for help.

- In your IDE, open the file `BotConfig.py`. You should see a weird set of numbers and text, that looks intimidating at first, but don't worry, it's just a few numbers you can change without touching the underlying structure. 
- For safety, I would recommend just replacing the values under the config marked as Main Bot. These values point to IDs and values used for the deployment on the Caribdis Games server. Since in all likelihood you won't be deploying there, it's safe to just keep the structure there while replacing the values.
- Replace the first set of numbers right beneath the "# Main Bot" comment with your bot's discord ID. You can obtain that either from the error message you would encounter at this stage, or on Discord by right-clicking your bot's profile and copying its discord ID (similar to the server ID copy you've made in section 1.C)). If you do not do this, the bot will not work. The rest of the values need to be modified as follows:
\> `deployment_type` is (already) kinda obsolete. Just leave it at "BUILD", unless you're planning on accessing that for mod purposes with a private test bot.
\> `emojiIDs` references the IDs of the custom emotes you added to your bot on the Discord Dev Portal, where you can find the IDs on the right. You can technically replace the emotes with anything you want, but the default visuals are all included in the project's `visuals` folder if you want to stick with the default ones.
\> the `maintainer`, `moderator` and `admin` values mirror the role IDs (obtained by right-clicking roles) for mod-exclusive commands. If you don't plan on using them altogether, replace the numbers with -1 to avoid weird potential bugs from ID collisions. So far there is no hierarchy, all commands are accessible to maintainer and above, so you can also just designate one role and copy it to all values.
\> `cooldown` represents the length in seconds of the cooldown between two pulls. The default value of 72.000 represents 20h, but if you want to change that here's the place.
\> `botSpamChannel` gets the discord ID of a specific whitelisted channel, outside of which Judie will refuse to post an answer. If you don't want a specific whitelisted channel, replace this value with -1.
\> `guildID` is the same value as you have in your .env file. Yes it's a bit dim, but that's how it is.

Once you've adjusted all of these values, you should be good to go! Run the program, and if it outputs a "Hello there!", that means everything went well. Enjoy your home-deployed Judie bot!

# 2. Modder's guide:

Now that you have the bot running, you might think "hey, I have this cool idea for a character the dev missed", or want to make your own contribution to your community by extending what Judie can do.
There's a few things that are fairly easy to do, as there are templated things like characters and existing collections, other things that might require a bit more elbow grease.

## A) Adding a custom character to the gf games [non-collectible]
This is super easy, all you need to do is head to the file [Egf/Ogf]Characters.py, and follow the templates there, and adding the images to the relevant folder, which should be code/images/EternumGfGameImages & code/images/gfGameImages respectively.
> the images MUST be in webp format, and named [character.filename]_x, with x being a number in the range [1, n]. If you add multiple pictures, make sure they do not have gaps in the numbers, this may lead to errors later on.

\> make sure to append the character objects to the `characters` list, otherwise they won't be included in the gf game pool!
\> nsfw characters work in similar fashion
\> I cut all egf pictures to have an aspect ratio of exactly 225x350. If you don't want it to look weird I recommend doing the same, there's some great free tools on https://www.ezgif.com/resize/ for that. You can also convert pictures to native webp there.
- example - you want to add your homie Tony to the egf game:
```
# in EgfCharacters.py:
myhomietony = EgfCharacterCard(
    name="My Homie Tony",                               # The name you want to see when you draw Tony
    picNumber=3,                                        # assuming you're adding 3 pictures of Tony  
    quotes=["If it hadn't been for Cotton Eye Joe"],    # any memorable lines or insiders from Tony
    filename="my_homie_tony"                            # the unique filename prefix for Tony's pictures
) 
self.characters.append(myhomietony)

# in images/EternumGfGameImages
my_homie_tony_1.webp
my_homie_tony_2.webp
my_homie_tony_4.webp <- X THIS WOULD CAUSE ISSUES! Should be my_homie_tony_3.webp
```

## B) Adding a character to an existing collection
This is a bit trickier, you will need some knowledge of SQL for this.
\> In your character on [Egf/Ogf]Characters.py, add in a collection (simply expand the object definition with collection=Collections.[HAREM/whatever collection you choose]; these values are visible at [Egf/Ogf]Utilis.py
\> in [Egf/Ogf]Utils.py, add your character's filename to the end of the list in the function `Collections.members(self)`
\> in main.py, go to the function createAndUpdateDatabase, and scroll ALL the way down. At any point ABOVE the set of instructions `db.commit(), cursor.close(), db.close()` you can add a try/catch sequence as shown right above, and replace the contents of cursor.execute with
> `"ALTER TABLE [collection.table] ADD COLUMN [character.filename] INTEGER DEFAULT 0"` - the all caps is relevant to syntax, and replace anything in square brackets [] with the corresponding values.
- Example, you think Bundledore is in need of friends, so he should be a homie.
```
# in EgfCharacters.py, line 362:
Bundledore = CharacterCard(
    name="Professor Balbus Bundledore",
    picNumber=2,
    quotes=[...],
    filename="bundledore",          # <- remember this value for the SQL statement
    aliases="...",
    # YOUR CONTRIBUTION HERE:
    collection=Collections.THE_HOMIES
)

# in main.py, line 778:
try:
    cursor.execute("ALTER TABLE homies ADD COLUMN bundledore INTEGER DEFAULT 0")
    db.commit()             # <- saves the change to the database in case things go wrong afterwards.
except Exception as e:
    # These statements are there for help narrowing down what went wrong.
    print(f"[Bundledore to homies] {e}")
    traceback.print_exc()
```

## C) Adding a new collection:
You want to make it hard on yourself, eh?
The first place to go is the Utils file for the game you want to extend. Let's take the example of adding a Praetorians collection.
\> beneath the last added collection, add in the name you want for your collection without whitespace.
> PRAETORIANS = 5
\> update all the functions of the Collections class: 
- `__str__(self)` is the natural name including whitespace for the collection (`the Praetorians`);
- `member_desc(self)` is the name describing an individual member of the collection (`praetorian`);
- `color(self)` points to a hex color code to embed collectibles in a non-standard color. You can either reuse the values defined in HelperClass (file Utils.py), define a new color there, or just directly define the hex code in the function (`0x050a52`).
- `table(self)` the SQL name of the table you will be adding. It MUST be all lowercase without whitespace (praetorians)
- `blacklist(self)` represents any column in the table that doesn't describe ownership of a member. You will always need the user_id column, and a last_collectible column, and if you add extra data these will need to be in here too (["user_id", "last_praetorian"])
- `members(self)` is a list of the filenames for all members of your collection (["four", "nine", "six", "three"])
> in `main.py`, add in a new table definition like with the other games. You can name them whatever you want as long as it's not an existing table. I go with the naming scheme of [game]_[collection] if the name is a bit ambiguous, but eh. All columns except the last_collectible MUST be integers, (defaulting to 0, except for the user ID's)
```
# in main.py, line 778:
try:
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS praetorians(     # <- value of table()
        user_id INTEGER,            # <- MUST be part of the table, otherwise you can't track who owns what characters; part of the blacklist()
        four INTEGER DEFAULT 0,     # <- part of the members() list
        nine INTEGER DEFAULT 0,     # <- part of the members() list
        six INTEGER DEFAULT 0,      # <- part of the members() list
        three INTEGER DEFAULT 0,    # <- part of the members() list
        last_praetorian TEXT        # <- part of the blacklist()
    )
    """)
    db.commit()             # <- saves the change to the database in case things go wrong afterwards.
except Exception as e:
    # These statements are there for help narrowing down what went wrong.
    print(f"[New Praetorians Collection] {e}")
    traceback.print_exc()
```

Then refer back to the section 2.B) on how to add members to your collection

## D) Other Additions:
For any other desired mods, this will need some actual implementation beyong copying a template. Read the code to figure out how to extend things like effects, or if you want to add new features entirely.

Documentation for discord.py is available online at https://www.discordpy.readthedocs.io/en/stable/, Python isn't such a hard language to read and understand in the grand scheme of things, and if you feel like using LLMs I can't stop you.

[back to top](#judie-bot-deployment--modders-guide)
