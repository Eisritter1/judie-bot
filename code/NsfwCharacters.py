from CharacterCard import NsfwCharacterCard
from os import listdir
from os.path import isfile, join

class NsfwCharacters:
    def __init__(self):
        self.list = []
        self.oialt = []
        self.eternum = []
        self.dict = {
                None: self.list,
                "oialt": self.oialt,
                "eternum": self.eternum,
            }
        self.setup()
        self.countUp()

    def setup(self):
        Aiko = NsfwCharacterCard(name="Aiko",
                                 picNumber=3,
                                 quotes=["Don't just stand there, you're going to catch a cold!",
                                         "At least we'll have a funny anecdote to tell!"],
                                 footers=["Why is he still covering my mouth?",
                                          "Man, if I die this sunday, this is what I hope heaven looks like."],
                                 game="OiaLt")
        self.list.append(Aiko)
        self.oialt.append(Aiko)
        self.dict["aiko"] = Aiko

        Carla = NsfwCharacterCard(name="Carla",
                                  picNumber=2,
                                  quotes=["Well, am I going to take a bath alone or..."],
                                  footers=["haha stop it, we're not gonna fuck in the dressing room. We're not animals..."],
                                  game="OiaLt")
        self.list.append(Carla)
        self.oialt.append(Carla)
        self.dict["carla"] = Carla

        Iris = NsfwCharacterCard(name="Iris",
                                 picNumber=5,
                                 quotes=["Come on babe! Don't be shy! This is fucking great!",
                                         "Do you know what would be absolutely crazy and impulsive right now?"],
                                 footers=["*hint: not stopping at a BJ!*"],
                                 game="OiaLt")
        self.oialt.append(Iris)
        self.list.append(Iris)
        self.dict["iris"] = Iris

        Jasmine = NsfwCharacterCard(name="Jasmine",
                                    picNumber=4,
                                    quotes=["You fucking prick... I don't know why, but you really turn me on...",
                                            "You're precious and you're smokin' hot, it had to happen sooner or later..."],
                                    footers=["Well, your ass looks good in these, I'll give you that.",
                                             "I'll have to stand aside, [...] let's say that MC really took it out of me..."],
                                    game="OiaLt")
        self.oialt.append(Jasmine)
        self.list.append(Jasmine)
        self.dict["jasmine"] = Jasmine
        self.dict["jas"] = Jasmine

        Judie = NsfwCharacterCard(name="Judie",
                                  picNumber=6,
                                  quotes=["This was such a good idea, sis!",
                                          "Come on babe! Don't be shy! This is fucking great!",
                                          "I don't know if I can take it step-bro!", "Hmm, this turns me on so much..."],
                                  footers=["You're setting the bar so high though...", "Duh, we had sex in Japan too!",
                                           "I wanna know what you taste like..."],
                                  game="OiaLt")
        self.oialt.append(Judie)
        self.list.append(Judie)
        self.dict["judie"] = Judie

        Lauren = NsfwCharacterCard(name="Lauren",
                                   picNumber=7,
                                   quotes=["You're precious and you're smokin' hot, it had to happen sooner or later...",
                                           "At least we'll have a funny anecdote to tell!",
                                           "This was such a good idea, sis!",
                                           "These are the ladies' baths, you shouldn't be here...",
                                           "Are you ready for the best massage your back will ever have?"],
                                   footers=["Man, if I die this sunday, this is what I hope heaven looks like.",
                                            "I'll have to stand aside, [...] let's say that MC really took it out of me...",
                                            "You're setting the bar so high though...",
                                            "Good! Then we can chill! See how easy that was?",
                                            "I see you've made yourself comfortable"],
                                   game="OiaLt")
        self.oialt.append(Lauren)
        self.list.append(Lauren)
        self.dict["lauren"] = Lauren

        Rebecca = NsfwCharacterCard(name="Rebecca",
                                    picNumber=1,
                                    quotes=["You fill me up completely"],
                                    footers=["I'm not a respectable teacher now, am I?"],
                                    game="OiaLt")
        self.oialt.append(Rebecca)
        self.list.append(Rebecca)
        self.dict["rebecca"] = Rebecca
        self.dict["reb"] = Rebecca

        Alex = NsfwCharacterCard(name="Alex",
                                 picNumber=9,
                                 quotes=["Oh you didn't know? Orion and I are fucking. Like rabbits.",
                                         "Now my skin can finally breathe.",
                                         "Do you wanna give Orion a show he'll never forget...?"],
                                 footers=["You wouldn't want my daddy to hear us, would you...?",
                                          "Did you even listen to a word I just said? Because it looked like you were "
                                          "staring at my tits the whole time.",
                                          "I'm just a sweet and innocent princess, I can't possibly imagine what you have "
                                          "in that dirty mind of yours.",
                                          "Don't act all shy now!"],
                                 game="Eternum")
        self.list.append(Alex)
        self.eternum.append(Alex)
        self.dict["alex"] = Alex
        self.dict["alexandra"] = Alex

        Annie = NsfwCharacterCard(name="Annie",
                                  picNumber=11,
                                  quotes=["\"Like\" it? It was the best experience of my life!"],
                                  footers=["My knight in shining armor..."],
                                  game="Eternum")
        self.list.append(Annie)
        self.eternum.append(Annie)
        self.dict["annie"] = Annie

        Calypso = NsfwCharacterCard(name="Calypso",
                                    picNumber=1,
                                    quotes=[
                                        "You look... \"hot as fuck\" as well.",
                                        "\*Whispers\* It is... better than I anticipated..."
                                    ],
                                    footers=["Holy Mother of Turska!", "\*Whispers\* What kind of curse is this...?"],
                                    game="Eternum")
        self.list.append(Calypso)
        self.eternum.append(Calypso)
        self.dict["calypso"] = Calypso
        self.dict["caly"] = Calypso

        Dalia = NsfwCharacterCard(name="Dalia",
                                  picNumber=9,
                                  quotes=["\*Panting\* T-Too much... d-dick... N-Need... oxygen!",
                                          "I don't know how, but somehow... it's always Orion who ends up winning."],
                                  footers=["*cum in my mouth.*",
                                           "Y-You're both nuts..."],
                                  game="Eternum")
        self.list.append(Dalia)
        self.eternum.append(Dalia)
        self.dict["dalia"] = Dalia
        self.dict["dal"] = Dalia

        EvaTroll = NsfwCharacterCard(name="SnoopWho",
                                     picNumber=1,
                                     quotes=["Eva who?"],
                                     footers=["side dish?"],
                                     game="Eternum")

        EvaSerious = NsfwCharacterCard(name="Eva",
                                       picNumber=1,
                                       quotes=[
                                           "I do find Mr. Orion very intriguing... and I'd love to learn more about him..."],
                                       footers=["Let me help you relax and ease your mind..."],
                                       game="Eternum")
        self.list.append(EvaSerious)
        self.eternum.append(EvaSerious)

        Eva = []
        Eva.append(EvaTroll)
        Eva.append(EvaSerious)
        self.dict["eva"] = Eva

        FoxMaidens = NsfwCharacterCard(name="FoxMaidens",
                                       picNumber=1,
                                       quotes=[""],
                                       footers=[""],
                                       game="Eternum")
        self.list.append(FoxMaidens)
        self.eternum.append(FoxMaidens)
        self.dict["foxmaidens"] = FoxMaidens

        Lorelei = NsfwCharacterCard(
            name="Lorelei",
            picNumber=0,
            quotes=[
                "I-I merely thought that a display of visually stimulating... a-activity might help the Princess.", 
                "H-Heavens above... I cannot... breathe properly when it is in my mouth..."
            ],
            footers=[
                "I'm curious from a purely academically perspective, naturally.", 
                "Both the Ancients and the Law will look the other way tonight.",
                "For you, Your Grace... anything..."
            ],
            game="Eternum"
        )
        self.list.append(Lorelei)
        self.eternum.append(Lorelei)
        self.dict["lorelei"] = Lorelei

        Luna = NsfwCharacterCard(name="Luna",
                                 picNumber=5,
                                 quotes=["Thank you for everything you said. It was... sweet.",
                                         "If you really don't mind... I won't say no. You've convinced me!",
                                         "I want you to keep massaging me",
                                         "OH M-MY GOD. Y-You're inside",
                                         "T-THat is... q-quite a sensation...",
                                         "G-God, w-what are you doing to meeee...?",
                                         "Por el amor de dios, no pares...",
                                         "\*T-That was the most intense thirty seconds of my whole life...\*"],
                                 footers=["It's amazing!",
                                          "I think that's a treatment plan I can follow",
                                          "I love the feeling of your hands.",
                                          "I-I want you to touch me.",
                                          "**F-FUCK**",
                                          "Make me yours..."],
                                 game="Eternum")
        self.list.append(Luna)
        self.eternum.append(Luna)
        self.dict["luna"] = Luna
        self.dict["luny"] = Luna

        Maat = NsfwCharacterCard(name="Maat",
                                 picNumber=2,
                                 quotes=["I want you to destroy me..."],
                                 footers=["This spectacle is pleasing the pharaohs!"],
                                 game="Eternum")
        self.list.append(Maat)
        self.eternum.append(Maat)
        self.dict["maat"] = Maat

        Nancy = NsfwCharacterCard(name="Nancy",
                                  picNumber=7,
                                  quotes=["Christ!! I'm looking like some inexperienced teenager here...",
                                          "I want you to fuck me, Orion. Hard. And filthy.",
                                          "Let your mommy take care of you. You've been such a good boy, after all...",
                                          "Jesus... What do they feed you boys nowadays?",
                                          "You had no right to turn my life upside down like this."
                                          ],
                                  footers=["Man, blue-balled by fucking war.",
                                           "Any special requests...?",
                                           "I guess I'll have to keep training...",
                                           "T-that would be quite the spectacle, eh...?",
                                           "M-make your mommy cum!"],
                                  game="Eternum")
        self.list.append(Nancy)
        self.eternum.append(Nancy)
        self.dict["nancy"] = Nancy

        Nova = NsfwCharacterCard(name="Nova",
                                 picNumber=7,
                                 quotes=["Have you ever had sex with a girl? Is she still alive?",
                                         "It's like something is making me just want to... tear off my clothes and go to town on myself...",
                                         "OKAY, FINE. Do you want me to touch myself? FINE, I'll do it.",
                                         "D-don't tell my mom what I'm about to do.",
                                         "That pose... doesn't let me... go deep enough."],
                                 footers=["Satisfying the wishes of a nympho freak seems like a small price to pay.",
                                          "Am I... broken, Orion?",
                                          "I feel... f-f-filled."],
                                 game="Eternum")
        self.list.append(Nova)
        self.eternum.append(Nova)
        self.dict["nova"] = Nova

        Orion = NsfwCharacterCard(name="Orion",
                                  picNumber=2,
                                  quotes=[
                                      "I don't want to lose the challenge just because you can't curb your irrepressible desire to kiss me.",
                                      "Isn't it funny how we always end up stuck in the most bizarre situations?",
                                      "You better have a spare change of sheets, girl, because we're gonna leave a big fucking mess..."],
                                  footers=["Admit you enjoy seeing me stroking my cock...",
                                           "You can touch me whenever you want!"],
                                  game="Eternum")
        self.list.append(Orion)
        self.dict["orion"] = Orion
        self.dict["main"] = Orion
        self.dict["mc"] = Orion

        Penny = NsfwCharacterCard(name="Penny",
                                  picNumber=5,
                                  quotes=["How should we do it?",
                                          "My fucking god, you're hung like a fucking horse. That cock is a weapon!",
                                          "I'm *so* very sorry for flaunting my lewd body in front of you. I had no idea it would cause you so much stress...",
                                          "Okay, superstud... you've convinced me.",
                                          "In the interest of science... do you wanna feel for yourself? You've caught me in a pretty good mood.",
                                          "Orion Junior over there was constantly poking me down here, in case you didn't notice.",
                                          "How about I give you a little memory that'll truly be unforgettable...",
                                          "I rejected all their requests, but here I am doing it for free, for some high school kid with a fat dick.",
                                          "Mom said no snacking before dinner..."],
                                  footers=["Isn 't there anything I can do for you to forgive me?",
                                           "Treat yourself...",
                                           "You're a filthy little degenerate.",
                                           "How'd you convince me to get you off in my archenemy's room?",
                                           "Like what you see...?"],
                                  game="Eternum")
        self.list.append(Penny)
        self.eternum.append(Penny)
        self.dict["penny"] = Penny
        self.dict["penelope"] = Penny

        Wenlin = NsfwCharacterCard(name="Wenlin",
                                   picNumber=1,
                                   quotes=[""],
                                   footers=[""],
                                   game="Eternum")
        self.list.append(Wenlin)
        self.eternum.append(Wenlin)
        self.dict["wenlin"] = Wenlin

    def countUp(self):
        for card in self.list:
            filename = card.name.lower()
            path = f'./NsfwPics/{card.game}/{filename}'
            counter = 0
            for file in listdir(path):
                if isfile(join(path, file)):
                    counter += 1

            card.picNumber = counter
