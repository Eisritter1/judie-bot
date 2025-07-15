import discord
from discord.ext.commands import Context
from discord import Embed, File
from enum import Enum


async def check_channel(ctx: Context) -> bool:
    """
    Checks whether the channel the command was called from was the designated bot & spam channel.
    -----------------------------------------------------------------------------------------------
    Parameters:
        - ctx: discord.ext.commands.Context
            the context provided with the message to check.

    Returns:
        bool: success of the comparison; 
            true = the channel is the bot & spam channel.
    """
    client = ctx.bot
    result = ctx.channel.id == client.config.botSpamChannel
    if not result:
        embed = discord.Embed(title="Wrong channel!",
                              description=f"Please take this to {client.get_channel(client.config.botSpamChannel).mention}",
                              color=HelperClass.orange)
        await ctx.send(embed=embed)
    return result


class Collections(Enum):
    """
    Enum listing all active Collections for the Eternum GF Game.
    ------------------------------------------------------------
    Values:
        0 = NONE
        1 = HAREM
        2 = SIDE_DISHES
        3 = THE_HOMIES
        4 = CREATURES
    """
    NONE = 0
    """
    Character is not part of any collection; 
    Embeds in "Eternum Blue"
    """
    HAREM = 1
    """
    Character is part of the Eternum Harem collection;
    Villain: Thanatos - Hero: Calypso;
    Embeds pink.
    """
    SIDE_DISHES = 2
    """
    Character is part of the Eternum Side Girls collection;
    Villain: Axel - Hero: Orion;
    Embeds purple.
    """
    THE_HOMIES = 3
    """
    Character is part of the Eternum Homies collection;
    Villain: Troll - Hero: Dalia;
    Embeds yellow.
    """
    CREATURES = 4
    """
    Character is part of the Eternum Pets collection;
    Villain: Golem - Hero: Pyramid Head;
    Embeds green.
    """

    def __str__(self):
        if self == Collections.NONE:
            return "No Collection"
        elif self == Collections.HAREM:
            return "Harem"
        elif self == Collections.SIDE_DISHES:
            return "Side Girls"
        elif self == Collections.THE_HOMIES:
            return "The Homies"
        elif self == Collections.CREATURES:
            return "Creatures"


class OgfCollections(Enum):
    """
    Enum listing all active Collections for the OiaLt GF Game.
    ------------------------------------------------------------
    Values:
        0 = NONE
        1 = HAREM
        2 = SIDE_DISHES
        3 = THE_HOMIES
        4 = CREATURES
    """
    NONE = 0
    """
    Character is not part of any collection;
    """
    HAREM = 1
    """
    Character is part of the OiaLt Harem collection;
    Villain: Orochi - Hero: Funtime Clan Leader;
    """
    STABBIES = 2
    """
    Character is part of the OiaLt Stabby Mike collection;
    Villain: Astaroth - Hero: MC;
    """
    BOYS = 3
    """
    Character is part of the OiaLt Homies collection;
    Villain: Azazel - Hero: Aiko;
    """
    POTENTIALS = 4
    """
    Character is part of the OiaLt Side Girls collection;
    Villain: Monster Lilith - Hero: 93;
    """

    def __str__(self):
        if self == OgfCollections.NONE:
            return "No Collection"
        elif self == OgfCollections.HAREM:
            return "Harem"
        elif self == OgfCollections.STABBIES:
            return "Stabby Clan"
        elif self == OgfCollections.BOYS:
            return "The Boys"
        elif self == OgfCollections.POTENTIALS:
            return "Potential LI's"


