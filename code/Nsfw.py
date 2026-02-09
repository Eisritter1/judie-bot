import discord
from discord import Embed, File
from discord.ext import commands, tasks
from discord.ext.commands import cooldown, BucketType
import random
import os
from Utilities import HelperClass
from CharacterCard import NsfwCharacterCard
from NsfwCharacters import NsfwCharacters


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
        self.characters = NsfwCharacters()
                

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
            result = self.characters.dict.get(parameter.lower() if parameter else None, self.characters.list)

            choice = random.choice(result) if isinstance(result, list) else result

            number = random.randint(1, choice.picNumber)

            await createAndSendEmbed(choice, number, ctx)
        else:
            await ctx.send("This channel is sfw!")


def setup(client):
    client.add_cog(Nsfw(client))
