from Utilities import Collections, Effects, OgfCollections, OgfEffects


class CharacterCard:
    def __init__(self, name, picNumber: int, quotes: list, filename: str, effects: Effects = Effects.NONE,
                 aliases: str = "no aliases", collection: Collections = Collections.NONE):
        self.name = name
        self.picNumber = picNumber
        self.quotes = quotes
        self.filename = filename
        self.effects = effects
        self.aliases = aliases
        self.collection = collection


class NsfwCharacterCard:
    def __init__(self, name: str, picNumber: int, quotes: list, footers: list, game: str):
        self.name = name
        self.picNumber = picNumber
        self.quotes = quotes
        self.footers = footers
        self.game = game


class OgfCharacterCard:
    def __init__(self, name: str, footer: str, filename: str,
                 collection: OgfCollections = OgfCollections.NONE, effect: OgfEffects = OgfEffects.NONE):
        self.name = name
        self.footer = footer
        self.filename = filename
        self.collection = collection
        self.effect = effect
