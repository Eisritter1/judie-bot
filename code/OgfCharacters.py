from CharacterCard import OgfCharacterCard
from Utilities import OgfCollections, OgfEffects, HelperClass


class OgfCharacters:
    def __init__(self):
        self.characters = []
        self.Setup()

    def Setup(self):
        # CHARACTER CARDS
        # <editor-fold desc="#0: Aiko - HAREM / HOMIE PROTECTOR">
        Aiko = OgfCharacterCard(
            name="Aiko",
            footer="Less talking and more fighting...",
            filename="aiko",
            collection=OgfCollections.HAREM,
            effect=OgfEffects.BOYS_SAVER
        )
        self.characters.append(Aiko)
        # </editor-fold>

        # <editor-fold desc="#1: Anastasia - STABBY MIKES">
        Anastasia = OgfCharacterCard(
            name="Anastasia",
            footer="What a fine lady.",
            filename="anastasia",
            collection=OgfCollections.STABBIES,
            effect=OgfEffects.NONE
        )
        self.characters.append(Anastasia)
        # </editor-fold>

        # <editor-fold desc="#2: Asmodeus - HOMIES">
        Asmodeus = OgfCharacterCard(
            name="Asmodeus",
            footer="feel safe already!",
            filename="asmodeus",
            collection=OgfCollections.BOYS,
            effect=OgfEffects.NONE
        )
        self.characters.append(Asmodeus)
        # </editor-fold>

        # <editor-fold desc="#3: Astaroth - STABBY MIKE KILLER">
        Astaroth = OgfCharacterCard(
            name="Astaroth",
            footer="YIKES",
            filename="astaroth",
            collection=OgfCollections.NONE,
            effect=OgfEffects.STABBY_KILLER
        )
        self.characters.append(Astaroth)
        # </editor-fold>

        # <editor-fold desc="#4: Ava - POTENTIAL LI'S">
        Ava = OgfCharacterCard(
            name="Ava",
            footer="Nice",
            filename="ava",
            collection=OgfCollections.POTENTIALS,
            effect=OgfEffects.NONE
        )
        self.characters.append(Ava)
        # </editor-fold>

        # <editor-fold desc="#5: Azazel - HOMIE KILLER">
        Azazel = OgfCharacterCard(
            name="Azazel",
            footer="YIKES",
            filename="azazel",
            collection=OgfCollections.NONE,
            effect=OgfEffects.BOYS_KILLER
        )
        self.characters.append(Azazel)
        # </editor-fold>

        # <editor-fold desc="#6: Carla - HAREM">
        Carla = OgfCharacterCard(
            name="Carla",
            footer="You're such a naughty boy... I'm going to have to punish you! Grounded for 2 weeks.",
            filename="carla",
            collection=OgfCollections.HAREM,
            effect=OgfEffects.NONE
        )
        self.characters.append(Carla)
        # </editor-fold>

        # <editor-fold desc="#7: Clarice">
        Clarice = OgfCharacterCard(
            name="Clarice",
            footer="'But I said that under the seal of confession!'",
            filename="clarice",
            collection=OgfCollections.NONE,
            effect=OgfEffects.NONE
        )
        self.characters.append(Clarice)
        # </editor-fold>

        # <editor-fold desc="#8: David">
        David = OgfCharacterCard(
            name="David",
            footer="WoRk hARd yOunG MAn",
            filename="david",
            collection=OgfCollections.NONE,
            effect=OgfEffects.NONE
        )
        self.characters.append(David)
        # </editor-fold>

        # <editor-fold desc="#9: Dildo Boi">
        DildoBoi = OgfCharacterCard(
            name="Dildo Boi",
            footer="*Please don't use me as a dildo...*",
            filename="dildo_boi",
            collection=OgfCollections.NONE,
            effect=OgfEffects.NONE
        )
        self.characters.append(DildoBoi)
        # </editor-fold>

        # <editor-fold desc="#10: Dojo Owner">
        DojoOwner = OgfCharacterCard(
            name="Dojo Owner",
            footer="Great company I guess...",
            filename="dojo_owner",
            collection=OgfCollections.NONE,
            effect=OgfEffects.NONE
        )
        self.characters.append(DojoOwner)
        # </editor-fold>

        # <editor-fold desc="#11: Fake Hiromi">
        FakeHiromi = OgfCharacterCard(
            name="Fake Hiromi",
            footer="Watashi o hitori ni shite kudasai...",
            filename="fake_hiromi",
            collection=OgfCollections.NONE,
            effect=OgfEffects.NONE
        )
        self.characters.append(FakeHiromi)
        # </editor-fold>

        # <editor-fold desc="#12: Father Mitchell - STABBY MIKES">
        FatherMitchell = OgfCharacterCard(
            name="Father Mitchell",
            footer="REPENT!",
            filename="priest",
            collection=OgfCollections.STABBIES,
            effect=OgfEffects.NONE
        )
        self.characters.append(FatherMitchell)
        # </editor-fold>

        # <editor-fold desc="#13: Fit Jack - HOMIES">
        FitJack = OgfCharacterCard(
            name="Fit Jack",
            footer="feel safe already!",
            filename="fit_jack",
            collection=OgfCollections.BOYS,
            effect=OgfEffects.NONE
        )
        self.characters.append(FitJack)
        # </editor-fold>

        # <editor-fold desc="#14: Fit Jack's Groupie - POTENTIAL LI'S">
        Groupie = OgfCharacterCard(
            name="Fit Jack's Groupie",
            footer="pure dedication",
            filename="fit_jack_groupie",
            collection=OgfCollections.POTENTIALS,
            effect=OgfEffects.NONE
        )
        self.characters.append(Groupie)
        # </editor-fold>

        # <editor-fold desc="#15: Former Asmodeus">
        FormerAsmo = OgfCharacterCard(
            name="Former Asmodeus",
            footer="Idk man, seems a little crazy but it's your choice",
            filename="former_asmodeus",
            collection=OgfCollections.NONE,
            effect=OgfEffects.NONE
        )
        self.characters.append(FormerAsmo)
        # </editor-fold>

        # <editor-fold desc="#16: Funtime Clan Leader - HAREM SAVER">
        Funtime = OgfCharacterCard(
            name="Funtime Clan Leader",
            footer="And the the Spaniard says: 'I didn't mean to interrupt, but that's not the melon!'",
            filename="funtime",
            collection=OgfCollections.NONE,
            effect=OgfEffects.HAREM_SAVER
        )
        self.characters.append(Funtime)
        # </editor-fold>

        # <editor-fold desc="#17: Hiromi - HOMIES">
        Hiromi = OgfCharacterCard(
            name="Hiromi",
            footer="Ahh, I'm the man you're looking for. What do you need? Coke?",
            filename="hiromi",
            collection=OgfCollections.BOYS,
            effect=OgfEffects.NONE
        )
        self.characters.append(Hiromi)
        # </editor-fold>

        # <editor-fold desc="#18: Hitman Mike - STABBY MIKES">
        Hitman = OgfCharacterCard(
            name="Hitman Mike",
            footer="Holy Shit!",
            filename="hitman",
            collection=OgfCollections.STABBIES,
            effect=OgfEffects.NONE
        )
        self.characters.append(Hitman)
        # </editor-fold>

        # <editor-fold desc="#19: Iris - HAREM">
        Iris = OgfCharacterCard(
            name="Iris",
            footer="Your brother has a huge dick Judie! Did you know it?",
            filename="iris",
            collection=OgfCollections.HAREM,
            effect=OgfEffects.NONE
        )
        self.characters.append(Iris)
        # </editor-fold>

        # <editor-fold desc="#20: Jasmine - HAREM">
        Jasmine = OgfCharacterCard(
            name="Jasmine",
            footer="Can't stop thinking about your fucking face since the day I threw the party",
            filename="jasmine",
            collection=OgfCollections.HAREM,
            effect=OgfEffects.NONE
        )
        self.characters.append(Jasmine)
        # </editor-fold>

        # <editor-fold desc="#21: Jason">
        Jason = OgfCharacterCard(
            name="Jason",
            footer="Hey Tom, your cousin called me a dick!",
            filename="jason",
            collection=OgfCollections.NONE,
            effect=OgfEffects.NONE
        )
        self.characters.append(Jason)
        # </editor-fold>

        # <editor-fold desc="#22: Johnny">
        Johnny = OgfCharacterCard(
            name="Johnny",
            footer="His dad is such a drama smh my head",
            filename="johnny",
            collection=OgfCollections.NONE,
            effect=OgfEffects.NONE
        )
        self.characters.append(Johnny)
        # </editor-fold>

        # <editor-fold desc="#23: Judie - HAREM"
        Judie = OgfCharacterCard(
            name="Judie",
            footer="You really like that pillow, don't you?",
            filename="judie",
            collection=OgfCollections.HAREM,
            effect=OgfEffects.NONE
        )
        self.characters.append(Judie)
        # </editor-fold>

        # <editor-fold desc="#24: Kazuma">
        Kazuma = OgfCharacterCard(
            name="Kazuma",
            footer="Free haircut!",
            filename="kazuma",
            collection=OgfCollections.NONE,
            effect=OgfEffects.NONE
        )
        self.characters.append(Kazuma)
        # </editor-fold>

        # <editor-fold desc="#25: Lauren - HAREM">
        Lauren = OgfCharacterCard(
            name="Lauren",
            footer="Hey what's up dumbass?",
            filename="lauren",
            collection=OgfCollections.HAREM,
            effect=OgfEffects.NONE
        )
        self.characters.append(Lauren)
        # </editor-fold>

        # <editor-fold desc="#26: Lilith - POTENTIAL LI'S">
        Lilith = OgfCharacterCard(
            name="Lilith",
            footer="Not too shabby...",
            filename="lilith",
            collection=OgfCollections.POTENTIALS,
            effect=OgfEffects.NONE
        )
        self.characters.append(Lilith)
        # </editor-fold>

        # <editor-fold desc="#27: Mayor">
        Mayor = OgfCharacterCard(
            name="Mayor",
            footer="'I'm not an underage girl, get away from me!'",
            filename="mayor",
            collection=OgfCollections.NONE,
            effect=OgfEffects.NONE
        )
        self.characters.append(Mayor)
        # </editor-fold>

        # <editor-fold desc="#28: MC - THE HOMIES / STABBY MIKE SAVER">
        MC = OgfCharacterCard(
            name="MC",
            footer="Holy shit I look so evil in this picture.",
            filename="mc",
            collection=OgfCollections.BOYS,
            effect=OgfEffects.STABBY_SAVER
        )
        self.characters.append(MC)
        # </editor-fold>

        # <editor-fold desc="#29: Messy Hair Lauren - HAREM">
        MHLauren = OgfCharacterCard(
            name="Messy Hair Lauren",
            footer="lucky you, dude...",
            filename="messy_hair_lauren",
            collection=OgfCollections.HAREM,
            effect=OgfEffects.NONE
        )
        self.characters.append(MHLauren)
        # </editor-fold>

        # <editor-fold desc="#30: Mike the Exterminator - STABBY MIKES">
        MikeExterminator = OgfCharacterCard(
            name="Mike the Exterminator",
            footer="feel safe already!",
            filename="exterminator",
            collection=OgfCollections.STABBIES,
            effect=OgfEffects.NONE
        )
        self.characters.append(MikeExterminator)
        # </editor-fold>

        # <editor-fold desc="#31: Moloch">
        Moloch = OgfCharacterCard(
            name="Moloch",
            footer="Anyone heard of a Peter from Birmingham?",
            filename="moloch",
            collection=OgfCollections.NONE,
            effect=OgfEffects.NONE
        )
        self.characters.append(Moloch)
        # </editor-fold>

        # <editor-fold desc="#32: Nightmare Demon">
        NightmareDemon = OgfCharacterCard(
            name="Nightmare Demon",
            footer="sorry buddy, can't help you on this one, you gotta run *faints*",
            filename="nightmare_demon",
            collection=OgfCollections.NONE,
            effect=OgfEffects.NONE
        )
        self.characters.append(NightmareDemon)
        # </editor-fold>

        # <editor-fold desc="#33: Oliver - HOMIES">
        Oliver = OgfCharacterCard(
            name="Oliver",
            footer="I was just inviting her over to my Equestrian property for the weekend.",
            filename="oliver",
            collection=OgfCollections.BOYS,
            effect=OgfEffects.NONE
        )
        self.characters.append(Oliver)
        # </editor-fold>

        # <editor-fold desc="#34: Orochi - HAREM BUYER">
        Orochi = OgfCharacterCard(
            name="Orochi Clan Leader",
            footer="YIKES",
            filename="orochi",
            collection=OgfCollections.NONE,
            effect=OgfEffects.HAREM_BUYER
        )
        self.characters.append(Orochi)
        # </editor-fold>

        # <editor-fold desc="#35: Priestess">
        Priestess = OgfCharacterCard(
            name="Priestess",
            footer="Blue balls for you today I'm afraid dude",
            filename="priestess",
            collection=OgfCollections.NONE,
            effect=OgfEffects.NONE
        )
        self.characters.append(Priestess)
        # </editor-fold>

        # <editor-fold desc="#36: Principal">
        Principal = OgfCharacterCard(
            name="Principal",
            footer="Oh you were talking history? Name every medieval Kingdom in England!",
            filename="principal",
            collection=OgfCollections.NONE,
            effect=OgfEffects.NONE
        )
        self.characters.append(Principal)
        # </editor-fold>

        # <editor-fold desc="#37: Rebecca - HAREM">
        Rebecca = OgfCharacterCard(
            name="Rebecca",
            footer="Now I don't look like a respectable teacher, do I?",
            filename="rebecca",
            collection=OgfCollections.HAREM,
            effect=OgfEffects.NONE
        )
        self.characters.append(Rebecca)
        # </editor-fold>

        # <editor-fold desc="#38: Robbie Murray">
        Robbie = OgfCharacterCard(
            name="Robbie Murray",
            footer="fucking priceless",
            filename="robbie",
            collection=OgfCollections.NONE,
            effect=OgfEffects.NONE
        )
        self.characters.append(Robbie)
        # </editor-fold>

        # <editor-fold desc="#39: Ruth">
        Ruth = OgfCharacterCard(
            name="Ruth",
            footer="I'll take the elephant, thank you...",
            filename="ruth",
            collection=OgfCollections.NONE,
            effect=OgfEffects.NONE
        )
        self.characters.append(Ruth)
        # </editor-fold>

        # <editor-fold desc="#40: Samael">
        Samael = OgfCharacterCard(
            name="Samael",
            footer="NOPE, hey Siri turn back time please!",
            filename="samael",
            collection=OgfCollections.NONE,
            effect=OgfEffects.NONE
        )
        self.characters.append(Samael)
        # </editor-fold>

        # <editor-fold desc="#41: Shop Girl - POTENTIAL LI'S">
        ShopGirl = OgfCharacterCard(
            name="Shop Girl",
            footer="Yeah why not...",  # in code: if frost custom text :D
            filename="shop_girl",
            collection=OgfCollections.POTENTIALS,
            effect=OgfEffects.NONE
        )
        self.characters.append(ShopGirl)
        # </editor-fold>

        # <editor-fold desc="#42: Slaughter Clan Leader">
        Slaughter = OgfCharacterCard(
            name="Slaughter Clan Leader",
            footer="Good luck with the baking business!",
            filename="slaughter",
            collection=OgfCollections.NONE,
            effect=OgfEffects.NONE
        )
        self.characters.append(Slaughter)
        # </editor-fold>

        # <editor-fold desc="#43: Spiderman">
        Spiderman = OgfCharacterCard(
            name="Spiderman",
            footer="",  # Need to make it in code - "Hey is there a [username]?...
            filename="spiderman",
            collection=OgfCollections.NONE,
            effect=OgfEffects.NONE
        )
        self.characters.append(Spiderman)
        # </editor-fold>

        # <editor-fold desc="#44: Stabby Police - STABBY MIKES">
        StabbyPolice = OgfCharacterCard(
            name="Stabby Police",
            footer="Let's give that mayor a scare, shall we?",
            filename="police",
            collection=OgfCollections.STABBIES,
            effect=OgfEffects.NONE
        )
        self.characters.append(StabbyPolice)
        # </editor-fold>

        # <editor-fold desc="#45: Stone Elephant - POTENTIAL LI'S">
        StoneElephant = OgfCharacterCard(
            name="Stone Elephant",
            footer="Better than the alternative tbf",
            filename="stone_elephant",
            collection=OgfCollections.POTENTIALS,
            effect=OgfEffects.NONE
        )
        self.characters.append(StoneElephant)
        # </editor-fold>

        # <editor-fold desc="#46: Sun Lovers">
        SunLovers = OgfCharacterCard(
            name="Sun Lovers",
            footer="It's a beautiful, sunny day...",
            filename="sun_lovers",
            collection=OgfCollections.NONE,
            effect=OgfEffects.NONE
        )
        self.characters.append(SunLovers)
        # </editor-fold>

        # <editor-fold desc="#47: Susanna">
        Susanna = OgfCharacterCard(
            name="Susanna",
            footer="What a sweet person she is...",
            filename="susanna",
            collection=OgfCollections.NONE,
            effect=OgfEffects.NONE
        )
        self.characters.append(Susanna)
        # </editor-fold>

        # <editor-fold desc="#48: Swimsuit Ruth">
        SwimsuitRuth = OgfCharacterCard(
            name="Swimsuit Ruth",
            footer="I'll take the elephant, thank you...",
            filename="swimsuit_ruth",
            collection=OgfCollections.NONE,
            effect=OgfEffects.NONE
        )
        self.characters.append(SwimsuitRuth)
        # </editor-fold>

        # <editor-fold desc="#49: Tom - HOMIES">
        Tom = OgfCharacterCard(
            name="Tom",
            footer="feel safe already!",
            filename="tom",
            collection=OgfCollections.BOYS,
            effect=OgfEffects.NONE
        )
        self.characters.append(Tom)
        # </editor-fold>

        # <editor-fold desc="#50: Train Conductor - POTENTIAL LI'S">
        TrainConductor = OgfCharacterCard(
            name="Train Conductor",
            footer="Not too shabby...",
            filename="train_conductor",
            collection=OgfCollections.POTENTIALS,
            effect=OgfEffects.NONE
        )
        self.characters.append(TrainConductor)
        # </editor-fold>

        # <editor-fold desc="#51: Ulric">
        Ulric = OgfCharacterCard(
            name="Ulric",
            footer="You haven't even bought one of my wines dude!",
            filename="ulric",
            collection=OgfCollections.NONE,
            effect=OgfEffects.NONE
        )
        self.characters.append(Ulric)
        # </editor-fold>

        # <editor-fold desc="#52: Yakuza Mike - STABBY MIKES">
        Yakuza = OgfCharacterCard(
            name="Yakuza Mike",
            footer="Hahaha the melon!",
            filename="yakuza",
            collection=OgfCollections.STABBIES,
            effect=OgfEffects.NONE
        )
        self.characters.append(Yakuza)
        # </editor-fold>

        # <editor-fold desc="#53: Zombie Magnus">
        Zombie = OgfCharacterCard(
            name="Zombie Magnus",
            footer="YIKES",
            filename="zombie",
            collection=OgfCollections.NONE,
            effect=OgfEffects.NONE
        )
        self.characters.append(Zombie)
        # </editor-fold>

        # <editor-fold desc="#54: Monster Lilith - POTENTIAL LI MUTATOR">
        MonsterLilith = OgfCharacterCard(
            name="Monster Lilith",
            footer="YIKES",
            filename="monster_lilith",
            collection=OgfCollections.NONE,
            effect=OgfEffects.POTENTIAL_MUTATOR
        )
        self.characters.append(MonsterLilith)
        # </editor-fold>

        # <editor-fold desc="#55: 93">
        NineThree = OgfCharacterCard(
            name="93",
            footer="Back off, you look scary dude...",
            filename="nine_three",
            collection=OgfCollections.NONE,
            effect=OgfEffects.POTENTIAL_SAVER
        )
        self.characters.append(NineThree)
        # </editor-fold>

    # Resolves a character card with a search through the name
    def Get(self, name: str):
        for character in self.characters:
            if character.name == name or character.filename == name:
                return character
        return None

    # Finds a character from its filename
    def GetName(self, filename: str):
        for character in self.characters:
            if character.filename == filename:
                return character.name
        return None

    # Returns the filename of a character given its full name
    def GetFilename(self, name: str):
        for character in self.characters:
            if character.name == name:
                return character.filename
        return None
