# EXTERNAL LIBRARIES
from enum import Enum
# INTERNAL IMPORTS
from Utilities import HelperClass


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
            return "Homies"
        elif self == Collections.CREATURES:
            return "Creatures"

    def member_desc(self) -> str:
        """Returns the descriptor for a generic member of the associated collection."""
        if self == Collections.NONE:
            return "character"
        elif self == Collections.HAREM:
            return "harem member"
        elif self == Collections.SIDE_DISHES:
            return "side girl"
        elif self == Collections.THE_HOMIES:
            return "homie"
        elif self == Collections.CREATURES:
            return "pet"

    def color(self) -> int:
        """Returns the embed colour associated with a collection."""
        if self == Collections.NONE:
            return HelperClass.eternumBlue
        elif self == Collections.HAREM:
            return HelperClass.pink
        elif self == Collections.SIDE_DISHES:
            return HelperClass.purple
        elif self == Collections.THE_HOMIES:
            return HelperClass.yellow
        elif self == Collections.CREATURES:
            return HelperClass.green

    def table(self) -> str:
        """Returns the collection's associated table name in the DB."""
        if self == Collections.NONE:
            return None
        elif self == Collections.HAREM:
            return "eternum_harem"
        elif self == Collections.SIDE_DISHES:
            return "side_girls"
        elif self == Collections.THE_HOMIES:
            return "homies"
        elif self == Collections.CREATURES:
            return "creatures"

    def blacklist(self) -> list[str]:
        """Returns a list of columns to ignore when consulting the collectibles."""
        if self == Collections.NONE:
            return None
        elif self == Collections.HAREM:
            return ["user_id", "last_girl"]
        elif self == Collections.SIDE_DISHES:
            return ["user_id", "last_affair"]
        elif self == Collections.THE_HOMIES:
            return ["user_id", "last_homie"]
        elif self == Collections.CREATURES:
            return ["user_id", "last_creature"]

    def lastColName(self) -> str:
        """Returns the column name of the 'last collectible' query column in the DB."""
        if self == Collections.NONE:
            return None
        elif self == Collections.HAREM:
            return "last_girl"
        elif self == Collections.SIDE_DISHES:
            return "last_affair"
        elif self == Collections.THE_HOMIES:
            return "last_homie"
        elif self == Collections.CREATURES:
            return "last_creature"

    def members(self) -> list[str]:
        """Returns a list of members (DB/filename format) for the provided collection."""
        if self == Collections.NONE:
            return []
        if self == Collections.HAREM:
            return ['alex', 'annie', 'calypso', 'dalia', 'luna', 'nancy', 'nova', 'penny']
        if self == Collections.SIDE_DISHES:
            return ['bluefoxmaiden', 'lorelei', 'eva', 'idriel', 'maat', 'redfoxmaiden', 'wenlin']
        if self == Collections.THE_HOMIES:
            return ['chang', 'chopchop', 'victor', 'jerry', 'micaela', 'noah', 'orion', 'raul']
        if self == Collections.CREATURES:
            return ['carolyn', 'igor', 'kermit', 'mauricec', 'mauriceg', 'mauricet', 'pancho']


