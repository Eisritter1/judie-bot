import discord
from discord import Embed, File
from discord.ext import commands, tasks
from discord.ext.commands import cooldown, BucketType
import random
import os
from Utilities import HelperClass
from CharacterCard import NsfwCharacterCard
import time


async def createAndSendEmbed(card: NsfwCharacterCard, number: int, ctx):
    """
    Creates and sends an embed using information from the provided NsfwCharacterCard.
    ----------------------------------------------------------------------------------
    Parameters:
        - card : NsfwCharacterCard - the card of the character to display,
        - number : int - the image number to choose for the character,
        - ctx : discord.ext.Context - discord-provided context to the command prompt.
    """
    color = HelperClass.orange
    if card.game == "Eternum":
        color = HelperClass.eternumBlue

    embed = discord.Embed(title=card.name, description=random.choice(card.quotes), colour=color)
    embed.set_footer(text=random.choice(card.footers))

    filename = card.name.lower()
    folder_path = f'./NsfwPics/{card.game}/{filename}'

    file_path = None
    file_extension = None
    for ext in ['png', 'jpg', 'jpeg', 'gif', 'webp']:
        potential_path = f'{folder_path}/{filename}_{number}.{ext}'
        if os.path.exists(potential_path):
            file_path = potential_path
            file_extension = ext
            break

    if not file_path:
        print(f"Error: No valid file found for {filename}_{number} in {folder_path}.")
        return

    image = discord.File(file_path, filename=f"nsfw.{file_extension}")
    embed.set_image(url=f"attachment://nsfw.{file_extension}")

    try:
        await ctx.send(file=image, embed=embed)
    except Exception as e:
        print(f"Failed to send image {filename}_{number}: {e}")


