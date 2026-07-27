import discord
import sqlite3


async def get_cols(table_name: str, blacklist: list) -> list:
    db = sqlite3.connect("main.sqlite")
    cursor = db.cursor()

    cursor.execute("""PRAGMA table_info(%s)""" % table_name)
    cols = [c[1] for c in cursor.fetchall() if c[1] not in blacklist]

    cursor.close()
    db.close()
    return cols

async def check_channel(interaction: discord.Interaction) -> bool:
    """
    Checks whether the channel the command was called from was the designated bot & spam channel.
    -----------------------------------------------------------------------------------------------
    Parameters:
        - ctx: discord.ext.commands.Context
            the context provided with the message to check.

    Returns:
        bool: success of the comparison; 
            true = the channel is the bot & spam channel.
    """
    client = interaction.client
    result = interaction.channel.id == client.config.botSpamChannel
    if not result:
        embed = discord.Embed(title="Wrong channel!",
                              description=f"Please take this to {client.get_channel(client.config.botSpamChannel).mention}",
                              color=HelperClass.orange)
        await interaction.response.send_message(embed=embed)
    return result

class HelperClass:
    """
    Self-explanatory name - contains helpful values and functions.
    ----------------------------------------------------------------
    Members:
        Attributes:
            Emotes : str
            - daliaParty
            - alexAngry
            - annieCry
            - annieYay
            - novaGun
            - pepeCry2

            Colors : int [hex codes]
            - orange = ffa800
            - eternumBlue = 00ffcc
            - pink = b502b8
            - purple = 530554
            - red = ff0000
            - black = 000000
            - yellow = eeff00
            - green = 57f287
            - blue = 0028ff
        Methods:
            - init(discord.Bot) - initializes values according to config data.
            - createEmbed(title : str, text : str, color : int = orange, footer : str = None) - creates an embed object ready to be sent.
    """
    daliaParty = ""
    alexAngry = ""
    annieCry = ""
    annieYay = ""
    novaGun = ""
    pepeCry2 = ""

    def init(client):
        """
        Initializes member parameters using config data 

        Required for proper functioning; Required to run, only after BotConfig.load() was called.
        """
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


    orange = 0xffa800
    """
    OiaLt default color
    """
    eternumBlue = 0x00ffcc
    """
    Eternum default color
    """
    pink = 0xb502b8 
    """
    Harem color
    """
    purple = 0x530554
    """
    Side Girl color
    """
    red = 0xff0000
    """
    Unsuccessful Villain color
    """
    black = 0x000000 
    """
    Successful Villain color
    """
    yellow = 0xeeff00
    """
    Homie color
    """
    green = 0x57F287
    """
    Eternum Pets color
    """
    blue = 0x0028ff
    """
    Protector color
    """

    async def createEmbed(title : str, text : str, color=orange, footer : str = None) -> discord.Embed:
        """
        Compiles parameter to an embed object ready to be sent.
        -------------------------------------------------------
        Parameters:
            - title : str
            - text : str
            - color : int (defaults to HelperClass.orange)
            - footer : str (defaults to None)
        -------------------------------------------------------
        Returns:
            discord.Embed object according to specifications.
        """
        embed = discord.Embed(title=title, description=text, colour=color)
        if footer is not None:
            embed.set_footer(text=footer)
        return embed
