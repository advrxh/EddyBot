import discord

from Embeds import BaseEmbed
from utils import EMOJI, IMAGE


class HelpEmbed(BaseEmbed):
    def __init__(self, user: discord.User, **kwargs):
        super().__init__(user=user, **kwargs)

        self.title = f"At your Service, {user.name.title()}!"
        self.description = f"Eddy is here for your help! {EMOJI.SPARKLE},\nUSE prefix {EMOJI.RIGHT_ARROW_HEAD} **pls ed**, or simply mention me!"

        self.add_field(name="Eddy", value=self.field_value_eddy())

    def field_value_eddy(self):
        _val = f"""
        **help** {EMOJI.RIGHT_ARROW_HEAD} This Menu!
        **ping** {EMOJI.RIGHT_ARROW_HEAD} Pong!\n\n
        """

        return _val
