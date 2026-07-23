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

    @discord.ui.button(label="CONFIRM", style=discord.ButtonStyle.red)
    async def delete_account(self, interaction: discord.Interaction, button: discord.ui.Button):
        success = await self.accountManager.removeUserFromDB(self.user.id)

        if not success:
            embed = discord.Embed(title=f"Error deleting {self.user.display_name}'s account!'", description="User is not registered to Judie's Database!", color=HelperClass.eternumBlue)
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
