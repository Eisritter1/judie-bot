import discord
from discord.ext.commands import Context
from discord import Embed, File
from enum import Enum


async def check_channel(ctx: Context) -> bool:
    """
    Checks whether the channel the command was called from was the designated bot & spam channel.

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
    NONE = 0  # non-collectibles; embedded orange
    HAREM = 1  # kidnapped by Axel, saved by Orion; embedded pink
    SIDE_DISHES = 2  # kidnapped by TBD, saved by TBD; embedded purple
    THE_HOMIES = 3  # attacked by Thanatos, saved by Calypso; embedded yellow
    CREATURES = 4 # attacked by golem, saved by pyramid head

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
    NONE = 0        # non-collectibles;
    HAREM = 1       # bought by Orochi, saved by Funtime clan leader
    STABBIES = 2    # Killed by Astaroth, saved by MC
    BOYS = 3        # Killed by Azazel, saved by Aiko
    POTENTIALS = 4  # Killed by Monster Lilith, saved by 93

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
    NONE = 0  # no effects; embedded orange
    HAREM_SAVIOUR = 1  # saves harem from Thanatos
    SIDE_GIRL_SAVIOUR = 2  # saves sides from Axel
    HOMIE_SAVIOUR = 3  # saves homies from troll
    HAREM_KILLER = 4  # kills a harem member
    SIDE_GIRL_KIDNAPPER = 5  # kidnaps a side girl
    HOMIE_KILLER = 6  # kills a homie
    CREATURE_SAVIOUR = 7  # saves a creature
    CREATURE_STOMPER = 8  # kills a creature

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
    NONE = 0                # No Effects
    HAREM_SAVER = 1         # Prevents Orochi from purchasing an LI
    HAREM_BUYER = 2         # Purchases an LI, preferably Lauren or Messy Hair Lauren
    STABBY_SAVER = 3        # Stops Astaroth from killing a Mike
    STABBY_KILLER = 4       # Kills a stabby mike, preferably Father Mitchell
    BOYS_SAVER = 5          # Kills Azazel before he can take out one of the boys
    BOYS_KILLER = 6         # Kills one of the boys, preferably the MC
    POTENTIAL_SAVER = 7     # Stops Monster Lilith from corrupting a potential LI
    POTENTIAL_MUTATOR = 8   # Mutates a potential LI to monsterhood, preferably Lilith

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
    daliaParty = ""
    alexAngry = ""
    annieCry = ""
    annieYay = ""
    novaGun = ""
    pepeCry2 = ""

    def init(client):
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


    orange = 0xffa800  # default
    eternumBlue = 0x00ffcc  # eternum default
    pink = 0xb502b8  # eternum harem
    purple = 0x530554  # eternum side girls
    red = 0xff0000  # eternum denied villain
    black = 0x000000  # eternum successful villain
    yellow = 0xeeff00  # eternum homies
    green = 0x57F287  # eternum creatures
    blue = 0x0028ff  # protectors

    async def createEmbed(title, text, color=orange, footer=None):
        embed = discord.Embed(title=title, description=text, colour=color)
        if footer is not None:
            embed.set_footer(text=footer)
        return embed


class Results():
    def __init__(self, duplicate: bool = False, protected: bool = False, victim: str = None):
        self.duplicate = duplicate
        self.protected = protected
        self.victim = victim


# Isn't this the exact same struct as Results???
class OgfResults:
    def __init__(self, duplicate: bool = False, protected: bool = False, victim: str = None):
        self.duplicate = duplicate
        self.protected = protected
        self.victim = victim


# time = time in seconds until timer ends -> will be used for cooldowns!
class TimeObject:
    def __init__(self, time):
        self.hours = int(time // 3600)
        self.minutes = int((time % 3600) // 60)
        self.seconds = int((time % 3600) % 60)