class Nsfw(commands.Cog):
    """
    Judie's NSFW Magazine Cog.
    ---------------------------------
    Members:
        - nsfw(discord.ext.Context, any) - displays a given or random charater's lewd scenes.
    """
    def __init__(self, client):
        self.client = client

    # Quotes for all OiaLt characters! - put in extra file like egf characters?
    Aiko = NsfwCharacterCard(name="Aiko",
                             picNumber=3,
                             quotes=["Don't just stand there, you're going to catch a cold!",
                                     "At least we'll have a funny anecdote to tell!"],
                             footers=["Why is he still covering my mouth?",
                                      "Man, if I die this sunday, this is what I hope heaven looks like."],
                             game="OiaLt")

    Carla = NsfwCharacterCard(name="Carla",
                              picNumber=2,
                              quotes=["Well, am I going to take a bath alone or..."],
                              footers=["haha stop it, we're not gonna fuck in the dressing room. We're not animals..."],
                              game="OiaLt")

    Iris = NsfwCharacterCard(name="Iris",
                             picNumber=5,
                             quotes=["Come on babe! Don't be shy! This is fucking great!",
                                     "Do you know what would be absolutely crazy and impulsive right now?"],
                             footers=["*hint: not stopping at a BJ!*"],
                             game="OiaLt")

    Jasmine = NsfwCharacterCard(name="Jasmine",
                                picNumber=4,
                                quotes=["You fucking prick... I don't know why, but you really turn me on...",
                                        "You're precious and you're smokin' hot, it had to happen sooner or later..."],
                                footers=["Well, your ass looks good in these, I'll give you that.",
                                         "I'll have to stand aside, [...] let's say that MC really took it out of me..."],
                                game="OiaLt")

    Judie = NsfwCharacterCard(name="Judie",
                              picNumber=6,
                              quotes=["This was such a good idea, sis!",
                                      "Come on babe! Don't be shy! This is fucking great!",
                                      "I don't know if I can take it step-bro!", "Hmm, this turns me on so much..."],
                              footers=["You're setting the bar so high though...", "Duh, we had sex in Japan too!",
                                       "I wanna know what you taste like..."],
                              game="OiaLt")

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

    Rebecca = NsfwCharacterCard(name="Rebecca",
                                picNumber=1,
                                quotes=["You fill me up completely"],
                                footers=["I'm not a respectable teacher now, am I?"],
                                game="OiaLt")

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

    Annie = NsfwCharacterCard(name="Annie",
                              picNumber=11,
                              quotes=["\"Like\" it? It was the best experience of my life!"],
                              footers=["My knight in shining armor..."],
                              game="Eternum")

    Calypso = NsfwCharacterCard(name="Calypso",
                                picNumber=1,
                                quotes=[
                                    "You look... \"hot as fuck\" as well.",
                                    "\*Whispers\* It is... better than I anticipated..."
                                ],
                                footers=["Holy Mother of Turska!", "\*Whispers\* What kind of curse is this...?"],
                                game="Eternum")

    Dalia = NsfwCharacterCard(name="Dalia",
                              picNumber=9,
                              quotes=["\*Panting\* T-Too much... d-dick... N-Need... oxygen!",
                                      "I don't know how, but somehow... it's always Orion who ends up winning."],
                              footers=["*cum in my mouth.*",
                                       "Y-You're both nuts..."],
                              game="Eternum")

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

    FoxMaidens = NsfwCharacterCard(name="FoxMaidens",
                                   picNumber=1,
                                   quotes=[""],
                                   footers=[""],
                                   game="Eternum")

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

    Maat = NsfwCharacterCard(name="Maat",
                             picNumber=2,
                             quotes=["I want you to destroy me..."],
                             footers=["This spectacle is pleasing the pharaohs!"],
                             game="Eternum")

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

    Orion = NsfwCharacterCard(name="Orion",
                              picNumber=2,
                              quotes=[
                                  "I don't want to lose the challenge just because you can't curb your irrepressible desire to kiss me.",
                                  "Isn't it funny how we always end up stuck in the most bizarre situations?",
                                  "You better have a spare change of sheets, girl, because we're gonna leave a big fucking mess..."],
                              footers=["Admit you enjoy seeing me stroking my cock...",
                                       "You can touch me whenever you want!"],
                              game="Eternum")

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

    Wenlin = NsfwCharacterCard(name="Wenlin",
                               picNumber=1,
                               quotes=[""],
                               footers=[""],
                               game="Eternum")

    Eva = []
    Eva.append(EvaTroll)
    Eva.append(EvaSerious)

    oialt = []
    oialt.append(Aiko)
    oialt.append(Carla)
    oialt.append(Iris)
    oialt.append(Jasmine)
    oialt.append(Judie)
    oialt.append(Lauren)
    oialt.append(Rebecca)

    options = []
    options.append(Aiko)
    options.append(Carla)
    options.append(Iris)
    options.append(Jasmine)
    options.append(Judie)
    options.append(Lauren)
    options.append(Rebecca)
    options.append(Alex)
    options.append(Annie)
    options.append(Calypso)
    options.append(Dalia)
    options.append(EvaSerious)
    options.append(FoxMaidens)
    options.append(Luna)
    options.append(Maat)
    options.append(Nancy)
    options.append(Nova)
    options.append(Orion)
    options.append(Penny)
    options.append(Wenlin)

    eternum = []
    eternum.append(Alex)
    eternum.append(Annie)
    eternum.append(Calypso)
    eternum.append(Dalia)
    eternum.append(EvaSerious)
    eternum.append(FoxMaidens)
    eternum.append(Luna)
    eternum.append(Maat)
    eternum.append(Nancy)
    eternum.append(Nova)
    eternum.append(Penny)
    eternum.append(Wenlin)

    @commands.command()
    async def nsfw(self, ctx, parameter=None):
        """
        Draws a random character from the pool unless one is specified and shows a random lewd scene of theirs from the Caribdis-verse.
        /!\ Only works in channels marked to discord as NSFW.
        ----------------------------------------------------------------------------------------------------------------------
        Parameters:
            - ctx : discord.ext.Context - discord-provided context to the command prompt.
            - parameter : any - filters the pool of characters to choose from (defaults to None).
                currently supported parameters: [Aiko, Carla, Iris, Jasmine, Judie, Lauren, Rebecca, Alex, Annie, Calypso, Dalia, Eva, 
                FoxMaidens, Luna, Maat, Nancy, Nova, Penny, Wenlin, OiaLt, Eternum]
        """
        if ctx.channel.is_nsfw():
            dict = {
                None: self.options,
                "aiko": self.Aiko,
                "carla": self.Carla,
                "iris": self.Iris,
                "jasmine": self.Jasmine,
                "jas": self.Jasmine,
                "judie": self.Judie,
                "lauren": self.Lauren,
                "rebecca": self.Rebecca,
                "reb": self.Rebecca,
                "oialt": self.oialt,
                "alex": self.Alex,
                "alexandra": self.Alex,
                "annie": self.Annie,
                "calypso": self.Calypso,
                "dalia": self.Dalia,
                "eva": self.Eva,
                "foxmaidens": self.FoxMaidens,
                "luna": self.Luna,
                "maat": self.Maat,
                "nancy": self.Nancy,
                "nova": self.Nova,
                "orion": self.Orion,
                "mc": self.Orion,
                "main": self.Orion,
                "penny": self.Penny,
                "penelope": self.Penny,
                "wenlin": self.Wenlin,
                "eternum": self.eternum,
            }

            result = dict.get(parameter.lower() if parameter else None, self.options)

            choice = random.choice(result) if isinstance(result, list) else result

            number = random.randint(1, choice.picNumber)

            await createAndSendEmbed(choice, number, ctx)
        else:
            await ctx.send("This channel is sfw!")


def setup(client):
    client.add_cog(Nsfw(client))