class Effects(Enum):
    """
    Enum listing all active Actors for the Eternum GF Game.
    ------------------------------------------------------------
    Values:
        0 = NONE
        1 = HAREM_SAVIOUR       [Calypso]
        2 = SIDE_GIRL_SAVIOUR   [Orion]
        3 = HOMIE_SAVIOUR       [Dalia]
        4 = HAREM_KILLER        [Thanatos]
        5 = SIDE_GIRL_KIDNAPPER [Axel]
        6 = HOMIE_KILLER        [Troll]
        7 = CREATURE_SAVIOUR    [Pyramid Head]
        8 = CREATURE_STOMPER    [Golem]
    """
    NONE = 0
    """
    Has no effect on collections;
    No alterations on color.
    """
    HAREM_SAVIOUR = 1
    """
    [Calypso]
    Blocks Harem Killer [Thanatos] once; 
    Protection refreshes with each pull;
    No alteration on color (collectible as well)
    """
    SIDE_GIRL_SAVIOUR = 2
    """
    [Orion]
    Blocks Side Girl Kidnapper [Axel] once; 
    Protection refreshes with each pull;
    No alteration on color (collectible as well)
    """
    HOMIE_SAVIOUR = 3
    """
    [Dalia]
    Blocks Homie Killer [Troll] once; 
    Protection refreshes with each pull;
    No alteration on color (collectible as well)
    """
    HAREM_KILLER = 4
    """
    [Thanatos]
    Removes a harem member - preference on Alex & Nova;
    Thwarted by Calypso;
    Displays red when blocked, black when successful.
    """
    SIDE_GIRL_KIDNAPPER = 5
    """
    [Axel]
    Removes a side girl - no preference;
    Thwarted by Orion;
    Displays red when blocked, black when successful.
    """
    HOMIE_KILLER = 6
    """
    [Troll]
    Removes a homie - preference on Jerry;
    Thwarted by Dalia;
    Displays red when blocked, black when successful.
    """
    CREATURE_SAVIOUR = 7
    """
    [Pyramid Head]
    Blocks Creature Stomper [Golem] once; 
    Protection refreshes with each pull;
    Displays midnight blue.
    """
    CREATURE_STOMPER = 8
    """
    [Golem]
    Removes a pet - preference on Lil' Kermie;
    Thwarted by Pyramid Head;
    Displays red when blocked, black when successful.
    """

    def __str__(self):
        if self == Effects.NONE:
            return "No Effect"
        elif self == Effects.HAREM_SAVIOUR:
            return "Harem heroine: Saves from Thanatos once."
        elif self == Effects.SIDE_GIRL_SAVIOUR:
            return "Side Girl hero: saves from Axel once."
        elif self == Effects.HOMIE_SAVIOUR:
            return "Homie heroine: saves from the troll once."
        elif self == Effects.HAREM_KILLER:
            return "Harem killer: kills a harem member, preferably Alex or Nova."
        elif self == Effects.SIDE_GIRL_KIDNAPPER:
            return "Side Girl kidnapper: kidnaps a side girl, with no preference."
        elif self == Effects.HOMIE_KILLER:
            return "Homie killer: kills a homie, preferably Jerry."
        elif self == Effects.CREATURE_SAVIOUR:
            return "Creature Defender: saves from the Golem once."
        elif self == Effects.CREATURE_STOMPER:
            return "Creature Stomper: stomps a creature to death, preferrably Kermit."

