from CharacterCard import CharacterCard, Villain
from Utilities import Collections, Effects
from os import listdir
from os.path import isfile, join


class EgfCharacters:
    """
    The character manager for the Eternum GF game.
    --------------------------------------------------------
    Members:
        - characters : list - a list of CharacterCard objects.
    """
    def __init__(self):
        self.characters = []
        self.setup()
        # set picNumbers dynamically? -> scan thru images folder and count number of files that start with 'filename_' => end of setup()

    def setup(self):
        # CHARACTER CARDS
        # 0
        Abbott = CharacterCard(
            name="Professor Abbott",
            picNumber=1,
            quotes=["You look like a well-prepared team."],
            filename="abbott"
        )
        self.characters.append(Abbott)

        # 1
        Ableman = CharacterCard(
            name="Ian Ableman",
            picNumber=1,
            quotes=["\*Chuckles\* My advice? Don't hold back. If you get a chance to outshine your companion, take it. They'll like that."],
            filename="ableman"
        )
        self.characters.append(Ableman)

        # 2
        Abuela = CharacterCard(
            name="Mrs. Hernandez",
            picNumber=1,
            quotes=["It's halfway through the morning already, we have to start cooking!",
                    "I need my annual picture of my granddaughter.",
                    "You're such a sweetheart, mija.",
                    "Dios mio. You remind me so much of my husband..."],
            filename="abuela",
            effects=Effects.NONE,
            aliases="Luna's grandma",
            collection=Collections.NONE
        )
        self.characters.append(Abuela)

        # 3
        Agatha = CharacterCard(
            name="Agatha",
            picNumber=1,
            quotes=["Good evening, folks! Welcome aboard the Cascadian Express."],
            filename="agatha",
            aliases="Train Conductor"
        )
        self.characters.append(Agatha)

        # 4 [DISCORD CAMEOS ?]
        Akira = CharacterCard(
            name="Akira-San",
            picNumber=2,
            quotes=["Akira-san to you! You've gotta show some respect, boy.",
                    "I'm a robotics and hardware engineer. I created my own processing unit faster and better than any other in the world.",
                    "There are two things I know something about in this life. Computers and parties.",
                    "You can deceive yourselves all you want, my machines are perfect."],
            filename="akira"
        )
        self.characters.append(Akira)

        # 5 [HAREM]
        Alex = CharacterCard(
            name="Alexandra Bardot",
            picNumber=10,
            quotes=["What! You're supposed to say no.", "Go hang out with Idriel or something...",
                    "My prince... bullshit...", "We're a team now... I guess.",
                    "Don't tell me I've damaged the Bardot royal raisins!",
                    "Thank you for sticking around for my TED talk, though.",
                    "Oh, I know what you want, a... you wouldn't be able to handle it, pretty boy.",
                    "You just want to see my tits!", "You're a real pain, you know that?",
                    "Who knows what you could do to my precious apartment while I'm pretty much unconscious",
                    "Thank you for rescuing me from those villainous villains with your super strength, Orion!",
                    "Anyway, let's not get all sappy like a bunch of drama nerds.",
                    "You better start talking or I'll paint the snow red with your blood!",
                    "I have a theory that some of the best activities in life involve a bit of sweat."],
            filename="alex",
            aliases="Alex, Orion's lil' super-soaker, Neptune",
            collection=Collections.HAREM
        )
        self.characters.append(Alex)

        # 6
        Alfonso = CharacterCard(
            name="Alfonso",
            picNumber=1,
            quotes=[
                "If you've got any last-minute buys to make before leaving the Citadel, please, swing by Alfonso's!"],
            filename="alfonso"
        )
        self.characters.append(Alfonso)

        # 7
        Alicia = CharacterCard(
            name="Alicia Flink",
            picNumber=1,
            quotes=["*moans*"],
            filename="aliciaflink"
        )
        self.characters.append(Alicia)

        # 8
        Anderson = CharacterCard(
            name="Toby Anderson",
            picNumber=1,
            quotes=["\*Awkward laugh\* Ha-hah, y-yeah, right."],
            filename="anderson"
        )
        self.characters.append(Anderson)

        # 9
        Ambrose = CharacterCard(
            name="Madam Ambrose",
            picNumber=1,
            quotes=["Men from around the world come here for... invigoration"],
            filename="ambrose"
        )
        self.characters.append(Ambrose)

        # 10
        Anastasia = CharacterCard(
            name="Anastasia",
            picNumber=1,
            quotes=["You opened fire on the mistress. Such uncivilized behavior.",
                    "Firearms are barbaric."],
            filename="anastasia"
        )
        self.characters.append(Anastasia)

        # 11
        Anna = CharacterCard(
            name="Anna Kellegan",
            picNumber=1,
            quotes=[
                "If you're the reason she doesn't make it to the next Olympics, I'll personally hunt you down to kick your ass.",
                "Get out of my pool."],
            filename="anna",
            aliases="Alex's Swimming Coach"
        )
        self.characters.append(Anna)

        # 12
        Annabelle = CharacterCard(
            name="Princess Annabelle",
            picNumber=1,
            quotes=["How did you get into my castle?!", "You worthless wretches!"],
            filename="annabelle",
            aliases="Annabelle the Skinner"
        )
        self.characters.append(Annabelle)

        # 13 [HAREM]
        Annie = CharacterCard(
            name="Annie Winters",
            picNumber=17,
            quotes=["THIS IS THE BEST DAY OF MY LIFE!",
                    "Not a worry in mah noggin' homie. I just be... chillaxin' all day!",
                    "Umm... like a d-date... date? With me?",
                    "Too excited? Me? I'm like... super chill! Chillin' like a villain on penicillin, bro!",
                    "They can't hurt you if you can't see them...",
                    "Private Annie Winters reports!",
                    "T-Thank you, but... um, c-can you get dressed, please?",
                    "Well... and I'll also be wearing heels so I don't look like a hobbit."],
            filename="annie",
            aliases="Pluto",
            collection=Collections.HAREM
        )
        self.characters.append(Annie)

        # 14
        Anne = CharacterCard(
            name="Annie Flink",
            picNumber=1,
            quotes=["I want Mr. Nebula."],
            filename="annieflink",
            aliases="Anne"
        )
        self.characters.append(Anne)

        # 15
        Apple = CharacterCard(
            name="Apple Salesman",
            picNumber=1,
            quotes=[
                "30% of the net profits are donated towards the preservation of\nthe ocean's species and their habitats."],
            filename="applemerchant",
            aliases="One eternal per apple guy"
        )
        self.characters.append(Apple)

        # 16
        Arannis = CharacterCard(
            name="General Arannis Thornvale",
            picNumber=1,
            quotes=["It is precisely such mercy that elevates us above your wretched kind.", 
                    "You will not grow stronger by sparring with toys.", 
                    "You speak of strength, and yet all I see is delusion and madness.",
                    "Strike me now before the eyes of the Ancients! Let the gods bear witness to your treason!",
                    "A throne won by blood and treachery is a throne cursed to ruin."],
            filename="arannis",
            aliases="General of the Royal Guard, The Morning Sword, Hammer of Iron"
        )
        self.characters.append(Arannis)

        # 17
        Aspen = CharacterCard(
            name="Aspen Simmons",
            picNumber=1,
            quotes=["\*sarcastic tone\* I'm devastated by your increeeedibly tragic story, but the answer is still no.",
                    "Yeah, I don't give a shit about what's going on between you two."],
            filename="aspen"
        )
        self.characters.append(Aspen)

        # 18
        Astor = CharacterCard(
            name="Ms. Astor",
            picNumber=1,
            quotes=["Cutie? Any rumours you've heard about lately?"],
            filename="astor"
        )
        self.characters.append(Astor)

        # 19
        Avery = CharacterCard(
            name="Avery",
            picNumber=1,
            quotes=["Let me go, goddammit! I don't wanna play anymore",
                    "I'm not into whatever this is!",
                    "I'm keeping my eyes closed, hun. I only have eyes for my wife anyways..."],
            filename="avery"
        )
        self.characters.append(Avery)

        # 20 [SIDE GIRL HARASSER]
        Axel = Villain(
            name="Axel Bardot",
            picNumber=3,
            quotes=["You messed with the wrong guy.",
                    "I know you're new around here but you have no idea how lucky you are right now.",
                    "All the girls in school would kill to spend an afternoon with me.",
                    "You're exactly my type. Quiet and compliant",
                    "I'm a Bardot. My family could buy out the police if they wanted.",
                    "I always get what I want in the end, baby.",
                    "You just signed your death warrant, motherfucker!"],
            filename="axel",
            killMessage="Oh no! Axel kidnapped {victim} from your side girl harem, {author}!",
            protectedMessage="Orion punched Axel the second he noticed him harassing {author}'s {victim}!",
            emptyMessage="Axel didn't find anyone to kidnap... Lucky you I guess, {author}",
            footer="You messed with the wrong guy, cocksucker ({author})!",
            effects=Effects.SIDE_GIRL_KIDNAPPER
        )
        self.characters.append(Axel)

        # 21
        Baek = CharacterCard(
            name="Sister Baek",
            picNumber=1,
            quotes=["The powers granted through my beliefs are immeasurable.",
                    "He says... \"I love you, broseph\"..."],
            filename="baek",
            aliases="Leader of the Church of Unitology"
        )
        self.characters.append(Baek)

        # 22
        Bakhar = CharacterCard(
            name="Father Bakhar",
            picNumber=1,
            quotes=["You don't belong here, outsiders.",
                    "We won't rest until those abominations have been eradicated.",
                    "I will kill you and fulfill my duty to purge the world of the devil's spawn.",
                    "I refuse to be ridiculed by these infernal creatures..."],
            filename="bakhar",
            aliases="Hunter"
        )
        self.characters.append(Bakhar)

        # 23
        Bartender = CharacterCard(
            name="Saloon Bartender",
            picNumber=1,
            quotes=["One whiskey, gotcha, comin' right up, partner!"],
            filename="bartender"
        )
        self.characters.append(Bartender)

        # 24
        Bellini = CharacterCard(
            name="Giuseppe Bellini",
            picNumber=1,
            quotes=["As much as I'm savoring this, I'm here to talk business.",
                    "Un pasto squisito, amico mio. Truly.",
                    "Can I offer you some wine, my friend?",
                    "*Il rispetto non si chiede... si guadagna."],
            filename="bellini"
        )
        self.characters.append(Bellini)

        # 25
        Benja = CharacterCard(
            name="Benjamin Dawson",
            picNumber=2,
            quotes=["You should show some respect when you're talking to Mr. Bardot, you fucking worm.",
                    "Want me to smash your face in, cocksucker?", "Man, I feel like a celebrity!"],
            filename="benjamin",
            aliases="Benja"
        )
        self.characters.append(Benja)

        # 26 [SIDE GIRL]
        BlueFoxMaiden = CharacterCard(
            name="Blue Fox Maiden",
            picNumber=1,
            quotes=["We hope you're enjoying your stay.",
                    "We are the gift. Our task is to satisfy all of your desires."],
            filename="bluefoxmaiden",
            collection=Collections.SIDE_DISHES
        )
        self.characters.append(BlueFoxMaiden)

        # 27
        Briena = CharacterCard(
            name="Lady Briena",
            picNumber=1,
            quotes=["Nature thrives on release, not restraint."],
            filename="briena",
            aliases="The Druid"
        )
        self.characters.append(Briena)

        # 28
        Brock = CharacterCard(
            name="Brock Domen",
            picNumber=2,
            quotes=["I call this... the Crested Crane pose.",
                    "Maybe you can convince them to give you a consolation prize, as the biggest loser?",
                    "I'll be honest, I never doubted that I'd win this competition.",
                    "Can you believe she didn't even know the rules? What a bimbo!",
                    "I have the reflexes of a feral cat",
                    "Come on, try to hit me, big man. Right here."],
            filename="brock"
        )
        self.characters.append(Brock)

        # 29
        Bundledore = CharacterCard(
            name="Professor Balbus Bundledore",
            picNumber=2,
            quotes=["WELCOME, NEW PUPILS...",
                    "THAT FUCKING BITCH STOLE MY IDEA 40 YEARS AGO AND MADE IT HER OWN!"],
            filename="bundledore",
            aliases="Headmaster of Warthogs School of Witchcraft and Wizardry."
        )
        self.characters.append(Bundledore)

        # 30
        Burpee = CharacterCard(
            name="Burpee",
            picNumber=1,
            quotes=["Of course she can speak, nitwit.",
                    "Yeah, forgot you're a weirdo.",
                    "Had to be fucking Tis.",
                    "Oh, forgive me for not being a human sociologist, Duke."],
            filename="burpee"
        )
        self.characters.append(Burpee)

        # 31 [HAREM; HAREM SAVER]
        Calypso = CharacterCard(
            name="Calypso",
            picNumber=12,
            quotes=["The more forbidden it is, the more thrilling it becomes... would you not agree?",
                    "Holy Mother of Turska!",
                    "I can do many things.",
                    "Glem ni sa' eradin.",
                    "Holy Mother of Aen Seidhe, can you not see that the Princess is talking here, you filthy peasant?!!",
                    "I usually do not like your peasant garb, but this time I was not entirely displeased by them.",
                    "You look... \"hot as fuck\" as well.",
                    "I AM CALYPSO, PRINCESS OF THE SY-TEL-QUESSIR. I WAS BORN TO RULE OVER ALL RACES!",
                    "Hmph.",
                    "They say I am a *weapon*. A *tool*. How dare they... I obey no one!",
                    "You did not just grab me and handle me as if I were some lowly servant.",
                    "What do you mistake me for, some kind of common harlot who gets naked without reciprocation?",
                    "You shall be granted a special place in my court when I reign over Hyril'ar once more.",
                    "B-By the grace of the Ancients, Orion... Did your time in the dungeons teach you nothing?",
                    "Please, remain silent. You are disturbing my inner peace.",
                    "I am fond of my horse as well, but that does not mean I intend to bed it.",
                    "G-Get that indecent look off your face!",
                    "The Princess of Hyril'Ar falling for a human. Can you believe it?"],
            filename="calypso",
            effects=Effects.HAREM_SAVIOUR,
            aliases="Daughter of Raewyn, Princess of the Sy-tel-quessir, Princess of the Hyril'ar Realm, Carrie, Gaia, Caly, Warden of the Eternal Soul",
            collection=Collections.HAREM
        )
        self.characters.append(Calypso)

        # 32
        Carolyn = CharacterCard(
            name="Carolyn",
            picNumber=3,
            quotes=["*meows*", "\*Purrs\*"],
            filename="carolyn",
            collection=Collections.CREATURES
        )
        self.characters.append(Carolyn)

        # 33
        Cassian = CharacterCard(
            name="Cassian",
            picNumber=1,
            quotes=["It's not every day you get to meet the 'Best tits on Instagram'."],
            filename="cassian",
            aliases="Mr. Handsy Man"
        )
        self.characters.append(Cassian)

        # 34
        Chamberlain = CharacterCard(
            name="Court Chamberlain",
            picNumber=1,
            quotes=[
                "It shall be done as your command.",
                "For starters, do not speak unless you are given permission, human.",
                "Make love to the canvas and let it feed upon your passion!"
            ],
            filename="chamberlain"
        )
        self.characters.append(Chamberlain)

        # 35 [HOMIE]
        Chang = CharacterCard(
            name="Chang Wong",
            picNumber=8,
            quotes=["Well I wouldn't say \"obsessed\", but...",
                    "Say no more. I'M YOUR MAN!",
                    "Between you and me, mate, I think ya boy is about to GET IT!",
                    "Chang'd!",
                    "Bro, if you believe you're a player, you'll become a player.",
                    "If all else fails, I'll always be someone you can depend on, my friend.",
                    "Nothing can cure the soul but the senses,\njust as nothing can cure the senses but the soul",
                    "Apparently, the dad is on a business trip. You know what that means...",
                    "Nobody will be safe from Chang the Casanova!",
                    "Ok, ok, not so loud. Keep it cool... I've got a reputation to uphold.",
                    "My future family of 13 is in your hands!",
                    "I'd recognize those broad, masculine, thick, solid, tight shoulders from a mile away!",
                    "\*Sobbing\* My god, you're so fucking beautiful, bro.",
                    "Agh... Okay I'll be Leia",
                    "It was a night that would make poets weep and bards retire.",
                    "If you ever break the heart of that angelic soul, I'm gonna have to kill you."],
            filename="chang",
            aliases="Roberto Canchez, Chang the Ladies' man, Chang the Socialite, Chang the Heist Meister, Chang the Velvet Blade",
            collection=Collections.THE_HOMIES
        )
        self.characters.append(Chang)

        # 36
        Charlotte = CharacterCard(
            name="Charlotte",
            picNumber=4,
            quotes=["I don't have saggy tits!!! Stop spreading that rumor!",
                    "Um... I have a boyfriend.",
                    "I wanted to see Penelope. I'll be studying here next year, and she's *literally* me, just... older.",
                    "W-why doesn't gravity affect her? What cruel fate is this...?"],
            filename="charlotte",
            aliases="Miss Saggy Tits"
        )
        self.characters.append(Charlotte)

        # 37 [HOMIE]
        ChopChop = CharacterCard(
            name="Chop-Chop",
            picNumber=5,
            quotes=["Junk?, Oh, why you try to hurt my achey-breaky heart?",
                    "Chop-Chop only have best materials! Best products!",
                    "Where I from, popular saying goes, \"If you can't reach your dreams, use more lube\".",
                    "What *DON'T* I  sell! Me have everything!",
                    "THANK YOU FRIEND! COME BACK TO CHOP CHOP'S ANOTHER DAY!",
                    "No wet-dream here, only best prices! Only best quality!",
                    "What can me say, fate lead best client Orion to most esteemed seller in Eternum!"],
            filename="chopchop",
            aliases="Gypsy Goldtooth, Bonsai Shearer, Quantum Quasar Starlord",
            collection=Collections.THE_HOMIES
        )
        self.characters.append(ChopChop)

        # 38
        Claudius = CharacterCard(
            name="Emperor Claudius III",
            picNumber=1,
            quotes=["Whenever I make an entrance, you must bow before me.",
                    "A woman? Emperor?! Hahaha! Nonsense. You shall become my concubine.",
                    "With this woman under my control, I'll finally be able to conquer the entire server. I'll become a God!",
                    "How dare he disobey an order of the Emperor!",
                    "Why you insolent little... (famous last words)"],
            filename="claudius",
            aliases="Claudius the Great, Claudius the Magnificent, Claudius the Godsend (all self-proclaimed)"
        )
        self.characters.append(Claudius)

        # 39
        Clonk = CharacterCard(
            name="Clonk",
            picNumber=2,
            quotes=["\*stare\*",
                    "W H O  K I L L E D  G I D E O N  C O O K ?"],
            filename="clonk"
        )
        self.characters.append(Clonk)

        # 40 [DISCORD CAMEOS ?]
        Con = CharacterCard(
            name="Con",
            picNumber=1,
            quotes=["I knew that fucking letter was a scam.",
                    "Oh no, an ambush! What am I gonna do... I'm so *scaaaaared*",
                    "You're in the presence of Eternum's future king!"],
            filename="con"
        )
        self.characters.append(Con)

        # 41 [DISCORD CAMEOS ?]
        Connor = CharacterCard(
            name="Professor Connor",
            picNumber=1,
            quotes=["Teaching is like my passion. And these students are my life.",
                    "Just don't tell the dean I'm smoking in here."],
            filename="connor"
        )
        self.characters.append(Connor)

        # 42
        Cook = CharacterCard(
            name="Elliot Cook",
            picNumber=1,
            quotes=["I... eh... I'm a taxi driver in New York.",
                    "I don't give a shit about you bunch of retards. I'm going out for a smoke."],
            filename="cook"
        )
        self.characters.append(Cook)

        # 43
        Coyote = CharacterCard(
            name="Boone",
            picNumber=3,
            quotes=["Pleased to meet another fishing enjoyer, the name's Boone.",
                    "I like to help kind people. And I'll be happy to show you my cabin.",
                    "I've gotta ask, what's your favourite species of sturgeon fish?",
                    "Now, now, no need to have a potty mouth! Swearing like a sailor on this ship?",
                    "Ahh... a magician never reveals his tricks, Orion."],
            filename="coyote",
            aliases="(spoiler) ||El Coyote||"
        )
        self.characters.append(Coyote)

        # 44 [HAREM; HOMIE SAVER]
        Dalia = CharacterCard(
            name="Dalia Carter",
            picNumber=10,
            quotes=["Come on! Less fright, more bite!!",
                    "I'm sorry, I was here making small talk as if you've been here for weeks.",
                    "This machine needs fuel!", "Ass to grass! Ass to grass!",
                    "Hello there, wanderer.",
                    "PANCAKES!! YAY!!",
                    "I'm a miserable mess...",
                    "You're goddamn right! I'm strong! Nothing's gonna stop me!",
                    "Never let it be said that Dalia doesn't honour her bets.",
                    "I'm not one to shy away from a competition, no matter the circumstances.",
                    "I like it when you get all \"romantico\"",
                    "I swear, whoever's holding him better pray I don't find them first."],
            filename="dalia",
            effects=Effects.HOMIE_SAVIOUR,
            aliases="Dalia the Explorer, Mars",
            collection=Collections.HAREM
        )
        self.characters.append(Dalia)

        # 45
        Dolores = CharacterCard(
            name="Dolores",
            picNumber=1,
            quotes=["Come on, don't be such a prude. We're just having fun.",
                    "What the fuck happened...?"],
            filename="dolores"
        )
        self.characters.append(Dolores)

        # 46
        Duke = CharacterCard(
            name="Duke",
            picNumber=1,
            quotes=["Dude, she's not reacting.",
                    "I don't enjoy tearing apart pretty things.",
                    "Just be sure to keep her away from Tissle. I like this girl's smell as it is.",
                    "T-The motherfucker really tried to shoot with the violin!"],
            filename="duke"
        )
        self.characters.append(Duke)

        # 47
        DuPont = CharacterCard(
            name="Dr. Du Pont",
            picNumber=1,
            quotes=["These programmers are terrible. I bet they hired immigrants.\nOr worse... women.",
                    "Incompetent..."],
            filename="dupont"
        )
        self.characters.append(DuPont)

        # 48
        Ed = CharacterCard(
            name="Ed",
            picNumber=1,
            quotes=["For fuck's sake, ain't there a single pirate left who's not retarded?!",
                    "Didn't you see the fucking sign you dingbats?",
                    "Yeah, I used to have one like that back when I still had flesh."],
            filename="ed"
        )
        self.characters.append(Ed)

        # 49 [DISCORD CAMEOS ?]
        Eggrik = CharacterCard(
            name="Anton Eggrik",
            picNumber=1,
            quotes=["I don't remember seeing you between the crowd when Jonah Hill was here last week!"],
            filename="eggrik"
        )
        self.characters.append(Eggrik)

        # 50
        Elenwen = CharacterCard(
            name="Regent Elenwen",
            picNumber=1,
            quotes=["You have no rightful place among us.", "Not only is he weak, but his people have lost even the pride that once defined them."],
            filename="elenwen"
        )
        self.characters.append(Elenwen)

        # 51
        ElfGuard1 = CharacterCard(
            name="Elven Guard 1",
            picNumber=1,
            quotes=["Oh come on, if I can't compliment our Princess' creamy tits to my friend and a few rats, I might as well quit this job."],
            filename="elf_guard1"
        )
        self.characters.append(ElfGuard1)

        # 52
        ElfGuard2 = CharacterCard(
            name="Elven Guard 2",
            picNumber=1,
            quotes=["The bastard really thought he could make a bargain with the Princess' life..."],
            filename="elf_guard2"
        )
        self.characters.append(ElfGuard2)

        # 53
        ElfGuard3 = CharacterCard(
            name="Sir Pyrand",
            picNumber=1,
            quotes=["You will serve as a reminder that no one defies Hyril'Ar, you filthy human.",
                    "\*Whispering\* Soon, Lord Sylax will rule as the sole regent and restore this realm to its former glory.",
                    "\*Whispering\* The age of shame... is over."],
            filename="elf_guard3",
            aliases="Elf Guard [3]"
        )
        self.characters.append(ElfGuard3)

        # 54
        Eulalie = CharacterCard(
            name="Eulalie",
            picNumber=1,
            quotes=["Good evening, and welcome to Gusteau's!",
                    "Gotta thank former President Stabb for the lowered drinking age.",
                    "If you need *anything* to make your wait shorter, please just let me know."],
            filename="eulalie"
        )
        self.characters.append(Eulalie)

        # 55 [SIDE GIRL]
        Eva = CharacterCard(
            name="Eva",
            picNumber=2,
            quotes=["Are you trying to make me blush? It might be working..."],
            filename="eva",
            aliases="Who?",
            collection=Collections.SIDE_DISHES
        )
        self.characters.append(Eva)

        # 56
        Fael = CharacterCard(
            name="Lord Fael of Thirinvale",
            picNumber=4,
            quotes=["I seek to unite our noble houses, [and] usher Hyril'Ar into an era of brilliance it has yet to behold[.]"],
            filename="fael",
            aliases="Heir of Thirinvale, Victor of the Sunlance Tournament"
        )
        self.characters.append(Fael)

        # 57
        FakeCoyote = CharacterCard(
            name="'El Coyote'",
            picNumber=1,
            quotes=["I'll admit that I'm flattered, but I usually prefer to stay in the shadows.",
                    "Ah, so you've chosen to meet your end with honor!",
                    "You see, when you carry a name like mine, you occasionally need to deal with nuisances."],
            filename="fakecoyote"
        )
        self.characters.append(FakeCoyote)

        # 58
        Fangrend = CharacterCard(
            name="Fangrend",
            picNumber=2,
            quotes=["I have nothing to discuss with a human from outside our pack.",
                    "You're not even worthy to be here",
                    "Welcome to the pack."],
            filename="fangrend"
        )
        self.characters.append(Fangrend)

        # 59
        Founder = CharacterCard(
            name="The Founder",
            picNumber=5,
            quotes=["...",
                    "I must admit that I am impressed.",
                    "I am sorry, where are my manners. Please, sit down",
                    "I have been looking forward to meeting you..."],
            filename="founder"
        )
        self.characters.append(Founder)

        # 60 [PRAETORIANS ?]
        Four = CharacterCard(name="Four",
                             picNumber=1,
                             quotes=["..."],
                             filename="four",
                             collection=Collections.NONE)
        self.characters.append(Four)

        # 61
        GarringtonJr = CharacterCard(
            name="Bennie Garrington",
            picNumber=1,
            quotes=[
                "Maybe we can continue this conversation in my private suite... in my hotel...",
                "Thank you. You can fuck off now.",
                "Their group tried to kill me not once, but twice!"],
            filename="garringtonjr"
        )
        self.characters.append(GarringtonJr)

        # 62
        Garrington = CharacterCard(
            name="Cornelius Garrington",
            picNumber=1,
            quotes=["So cocky. You remind me of myself when I was young.",
                    "Ah, that must be my men telling me the job is done.\nSPOILER: ||it was not||"],
            filename="garringtonsr"
        )
        self.characters.append(Garrington)

        # 63
        Gemini = CharacterCard(
            name="Gemini",
            picNumber=1,
            quotes=["I am capable of seeing the future",
                    "I'm afraid I see... nothing. I'm sorry."],
            filename="gemini",
            aliases="The Blind Oracle"
        )
        self.characters.append(Gemini)

        # 64
        Gertrude = CharacterCard(
            name="Gertrude",
            picNumber=1,
            quotes=["I don't like to brag, but... I'll have you know I'm the president of Kredon's School PTA.",
                    "I can't believe *I'm* the one who has to do this!\nAfter so many years at the company!",
                    "Dalia will learn a lot seeing two empowered women like us at their workplace.",
                    "Ugh, these elevators smell more and more like sweat everyday."],
            filename="gertrude",
            aliases="President of Kredon's School PTA"
        )
        self.characters.append(Gertrude)

        # 65 [CREATURE STOMPER]
        Golem = Villain(
            name="Golem",
            picNumber=1,
            quotes=["*groans*"],
            filename="golem",
            killMessage="The golem has stomped {victim} to death. They are no longer your pet, {author}.",
            protectedMessage="Pyramid Head managed to kill the golem before it could get its feet on {author}'s {victim}!",
            emptyMessage="The golem didn't find anyone to trample on... Lucky you I guess, {author}.",
            footer="*groans* ({author})",
            effects=Effects.CREATURE_STOMPER
        )
        self.characters.append(Golem)

        # 66
        Harley = CharacterCard(
            name="Harley Jones",
            picNumber=1,
            quotes=["I'm glad to see people my age. These boomers are a total bore.",
                    "I kill people, I get paid, etcetera, etcetera, repeat, clink, cha-ching."],
            filename="harley",
            aliases="The best hitwoman in all of Eternum."
        )
        self.characters.append(Harley)

        # 67
        Haskel = CharacterCard(
            name="Haskel",
            picNumber=1,
            quotes=["There's no way on earth we're losing to two freshman rookies."],
            filename="haskel"
        )
        self.characters.append(Haskel)

        # 68
        Hasler = CharacterCard(
            name="Commander Hasler",
            picNumber=2,
            quotes=["Turn around reeeeeal slow.",
                    "Thank you for your cooperation.",
                    "And don't try to stop me. You, women, elders, or even children - I'll kill ANYONE who stays in my way."],
            filename="hasler",
            aliases="Leader of the Second Brigade of the Galactic Union"
        )
        self.characters.append(Hasler)

        # 69
        Hassan = CharacterCard(
            name="Hassan Al-Rashid",
            picNumber=1,
            quotes=["You seem frightened, my young flowers of the desert... but I assure you, there's nothing to fear.",
                    "To the incubation room."],
            filename="hassan",
            aliases="the Sultan of the Valley of Kings"
        )
        self.characters.append(Hassan)

        # 70
        Hugo = CharacterCard(
            name="Hugo Hernandez",
            picNumber=1,
            quotes=["Victor, pedazo de cabrón!",
                    "You need to spend more time with us! You've lost your accent!",
                    "I guess you must be Luna's boyfriend.",
                    "OH SHIT, the chilaquiles",
                    "You see, I'm running a cartel and a human trafficking ring.",
                    "Órale, que tal. Mira, tengo una chamba para ti."],
            filename="hugo",
            aliases="Luna's uncle"
        )
        self.characters.append(Hugo)

        # 71 [SIDE GIRL]
        Idriel = CharacterCard(
            name="Idriel",
            picNumber=5,
            quotes=["Are you enjoying your experience in Eternum so far?",
                    "Maybe you're not asking the right questions...",
                    "What makes something real, I wonder?"],
            filename="idriel",
            aliases="The Eternum Lady, Eternum's AI",
            collection=Collections.SIDE_DISHES
        )
        self.characters.append(Idriel)

        # 72 [PETS]
        Igor = CharacterCard(
            name="Igor",
            picNumber=1,
            quotes=["Mmmm, Igor is hungry for the only thing on the menu -  one nice, biiiiig cock!",
                    "What's up with this trend among women lately in not having penises?"],
            filename="igor",
            collection=Collections.CREATURES
        )
        self.characters.append(Igor)

        # 73
        Iliescu = CharacterCard(
            name="Lord Lazarus Iliescu",
            picNumber=1,
            quotes=["You may go now, carrying my eternal gratitude.",
                    "Ah, your radiance shines even brighter in the light of day."],
            filename="iliescu",
            aliases="Sovereign of Stravenovia"
        )
        self.characters.append(Iliescu)

        # 74
        Innkeeper = CharacterCard(
            name="John",
            picNumber=1,
            quotes=["I'm as powerless as one can be! No sex dungeons I swear!"],
            filename="innkeeper",
            aliases="The Innkeeper"
        )
        self.characters.append(Innkeeper)

        # 75 [DISCORD CAMEOS ?]
        Jasticus = CharacterCard(
            name="Jasticus the Decapitator",
            picNumber=1,
            quotes=["They won't be able to scrub out your blood from the Rotunda floors after I'm done with you!",
                    "COME HERE, BOY!",
                    "Well, thanks again for not killing me, buddy."],
            filename="jasticus"
        )
        self.characters.append(Jasticus)

        # 76 [HOMIE]
        Jerry = CharacterCard(
            name="Jerry",
            picNumber=7,
            quotes=["This face ring a bell?",
                    "I AM THY SAVIOUR",
                    "I AM THE BEST PLAYERETH IN THIS COUNTRY...ETH",
                    "I recognize that prepubescent voice.",
                    "People used to bow before me, Orion.",
                    "I WON'T LET MYSELF BE DISRESPECTED ANY LONGER!",
                    "My therapist said I need to express my feelings more intensely.",
                    "AAAAAWWW SHIT, NOT AGAIN! It's even worse when you see it coming!",
                    "Magnificent instrument, General!"],
            filename="jerry",
            aliases="Sir Jermaine of Noriander, Leader of the Ishari",
            collection=Collections.THE_HOMIES
        )
        self.characters.append(Jerry)

        # 77 [VN CAMEOS ?]
        Judith = CharacterCard(
            name="Judith",
            picNumber=1,
            quotes=["Welcome to the University of Kredon's Annual Halloween Party."],
            filename="judith"
        )
        self.characters.append(Judith)

        # 78
        Junkie = CharacterCard(
            name="Junkie",
            picNumber=1,
            quotes=["Hey bro, you got a smoke...?",
                    "Whoa, look at this... this lil' bitch thinks he's tough.",
                    "You're fuckin' dead, you hear me?!"],
            filename="junkie1"
        )
        self.characters.append(Junkie)

        # 79
        Junkie2 = CharacterCard(
            name="JJ",
            picNumber=1,
            quotes=["Are you fucking nuts?!!"],
            filename="junkie2"
        )
        self.characters.append(Junkie2)

        # 80 [DISCORD CAMEOS ?]
        Kai = CharacterCard(
            name="Kai",
            picNumber=2,
            quotes=["Welcome to your *reawakening*."],
            filename="kai",
            aliases="Kai from Kainan Engineering"
        )
        self.characters.append(Kai)

        # 81
        Keating = CharacterCard(
            name="Professor Keating",
            picNumber=2,
            quotes=["You can do the p-project another day then. N-no problem. F-family comes first.",
                    "Didn't you hear me?! Class is dismissed!"],
            filename="keating"
        )
        self.characters.append(Keating)

        # 82 [PETS]
        Kermit = CharacterCard(
            name="Kermit",
            picNumber=1,
            quotes=["\*Croaks\*"],
            filename="kermit",
            aliases="lil' Kermie",
            collection=Collections.CREATURES
        )
        self.characters.append(Kermit)

        # 83
        Kimberly = CharacterCard(
            name="Kimberly",
            picNumber=1,
            quotes=["I knew that one! You need to consult with us before answering!"],
            filename="kimberly"
        )
        self.characters.append(Kimberly)

        # 84
        Kitty = CharacterCard(
            name="Kitty",
            picNumber=1,
            quotes=["Normally an item like this would have a high asking price, but since I owe Annie a favour... Consider yourself lucky."],
            filename="kitty",
            aliases="Kitytu"
        )
        self.characters.append(Kitty)

        # 85
        Lily = CharacterCard(
            name="Lily",
            picNumber=1,
            quotes=["You need an assistant! And I offer myself!"],
            filename="lily"
        )
        self.characters.append(Lily)

        # 86
        Linus = CharacterCard(
            name="Alastor Linus",
            picNumber=1,
            quotes=["For this project, we reached out to Eternum's players to figure out the number one question on everyone's mind... DOES IDRIEL HAVE A PUSSY?!"],
            filename="linus"
        )
        self.characters.append(Linus)

        # 87 [SIDE GIRL]
        Lorelei = CharacterCard(
            name="Lorelei Thornvale",
            picNumber=1,
            quotes=["You can... speak so fluently?",
                    "I-I merely possess a keen interest in human biology."],
            filename="lorelei",
            collection=Collections.SIDE_DISHES
        )
        self.characters.append(Lorelei)

        # 88 [DISCORD CAMEOS ?]
        Lorrdy = CharacterCard(
            name="Lorrdy Silverhook",
            picNumber=1,
            quotes=["Ahoy, Mr. Orion! Lordy Silverhook at your service!",
                    "Take me on, and you won't be disappointed.",
                    "As a German, born and raised miles from any ocean, the vastness of the seas always filled me with yearning.",
                    "Once, I convinced a great white shark to stop snacking on kids at the beaches of Copacabana, Mexico."],
            filename="lorrdy"
        )
        self.characters.append(Lorrdy)

        # 89
        Lucinda = CharacterCard(
            name="Lucinda Garcia",
            picNumber=1,
            quotes=["Nice to finally meet you!", "Ohh, aren't you a polite and handsome young boy?",
                    "\*Whispering\* he's so good-looking, isn't he?"],
            filename="lucinda"
        )
        self.characters.append(Lucinda)

        # 90 [HAREM]
        Luna = CharacterCard(
            name="Luna Hernandez",
            picNumber=16,
            quotes=[
                "Thank you for everything you said. It was... sweet.",
                "I'm sorry. I didn't mean to scare you.",
                "I... like the feel of silk and velvet, that's all.",
                "At 1 month and 14 days post-mortem... only the bones remain.",
                "At least he doesn't call me a weirdo like everyone else.",
                "Don't look into the room on the right. My father's corpse is still there.",
                "You have a very... g-good body.",
                "Gracias por venir. Me gusta mucho pasar tiempo contigo.",
                "I'm sure my family wouldn't mind. They really liked you.",
                "I... I feel safe when I'm with you.",
                "Y-You goof!",
                "You mean the world to me. More than you can probably realize."
            ],
            filename="luna",
            aliases="Ganymede, Lunita, Luny, Mia Smith",
            collection=Collections.HAREM
        )
        self.characters.append(Luna)

        # 91
        Lysa = CharacterCard(
            name="Lady Lysandra Iliescu",
            picNumber=1,
            quotes=["Aaaaahhh... yeeeesss... I could smell them outside the crypt...",
                    "Y-You would make an exceptional vampire, young man.",
                    "Bravo! That was absolutely enchanting!"],
            filename="lysa"
        )
        self.characters.append(Lysa)

        # 92 [SIDE GIRL]
        Maat = CharacterCard(
            name="Maat",
            picNumber=3,
            quotes=["Welcome to my Oasis.",
                    "I feel like playing right now... Don't you?",
                    "You can ask around. Maat always keeps her promises.",
                    "You really thought you could waltz back into *my* server without me finding out, huh?"],
            filename="maat",
            collection=Collections.SIDE_DISHES
        )
        self.characters.append(Maat)

        # 93
        Mandrake = CharacterCard(
            name="Dona Mandrake",
            picNumber=1,
            quotes=["Welcome to Potions!",
                    "My classroom, my rules"],
            filename="mandrake",
            aliases="Professor Mandrake"
        )
        self.characters.append(Mandrake)

        # 94 [PETS]
        Maurice1 = CharacterCard(
            name="Maurice (cat)",
            picNumber=1,
            quotes=["*meows*"],
            filename="mauricec",
            collection=Collections.CREATURES
        )
        self.characters.append(Maurice1)

        # 95 [PETS]
        Maurice2 = CharacterCard(
            name="Maurice (goat)",
            picNumber=1,
            quotes=["*bleats*",
                    "Tired of cleaning up after him? He turn into many meals\nand delicious broth!"],
            filename="mauriceg",
            collection=Collections.CREATURES
        )
        self.characters.append(Maurice2)

        # 96 [PETS]
        Maurice3 = CharacterCard(
            name="Maurice (toucan)",
            picNumber=1,
            quotes=["Stockholm", "Maurice very intelligent! He know all the answers!"],
            filename="mauricet",
            collection=Collections.CREATURES
        )
        self.characters.append(Maurice3)

        # 97 [HOMIES ?]
        Maximo = CharacterCard(
            name="Maximo",
            picNumber=2,
            quotes=["The word of the Emperor is sacred and must be kept.",
                    "Please do not resist. I've already dealt with enough troublemakers today.",
                    "Death or Glory.",
                    "The sun has finally come out, my Empress.",
                    "I pledge to dedicate my entire life to the WRE, Empress Nancy and to you, my General!"],
            filename="maximo",
            aliases="Dingleberry"
        )
        self.characters.append(Maximo)

        # 98
        Mercer = CharacterCard(
            name="Dr. Irina Mercer",
            picNumber=1,
            quotes=["Let's see what people call me in 50 years...",
                    "Little sacrifices are sometimes necessary for the sake of progress, don't you think?"],
            filename="mercer"
        )
        self.characters.append(Mercer)

        # 99
        Mermaid = CharacterCard(
            name="Mermaid",
            picNumber=1,
            quotes=["Boo!", "I can do a lot of magical things, Orion... especially to young handsome men like you."],
            filename="mermaid"
        )
        self.characters.append(Mermaid)

        # 100 [HOMIE]
        Micaela = CharacterCard(name="Micaela Garcia",
                                picNumber=4,
                                quotes=["I know I can have a rather intimidating appearance at first.",
                                        "You've improved a lot over the last year. I'm impressed!"],
                                filename="micaela",
                                collection=Collections.THE_HOMIES)
        self.characters.append(Micaela)

        # 101
        Millie = CharacterCard(
            name="Millie",
            picNumber=2,
            quotes=["You can do it all here at PUMP IT!"],
            filename="millie"
        )
        self.characters.append(Millie)

        # 102 [VN CAMEOS ?]
        Moon = CharacterCard(
            name="Moon",
            picNumber=1,
            quotes=["I have to go. See you Monday."],
            filename="moon"
        )
        self.characters.append(Moon)

        # 103
        Mortimer = CharacterCard(
            name="Mortimer",
            picNumber=1,
            quotes=["\*Bowing gracefully\* Good evening, madam and sir.",
                    "It is my great pleasure to welcome you to Lord Iliescu's residence.",
                    "I live to serve.",
                    "Stick close, you two lovebirds, unless you fancy becoming dinner for giant tarantulas!"],
            filename="mortimer"
        )
        self.characters.append(Mortimer)

        # 104
        Morty = CharacterCard(
            name="Morty",
            picNumber=1,
            quotes=["It happened again!",
                    "It's not good for your heart. Metaphorically.",
                    "\*Whispering\* I can't stop staring at his junk.",
                    "Okay, it's the Kraken."],
            filename="morty"
        )
        self.characters.append(Morty)

        # 105 [DISCORD CAMEOS ?]
        Mos = CharacterCard(
            name="Mr. Mos",
            picNumber=1,
            quotes=["No self-respecting man should go around without a good suit."],
            filename="mos"
        )
        self.characters.append(Mos)

        # 106 [HAREM]
        Nancy = CharacterCard(
            name="Nancy Carter",
            picNumber=14,
            quotes=["What have I done to deserve such chivalry?",
                    "I'm sorry, I just took a shower and I'm all wet.",
                    "Family always comes first.",
                    "I want your eyes on me. You know it'd be quite rude to look away from your Empress.",
                    "Well, are you enjoying this time with your Empress?",
                    "I refuse to let those ERE bastards take my city! Take OUR city!",
                    "Well, I have a city to save.",
                    "The Macedonians are trying to reconquer Megara. OVER MY DEAD BODY.",
                    "Welcome to Rome, Cicero.",
                    "Then I'll expand the Empire to other servers. The WRE knows no borders.",
                    "I don't seem to see any Praetorians around... do you?",
                    "It's like we're fighting against fate or destiny or something like that.",
                    "Ah, young love... my little princesses grew up too fast!",
                    "\*Moans\* Will you... make me... beg...?"],
            filename="nancy",
            aliases="Nan, Empress of the Western Roman Empire, Saturn",
            collection=Collections.HAREM
        )
        self.characters.append(Nancy)

        # 107
        Nikolay = CharacterCard(
            name="Nikolay",
            picNumber=1,
            quotes=["Границы России нигде не заканчиваются."],
            filename="nikolay"
        )
        self.characters.append(Nikolay)

        # 108 [HOMIES]
        Noah = CharacterCard(
            name="Noah",
            picNumber=4,
            quotes=["We can help you for money",
                    "I... haven't seen my... Mom... for a very long time, Mr. Keating",
                    "You'll never fight alone",
                    "To hell and back, moj brat."],
            filename="noah",
            collection=Collections.THE_HOMIES
        )
        self.characters.append(Noah)

        # 109 [HAREM]
        Nova = CharacterCard(
            name="Nova Johnson",
            picNumber=17,
            quotes=["Sorry for all the commotion, I just had to make sure!",
                    "I just happened to be looking at my phone and then you called!",
                    "Sorry, I saw these donuts and I couldn't resist.",
                    "STOP. HACKING. ME.",
                    "I'm a hacker, that's my thing. Would you ask an alcoholic to stop drinking?",
                    "I might look like a walking cheeto, but I promise you, I do not taste like one.",
                    "Well, one, I can't read minds. I merely uncover personal information that people so foolishly leave unsecure.",
                    "From now on, I'll be your personal hacker.",
                    "It was a breeze! Like stealing candy from a baby!",
                    "Hey, you didn't scream this time! Just a little gasp.",
                    "Bang! Headshot!",
                    "\*giggles\* A magician never explains his tricks.",
                    "And that's how you play Eternum!",
                    "I swear, if *anything* goes wrong, I'm gonna die.",
                    "Any last comments before getting down to business?",
                    "\*Mumbling\* The numbers... what do they even mean??"],
            filename="nova",
            aliases="Delilah Warren, Mercury",
            collection=Collections.HAREM
        )
        self.characters.append(Nova)

        # 110 [HOMIE; SIDE GIRL SAVER]
        Orion = CharacterCard(
            name="Orion Richards",
            picNumber=15,
            quotes=["I was hoping [Calypso] was a lightsaber crossbow or something",
                    "My hair is a wild beast that cannot be tamed!",
                    "Learn? Me Orion. Me point to pretty thing. Me press button. Me likey.",
                    "*\"Thit bitch hurs lust duh chins ti bi i midil\"*",
                    "I'm gonna look like a deformed potato next to you!",
                    "It's been a pleasure, Mr. Garrington.",
                    "It's just sushi, not a joint.",
                    "Did you know that sex is a death sentence for octopuses?",
                    "I can withstand spicy food.",
                    "Here at Richards Massage Parlor, customer satisfaction is priority numero uno!",
                    "I just hope I didn't taste like your dad's tacos.",
                    "Nothing a good shower and a HUGE cup of coffee can't fix.",
                    "I was promised cookies, but I don't see them anywhere.",
                    "Damn, these whiskeys sure are taking a while, aren't they?",
                    "As a fan of big speeches myself, I must admit that your boss delivered a pretty good one.",
                    "Sometimes I feel like I can ace pretty much everything I try to do here.",
                    "(Hmm, these barrels are quite big. I could probably squeeze myself into one.)",
                    "Dude, you're such a hater.",
                    "Mmm, I can trade you a cookie for a kiss."],
            filename="orion",
            effects=Effects.SIDE_GIRL_SAVIOUR,
            aliases="MC, Alek Claimant, Orion Holmes, Orion the Merciful, Jupiter, Sir Grothelborn of Kredon",
            collection=Collections.THE_HOMIES
        )
        self.characters.append(Orion)

        # 111
        Orym = CharacterCard(
            name="Lord Orym of Ilvenmyr",
            picNumber=3,
            quotes=["I tremble before your radiance, Your Grace."],
            filename="orym",
            aliases="Sworn Sword of Honor"
        )
        self.characters.append(Orym)

        # 112
        Owler = CharacterCard(
            name="Helga Owler",
            picNumber=1,
            quotes=["Oh god! I didn't hear you coming... How embarrassing!"],
            filename="owler",
            aliases="Professor Owler"
        )
        self.characters.append(Owler)

        # 113 [PETS]
        Pancho = CharacterCard(
            name="Pancho",
            picNumber=1,
            quotes=["\*clucks\*"],
            filename="pancho",
            aliases="Hugo's Chicken",
            collection=Collections.CREATURES
        )
        self.characters.append(Pancho)

        # 114 [HAREM]
        Penny = CharacterCard(
            name="Penelope Paige Carter",
            picNumber=15,
            quotes=["All that humidity outside better not turn my hair into a frizzy mess!",
                    "How can stop be the keyword?",
                    "Did you know that that Gigachad meme guy from a few years ago tried sliding into my DMs?",
                    "Anyway, now that we've both seen each other naked, there's no reason to make a big deal about this in the future.",
                    "Didn't mean to give you a *hard* time.",
                    "Are you planning to enchant anyone with your bow tonight?",
                    "It's too bad I couldn't dress up as Psyche. You know... so we could match.",
                    "I'm not up to anything. I'm a good girl.",
                    "You're such a dork. You're lucky I think you're cute.",
                    "No matter the occasion, one should always dress sexy and stylish!",
                    "There are tons of hot guys hitting on me literally EVERY DAY.",
                    "Did you come up with that comeback on your own? Or did you ask for advice on r/clevercomebacks again?",
                    "I'll make sure all your Christmases feel special from now on..."],
            filename="penny",
            aliases="Penny, miss_penny, best tits on instagram, Venus",
            collection=Collections.HAREM
        )
        self.characters.append(Penny)

        # 115
        Phil = CharacterCard(
            name="Phil",
            picNumber=1,
            quotes=["\*Swallows\*"],
            filename="phil",
            aliases="the devourer of men, the Abyssal Terror"
        )
        self.characters.append(Phil)

        # 116
        Philippe = CharacterCard(
            name="Philippe",
            picNumber=1,
            quotes=["How can you shine so much, sweetie? I'm going to start\nwearing my sunglasses around you!",
                    "Don't \"Philippe\" me, darling!",
                    "Don't frown so much or you'll get wrinkles on that pretty face of yours!"],
            filename="philippe"
        )
        self.characters.append(Philippe)

        # 117
        Piaget = CharacterCard(
            name="Anna Piaget",
            picNumber=1,
            quotes=["I was honestly expecting this to be a bit more challenging."],
            filename="piaget",
            aliases=""
        )
        self.characters.append(Piaget)

        #118
        Powell = CharacterCard(
            name="Adrian Powell",
            picNumber=1,
            quotes=[
                "Here at Ulysses, we respect women and believe in gender equality. What the fuck is your problem?",
                "Any self-respecting gentleman should always wear a nice tie... Not like fucking Toby.",
                "You two have some *impressive* resumes. Haven't seen ones this polished since that guy who faked his diploma.",
                "Everyone knows *real* businessmen only use cocaine anyway. Or microdoses of LSD.",
                "The memory of Tigoryakhovgrad will prevail as long as we remember it.",
                "Tell that Toby douche to hold an isometric air squat until it's his turn."
            ],
            filename="powell"
        )
        self.characters.append(Powell)

        # 119 [PRAETORIANS ?]
        Praetorian = CharacterCard(
            name="Praetorian 1",
            picNumber=1,
            quotes=["Put your hands up and back away from the girl.",
                    "You've committed crimes against Eternum's\nGeneral Code of Ethics."],
            filename="praetorian1"
        )
        self.characters.append(Praetorian)

        # 120 [PRAETORIANS ?]
        Praetorian2 = CharacterCard(
            name="Praetorian 2",
            picNumber=1,
            quotes=["Resisting will only make things more painful for you.",
                    "Surrender now. This is your last warning."],
            filename="praetorian2"
        )
        self.characters.append(Praetorian2)

        # 121 [PRAETORIANS ?]
        Praetorian3 = CharacterCard(
            name="Praetorian 3",
            picNumber=1,
            quotes=["We're taking all necessary precautions to ensure\nthe security and safety of the players attending tonight."],
            filename="praetorian3"
        )
        self.characters.append(Praetorian3)

        # 122
        Priscilla = CharacterCard(
            name="Priscilla Bardot",
            picNumber=1,
            quotes=["I guess you can get away with whatever you want,\nif you have the finest lawyers money can buy."],
            filename="priscilla"
        )
        self.characters.append(Priscilla)

        # 123 [PET SAVER]
        Pyri = CharacterCard(
            name="Pyramid Head",
            picNumber=1,
            quotes=["**The time of judgement has come.**"],
            filename="pyramid_head",
            effects=Effects.CREATURE_SAVIOUR,
            aliases="Pyri"
        )
        self.characters.append(Pyri)

        # 124 [HOMIE]
        Raul = CharacterCard(
            name="Raul",
            picNumber=4,
            quotes=["Do you remember what I told you in the trenches in Sarajevo?",
                    "Let's have one last dance.",
                    "To hell... and back."],
            filename="raul",
            collection=Collections.THE_HOMIES
        )
        self.characters.append(Raul)

        # 125 [DISCORD CAMEOS ?]
        Reddss = CharacterCard(
            name="Blackheart Reddss",
            picNumber=1,
            quotes=["Just one D brings terrible luck.",
                    "Dragging the D but not the S brings even worse luck!",
                    "I'll be in the kitchen whipping up another delectable cake."],
            filename="reddss"
        )
        self.characters.append(Reddss)

        # 126 [SIDE GIRL]
        RedFoxMaiden = CharacterCard(
            name="Red Fox Maiden",
            picNumber=1,
            quotes=["We hope you're enjoying your stay.",
                    "We are the gift. Our task is to satisfy all of your desires."],
            filename="redfoxmaiden",
            collection=Collections.SIDE_DISHES
        )
        self.characters.append(RedFoxMaiden)

        # 127
        Regina = CharacterCard(
            name="Regina",
            picNumber=2,
            quotes=["You definitely deserve someone better than Penelope to accompany you at this party.",
                    "Depends on whether you prefer a dumb, boring, walking piece of titty meat, or... something spicier.",
                    "This is a party, and I have an entire bottle of Jäger right here, ready to be drunk.",
                    "Boy, you've gotta be the palest Blacked actor I've seen"],
            filename="regina"
        )
        self.characters.append(Regina)

        # 128
        Rowan = CharacterCard(
            name="Rowan",
            picNumber=1,
            quotes=["The game's about to start and I can't find the damn gin."],
            filename="rowan"
        )
        self.characters.append(Rowan)

        # 129
        Ruiz = CharacterCard(
            name="Clarence Ruiz",
            picNumber=1,
            quotes=["What the hell...",
                    "I'm afraid you're not leaving this building on your own, son."],
            filename="ruiz"
        )
        self.characters.append(Ruiz)

        # 130
        Ruth = CharacterCard(
            name="Ruth",
            picNumber=1,
            quotes=["Well, if I knew a handsome fellow like you was waiting for me, I'd have hurried out sooner!"],
            filename="ruth",
            aliases="Clerk"
        )
        self.characters.append(Ruth)

        # 131
        Samir = CharacterCard(
            name="Samir",
            picNumber=2,
            quotes=["All we want... is to reclaim what’s rightfully ours.",
                    "The Ishari are always on the lookout for valiant players to join our cause."],
            filename="samir",
            aliases="Leader of the Ishari"
        )
        self.characters.append(Samir)

        # 132
        Sandra = CharacterCard(
            name="Sandra Johnson",
            picNumber=1,
            quotes=["If it keeps raining this hard, I might need a ride on Noah's ark..."],
            filename="sandra",
            aliases="Nova's mom"
        )
        self.characters.append(Sandra)

        # 133
        Scarlet = CharacterCard(
            name="Red Scarlet",
            picNumber=1,
            quotes=["Hi, handsome... I'm Red Scarlet.", "I give really, *really* good blowjobs."],
            filename="scarlet"
        )
        self.characters.append(Scarlet)

        # 134
        Sheriff = CharacterCard(
            name="Sheriff of Blackridge",
            picNumber=1,
            quotes=["Lookey here at my shiny precious and read, boy.",
                    "They say crime doesn't pay but what they don't tell ya ish that THE LAW DON'T EITHER!"],
            filename="sheriff"
        )
        self.characters.append(Sheriff)

        # 135
        Snuggles = CharacterCard(
            name="Snuggles",
            picNumber=1,
            quotes=["Me chesty... so much hurty...", "Me only wanted to welcomey...",
                    "Snuggles... is in big owieeeee...",
                    "Me hurty so much... I no know if me can snuggle anymore...",
                    "These... These two girls... Promise me... that... that... They're going to rot in a filthy prison cell like the dirty whores they are."],
            filename="snuggles",
            aliases="Snuggles the happy bear, Snuggles the sadistic bear"
        )
        self.characters.append(Snuggles)

        # 136
        StoreClerk = CharacterCard(
            name="General Store Clerk",
            picNumber=1,
            quotes=["You're offending my Wamapoke roots!",
                    "I can already feel the warmth of my ancestors smiling down on us."],
            filename="storeclerk",
            aliases="Brendan from Queens"
        )
        self.characters.append(StoreClerk)

        #137
        Sylax = CharacterCard(
            name="Regent Sylax",
            picNumber=3,
            quotes=["The stench is even more nauseating than I anticipated.", 
                    "The Council will determine the degree of your punishment.", 
                    "Please. Even the humblest of our farmers could best you in a duel.",
                    "By Turska's mercy, get to the point.",
                    "Hyril'Ar demands rebirth."],
            filename="sylax"
        )
        self.characters.append(Sylax)

        # 138
        Tartaria = CharacterCard(
            name="Mr. Tartaria",
            picNumber=1,
            quotes=[
                "Forgive me for not revealing my real name, one can never be sure someone else isn't a secret agent of the NWO.",
                "At least you can afford to joke here - luckily, there are no birds.",
                "The \"globe\"? Interesting name for something that's actually shaped like a cube.",
                "Believe what you want, I'm just trying to open your eyes."],
            filename="tartaria"
        )
        self.characters.append(Tartaria)

        # 139
        Tatiana = CharacterCard(
            name="Tatiana",
            picNumber=1,
            quotes=["He called us **things**, sister",
                    "Enough pleasantries."],
            filename="tatiana"
        )
        self.characters.append(Tatiana)

        # 140
        Thalindra = CharacterCard(
            name="Thalindra",
            picNumber=1,
            quotes=["Lady Calypso!", "Of course, Your Grace!"],
            filename="thalindra",
            aliases="Calypso's Maid"
        )
        self.characters.append(Thalindra)

        # 141 [HAREM KILLER]
        Thanatos = Villain(
            name="Thanatos",
            picNumber=8,
            quotes=["I must say, you've done more damage here than most.",
                    "**The strong... prevail. The weak... die.**",
                    "You are powerless. Inferior. Defective. Weak.", "No one can escape from me.",
                    "Where is the Gem of Doom?", "You're no longer useful to me. Open the gates.",
                    "All I am surrounded by... is fear. **And dead men.**",
                    "I can respect the resolve of a warrior."],
            filename="thanatos",
            killMessage="Thanatos killed {victim}. She is no longer in your harem, {author}.",
            protectedMessage="Calypso managed to evacuate {author}'s {victim} before Thanatos could kill her!",
            emptyMessage="Thanatos didn't find anyone to kill... Lucky you I guess, {author}.",
            footer="You won't be this lucky next time, {author}.",
            effects=Effects.HAREM_KILLER,
            aliases="The best Eternum player, Wyatt R. Pitman"
        )
        self.characters.append(Thanatos)

        # 142
        Thorund = CharacterCard(
            name="Regent Thorund",
            picNumber=2,
            quotes=["\*Disdainfully\* Silence."],
            filename="thorund",
            aliases="High Chancellor of Hyril'Ar"
        )
        self.characters.append(Thorund)

        # 143
        Thorund_Daughter = CharacterCard(
            name="Regent Thorund's Daughter",
            picNumber=1,
            quotes=["If you have any question of your own, speak now."],
            filename="thorund_daughter"
        )
        self.characters.append(Thorund_Daughter)

        # 144
        TicketGuy = CharacterCard(
            name="Tickets Seller",
            picNumber=1,
            quotes=["Do you have a ticket to watch the upcoming Munus?"],
            filename="ticketmaster"
        )
        self.characters.append(TicketGuy)

        # 145
        TonyMack = CharacterCard(
            name="Tony Mack",
            picNumber=1,
            quotes=["Thank you for your help, citizen."],
            filename="tonymack",
            aliases="Blackridge Sheriff's Deputy"
        )
        self.characters.append(TonyMack)

        # 146
        Torion = CharacterCard(
            name="Lord Torion of Redveil",
            picNumber=4,
            quotes=["Choose me, Princess, and I shall give you sons and daughters born of fire and fury. Children who will tower like oaks and march like storms!",
                    "Should your path ever lead you to Redveil, you would be most welcome. We always open our gates to knights of your caliber."],
            filename="torion"
        )
        self.characters.append(Torion)

        # 147 [DISCORD CAMEOS]
        Tissle = CharacterCard(
            name="Tissle",
            picNumber=1,
            quotes=["*You guys are such wimps. Let the alpha deal with it.*",
                    "Oh, COME ON, guys! I don't smell anymore!"],
            filename="tissle",
            aliases="Tis"
        )
        self.characters.append(Tissle)

        # 148 [HOMIE KILLER]
        Troll = Villain(
            name="Troll",
            picNumber=1,
            quotes=["*groans*"],
            filename="troll",
            killMessage="The troll killed {victim}. They are no longer in your homie group, {author}!",
            protectedMessage="Dalia managed to kill the troll before it could get its hands on {author}'s {victim}!",
            emptyMessage="The troll didn't find anyone to kill... Lucky you I guess, {author}",
            footer="*groans* ({author})",
            effects=Effects.HOMIE_KILLER
        )
        self.characters.append(Troll)

        # 149 [PRAETORIANS ?]
        Twelve = CharacterCard(
            name="Twelve",
            picNumber=1,
            quotes=["..."],
            filename="twelve"
        )
        self.characters.append(Twelve)

        # 150
        Valentino = CharacterCard(
            name="Nico Valentino",
            picNumber=1,
            quotes=["Who the fuck are you? Her manager?",
                    "Are you new to this industry or something?",
                    "I'm not even asking for a blowjob this time",
                    "(This is what happens when you give women any kind of important job.)"],
            filename="valentino",
            aliases="the best fashion agent in the country"
        )
        self.characters.append(Valentino)

        # 151
        Vasil = CharacterCard(
            name="Vasil",
            picNumber=1,
            quotes=["Bring the egg and I'll open the door, I promise..."],
            filename="vasil"
        )
        self.characters.append(Vasil)

        # 152 [HOMIE]
        Victor = CharacterCard(
            name="Victor Hernandez",
            picNumber=7,
            quotes=["Death is not the scariest fate",
                    "minusfiftypointssaywhat?",
                    "ORION MY MAN! I KNEW YOU WOULDN'T LET US DOWN!",
                    "YOU'RE GONNA MAKE MEXICO PROUD!",
                    "Ahh! Isn't it a lovely day to celebrate the Day of the Dead?",
                    "Hey! It's just an old Mexican saying!",
                    "Are you ready to try the best tacos you've ever eaten?",
                    "Look at me, I'm handsome! 100% objective.",
                    "Dame un abrazo, perro!",
                    "I'm sorry, my English is no bueno.",
                    "Thanks for keeping a smile on my little girl's face.",
                    "If you EVER hurt her, I will hunt you down across the outback till the day I die.",
                    "THAT FUCKING CHICKEN TOOK MY CHEESE! I'M GONNA KILL HIM!"],
            filename="victor",
            collection=Collections.THE_HOMIES
        )
        self.characters.append(Victor)

        # 153 [DISCORD CAMEOS ???]
        Wagner = CharacterCard(
            name="Colonel Jasper Wagner",
            picNumber=1,
            quotes=["No one has ever taken the Wagner bunker and today will be no exception!",
                    "Graveyards are full of honorable people.", "I always win.",
                    "So you choose... death. Disappointing.",
                    "Now, now, now... not so fast, Thanny."],
            filename="wagner"
        )
        self.characters.append(Wagner)

        # 154 [SIDE GIRL]
        Wenlin = CharacterCard(
            name="Wenlin",
            picNumber=4,
            quotes=["I was starting to think this server only had stingy, mean people!",
                    "Business first, pleasure later!"],
            filename="wenlin",
            collection=Collections.SIDE_DISHES
        )
        self.characters.append(Wenlin)

        # 155
        William = CharacterCard(
            name="William Bardot",
            picNumber=3,
            quotes=["Hmm, where did I go wrong with you...?",
                    "LOOK ME IN THE EYE WHEN I'M TALKING TO YOU!",
                    "Excuse me..? I *know* you aren't talking to me like that.",
                    "You clearly have no idea who you're speaking to, so let me spell it out for your simpleminded brain.",
                    "You're not even worth the trouble.",
                    "I'm surrounded by idiots fucking everywhere.",
                    "Perhaps I was overestimating you after all."],
            filename="william",
            aliases="C.E.O. of Ulysses, William 'huge-ass forehead' Bardot, Baldy Bardot"
        )
        self.characters.append(William)

        # 156
        WyattsMom = CharacterCard(
            name="Wyatt's Mother",
            picNumber=2,
            quotes=["If you try to trick me, I'm gonna shoot you both! I've got nothing to lose!",
                    "Please, I'd like you to leave now."],
            filename="wyattsmom",
            aliases="Old Lady, Mrs. Pitman"
        )
        self.characters.append(WyattsMom)

        # 157
        Xeno = CharacterCard(
            name="Xenomorph",
            picNumber=2,
            quotes=["\*Squeals\*"],
            filename="xenomorph"
        )
        self.characters.append(Xeno)

        # 158
        Zahra = CharacterCard(
            name="Zahra Al-Nabi",
            picNumber=1,
            quotes=["Wait... She's... still pure.",
                    "Hey, the first time is always the worst."],
            filename="zahra",
            aliases="The Citadel's Oracle"
        )
        self.characters.append(Zahra)

        # 159
        Zap = CharacterCard(
            name="Zap",
            picNumber=2,
            quotes=["ZAP!"],
            filename="zap"
        )
        self.characters.append(Zap)

        # 160
        Zippy = CharacterCard(
            name="Zippy",
            picNumber=1,
            quotes=["I'm a magic fox, of course!",
                    "What a klumpy-dumpy!"],
            filename="zippy"
        )
        self.characters.append(Zippy)


        egf_path = f"./EternumGfGameImages/"
        # auto-set picNumber values:
        for chara in self.characters:
            # count n(files) with format chara.filename_x
            matches = []
            for f in listdir(egf_path):
               if isfile(join(egf_path, f)) and (f[:-7] == chara.filename or f[:-8] == chara.filename):
                   matches.append(f);
            chara.picNumber = len(matches)

    def searchNameWithFilename(self, filename: str):
        # since sorted alphabetically, maybe bin-search?
        for c in self.characters:
            if c.filename == filename:
                return c.name
        
        return None
