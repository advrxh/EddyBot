import discord

from Embeds import BaseEmbed
from utils import EMOJI, IMAGE


class ErrorEmbed(BaseEmbed):
    def __init__(self, exception, **kwargs):
        super().__init__(**kwargs)

        self.title = f"Uh Oh {EMOJI.HEART_BREAK}"
        self.description = f"An error occured!, ' **{exception}** '\n try using **pls ed help**, or simply mention me!"
        self.url = "https://github.com/AadilVarsh/EddyBot"
        self.set_footer(
            icon_url="https://aadilvarsh.github.io/images/pfp.png",
            text=f"Contact the author, if occurs again {EMOJI.SPARKLE}",
        )
