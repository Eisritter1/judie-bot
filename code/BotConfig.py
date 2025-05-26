CONFIG = {
    # Main Bot
    867731565970718740: {
        "emojiIDs": {
            "ChibiDaliaParty": 1372504172330487918,
            "ChibiAlexAngry": 1372504159474942014,
            "ChibiAnnieCry": 1372504194249916496,
            "ChibiAnnieYay": 1372504183000793168,
            "ChibiNovaGun": 1372504132199383060,
            "PepeCry2": 1372504148402241577
        },
        "cooldown" : 72000,
        "botSpamChannel" : 779873459756335104
    },
    # Test Bot
    877834464472993842: {
        "emojiIDs": {
            "ChibiDaliaParty": 1372516695817715712,
            "ChibiAlexAngry": 1372516686565212170,
            "ChibiAnnieCry": 1372516717913440320,
            "ChibiAnnieYay": 1372516707716825161,
            "ChibiNovaGun": 1372516662556758046,
            "PepeCry2": 1372516676486303764
        },
        "cooldown": 5,
        "botSpamChannel": 929419591573188608
    }
}

class BotConfig:
    def __init__(self, client):
        self.client = client
        self._config = None

    async def load(self):
        await self.client.wait_until_ready()
        self._config = CONFIG.get(self.client.user.id)
        if self._config is None:
            raise RuntimeError(f"No config found for bot with user ID {self.client.user.id}.")

        self.cooldown = self._config.get("cooldown")
        self.botSpamChannel = self._config.get("botSpamChannel")
        self.emotes = self._config.get("emojiIDs")


