import sqlite3
import traceback
import discord
from Utilities import HelperClass

class DeleteAccView(discord.ui.View):
    def __init__(self, deleting_user: discord.User, accountManager, timeout = 180):
        self.user = deleting_user
        self.accountManager = accountManager
        super().__init__(timeout=timeout)

    async def interaction_check(self, interaction):
        if interaction.user == self.user:
            return True

        await interaction.response.send_message("Sorry, this message is handling a different user!", ephemeral=True)
        return False

    async def on_timeout(self):
        await self.terminate()
        return await super().on_timeout()

    async def terminate(self, interaction: discord.Interaction = None, success: bool = False):
        for child in self.children:
            child.disabled = True

        if interaction:
            await interaction.response.edit_message(
                embed=await self.get_success_embed() if success else await self.get_cancel_embed(), 
                view=self
            )
        else:
            await self.message.edit(embed=await self.get_timeout_embed(), view=self)
        self.stop()

    @discord.ui.button(label="CONFIRM", style=discord.ButtonStyle.red)
    async def delete_account(self, interaction: discord.Interaction, button: discord.ui.Button):
        success = await self.accountManager.removeUserFromDB(self.user.id)

        if not success:
            embed = discord.Embed(title=f"Error deleting {self.user.display_name}'s account!", description="User is not registered to Judie's Database!", color=HelperClass.eternumBlue)
            self.message.reply(embed=embed)

        await self.terminate(interaction=interaction, success=success)

    @discord.ui.button(label="CANCEL", style=discord.ButtonStyle.primary)
    async def cancel_action(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.terminate(interaction=interaction, success=False)

    async def get_success_embed(self) -> discord.Embed:
        return discord.Embed(
            title="Success.",
            description=f"User {self.user.display_name} has been removed from the database.",
            color=HelperClass.eternumBlue
        )

    async def get_cancel_embed(self) -> discord.Embed:
        return discord.Embed(
            title="Cancelled/Unsuccessful.",
            description=f"User {self.user.display_name} (id=`{self.user.id}`) has NOT been removed from the database.",
            color=HelperClass.eternumBlue
        )

    async def get_timeout_embed(self) -> discord.Embed:
        return discord.Embed(
            title="Timed Out.",
            description=f"User {self.user.display_name} has NOT been removed from the database.",
            color=HelperClass.eternumBlue
        )


class GiveCharacterView(discord.ui.View):
    def __init__(self, user: discord.User, timeout = 180):
        super().__init__(timeout=timeout)
        self.selected_user = user
        self.character_menu = GiveCharacterMenu(self.selected_user, self)
        self.add_item(self.character_menu)

        # switch to dropdown
        for child in self.children:
            child.disabled = True

        self.character_menu.disabled = False

    async def switch_to_dropdown(self):
        for child in self.children:
            child.disabled = True

        self.character_menu.disabled = False

    async def switch_to_buttons(self):
        for child in self.children:
            child.disabled = False

        self.character_menu.disabled = True

    async def terminate(self):
        for child in self.children:
            child.disabled = True
        
        self.stop()

    @discord.ui.button(label="CONFIRM", style=discord.ButtonStyle.green)
    async def confirm_give(self, interaction: discord.Interaction, button: discord.ui.Button):
        success = await self.character_menu.selection.give_character(interaction, str(self.selected_user.id))

        text = f"Gave character {self.character_menu.selection.character[0]} to user {self.selected_user.display_name}!" if success \
            else f"Error giving user {self.selected_user.display_name} the character {self.character_menu.selection.character[0]}."

        embed = discord.Embed(
            title="Success!" if success else "Error!",
            description=text,
            color=HelperClass.eternumBlue
        )
        
        await self.terminate()
        await self.message.edit(embed=embed, view=self)
        await interaction.response.defer()

    @discord.ui.button(label="AMEND CHOICE", style=discord.ButtonStyle.red)
    async def change_choice(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.switch_to_dropdown()
        await self.message.edit(view=self)
        await interaction.response.defer()

    @discord.ui.button(label="CANCEL", style=discord.ButtonStyle.primary)
    async def cancel_interaction(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.terminate()
        await self.message.edit(view=self)
        await interaction.response.defer()

class Selection:
    def __init__(self):
        self.game = None
        self.collection: tuple = None
        self.character: tuple = None
        self.depth = 0

    async def select_game(self, game: str):
        self.game = game
        self.depth = 0 if game is None else 1

    async def select_collection(self, label: str, table_name: str):
        self.collection = None if table_name is None else (label, table_name)
        self.depth = 0 if table_name is None else 2

    async def select_character(self, label: str, table_name: str):
        self.character = None if table_name is None else (label, table_name)
        self.depth = 1 if table_name is None else 3

    async def get_text(self):
        if self.depth == 0:
            return "Select the game of the character you want to grant:"
        if self.depth == 1:
            return f"Select a collection from the game **{self.game}**:"
        if self.depth == 2:
            return f"Select a character from the collection **{self.game}** > **{self.collection[0]}**:"
        if self.depth > 2:
            return f"Are you sure about your selection of **{self.game}** > **{self.collection[0]}** > **{self.character[0]}**:"

    async def give_character(self, interaction: discord.Interaction, discordID: str):
        if self.game is None or self.collection is None or self.character is None:
            print("Incomplete selection!")
            return False

        try:
            uid = await interaction.client.accountManager.getUserID(discordID)

            db = sqlite3.connect(interaction.client.db_path)
            cursor = db.cursor()

            cursor.execute("UPDATE %s SET %s=1 WHERE user_id=?" % (self.collection[1], self.character[1]), [uid])

            db.commit()
            cursor.close()
            db.close()

            return True

        except Exception as e:
            traceback.print_exc()
            return False

    async def is_complete(self) -> bool:
        return self.game is not None and self.collection is not None and self.character is not None

class GiveCharacterMenu(discord.ui.Select):
    options_dict = {
        "OiaLt": {
            "Harem": ({
                "Judie": "judie",
                "Lauren": "lauren",
                "Messy Hair Lauren": "messy_hair_lauren",
                "Carla": "carla",
                "Iris": "iris",
                "Aiko": "aiko",
                "Jasmine": "jasmine",
                "Rebecca": "rebecca",
                "Back to OiaLt": None
            }, "oialt_harem"),
            "Stabby Mikes": ({
                "Policeman Mike": "police",
                "Hitman Mike": "hitman",
                "Yakuza Mike": "yakuza",
                "Father Mitchell": "priest",
                "Mike the Exterminator": "exterminator",
                "Anastasia": "anastasia",
                "Back to OiaLt": None
            }, "stabby_mikes"),
            "The Boys": ({
                "MC": "mc",
                "Tom": "tom",
                "Oliver": "oliver",
                "Fit Jack": "fit_jack",
                "Asmodeus": "asmodeus",
                "Hiromi": "hiromi",
                "Back to OiaLt": None
            }, "the_boys"),
            "Potential LI's": ({
                "Ava": "ava",
                "Lilith": "lilith",
                "Fit Jack's Groupie": "fit_jack_groupie",
                "Train Conductor": "train_conductor",
                "Shop Girl": "shop_girl",
                "Stone Elephant": "stone_elephant",
                "Back to OiaLt": None
            }, "li_potential"),
            "Protectors": ({
                "Funtime Clan Leader": "funtime",
                "MC": "mc",
                "Aiko": "aiko",
                "93": "nine_three",
                "Back to OiaLt": None
            }, "oialt"),
            "Back to Games": None
        },
        "Eternum": {
            "Harem": ({
                "Alexandra Bardot": "alex",
                "Annie Winters": "annie",
                "Calypso": "calypso",
                "Dalia Carter": "dalia",
                "Luna Hernandez": "luna",
                "Nancy Carter": "nancy",
                "Nova Johnson": "nova",
                "Penelope Carter": "penny",
                "Back to Eternum": None
            }, "eternum_harem"),
            "Side Girls": ({
                "Blue Fox Maiden": "bluefoxmaiden",
                "Eva": "eva",
                "Idriel": "idriel",
                "Lorelei Thornvale": "lorelei",
                "Maat": "maat",
                "Red Fox Maiden": "redfoxmaiden",
                "Wenlin": "wenlin",
                "Back to Eternum": None
            }, "side_girls"),
            "Homies": ({
                "Chang Wong": "chang",
                "Chop-Chop": "chopchop",
                "Victor Hernandez": "victor",
                "Jerry": "jerry",
                "Micaela Garcia": "micaela",
                "Noah": "noah",
                "Orion Richards": "orion",
                "Raul": "raul",
                "Back to Eternum": None
            }, "homies"),
            "Pets": ({
                "Carolyn": "carolyn",
                "Igor": "igor",
                "Kermit": "kermit",
                "Maurice (Cat)": "mauricec",
                "Maurice (Goat)": "mauriceg",
                "Maurice (Toucan)": "mauricet",
                "Pancho": "pancho",
                "Back to Eternum": None}, "creatures"),
            "Protectors": ({
                "Orion Richards": "orion",
                "Calypso": "calypso",
                "Dalia Carter": "dalia",
                "Pyramid Head": "pyramid_head",
                "Back to Eternum": None
            }, "eternum"),
            "Back to Games": None
        }
    }


    def __init__(self, user: discord.User, view: GiveCharacterView):
        self.user = user
        self.view_ref = view
        self.selection = Selection()
        options = GiveCharacterMenu.create_default_options()
        super().__init__(placeholder="", min_values=1, max_values=1, options=options)


    def create_default_options() -> list[discord.SelectOption]:
        options = []

        for key in GiveCharacterMenu.options_dict.keys():
            options.append(
                discord.SelectOption(
                    label=key,
                    description=""
                )
            )
        return options


    async def update_options(self) -> list[discord.SelectOption]:
        if self.selection.depth < 0:
            return []

        options = []
        _dict = {}

        if self.selection.depth >= 0:
            _dict = GiveCharacterMenu.options_dict
        if self.selection.depth >= 1:
            _dict = _dict[self.selection.game]
        if self.selection.depth >= 2:
            _dict = _dict[self.selection.collection[0]][0]

        for key in _dict.keys():
            options.append(
                discord.SelectOption(
                    label=key,
                    description=""
                )
            )
        return options


    async def callback(self, interaction: discord.Interaction):
        # self.values[0] to get the selection.
        current = self.values[0]

        if self.selection.depth == 0:
            await self.selection.select_game(game=current)

        elif self.selection.depth == 1:
            val = GiveCharacterMenu.options_dict[self.selection.game][current]
            await self.selection.select_collection(label=current, table_name=None if val is None else val[1])

        else:
            val = GiveCharacterMenu.options_dict[self.selection.game][self.selection.collection[0]][0][current]
            await self.selection.select_character(label=current, table_name=val)
            
        self.options = await self.update_options()

        text = await self.selection.get_text()
        embed = discord.Embed(
            title=f"Selecting a character to give to {self.user.display_name}.",
            description=text,
            color = HelperClass.eternumBlue
        )

        if await self.selection.is_complete():
            await self.view_ref.switch_to_buttons()

        await self.view_ref.message.edit(embed=embed, view=self.view_ref)
        await interaction.response.defer()
