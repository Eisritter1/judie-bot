class CharacterCard:
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