class Effects(Enum):
    """
    Enum listing all active Actors for the Eternum GF Game.
    ------------------------------------------------------------
    Values:
        0 = NONE
        1 = HAREM_SAVIOUR       [Calypso]
        2 = HAREM_KILLER        [Thanatos]
        3 = SIDE_GIRL_SAVIOUR   [Orion]
        4 = SIDE_GIRL_KIDNAPPER [Axel]
        5 = HOMIE_SAVIOUR       [Dalia]
        6 = HOMIE_KILLER        [Troll]
        7 = CREATURE_SAVIOUR    [Pyramid Head]
        8 = CREATURE_STOMPER    [Golem]

        For future expansions, just add in order Saviour (odd numbers) then Villain (even numbers); Best for testing purposes.
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
    HAREM_KILLER = 2
    """
    [Thanatos]
    Removes a harem member - preference on Alex & Nova;
    Thwarted by Calypso;
    Displays red when blocked, black when successful.
    """
    SIDE_GIRL_SAVIOUR = 3
    """
    [Orion]
    Blocks Side Girl Kidnapper [Axel] once; 
    Protection refreshes with each pull;
    No alteration on color (collectible as well)
    """
    SIDE_GIRL_KIDNAPPER = 4
    """
    [Axel]
    Removes a side girl - no preference;
    Thwarted by Orion;
    Displays red when blocked, black when successful.
    """
    HOMIE_SAVIOUR = 5
    """
    [Dalia]
    Blocks Homie Killer [Troll] once; 
    Protection refreshes with each pull;
    No alteration on color (collectible as well)
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

    def action(self):
        """Returns an action that is executed once a character is pulled."""
        if self == Effects.NONE:
            return Effects.doNothing
        if self == Effects.HAREM_SAVIOUR:
            return Effects.protectHarem
        if self == Effects.SIDE_GIRL_SAVIOUR:
            return Effects.protectSides
        if self == Effects.HOMIE_SAVIOUR:
            return Effects.protectHomies
        if self == Effects.HAREM_KILLER:
            return Effects.killFromHarem
        if self == Effects.SIDE_GIRL_KIDNAPPER:
            return Effects.kidnapSideGirl
        if self == Effects.HOMIE_KILLER:
            return Effects.killHomie
        if self == Effects.CREATURE_SAVIOUR:
            return Effects.protectCreature
        if self == Effects.CREATURE_STOMPER:
            return Effects.stompCreature

    def doNothing(cursor, uid, _) -> tuple:
        return (True, "Nobody")

    # 'characters' param discarded for saviours for compatibility w. villains w/o needing to rewrite the class. 
    # Same reason for the non-relevant output tuple.
    # Bad practise I know but gimme a break. If it's acceptable for TLS it's fine for Judie.
    def protectHarem(cursor, uid, _) -> tuple:
        cursor.execute("UPDATE eternum SET calypso=1 WHERE user_id =?", [uid])
        return (True, "Nobody")

    def protectSides(cursor, uid, _) -> tuple:
        cursor.execute("UPDATE eternum SET orion=1 WHERE user_id =?", [uid])
        return (True, "Nobody")

    def protectHomies(cursor, uid, _) -> tuple:
        cursor.execute("UPDATE eternum SET dalia=1 WHERE user_id =?", [uid])
        return (True, "Nobody")

    def killFromHarem(cursor, uid, characters) -> tuple:
        protected = False
        victim = "Nobody"

        # search for Alex then Nova then the latest harem member
        cursor.execute("SELECT alex FROM eternum_harem WHERE user_id=?", [uid])
        alex = cursor.fetchone()

        if alex[0]:
            victim = "Alexandra Bardot"
        else:
            cursor.execute("SELECT nova FROM eternum_harem WHERE user_id=?", [uid])
            nova = cursor.fetchone()
            if nova[0]:
                victim = "Nova Johnson"
            else:
                cursor.execute("SELECT last_girl FROM eternum_harem WHERE user_id=?", [uid])
                lastgf = cursor.fetchone()
                if lastgf[0] in Collections.HAREM.members():
                    for i in range(len(characters)):
                        if characters[i].filename == lastgf[0]:
                            victim = characters[i].name
                # if no one in last_li, user is off the hook.
                else:
                    victim = "Nobody"

        # check Calypso in eternum for protection
        cursor.execute("SELECT calypso FROM eternum WHERE user_id=?", [uid])
        protection = cursor.fetchone()

        if protection[0] == 0 and victim != "Nobody":
            for i in range(len(characters)):
                if characters[i].name == victim:
                    column = characters[i].filename
                    cursor.execute("UPDATE eternum_harem SET %s=0 WHERE user_id=?" % column, [uid])

            cursor.execute("UPDATE eternum_harem SET last_girl='NONE' WHERE user_id=?", [uid])
        # if calypso was there, protection expired.
        else:
            if victim != "Nobody":
                cursor.execute("UPDATE eternum SET calypso=0 WHERE user_id=?", [uid])
                protected = True

        return (protected, victim)

    def kidnapSideGirl(cursor, uid, characters) -> tuple:
        protected = False
        victim = "Nobody"

        # select the last side girl collected
        cursor.execute("SELECT last_affair FROM side_girls WHERE user_id=?", [uid])
        lastgf = cursor.fetchone()
        if lastgf[0] in Collections.SIDE_DISHES.members():
            for i in range(len(characters)):
                if characters[i].filename == lastgf[0]:
                    victim = characters[i].name
        # if field last_affair is empty, user is off the hook.
        else:
            victim = "Nobody"
            
        # check for Orion's protection
        cursor.execute("SELECT orion FROM eternum WHERE user_id=?", [uid])
        protection = cursor.fetchone()

        if protection[0] == 0 and victim != "Nobody":
            for i in range(len(characters)):
                if characters[i].name == victim:
                    column = characters[i].filename
                    cursor.execute("UPDATE side_girls SET %s=0 WHERE user_id=?" % column, [uid])

            cursor.execute("UPDATE side_girls SET last_affair='NONE' WHERE user_id=?", [uid])
        
        # remove future protection if Orion intervened
        elif victim != "Nobody":
            cursor.execute("UPDATE eternum SET orion=0 WHERE user_id=?", [uid])
            protected = True

        return (protected, victim)

    def killHomie(cursor, uid, characters) -> tuple:
        protected = False
        victim = "Nobody"
        
        # check for Jerry, then the last homie collected if Jerry not found.
        cursor.execute("SELECT jerry FROM homies WHERE user_id=?", [uid])
        jerry = cursor.fetchone()

        if jerry[0]:
            victim = "Jerry"
        else:
            cursor.execute("SELECT last_homie FROM homies WHERE user_id=?", [uid])
            lastgf = cursor.fetchone()
            if lastgf[0] in ['chang', 'orion', 'chopchop', 'victor', 'micaela', 'noah', 'raul']:
                for i in range(len(characters)):
                    if characters[i].filename == lastgf[0]:
                        victim = characters[i].name
            # if last_homie is empty, user is off the hook.
            else:
                victim = "Nobody"

        # check for Dalia's protection
        cursor.execute("SELECT dalia FROM eternum WHERE user_id=?", [uid])
        protection = cursor.fetchone()

        if protection[0] == 0 and victim != "Nobody":
            for i in range(len(characters)):
                if characters[i].name == victim:
                    column = characters[i].filename
                    cursor.execute("UPDATE homies SET %s=0 WHERE user_id=?" % column, [uid])

                cursor.execute("UPDATE homies SET last_homie='NONE' WHERE user_id=?", [uid])

        # remove future protection if Dalia intervened.
        else:
            if victim != "Nobody":
                cursor.execute("UPDATE eternum SET dalia=0 WHERE user_id=?", [uid])
                protected = True

        return (protected, victim)

    def protectCreature(cursor, uid, _) -> tuple:
        cursor.execute("UPDATE eternum SET pyramid_head=1 WHERE user_id =?", [uid])
        return (True, "Nobody")

    def stompCreature(cursor, uid, characters) -> tuple:
        protected = False
        victim = "Nobody"

        # check for kermit, then last collected pet if not found.
        cursor.execute("SELECT kermit FROM creatures WHERE user_id=?", [uid])
        kermit = cursor.fetchone()

        if kermit[0]:
            victim = "Kermit"
        else:
            cursor.execute("SELECT last_creature FROM creatures WHERE user_id=?", [uid])
            lastgf = cursor.fetchone()
            if lastgf[0] in Collections.CREATURES.members():
                for i in range(len(characters)):
                    if characters[i].filename == lastgf[0]:
                        victim = characters[i].name
            # if last_creature is empty, user is off the hook.
            else:
                victim = "Nobody"

        # check for Pyri's protection.
        cursor.execute("SELECT pyramid_head FROM eternum WHERE user_id=?", [uid])
        protection = cursor.fetchone()

        if protection[0] == 0 and victim != "Nobody":
            for i in range(len(characters)):
                if characters[i].name == victim:
                    column = characters[i].filename
                    cursor.execute("UPDATE creatures SET %s=0 WHERE user_id=?" % column, [uid])

                cursor.execute("UPDATE creatures SET last_creature='NONE' WHERE user_id=?", [uid])

        # remove future protection if Pyri intervened.
        else:
            if victim != "Nobody":
                cursor.execute("UPDATE eternum SET pyramid_head=0 WHERE user_id=?", [uid])
                protected = True

        return (protected, victim)


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
    Object representing a character from the Eternum GF game.
    --------------------------------------------------------
    Values:
        - name - the character's name,
        - picNumber - the amount of pictures attributed to a character for random selection,
        - quotes - a list of quotes said by the character,
        - filename - the unique name attributed to all files and fields relating to the character,
        - effects - an action triggered when the character is rolled (defaults to Effects.NONE),
        - aliases - a list of aliases given to the character (defaults to 'no aliases'),
        - collection - the collection the character is a part of (defaults to Collections.NONE).
    """
    def __init__(
            self, 
            name : str, 
            picNumber: int, 
            quotes: list, 
            filename: str, 
            effects: Effects = Effects.NONE,
            aliases: str = "no aliases", 
            collection: Collections = Collections.NONE
        ):
        self.name = name
        self.picNumber = picNumber
        self.quotes = quotes
        self.filename = filename
        self.effects = effects
        self.aliases = aliases
        self.collection = collection


class Villain(CharacterCard):
    def __init__(
        self, 
        name: str, 
        picNumber: int, 
        quotes: list, 
        filename: str,
        killMessage: str,
        protectedMessage: str,
        emptyMessage: str,
        footer: str,
        effects: Effects = Effects.NONE, 
        aliases: str = "no aliases", 
        collection: Collections = Collections.NONE
    ):
        super().__init__(name, picNumber, quotes, filename, effects, aliases, collection)
        self.killMessage = killMessage
        self.protectedMessage = protectedMessage
        self.emptyMessage = emptyMessage
        self.footer = footer

    def kill_message(self, victim: str, author: str):
        return self.killMessage.format(
            victim=victim,
            author=author
        )

    def protected_message(self, victim: str, author: str):
        return self.protectedMessage.format(
            victim=victim,
            author=author
        )

    def empty_message(self, author: str):
        return self.emptyMessage.format(
            author=author
        )

    def get_footer(self, author: str):
        return self.footer.format(
            author=author
        )
