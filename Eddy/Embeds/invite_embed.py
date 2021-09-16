import discord

from Embeds import BaseEmbed
from utils import EMOJI, IMAGE


class InviteEmbed(BaseEmbed):
    def __init__(self, user: discord.User, **kwargs):
        super().__init__(user, **kwargs)

        self.title = f"Want me on your server? {EMOJI.HEART_EYE}"
        self.description = f"I'm a multipurpose BOT developed by aadilvarsh#1241"
        self.url = "https://github.com/AadilVarsh/EddyBot"
        self.set_footer(
            icon_url="https://aadilvarsh.github.io/images/pfp.png",
            text=f"Developed by Aadil {EMOJI.SPARKLE}",
        )
