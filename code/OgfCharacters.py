from OgfUtils import Collections, Effects, CharacterCard


class OgfCharacters:
    """
    The character manager for the OiaLt GF game.
    --------------------------------------------------------
    Members:
        - characters : list - a list of CharacterCard objects.
    """
    def __init__(self):
        self.characters = []
        self.Setup()

    def Setup(self):
        # CHARACTER CARDS
        # <editor-fold desc="#0: Aiko - HAREM / HOMIE PROTECTOR">
        Aiko = CharacterCard(
            name="Aiko",
            footer="Less talking and more fighting...",
            filename="aiko",
            collection=Collections.HAREM,
            effect=Effects.BOYS_SAVER
        )
        self.characters.append(Aiko)
        # </editor-fold>

        # <editor-fold desc="#1: Anastasia - STABBY MIKES">
        Anastasia = CharacterCard(
            name="Anastasia",
            footer="What a fine lady.",
            filename="anastasia",
            collection=Collections.STABBIES,
            effect=Effects.NONE
        )
        self.characters.append(Anastasia)
        # </editor-fold>

        # <editor-fold desc="#2: Asmodeus - HOMIES">
        Asmodeus = CharacterCard(
            name="Asmodeus",
            footer="feel safe already!",
            filename="asmodeus",
            collection=Collections.BOYS,
            effect=Effects.NONE
        )
        self.characters.append(Asmodeus)
        # </editor-fold>

        # <editor-fold desc="#3: Astaroth - STABBY MIKE KILLER">
        Astaroth = CharacterCard(
            name="Astaroth",
            footer="YIKES",
            filename="astaroth",
            collection=Collections.NONE,
            effect=Effects.STABBY_KILLER
        )
        self.characters.append(Astaroth)
        # </editor-fold>

        # <editor-fold desc="#4: Ava - POTENTIAL LI'S">
        Ava = CharacterCard(
            name="Ava",
            footer="Nice",
            filename="ava",
            collection=Collections.POTENTIALS,
            effect=Effects.NONE
        )
        self.characters.append(Ava)
        # </editor-fold>

        # <editor-fold desc="#5: Azazel - HOMIE KILLER">
        Azazel = CharacterCard(
            name="Azazel",
            footer="YIKES",
            filename="azazel",
            collection=Collections.NONE,
            effect=Effects.BOYS_KILLER
        )
        self.characters.append(Azazel)
        # </editor-fold>

        # <editor-fold desc="#6: Carla - HAREM">
        Carla = CharacterCard(
            name="Carla",
            footer="You're such a naughty boy... I'm going to have to punish you! Grounded for 2 weeks.",
            filename="carla",
            collection=Collections.HAREM,
            effect=Effects.NONE
        )
        self.characters.append(Carla)
        # </editor-fold>

        # <editor-fold desc="#7: Clarice">
        Clarice = CharacterCard(
            name="Clarice",
            footer="'But I said that under the seal of confession!'",
            filename="clarice",
            collection=Collections.NONE,
            effect=Effects.NONE
        )
        self.characters.append(Clarice)
        # </editor-fold>

        # <editor-fold desc="#8: David">
        David = CharacterCard(
            name="David",
            footer="WoRk hARd yOunG MAn",
            filename="david",
            collection=Collections.NONE,
            effect=Effects.NONE
        )
        self.characters.append(David)
        # </editor-fold>

        # <editor-fold desc="#9: Dildo Boi">
        DildoBoi = CharacterCard(
            name="Dildo Boi",
            footer="*Please don't use me as a dildo...*",
            filename="dildo_boi",
            collection=Collections.NONE,
            effect=Effects.NONE
        )
        self.characters.append(DildoBoi)
        # </editor-fold>

        # <editor-fold desc="#10: Dojo Owner">
        DojoOwner = CharacterCard(
            name="Dojo Owner",
            footer="Great company I guess...",
            filename="dojo_owner",
            collection=Collections.NONE,
            effect=Effects.NONE
        )
        self.characters.append(DojoOwner)
        # </editor-fold>

        # <editor-fold desc="#11: Fake Hiromi">
        FakeHiromi = CharacterCard(
            name="Fake Hiromi",
            footer="Watashi o hitori ni shite kudasai...",
            filename="fake_hiromi",
            collection=Collections.NONE,
            effect=Effects.NONE
        )
        self.characters.append(FakeHiromi)
        # </editor-fold>

        # <editor-fold desc="#12: Father Mitchell - STABBY MIKES">
        FatherMitchell = CharacterCard(
            name="Father Mitchell",
            footer="REPENT!",
            filename="priest",
            collection=Collections.STABBIES,
            effect=Effects.NONE
        )
        self.characters.append(FatherMitchell)
        # </editor-fold>

        # <editor-fold desc="#13: Fit Jack - HOMIES">
        FitJack = CharacterCard(
            name="Fit Jack",
            footer="feel safe already!",
            filename="fit_jack",
            collection=Collections.BOYS,
            effect=Effects.NONE
        )
        self.characters.append(FitJack)
        # </editor-fold>

        # <editor-fold desc="#14: Fit Jack's Groupie - POTENTIAL LI'S">
        Groupie = CharacterCard(
            name="Fit Jack's Groupie",
            footer="pure dedication",
            filename="fit_jack_groupie",
            collection=Collections.POTENTIALS,
            effect=Effects.NONE
        )
        self.characters.append(Groupie)
        # </editor-fold>

        # <editor-fold desc="#15: Former Asmodeus">
        FormerAsmo = CharacterCard(
            name="Former Asmodeus",
            footer="Idk man, seems a little crazy but it's your choice",
            filename="former_asmodeus",
            collection=Collections.NONE,
            effect=Effects.NONE
        )
        self.characters.append(FormerAsmo)
        # </editor-fold>

        # <editor-fold desc="#16: Funtime Clan Leader - HAREM SAVER">
        Funtime = CharacterCard(
            name="Funtime Clan Leader",
            footer="And the the Spaniard says: 'I didn't mean to interrupt, but that's not the melon!'",
            filename="funtime",
            collection=Collections.NONE,
            effect=Effects.HAREM_SAVER
        )
        self.characters.append(Funtime)
        # </editor-fold>

        # <editor-fold desc="#17: Hiromi - HOMIES">
        Hiromi = CharacterCard(
            name="Hiromi",
            footer="Ahh, I'm the man you're looking for. What do you need? Coke?",
            filename="hiromi",
            collection=Collections.BOYS,
            effect=Effects.NONE
        )
        self.characters.append(Hiromi)
        # </editor-fold>

        # <editor-fold desc="#18: Hitman Mike - STABBY MIKES">
        Hitman = CharacterCard(
            name="Hitman Mike",
            footer="Holy Shit!",
            filename="hitman",
            collection=Collections.STABBIES,
            effect=Effects.NONE
        )
        self.characters.append(Hitman)
        # </editor-fold>

        # <editor-fold desc="#19: Iris - HAREM">
        Iris = CharacterCard(
            name="Iris",
            footer="Your brother has a huge dick Judie! Did you know it?",
            filename="iris",
            collection=Collections.HAREM,
            effect=Effects.NONE
        )
        self.characters.append(Iris)
        # </editor-fold>

        # <editor-fold desc="#20: Jasmine - HAREM">
        Jasmine = CharacterCard(
            name="Jasmine",
            footer="Can't stop thinking about your fucking face since the day I threw the party",
            filename="jasmine",
            collection=Collections.HAREM,
            effect=Effects.NONE
        )
        self.characters.append(Jasmine)
        # </editor-fold>

        # <editor-fold desc="#21: Jason">
        Jason = CharacterCard(
            name="Jason",
            footer="Hey Tom, your cousin called me a dick!",
            filename="jason",
            collection=Collections.NONE,
            effect=Effects.NONE
        )
        self.characters.append(Jason)
        # </editor-fold>

        # <editor-fold desc="#22: Johnny">
        Johnny = CharacterCard(
            name="Johnny",
            footer="His dad is such a drama smh my head",
            filename="johnny",
            collection=Collections.NONE,
            effect=Effects.NONE
        )
        self.characters.append(Johnny)
        # </editor-fold>

        # <editor-fold desc="#23: Judie - HAREM"
        Judie = CharacterCard(
            name="Judie",
            footer="You really like that pillow, don't you?",
            filename="judie",
            collection=Collections.HAREM,
            effect=Effects.NONE
        )
        self.characters.append(Judie)
        # </editor-fold>

        # <editor-fold desc="#24: Kazuma">
        Kazuma = CharacterCard(
            name="Kazuma",
            footer="Free haircut!",
            filename="kazuma",
            collection=Collections.NONE,
            effect=Effects.NONE
        )
        self.characters.append(Kazuma)
        # </editor-fold>

        # <editor-fold desc="#25: Lauren - HAREM">
        Lauren = CharacterCard(
            name="Lauren",
            footer="Hey what's up dumbass?",
            filename="lauren",
            collection=Collections.HAREM,
            effect=Effects.NONE
        )
        self.characters.append(Lauren)
        # </editor-fold>

        # <editor-fold desc="#26: Lilith - POTENTIAL LI'S">
        Lilith = CharacterCard(
            name="Lilith",
            footer="Not too shabby...",
            filename="lilith",
            collection=Collections.POTENTIALS,
            effect=Effects.NONE
        )
        self.characters.append(Lilith)
        # </editor-fold>

        # <editor-fold desc="#27: Mayor">
        Mayor = CharacterCard(
            name="Mayor",
            footer="'I'm not an underage girl, get away from me!'",
            filename="mayor",
            collection=Collections.NONE,
            effect=Effects.NONE
        )
        self.characters.append(Mayor)
        # </editor-fold>

        # <editor-fold desc="#28: MC - THE HOMIES / STABBY MIKE SAVER">
        MC = CharacterCard(
            name="MC",
            footer="Holy shit I look so evil in this picture.",
            filename="mc",
            collection=Collections.BOYS,
            effect=Effects.STABBY_SAVER
        )
        self.characters.append(MC)
        # </editor-fold>

        # <editor-fold desc="#29: Messy Hair Lauren - HAREM">
        MHLauren = CharacterCard(
            name="Messy Hair Lauren",
            footer="lucky you, dude...",
            filename="messy_hair_lauren",
            collection=Collections.HAREM,
            effect=Effects.NONE
        )
        self.characters.append(MHLauren)
        # </editor-fold>

        # <editor-fold desc="#30: Mike the Exterminator - STABBY MIKES">
        MikeExterminator = CharacterCard(
            name="Mike the Exterminator",
            footer="feel safe already!",
            filename="exterminator",
            collection=Collections.STABBIES,
            effect=Effects.NONE
        )
        self.characters.append(MikeExterminator)
        # </editor-fold>

        # <editor-fold desc="#31: Moloch">
        Moloch = CharacterCard(
            name="Moloch",
            footer="Anyone heard of a Peter from Birmingham?",
            filename="moloch",
            collection=Collections.NONE,
            effect=Effects.NONE
        )
        self.characters.append(Moloch)
        # </editor-fold>

        # <editor-fold desc="#32: Nightmare Demon">
        NightmareDemon = CharacterCard(
            name="Nightmare Demon",
            footer="sorry buddy, can't help you on this one, you gotta run *faints*",
            filename="nightmare_demon",
            collection=Collections.NONE,
            effect=Effects.NONE
        )
        self.characters.append(NightmareDemon)
        # </editor-fold>

        # <editor-fold desc="#33: Oliver - HOMIES">
        Oliver = CharacterCard(
            name="Oliver",
            footer="I was just inviting her over to my Equestrian property for the weekend.",
            filename="oliver",
            collection=Collections.BOYS,
            effect=Effects.NONE
        )
        self.characters.append(Oliver)
        # </editor-fold>

        # <editor-fold desc="#34: Orochi - HAREM BUYER">
        Orochi = CharacterCard(
            name="Orochi Clan Leader",
            footer="YIKES",
            filename="orochi",
            collection=Collections.NONE,
            effect=Effects.HAREM_BUYER
        )
        self.characters.append(Orochi)
        # </editor-fold>

        # <editor-fold desc="#35: Priestess">
        Priestess = CharacterCard(
            name="Priestess",
            footer="Blue balls for you today I'm afraid dude",
            filename="priestess",
            collection=Collections.NONE,
            effect=Effects.NONE
        )
        self.characters.append(Priestess)
        # </editor-fold>

        # <editor-fold desc="#36: Principal">
        Principal = CharacterCard(
            name="Principal",
            footer="Oh you were talking history? Name every medieval Kingdom in England!",
            filename="principal",
            collection=Collections.NONE,
            effect=Effects.NONE
        )
        self.characters.append(Principal)
        # </editor-fold>

        # <editor-fold desc="#37: Rebecca - HAREM">
        Rebecca = CharacterCard(
            name="Rebecca",
            footer="Now I don't look like a respectable teacher, do I?",
            filename="rebecca",
            collection=Collections.HAREM,
            effect=Effects.NONE
        )
        self.characters.append(Rebecca)
        # </editor-fold>

        # <editor-fold desc="#38: Robbie Murray">
        Robbie = CharacterCard(
            name="Robbie Murray",
            footer="fucking priceless",
            filename="robbie",
            collection=Collections.NONE,
            effect=Effects.NONE
        )
        self.characters.append(Robbie)
        # </editor-fold>

        # <editor-fold desc="#39: Ruth">
        Ruth = CharacterCard(
            name="Ruth",
            footer="I'll take the elephant, thank you...",
            filename="ruth",
            collection=Collections.NONE,
            effect=Effects.NONE
        )
        self.characters.append(Ruth)
        # </editor-fold>

        # <editor-fold desc="#40: Samael">
        Samael = CharacterCard(
            name="Samael",
            footer="NOPE, hey Siri turn back time please!",
            filename="samael",
            collection=Collections.NONE,
            effect=Effects.NONE
        )
        self.characters.append(Samael)
        # </editor-fold>

        # <editor-fold desc="#41: Shop Girl - POTENTIAL LI'S">
        ShopGirl = CharacterCard(
            name="Shop Girl",
            footer="Yeah why not...",  # in code: if frost custom text :D
            filename="shop_girl",
            collection=Collections.POTENTIALS,
            effect=Effects.NONE
        )
        self.characters.append(ShopGirl)
        # </editor-fold>

        # <editor-fold desc="#42: Slaughter Clan Leader">
        Slaughter = CharacterCard(
            name="Slaughter Clan Leader",
            footer="Good luck with the baking business!",
            filename="slaughter",
            collection=Collections.NONE,
            effect=Effects.NONE
        )
        self.characters.append(Slaughter)
        # </editor-fold>

        # <editor-fold desc="#43: Spiderman">
        Spiderman = CharacterCard(
            name="Spiderman",
            footer="",  # Need to make it in code - "Hey is there a [username]?...
            filename="spiderman",
            collection=Collections.NONE,
            effect=Effects.NONE
        )
        self.characters.append(Spiderman)
        # </editor-fold>

        # <editor-fold desc="#44: Stabby Police - STABBY MIKES">
        StabbyPolice = CharacterCard(
            name="Stabby Police",
            footer="Let's give that mayor a scare, shall we?",
            filename="police",
            collection=Collections.STABBIES,
            effect=Effects.NONE
        )
        self.characters.append(StabbyPolice)
        # </editor-fold>

        # <editor-fold desc="#45: Stone Elephant - POTENTIAL LI'S">
        StoneElephant = CharacterCard(
            name="Stone Elephant",
            footer="Better than the alternative tbf",
            filename="stone_elephant",
            collection=Collections.POTENTIALS,
            effect=Effects.NONE
        )
        self.characters.append(StoneElephant)
        # </editor-fold>

        # <editor-fold desc="#46: Sun Lovers">
        SunLovers = CharacterCard(
            name="Sun Lovers",
            footer="It's a beautiful, sunny day...",
            filename="sun_lovers",
            collection=Collections.NONE,
            effect=Effects.NONE
        )
        self.characters.append(SunLovers)
        # </editor-fold>

        # <editor-fold desc="#47: Susanna">
        Susanna = CharacterCard(
            name="Susanna",
            footer="What a sweet person she is...",
            filename="susanna",
            collection=Collections.NONE,
            effect=Effects.NONE
        )
        self.characters.append(Susanna)
        # </editor-fold>

        # <editor-fold desc="#48: Swimsuit Ruth">
        SwimsuitRuth = CharacterCard(
            name="Swimsuit Ruth",
            footer="I'll take the elephant, thank you...",
            filename="swimsuit_ruth",
            collection=Collections.NONE,
            effect=Effects.NONE
        )
        self.characters.append(SwimsuitRuth)
        # </editor-fold>

        # <editor-fold desc="#49: Tom - HOMIES">
        Tom = CharacterCard(
            name="Tom",
            footer="feel safe already!",
            filename="tom",
            collection=Collections.BOYS,
            effect=Effects.NONE
        )
        self.characters.append(Tom)
        # </editor-fold>

        # <editor-fold desc="#50: Train Conductor - POTENTIAL LI'S">
        TrainConductor = CharacterCard(
            name="Train Conductor",
            footer="Not too shabby...",
            filename="train_conductor",
            collection=Collections.POTENTIALS,
            effect=Effects.NONE
        )
        self.characters.append(TrainConductor)
        # </editor-fold>

        # <editor-fold desc="#51: Ulric">
        Ulric = CharacterCard(
            name="Ulric",
            footer="You haven't even bought one of my wines dude!",
            filename="ulric",
            collection=Collections.NONE,
            effect=Effects.NONE
        )
        self.characters.append(Ulric)
        # </editor-fold>

        # <editor-fold desc="#52: Yakuza Mike - STABBY MIKES">
        Yakuza = CharacterCard(
            name="Yakuza Mike",
            footer="Hahaha the melon!",
            filename="yakuza",
            collection=Collections.STABBIES,
            effect=Effects.NONE
        )
        self.characters.append(Yakuza)
        # </editor-fold>

        # <editor-fold desc="#53: Zombie Magnus">
        Zombie = CharacterCard(
            name="Zombie Magnus",
            footer="YIKES",
            filename="zombie",
            collection=Collections.NONE,
            effect=Effects.NONE
        )
        self.characters.append(Zombie)
        # </editor-fold>

        # <editor-fold desc="#54: Monster Lilith - POTENTIAL LI MUTATOR">
        MonsterLilith = CharacterCard(
            name="Monster Lilith",
            footer="YIKES",
            filename="monster_lilith",
            collection=Collections.NONE,
            effect=Effects.POTENTIAL_MUTATOR
        )
        self.characters.append(MonsterLilith)
        # </editor-fold>

        # <editor-fold desc="#55: 93">
        NineThree = CharacterCard(
            name="93",
            footer="Back off, you look scary dude...",
            filename="nine_three",
            collection=Collections.NONE,
            effect=Effects.POTENTIAL_SAVER
        )
        self.characters.append(NineThree)
        # </editor-fold>

    async def searchNameWithFilename(self, filename: str) -> str:
        # since sorted alphabetically, maybe bin-search?
        for c in self.characters:
            if c.filename == filename:
                return c.name
        return None

    async def getCharacter(self, name: str) -> CharacterCard:
        for chara in self.characters:
            if name.lower() in chara.name.lower():
                return chara

        print(f"getCharacter<{name}>: No matches found!")
        return None

    async def getCharacterWithFilename(self, filename: str) -> CharacterCard:
        for chara in self.characters:
            if filename == chara.filename:
                return chara

        print(f"getCharacter<{filename}>: No matches found!")
        return None

    async def getCollectiblesOfType(self, collection: Collections) -> list[CharacterCard]:
        results = []
        for chara in self.characters:
            if chara.collection == collection:
                results.append(chara)

        return results

    async def getEffectorsOfType(self, effect: Effects) -> list[CharacterCard]:
        results = []
        for chara in self.characters:
            if chara.effects == effect:
                results.append(chara)

        return results