class OgfEffects(Enum):
    """
    Enum listing all active Actors for the OiaLt GF Game.
    ------------------------------------------------------------
    Values:
        0 = NONE
        1 = HAREM_SAVER         [Funtime Clan Leader]
        2 = HAREM_BUYER         [Orochi Clan Leader]
        3 = STABBY_SAVER        [MC]
        4 = STABBY_KILLER       [Astaroth]
        5 = BOYS_SAVER          [Aiko]
        6 = BOYS_KILLER         [Azazel]
        7 = POTENTIAL_SAVER     [93]
        8 = POTENTIAL_MUTATOR   [Monster Lilith]
    """
    NONE = 0
    """
    Has no effect on collections;
    No alterations on color.
    """
    HAREM_SAVER = 1
    """
    [Funtime Clan Leader]
    Blocks Harem Buyer [Orochi Clan Leader] once; 
    Protection refreshes with each pull;
    Displays midnight blue.
    """
    HAREM_BUYER = 2
    """
    [Orochi Clan Leader]
    Removes a harem member - preference on Lauren & Messy Hair Lauren;
    Thwarted by Funtime Clan Leader;
    Displays red when blocked, black when successful.
    """
    STABBY_SAVER = 3
    """
    [MC]
    Blocks Stabby Killer [Astaroth] once; 
    Protection refreshes with each pull;
    No alteration on display color (collectible as well)
    """
    STABBY_KILLER = 4
    """
    [Astaroth]
    Removes a Stabby Mike - preference on Father Mitchell;
    Thwarted by MC;
    Displays red when blocked, black when successful.
    """
    BOYS_SAVER = 5
    """
    [Aiko]
    Blocks Boys Killer [Azazel] once; 
    Protection refreshes with each pull;
    No alteration on display color (collectible as well)
    """
    BOYS_KILLER = 6
    """
    [Azazel]
    Removes a homie - preference on MC;
    Thwarted by Aiko;
    Displays red when blocked, black when successful.
    """
    POTENTIAL_SAVER = 7
    """
    [93]
    Blocks Potential Mutator [Monster Lilith] once; 
    Protection refreshes with each pull;
    Displays midnight blue.
    """
    POTENTIAL_MUTATOR = 8
    """
    [Monster Lilith]
    Removes a Potential LI - preference on Lilith;
    Thwarted by 93;
    Displays red when blocked, black when successful.
    """

    def __str__(self):
        if self == OgfEffects.NONE:
            return "Effects:"
        elif self == OgfEffects.HAREM_SAVER:
            return "Harem Hero:"
        elif self == OgfEffects.HAREM_BUYER:
            return "Harem Hijacker:"
        elif self == OgfEffects.STABBY_SAVER:
            return "Main Character:"
        elif self == OgfEffects.STABBY_KILLER:
            return "Mike Shooter:"
        elif self == OgfEffects.BOYS_SAVER:
            return "Ambusher:"
        elif self == OgfEffects.BOYS_KILLER:
            return "Masked Killer:"
        elif self == OgfEffects.POTENTIAL_SAVER:
            return "Scapegoat:"
        elif self == OgfEffects.POTENTIAL_MUTATOR:
            return "Human Trial:"

    def Describe(self) -> str:
        if self == OgfEffects.NONE:
            return "No effects - probably for the best."
        elif self == OgfEffects.HAREM_SAVER:
            return "Stops Orochi from buying out your harem once."
        elif self == OgfEffects.HAREM_BUYER:
            return "Buys a henchwoman out of your harem, preferably any Lauren."
        elif self == OgfEffects.STABBY_SAVER:
            return "Saves a Stabby Mike from Astaroth's wrath once."
        elif self == OgfEffects.STABBY_KILLER:
            return "Kills a Stabby Mike, preferably Father Mitchell"
        elif self == OgfEffects.BOYS_SAVER:
            return "Ambushes Azazel to save one of the boys once."
        elif self == OgfEffects.BOYS_KILLER:
            return "Puts one of the boys to sleep forever, preferably the MC."
        elif self == OgfEffects.POTENTIAL_SAVER:
            return "Distracts Monster Lilith away from a Potential LI once."
        elif self == OgfEffects.POTENTIAL_MUTATOR:
            return "Mutates a potential LI to monster status, preferably Lilith."


