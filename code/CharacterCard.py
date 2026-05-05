from discord.ext.commands.parameters import empty
from Utilities import Collections, Effects, OgfCollections, OgfEffects

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

class NsfwCharacterCard:
    """
    Object representing a character's lewd personality from the Caribdis-verse.
    --------------------------------------------------------
    Values:
        - name - the character's name,
        - picNumber - the amount of pictures attributed to a character for random selection,
        - quotes - a list of quotes said by the character,
        - footers - a list of witty lines addressed to the character,
        - game - the name of the game the character is from.
    """
    def __init__(
            self, 
            name: str, 
            picNumber: int, 
            quotes: list, 
            footers: list, 
            game: str
        ):
        self.name = name
        self.picNumber = picNumber
        self.quotes = quotes
        self.footers = footers
        self.game = game


class OgfCharacterCard:
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
            collection: OgfCollections = OgfCollections.NONE, 
            effect: OgfEffects = OgfEffects.NONE
        ):
        self.name = name
        self.footer = footer
        self.filename = filename
        self.collection = collection
        self.effect = effect
