# EXTERNAL LIBRARIES
from enum import Enum
# INTERNAL IMPORTS
from Utilities import HelperClass


class Collections(Enum):
    """
    Enum listing all active Collections for the OiaLt GF Game.
    ------------------------------------------------------------
    Values:
        0 = NONE
        1 = HAREM
        2 = STABBIES
        3 = BOYS
        4 = POTENTIALS
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
        if self == Collections.NONE:
            return "No Collection"
        elif self == Collections.HAREM:
            return "Harem"
        elif self == Collections.STABBIES:
            return "Stabby Clan"
        elif self == Collections.BOYS:
            return "The Boys"
        elif self == Collections.POTENTIALS:
            return "Potential LI's"

    def member_desc(self) -> str:
        """Returns the descriptor for a generic member of the associated collection."""
        if self == Collections.NONE:
            return "character"
        elif self == Collections.HAREM:
            return "harem member"
        elif self == Collections.STABBIES:
            return "Stabby Mike"
        elif self == Collections.BOYS:
            return "homie"
        elif self == Collections.POTENTIALS:
            return "potential LI"

    def color(self) -> int:
        """Returns the embed colour associated with a collection."""
        # always return orange for now. Not implemented as of slash command 'patch' :D
        return HelperClass.orange
        if self == Collections.NONE:
            return HelperClass.orange
        elif self == Collections.HAREM:
            return HelperClass.pink
        elif self == Collections.STABBIES:
            return HelperClass.yellow
        elif self == Collections.BOYS:
            return HelperClass.green
        elif self == Collections.POTENTIALS:
            return HelperClass.purple

    def table(self) -> str:
        """Returns the collection's associated table name in the DB."""
        if self == Collections.NONE:
            return None
        elif self == Collections.HAREM:
            return "oialt_harem"
        elif self == Collections.STABBIES:
            return "stabby_mikes"
        elif self == Collections.BOYS:
            return "the_boys"
        elif self == Collections.POTENTIALS:
            return "li_potential"

    def blacklist(self) -> list[str] :
        """Returns a list of columns to ignore when consulting the collectibles."""
        if self == Collections.NONE:
            return None
        elif self == Collections.HAREM:
            return ["user_id", "last_li"]
        elif self == Collections.STABBIES:
            return ["user_id", "last_mike"]
        elif self == Collections.BOYS:
            return ["user_id", "last_boi"]
        elif self == Collections.POTENTIALS:
            return ["user_id", "last_potential_li"]

    def lastColName(self) -> str:
        """Returns the column name of the 'last collectible' query column in the DB."""
        if self == Collections.NONE:
            return None
        elif self == Collections.HAREM:
            return "last_li"
        elif self == Collections.STABBIES:
            return "last_mike"
        elif self == Collections.BOYS:
            return "last_boi"
        elif self == Collections.POTENTIALS:
            return "last_potential_li"

    def members(self) -> list[str]:
        """Returns a list of members (DB/filename format) for the provided collection."""
        if self == Collections.NONE:
            return None
        elif self == Collections.HAREM:
            return ["judie", "lauren", "messy_hair_lauren", "carla", "iris", "aiko", "jasmine", "rebecca"]
        elif self == Collections.STABBIES:
            return ["police", "hitman", "yakuza", "priest", "exterminator", "anastasia"]
        elif self == Collections.BOYS:
            return ["mc", "tom", "oliver", "fit_jack", "asmodeus", "hiromi"]
        elif self == Collections.POTENTIALS:
            return ["ava", "lilith", "fit_jack_groupie", "train_conductor", "shop_girl", "stone_elephant"]


class Effects(Enum):
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
        if self == Effects.NONE:
            return "Effects:"
        elif self == Effects.HAREM_SAVER:
            return "Harem Hero:"
        elif self == Effects.HAREM_BUYER:
            return "Harem Hijacker:"
        elif self == Effects.STABBY_SAVER:
            return "Main Character:"
        elif self == Effects.STABBY_KILLER:
            return "Mike Shooter:"
        elif self == Effects.BOYS_SAVER:
            return "Ambusher:"
        elif self == Effects.BOYS_KILLER:
            return "Masked Killer:"
        elif self == Effects.POTENTIAL_SAVER:
            return "Scapegoat:"
        elif self == Effects.POTENTIAL_MUTATOR:
            return "Human Trial:"

    def Describe(self) -> str:
        if self == Effects.NONE:
            return "No effects - probably for the best."
        elif self == Effects.HAREM_SAVER:
            return "Stops Orochi from buying out your harem once."
        elif self == Effects.HAREM_BUYER:
            return "Buys a henchwoman out of your harem, preferably any Lauren."
        elif self == Effects.STABBY_SAVER:
            return "Saves a Stabby Mike from Astaroth's wrath once."
        elif self == Effects.STABBY_KILLER:
            return "Kills a Stabby Mike, preferably Father Mitchell"
        elif self == Effects.BOYS_SAVER:
            return "Ambushes Azazel to save one of the boys once."
        elif self == Effects.BOYS_KILLER:
            return "Puts one of the boys to sleep forever, preferably the MC."
        elif self == Effects.POTENTIAL_SAVER:
            return "Distracts Monster Lilith away from a Potential LI once."
        elif self == Effects.POTENTIAL_MUTATOR:
            return "Mutates a potential LI to monster status, preferably Lilith."


class Results:
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


class CharacterCard:
    """
    Object representing a character from the OiaLt GF game.
    --------------------------------------------------------
    Values:
        - name - the character's name,
        - footer - a witty one-liner about the character,
        - filename - the unique name attributed to all files and fields relating to the character,
        - effects - an action triggered when the character is rolled (defaults to Effects.NONE),
        - collection - the collection the character is a part of (defaults to Collections.NONE).
    """
    def __init__(
            self, 
            name: str, 
            footer: str, 
            filename: str,
            collection: Collections = Collections.NONE, 
            effect: Effects = Effects.NONE
        ):
        self.name = name
        self.footer = footer
        self.filename = filename
        self.collection = collection
        self.effect = effect