class HelperClass:
    """
    Self-explanatory name - contains helpful values and functions.
    ----------------------------------------------------------------
    Members:
        Attributes:
            Emotes : str
            - daliaParty
            - alexAngry
            - annieCry
            - annieYay
            - novaGun
            - pepeCry2

            Colors : int [hex codes]
            - orange = ffa800
            - eternumBlue = 00ffcc
            - pink = b502b8
            - purple = 530554
            - red = ff0000
            - black = 000000
            - yellow = eeff00
            - green = 57f287
            - blue = 0028ff
        Methods:
            - init(discord.Bot) - initializes values according to config data.
            - createEmbed(title : str, text : str, color : int = orange, footer : str = None) - creates an embed object ready to be sent.
    """
    daliaParty = ""
    alexAngry = ""
    annieCry = ""
    annieYay = ""
    novaGun = ""
    pepeCry2 = ""

    def init(client):
        """
        Initializes member parameters using config data 

        Required for proper functioning; Required to run, only after BotConfig.load() was called.
        """
        emoji_map = {
                "daliaParty": "ChibiDaliaParty",
                "alexAngry": "ChibiAlexAngry",
                "annieCry": "ChibiAnnieCry",
                "annieYay": "ChibiAnnieYay",
                "novaGun": "ChibiNovaGun",
                "pepeCry2": "PepeCry2"
        }

        for attr_name, emoji_key in emoji_map.items():
            emoji_id = client.config.emotes.get(emoji_key)
            if emoji_id:
                setattr(HelperClass, attr_name, f"<:{emoji_key}:{emoji_id}>")
            else:
                setattr(HelperClass, attr_name, f"<missing:{emoji_key}>")


    orange = 0xffa800
    """
    OiaLt default color
    """
    eternumBlue = 0x00ffcc
    """
    Eternum default color
    """
    pink = 0xb502b8 
    """
    Harem color
    """
    purple = 0x530554
    """
    Side Girl color
    """
    red = 0xff0000
    """
    Unsuccessful Villain color
    """
    black = 0x000000 
    """
    Successful Villain color
    """
    yellow = 0xeeff00
    """
    Homie color
    """
    green = 0x57F287
    """
    Eternum Pets color
    """
    blue = 0x0028ff
    """
    Protector color
    """

    async def createEmbed(title : str, text : str, color=orange, footer : str = None) -> discord.Embed:
        """
        Compiles parameter to an embed object ready to be sent.
        -------------------------------------------------------
        Parameters:
            - title : str
            - text : str
            - color : int (defaults to HelperClass.orange)
            - footer : str (defaults to None)
        -------------------------------------------------------
        Returns:
            discord.Embed object according to specifications.
        """
        embed = discord.Embed(title=title, description=text, colour=color)
        if footer is not None:
            embed.set_footer(text=footer)
        return embed


class Results():
    """
    Struct containing context following a character draw
    -----------------------------------------------------
    Parameters:
        - duplicate : bool - displays whether the character is already present in the collection (defaults to False).
        - protected : bool - displays whether a character was targeted unsuccessfully by a villain (defaults to False).
        - victim : str - displays what character the villain has targeted in this iteration (defaults to None).
    """
    def __init__(self, duplicate: bool = False, protected: bool = False, victim: str = None):
        self.duplicate = duplicate
        self.protected = protected
        self.victim = victim

class OgfResults:
    """
    Struct containing context following a character draw
    -----------------------------------------------------
    Parameters:
        - duplicate : bool - displays whether the character is already present in the collection (defaults to False).
        - protected : bool - displays whether a character was targeted unsuccessfully by a villain (defaults to False).
        - victim : str - displays what character the villain has targeted in this iteration (defaults to None).
    """
    def __init__(self, duplicate: bool = False, protected: bool = False, victim: str = None):
        self.duplicate = duplicate
        self.protected = protected
        self.victim = victim


# time = time in seconds until timer ends -> will be used for cooldowns!
class TimeObject:
    """
    Struct for more intuitive use of time. Takes a certain interval in seconds as input.
    -----------------------------------------------------
    Parameters:
        - hours : int
        - minutes : int
        - seconds : int
    """
    def __init__(self, time):
        self.hours = int(time // 3600)
        self.minutes = int((time % 3600) // 60)
        self.seconds = int((time % 3600) % 60)
