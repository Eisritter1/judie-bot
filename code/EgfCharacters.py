from CharacterCard import CharacterCard
from Utilities import Collections, Effects


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

        # 2 [DISCORD CAMEOS ?]
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

        # 3 [HAREM]
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
                    "Anyway, let's not get all sappy like a bunch of drama nerds."],
            filename="alex",
            aliases="Alex, Orion's lil' super-soaker, Neptune",
            collection=Collections.HAREM
        )
        self.characters.append(Alex)

        # 4
        Alfonso = CharacterCard(
            name="Alfonso",
            picNumber=1,
            quotes=[
                "If you've got any last-minute buys to make before leaving the Citadel, please, swing by Alfonso's!"],
            filename="alfonso"
        )
        self.characters.append(Alfonso)

        # 5
        Alicia = CharacterCard(
            name="Alicia Flink",
            picNumber=1,
            quotes=["*moans*"],
            filename="aliciaflink"
        )
        self.characters.append(Alicia)

        # 6
        Ambrose = CharacterCard(
            name="Madam Ambrose",
            picNumber=1,
            quotes=["Men from around the world come here for... invigoration"],
            filename="ambrose"
        )
        self.characters.append(Ambrose)

        # 7
        Anastasia = CharacterCard(
            name="Anastasia",
            picNumber=1,
            quotes=["You opened fire on the mistress. Such uncivilized behavior.",
                    "Firearms are barbaric."],
            filename="anastasia"
        )
        self.characters.append(Anastasia)

        # 8
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

        # 9
        Annabelle = CharacterCard(
            name="Princess Annabelle",
            picNumber=1,
            quotes=["How did you get into my castle?!", "You worthless wretches!"],
            filename="annabelle",
            aliases="Annabelle the Skinner"
        )
        self.characters.append(Annabelle)

        # 10 [HAREM]
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

        # 11
        Anne = CharacterCard(
            name="Annie Flink",
            picNumber=1,
            quotes=["I want Mr. Nebula."],
            filename="annieflink",
            aliases="Anne"
        )
        self.characters.append(Anne)

        # 12
        Apple = CharacterCard(
            name="Apple Salesman",
            picNumber=1,
            quotes=[
                "30% of the net profits are donated towards the preservation of\nthe ocean's species and their habitats."],
            filename="applemerchant",
            aliases="One eternal per apple guy"
        )
        self.characters.append(Apple)

        # 13
        Arannis = CharacterCard(
            name="Arannis Thornvale",
            picNumber=1,
            quotes=["It is precisely such mercy that elevates us above your wretched kind."],
            filename="arannis",
            aliases="General Arannis, General of the Royal Guard"
        )
        self.characters.append(Arannis)

        # 14
        Aspen = CharacterCard(
            name="Aspen Simmons",
            picNumber=1,
            quotes=["\*sarcastic tone\* I'm devastated by your increeeedibly tragic story, but the answer is still no.",
                    "Yeah, I don't give a shit about what's going on between you two."],
            filename="aspen"
        )
        self.characters.append(Aspen)

        # 15
        Astor = CharacterCard(
            name="Ms. Astor",
            picNumber=1,
            quotes=["Cutie? Any rumours you've heard about lately?"],
            filename="astor"
        )
        self.characters.append(Astor)

        # 16
        Avery = CharacterCard(
            name="Avery",
            picNumber=1,
            quotes=["Let me go, goddammit! I don't wanna play anymore",
                    "I'm not into whatever this is!",
                    "I'm keeping my eyes closed, hun. I only have eyes for my wife anyways..."],
            filename="avery"
        )
        self.characters.append(Avery)

        # 17 [SIDE GIRL HARASSER]
        Axel = CharacterCard(
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
            effects=Effects.SIDE_GIRL_KIDNAPPER
        )
        self.characters.append(Axel)

        # 18
        Baek = CharacterCard(
            name="Sister Baek",
            picNumber=1,
            quotes=["The powers granted through my beliefs are immeasurable.",
                    "He says... \"I love you, broseph\"..."],
            filename="baek",
            aliases="Leader of the Church of Unitology"
        )
        self.characters.append(Baek)

        # 19
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

        # 20
        Bartender = CharacterCard(
            name="Saloon Bartender",
            picNumber=1,
            quotes=["One whiskey, gotcha, comin' right up, partner!"],
            filename="bartender"
        )
        self.characters.append(Bartender)

        # 21
        Bellini = CharacterCard(
            name="Giuseppe Bellini",
            picNumber=1,
            quotes=["As much as I'm savoring this, I'm here to talk business.",
                    "Un pasto squisito, amico mio. Truly."],
            filename="bellini"
        )
        self.characters.append(Bellini)

        # 22
        Benja = CharacterCard(
            name="Benjamin Dawson",
            picNumber=2,
            quotes=["You should show some respect when you're talking to Mr. Bardot, you fucking worm.",
                    "Want me to smash your face in, cocksucker?", "Man, I feel like a celebrity!"],
            filename="benjamin",
            aliases="Benja"
        )
        self.characters.append(Benja)

        # 23 [SIDE GIRL]
        BlueFoxMaiden = CharacterCard(
            name="Blue Fox Maiden",
            picNumber=1,
            quotes=["We hope you're enjoying your stay.",
                    "We are the gift. Our task is to satisfy all of your desires."],
            filename="bluefoxmaiden",
            collection=Collections.SIDE_DISHES
        )
        self.characters.append(BlueFoxMaiden)

        # 24
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

        # 25
        Bundledore = CharacterCard(
            name="Balbus Bundledore",
            picNumber=2,
            quotes=["WELCOME, NEW PUPILS...",
                    "THAT FUCKING BITCH STOLE MY IDEA 40 YEARS AGO AND MADE IT HER OWN!"],
            filename="bundledore",
            aliases="Professor Bundledore, Headmaster of Warthogs School of Witchcraft and Wizardry."
        )
        self.characters.append(Bundledore)

        # 26
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

        # 27 [SIDE GIRL; HAREM SAVER]
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
                    "You shall be granted a special place in my court when I reign over Hyril'ar once more."],
            filename="calypso",
            effects=Effects.HAREM_SAVIOUR,
            aliases="Daughter of Raewyn, Princess of the Sy-tel-quessir, Princess of the Hyril'ar Realm, Carrie, Gaia, Caly, Warden of the Eternal Soul",
            collection=Collections.SIDE_DISHES
        )
        self.characters.append(Calypso)

        # 28
        Carolyn = CharacterCard(
            name="Carolyn",
            picNumber=3,
            quotes=["*meows*", "\*Purrs\*"],
            filename="carolyn",
            collection=Collections.CREATURES
        )
        self.characters.append(Carolyn)

        # 29
        Cassian = CharacterCard(
            name="Cassian",
            picNumber=1,
            quotes=["It's not every day you get to meet the 'Best tits on Instagram'."],
            filename="cassian",
            aliases="Mr. Handsy Man"
        )
        self.characters.append(Cassian)

        # 30 [HOMIE]
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
                    "Agh... Okay I'll be Leia"],
            filename="chang",
            aliases="Chang the Ladies' man, Chang the Socialite, Chang the Heist Meister",
            collection=Collections.THE_HOMIES
        )
        self.characters.append(Chang)

        # 31
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

        # 32 [HOMIE]
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

        # 33
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

        # 34
        Clonk = CharacterCard(
            name="Clonk",
            picNumber=2,
            quotes=["\*stare\*",
                    "W H O  K I L L E D  G I D E O N  C O O K ?"],
            filename="clonk"
        )
        self.characters.append(Clonk)

        # 35 [DISCORD CAMEOS ?]
        Con = CharacterCard(
            name="Con",
            picNumber=1,
            quotes=["I knew that fucking letter was a scam.",
                    "Oh no, an ambush! What am I gonna do... I'm so *scaaaaared*",
                    "You're in the presence of Eternum's future king!"],
            filename="con"
        )
        self.characters.append(Con)

        # 36 [DISCORD CAMEOS ?]
        Connor = CharacterCard(
            name="Professor Connor",
            picNumber=1,
            quotes=["Teaching is like my passion. And these students are my life.",
                    "Just don't tell the dean I'm smoking in here."],
            filename="connor"
        )
        self.characters.append(Connor)

        # 37
        Cook = CharacterCard(
            name="Elliot Cook",
            picNumber=1,
            quotes=["I... eh... I'm a taxi driver in New York.",
                    "I don't give a shit about you bunch of retards. I'm going out for a smoke."],
            filename="cook"
        )
        self.characters.append(Cook)

        # 38
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

        # 39 [HAREM; HOMIE SAVER]
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
                    "I like it when you get all \"romantico\""],
            filename="dalia",
            effects=Effects.HOMIE_SAVIOUR,
            aliases="Dalia the Explorer, Mars",
            collection=Collections.HAREM
        )
        self.characters.append(Dalia)

        # 40
        Dolores = CharacterCard(
            name="Dolores",
            picNumber=1,
            quotes=["Come on, don't be such a prude. We're just having fun.",
                    "What the fuck happened...?"],
            filename="dolores"
        )
        self.characters.append(Dolores)

        # 41
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

        # 42
        DuPont = CharacterCard(
            name="Dr. Du Pont",
            picNumber=1,
            quotes=["These programmers are terrible. I bet they hired immigrants.\nOr worse... women.",
                    "Incompetent..."],
            filename="dupont"
        )
        self.characters.append(DuPont)

        # 43
        Ed = CharacterCard(
            name="Ed",
            picNumber=1,
            quotes=["For fuck's sake, ain't there a single pirate left who's not retarded?!",
                    "Didn't you see the fucking sign you dingbats?",
                    "Yeah, I used to have one like that back when I still had flesh."],
            filename="ed"
        )
        self.characters.append(Ed)

        # 44 [DISCORD CAMEOS ?]
        Eggrik = CharacterCard(
            name="Anton Eggrik",
            picNumber=1,
            quotes=["I don't remember seeing you between the crowd when Jonah Hill was here last week!"],
            filename="eggrik"
        )
        self.characters.append(Eggrik)

        # 45
        Eulalie = CharacterCard(
            name="Eulalie",
            picNumber=1,
            quotes=["Good evening, and welcome to Gusteau's!",
                    "Gotta thank former President Stabb for the lowered drinking age.",
                    "If you need *anything* to make your wait shorter, please just let me know."],
            filename="eulalie"
        )
        self.characters.append(Eulalie)

        # 46 [SIDE GIRL]
        Eva = CharacterCard(
            name="Eva",
            picNumber=2,
            quotes=["Are you trying to make me blush? It might be working..."],
            filename="eva",
            aliases="Who?",
            collection=Collections.SIDE_DISHES
        )
        self.characters.append(Eva)

        # 47
        FakeCoyote = CharacterCard(
            name="'El Coyote'",
            picNumber=1,
            quotes=["I'll admit that I'm flattered, but I usually prefer to stay in the shadows.",
                    "Ah, so you've chosen to meet your end with honor!",
                    "You see, when you carry a name like mine, you occasionally need to deal with nuisances."],
            filename="fakecoyote"
        )
        self.characters.append(FakeCoyote)

        # 48
        Fangrend = CharacterCard(
            name="Fangrend",
            picNumber=2,
            quotes=["I have nothing to discuss with a human from outside our pack.",
                    "You're not even worthy to be here",
                    "Welcome to the pack."],
            filename="fangrend"
        )
        self.characters.append(Fangrend)

        # 49
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

        # 50 [PRAETORIANS ?]
        Four = CharacterCard(name="Four",
                             picNumber=1,
                             quotes=["..."],
                             filename="four",
                             collection=Collections.NONE)
        self.characters.append(Four)

        # 51
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

        # 52
        Garrington = CharacterCard(
            name="Cornelius Garrington",
            picNumber=1,
            quotes=["So cocky. You remind me of myself when I was young.",
                    "Ah, that must be my men telling me the job is done.\nSPOILER: ||it was not||"],
            filename="garringtonsr"
        )
        self.characters.append(Garrington)

        # 53
        Gemini = CharacterCard(
            name="Gemini",
            picNumber=1,
            quotes=["I am capable of seeing the future",
                    "I'm afraid I see... nothing. I'm sorry."],
            filename="gemini",
            aliases="The Blind Oracle"
        )
        self.characters.append(Gemini)

        # 54
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

        # 55 [CREATURE STOMPER]
        Golem = CharacterCard(
            name="Golem",
            picNumber=1,
            quotes=["*groans*"],
            filename="golem",
            effects=Effects.CREATURE_STOMPER
        )
        self.characters.append(Golem)

        # 56
        Harley = CharacterCard(
            name="Harley Jones",
            picNumber=1,
            quotes=["I'm glad to see people my age. These boomers are a total bore.",
                    "I kill people, I get paid, etcetera, etcetera, repeat, clink, cha-ching."],
            filename="harley",
            aliases="The best hitwoman in all of Eternum."
        )
        self.characters.append(Harley)

        # 57
        Haskel = CharacterCard(
            name="Haskel",
            picNumber=1,
            quotes=["There's no way on earth we're losing to two freshman rookies."],
            filename="haskel"
        )
        self.characters.append(Haskel)

        # 58
        Hasler = CharacterCard(
            name="Commander Hasler",
            picNumber=2,
            quotes=["Turn around reeeeeal slow.",
                    "Thank you for your cooperation.",
                    "And don't try to stop me. You, women, elders, or even children - I'll kill ANYONE who stays in my way."],
            filename="hasler",
            aliases="Commander Hasler, leader of the Second Brigade of the Galactic Union"
        )
        self.characters.append(Hasler)

        # 59
        Hassan = CharacterCard(
            name="Hassan Al-Rashid",
            picNumber=1,
            quotes=["You seem frightened, my young flowers of the desert... but I assure you, there's nothing to fear.",
                    "To the incubation room."],
            filename="hassan",
            aliases="the Sultan of the Valley of Kings"
        )
        self.characters.append(Hassan)

        # 60
        Hugo = CharacterCard(
            name="Hugo Hernandez",
            picNumber=1,
            quotes=["Victor, pedazo de cabrón!",
                    "You need to spend more time with us! You've lost your accent!",
                    "I guess you must be Luna's boyfriend.",
                    "OH SHIT, the chilaquiles",
                    "You see, I'm running a cartel and a human trafficking ring."],
            filename="hugo",
            aliases="Luna's uncle"
        )
        self.characters.append(Hugo)

        # 61 [SIDE GIRL]
        Idriel = CharacterCard(
            name="Idriel",
            picNumber=5,
            quotes=["Are you enjoying your experience in Eternum so far?",
                    "Maybe you're not asking the right questions..."],
            filename="idriel",
            aliases="The Eternum Lady, Eternum's AI",
            collection=Collections.SIDE_DISHES
        )
        self.characters.append(Idriel)

        # 62 [PETS]
        Igor = CharacterCard(
            name="Igor",
            picNumber=1,
            quotes=["Mmmm, Igor is hungry for the only thing on the menu -  one nice, biiiiig cock!",
                    "What's up with this trend among women lately in not having penises?"],
            filename="igor",
            collection=Collections.CREATURES
        )
        self.characters.append(Igor)

        # 63
        Iliescu = CharacterCard(
            name="Lazarus Iliescu",
            picNumber=1,
            quotes=["You may go now, carrying my eternal gratitude.",
                    "Ah, your radiance shines even brighter in the light of day."],
            filename="iliescu",
            aliases="Lord Iliescu, sovereign of Stravenovia"
        )
        self.characters.append(Iliescu)

        # 64 [DISCORD CAMEOS ?]
        Jasticus = CharacterCard(
            name="Jasticus the Decapitator",
            picNumber=1,
            quotes=["They won't be able to scrub out your blood from the Rotunda floors after I'm done with you!",
                    "COME HERE, BOY!",
                    "Well, thanks again for not killing me, buddy."],
            filename="jasticus"
        )
        self.characters.append(Jasticus)

        # 65 [HOMIE]
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

        # 66 [VN CAMEOS ?]
        Judith = CharacterCard(
            name="Judith",
            picNumber=1,
            quotes=["Welcome to the University of Kredon's Annual Halloween Party."],
            filename="judith"
        )
        self.characters.append(Judith)

        # 67
        Junkie = CharacterCard(
            name="Junkie",
            picNumber=1,
            quotes=["Hey bro, you got a smoke...?",
                    "Whoa, look at this... this lil' bitch thinks he's tough.",
                    "You're fuckin' dead, you hear me?!"],
            filename="junkie1"
        )
        self.characters.append(Junkie)

        # 68
        Junkie2 = CharacterCard(
            name="JJ",
            picNumber=1,
            quotes=["Are you fucking nuts?!!"],
            filename="junkie2"
        )
        self.characters.append(Junkie2)

        # 69 [DISCORD CAMEOS ?]
        Kai = CharacterCard(
            name="Kai",
            picNumber=2,
            quotes=["Welcome to your *reawakening*."],
            filename="kai",
            aliases="Kai from Kainan Engineering"
        )
        self.characters.append(Kai)

        # 70
        Keating = CharacterCard(
            name="Professor Keating",
            picNumber=2,
            quotes=["You can do the p-project another day then. N-no problem. F-family comes first.",
                    "Didn't you hear me?! Class is dismissed!"],
            filename="keating"
        )
        self.characters.append(Keating)

        # 71 [PETS]
        Kermit = CharacterCard(
            name="Kermit",
            picNumber=1,
            quotes=["\*Croaks\*"],
            filename="kermit",
            aliases="lil' Kermie",
            collection=Collections.CREATURES
        )
        self.characters.append(Kermit)

        # 72
        Kimberly = CharacterCard(
            name="Kimberly",
            picNumber=1,
            quotes=["I knew that one! You need to consult with us before answering!"],
            filename="kimberly"
        )
        self.characters.append(Kimberly)

        # 73
        Kitty = CharacterCard(
            name="Kitty",
            picNumber=1,
            quotes=["Normally an item like this would have a high asking price, but since I owe Annie a favour... Consider yourself lucky."],
            filename="kitty",
            aliases="Kitytu"
        )
        self.characters.append(Kitty)

        # 74
        Lily = CharacterCard(
            name="Lily",
            picNumber=1,
            quotes=["You need an assistant! And I offer myself!"],
            filename="lily"
        )
        self.characters.append(Lily)

        # 75
        Linus = CharacterCard(
            name="Alastor Linus",
            picNumber=1,
            quotes=["For this project, we reached out to Eternum's players to figure out the number one question on everyone's mind... DOES IDRIEL HAVE A PUSSY?!"],
            filename="linus"
        )
        self.characters.append(Linus)

        # 76
        Lorelei = CharacterCard(
            name="Lorelei Thornvale",
            picNumber=1,
            quotes=["You can... speak so fluently?"],
            filename="lorelei"
        )
        self.characters.append(Lorelei)

        # 77 [DISCORD CAMEOS ?]
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

        # 78
        Lucinda = CharacterCard(
            name="Lucinda Garcia",
            picNumber=1,
            quotes=["Nice to finally meet you!", "Ohh, aren't you a polite and handsome young boy?",
                    "\*Whispering\* he's so good-looking, isn't he?"],
            filename="lucinda"
        )
        self.characters.append(Lucinda)

        # 79 [HAREM]
        Luna = CharacterCard(
            name="Luna Hernandez",
            picNumber=16,
            quotes=["Thank you for everything you said. It was... sweet.",
                    "I'm sorry. I didn't mean to scare you.",
                    "I... like the feel of silk and velvet, that's all.",
                    "At 1 month and 14 days post-mortem... only the bones remain.",
                    "At least he doesn't call me a weirdo like everyone else.",
                    "Don't look into the room on the right. My father's corpse is still there.",
                    "You have a very... g-good body.",
                    "Gracias por venir. Me gusta mucho pasar tiempo contigo.",
                    "I'm sure my family wouldn't mind. They really liked you.",
                    "I... I feel safe when I'm with you."],
            filename="luna",
            aliases="Ganymede, Lunita, Luny",
            collection=Collections.HAREM
        )
        self.characters.append(Luna)

        # 80
        Lysa = CharacterCard(
            name="Lysandra Iliescu",
            picNumber=1,
            quotes=["Aaaaahhh... yeeeesss... I could smell them outside the crypt...",
                    "Y-You would make an exceptional vampire, young man.",
                    "Bravo! That was absolutely enchanting!"],
            filename="lysa",
            aliases="Lady Iliescu"
        )
        self.characters.append(Lysa)

        # 81 [SIDE GIRL]
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

        # 82
        Mandrake = CharacterCard(
            name="Dona Mandrake",
            picNumber=1,
            quotes=["Welcome to Potions!",
                    "My classroom, my rules"],
            filename="mandrake",
            aliases="Professor Mandrake"
        )
        self.characters.append(Mandrake)

        # 83 [PETS]
        Maurice1 = CharacterCard(
            name="Maurice (cat)",
            picNumber=1,
            quotes=["*meows*"],
            filename="mauricec",
            collection=Collections.CREATURES
        )
        self.characters.append(Maurice1)

        # 84 [PETS]
        Maurice2 = CharacterCard(
            name="Maurice (goat)",
            picNumber=1,
            quotes=["*bleats*",
                    "Tired of cleaning up after him? He turn into many meals\nand delicious broth!"],
            filename="mauriceg",
            collection=Collections.CREATURES
        )
        self.characters.append(Maurice2)

        # 85 [PETS]
        Maurice3 = CharacterCard(
            name="Maurice (toucan)",
            picNumber=1,
            quotes=["Stockholm", "Maurice very intelligent! He know all the answers!"],
            filename="mauricet",
            collection=Collections.CREATURES
        )
        self.characters.append(Maurice3)

        # 86 [HOMIES ?]
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

        # 87
        Mercer = CharacterCard(
            name="Irina Mercer",
            picNumber=1,
            quotes=["Let's see what people call me in 50 years...",
                    "Little sacrifices are sometimes necessary for the sake of progress, don't you think?"],
            filename="mercer",
            aliases="Doctor Mercer"
        )
        self.characters.append(Mercer)

        # 88
        Mermaid = CharacterCard(
            name="Mermaid",
            picNumber=1,
            quotes=["Boo!", "I can do a lot of magical things, Orion... especially to young handsome men like you."],
            filename="mermaid"
        )
        self.characters.append(Mermaid)

        # 89 [HOMIE]
        Micaela = CharacterCard(name="Micaela Garcia",
                                picNumber=4,
                                quotes=["I know I can have a rather intimidating appearance at first.",
                                        "You've improved a lot over the last year. I'm impressed!"],
                                filename="micaela",
                                collection=Collections.THE_HOMIES)
        self.characters.append(Micaela)

        # 90
        Millie = CharacterCard(
            name="Millie",
            picNumber=2,
            quotes=["You can do it all here at PUMP IT!"],
            filename="millie"
        )
        self.characters.append(Millie)

        # 91 [VN CAMEOS ?]
        Moon = CharacterCard(
            name="Moon",
            picNumber=1,
            quotes=["I have to go. See you Monday."],
            filename="moon"
        )
        self.characters.append(Moon)

        # 92
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

        # 93
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

        # 94 [DISCORD CAMEOS ?]
        Mos = CharacterCard(
            name="Mr. Mos",
            picNumber=1,
            quotes=["No self-respecting man should go around without a good suit."],
            filename="mos"
        )
        self.characters.append(Mos)

        # 95 [HAREM]
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
                    "Ah, young love... my little princesses grew up too fast!"],
            filename="nancy",
            aliases="Nan, Empress of the Western Roman Empire, Saturn",
            collection=Collections.HAREM
        )
        self.characters.append(Nancy)

        # 96
        Nikolay = CharacterCard(
            name="Nikolay",
            picNumber=1,
            quotes=["Границы России нигде не заканчиваются."],
            filename="nikolay"
        )
        self.characters.append(Nikolay)

        # 97 [HOMIES]
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

        # 98 [HAREM]
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
                    "Any last comments before getting down to business?"],
            filename="nova",
            aliases="Delilah Warren, Mercury",
            collection=Collections.HAREM
        )
        self.characters.append(Nova)

        # 99 [HOMIE; SIDE GIRL SAVER]
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
                    "(Hmm, these barrels are quite big. I could probably squeeze myself into one.)"],
            filename="orion",
            effects=Effects.SIDE_GIRL_SAVIOUR,
            aliases="MC, Orion Holmes, Orion the Merciful, Jupiter",
            collection=Collections.THE_HOMIES
        )
        self.characters.append(Orion)

        # 100
        Owler = CharacterCard(
            name="Helga Owler",
            picNumber=1,
            quotes=["Oh god! I didn't hear you coming... How embarrassing!"],
            filename="owler",
            aliases="Professor Owler"
        )
        self.characters.append(Owler)

        # 101 [PETS]
        Pancho = CharacterCard(
            name="Pancho",
            picNumber=1,
            quotes=["\*clucks\*"],
            filename="pancho",
            aliases="Hugo's Chicken",
            collection=Collections.CREATURES
        )
        self.characters.append(Pancho)

        # 102 [HAREM]
        Penny = CharacterCard(
            name="Penelope Carter",
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
                    "There are tons of hot guys hitting on me literally EVERY DAY."],
            filename="penny",
            aliases="Penny, miss_penny, best tits on instagram, Venus, Penelope Paige Carter",
            collection=Collections.HAREM
        )
        self.characters.append(Penny)

        # 103
        Phil = CharacterCard(
            name="Phil",
            picNumber=1,
            quotes=["\*Swallows\*"],
            filename="phil",
            aliases="the devourer of men, the Abyssal Terror"
        )
        self.characters.append(Phil)

        # 104
        Philippe = CharacterCard(
            name="Philippe",
            picNumber=1,
            quotes=["How can you shine so much, sweetie? I'm going to start\nwearing my sunglasses around you!",
                    "Don't \"Philippe\" me, darling!",
                    "Don't frown so much or you'll get wrinkles on that pretty face of yours!"],
            filename="philippe"
        )
        self.characters.append(Philippe)

        # 106
        Piaget = CharacterCard(
            name="Anna Piaget",
            picNumber=1,
            quotes=["I was honestly expecting this to be a bit more challenging."],
            filename="piaget",
            aliases=""
        )
        self.characters.append(Piaget)

        # 107 [PRAETORIANS ?]
        Praetorian = CharacterCard(
            name="Praetorian 1",
            picNumber=1,
            quotes=["Put your hands up and back away from the girl.",
                    "You've committed crimes against Eternum's\nGeneral Code of Ethics."],
            filename="praetorian1"
        )
        self.characters.append(Praetorian)

        # 108 [PRAETORIANS ?]
        Praetorian2 = CharacterCard(
            name="Praetorian 2",
            picNumber=1,
            quotes=["Resisting will only make things more painful for you.",
                    "Surrender now. This is your last warning."],
            filename="praetorian2"
        )
        self.characters.append(Praetorian2)

        # 109 [PRAETORIANS ?]
        Praetorian3 = CharacterCard(
            name="Praetorian 3",
            picNumber=1,
            quotes=["We're taking all necessary precautions to ensure\nthe security and safety of the players attending tonight."],
            filename="praetorian3"
        )
        self.characters.append(Praetorian3)

        # 110
        Priscilla = CharacterCard(
            name="Priscilla Bardot",
            picNumber=1,
            quotes=["I guess you can get away with whatever you want,\nif you have the finest lawyers money can buy."],
            filename="priscilla"
        )
        self.characters.append(Priscilla)

        # 111 [PET SAVER]
        Pyri = CharacterCard(
            name="Pyramid Head",
            picNumber=1,
            quotes=["**The time of judgement has come.**"],
            filename="pyramid_head",
            effects=Effects.CREATURE_SAVIOUR,
            aliases="Pyri"
        )
        self.characters.append(Pyri)

        # 112 [HOMIE]
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

        # 113 [DISCORD CAMEOS ?]
        Reddss = CharacterCard(
            name="Blackheart Reddss",
            picNumber=1,
            quotes=["Just one D brings terrible luck.",
                    "Dragging the D but not the S brings even worse luck!",
                    "I'll be in the kitchen whipping up another delectable cake."],
            filename="reddss"
        )
        self.characters.append(Reddss)

        # 114 [SIDE GIRL]
        RedFoxMaiden = CharacterCard(
            name="Red Fox Maiden",
            picNumber=1,
            quotes=["We hope you're enjoying your stay.",
                    "We are the gift. Our task is to satisfy all of your desires."],
            filename="redfoxmaiden",
            collection=Collections.SIDE_DISHES
        )
        self.characters.append(RedFoxMaiden)

        # 115
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

        # 116
        Ruiz = CharacterCard(
            name="Clarence Ruiz",
            picNumber=1,
            quotes=["What the hell...",
                    "I'm afraid you're not leaving this building on your own, son."],
            filename="ruiz"
        )
        self.characters.append(Ruiz)

        # 117
        Ruth = CharacterCard(
            name="Ruth",
            picNumber=1,
            quotes=["Well, if I knew a handsome fellow like you was waiting for me, I'd have hurried out sooner!"],
            filename="ruth",
            aliases="Clerk"
        )
        self.characters.append(Ruth)

        # 118
        Samir = CharacterCard(
            name="Samir",
            picNumber=2,
            quotes=["All we want... is to reclaim what’s rightfully ours.",
                    "The Ishari are always on the lookout for valiant players to join our cause."],
            filename="samir",
            aliases="Leader of the Ishari"
        )
        self.characters.append(Samir)

        # 119
        Sandra = CharacterCard(
            name="Sandra Johnson",
            picNumber=1,
            quotes=["If it keeps raining this hard, I might need a ride on Noah's ark..."],
            filename="sandra",
            aliases="Nova's mom"
        )
        self.characters.append(Sandra)

        # 120
        Scarlet = CharacterCard(
            name="Red Scarlet",
            picNumber=1,
            quotes=["Hi, handsome... I'm Red Scarlet.", "I give really, *really* good blowjobs."],
            filename="scarlet"
        )
        self.characters.append(Scarlet)

        # 121
        Sheriff = CharacterCard(
            name="Sheriff of Blackridge",
            picNumber=1,
            quotes=["Lookey here at my shiny precious and read, boy.",
                    "They say crime doesn't pay but what they don't tell ya ish that THE LAW DON'T EITHER!"],
            filename="sheriff"
        )
        self.characters.append(Sheriff)

        # 122
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

        # 123
        StoreClerk = CharacterCard(
            name="General Store Clerk",
            picNumber=1,
            quotes=["You're offending my Wamapoke roots!",
                    "I can already feel the warmth of my ancestors smiling down on us."],
            filename="storeclerk",
            aliases="Brendan from Queens"
        )
        self.characters.append(StoreClerk)

        # 124
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

        # 125
        Tatiana = CharacterCard(
            name="Tatiana",
            picNumber=1,
            quotes=["He called us **things**, sister",
                    "Enough pleasantries."],
            filename="tatiana"
        )
        self.characters.append(Tatiana)

        # 126 [HAREM KILLER]
        Thanatos = CharacterCard(
            name="Thanatos",
            picNumber=8,
            quotes=["I must say, you've done more damage here than most.",
                    "**The strong... prevail. The weak... die.**",
                    "You are powerless. Inferior. Defective. Weak.", "No one can escape from me.",
                    "Where is the Gem of Doom?", "You're no longer useful to me. Open the gates.",
                    "All I am surrounded by... is fear. **And dead men.**",
                    "I can respect the resolve of a warrior."],
            filename="thanatos",
            effects=Effects.HAREM_KILLER,
            aliases="The best Eternum player, Wyatt R. Pitman"
        )
        self.characters.append(Thanatos)

        # 127
        TicketGuy = CharacterCard(
            name="Tickets Seller",
            picNumber=1,
            quotes=["Do you have a ticket to watch the upcoming Munus?"],
            filename="ticketmaster"
        )
        self.characters.append(TicketGuy)

        # 127
        TonyMack = CharacterCard(
            name="Tony Mack",
            picNumber=1,
            quotes=["Thank you for your help, citizen."],
            filename="tonymack",
            aliases="Blackridge Sheriff's Deputy"
        )
        self.characters.append(TonyMack)

        # 128 [DISCORD CAMEOS]
        Tissle = CharacterCard(
            name="Tissle",
            picNumber=1,
            quotes=["*You guys are such wimps. Let the alpha deal with it.*",
                    "Oh, COME ON, guys! I don't smell anymore!"],
            filename="tissle",
            aliases="Tis"
        )
        self.characters.append(Tissle)

        # 129 [HOMIE KILLER]
        Troll = CharacterCard(
            name="Troll",
            picNumber=1,
            quotes=["*groans*"],
            filename="troll",
            effects=Effects.HOMIE_KILLER
        )
        self.characters.append(Troll)

        # 130 [PRAETORIANS ?]
        Twelve = CharacterCard(
            name="Twelve",
            picNumber=1,
            quotes=["..."],
            filename="twelve"
        )
        self.characters.append(Twelve)

        # 131
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

        # 132
        Vasil = CharacterCard(
            name="Vasil",
            picNumber=1,
            quotes=["Bring the egg and I'll open the door, I promise..."],
            filename="vasil"
        )
        self.characters.append(Vasil)

        # 133 [HOMIE]
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

        # 134 [DISCORD CAMEOS ???]
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

        # 135 [SIDE GIRL]
        Wenlin = CharacterCard(
            name="Wenlin",
            picNumber=4,
            quotes=["I was starting to think this server only had stingy, mean people!",
                    "Business first, pleasure later!"],
            filename="wenlin",
            collection=Collections.SIDE_DISHES
        )
        self.characters.append(Wenlin)

        # 136
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
            filename="william"
        )
        self.characters.append(William)

        # 137
        WyattsMom = CharacterCard(
            name="Wyatt's Mother",
            picNumber=2,
            quotes=["If you try to trick me, I'm gonna shoot you both! I've got nothing to lose!",
                    "Please, I'd like you to leave now."],
            filename="wyattsmom",
            aliases="Old Lady, Mrs. Pitman"
        )
        self.characters.append(WyattsMom)

        # 138
        Xeno = CharacterCard(
            name="Xenomorph",
            picNumber=2,
            quotes=["\*Squeals\*"],
            filename="xenomorph"
        )
        self.characters.append(Xeno)

        # 139
        Zahra = CharacterCard(
            name="Zahra Al-Nabi",
            picNumber=1,
            quotes=["Wait... She's... still pure.",
                    "Hey, the first time is always the worst."],
            filename="zahra",
            aliases="The Citadel's Oracle"
        )
        self.characters.append(Zahra)

        # 140
        Zap = CharacterCard(
            name="Zap",
            picNumber=2,
            quotes=["ZAP!"],
            filename="zap"
        )
        self.characters.append(Zap)

        # 141
        Zippy = CharacterCard(
            name="Zippy",
            picNumber=1,
            quotes=["I'm a magic fox, of course!",
                    "What a klumpy-dumpy!"],
            filename="zippy"
        )
        self.characters.append(Zippy)
