from discord import Embed
import discord
import datetime
from typing import Optional

from utils import IMAGE
from utils import EMOJI


class BaseEmbed(Embed):
    def __init__(self, user: Optional[discord.User] = None, **kwargs):
        super().__init__(color=0x0D115E, timestamp=datetime.datetime.now(), **kwargs)

        if user is not None:
            self.set_footer(
                text=f"Requested by {user.name.title()} {EMOJI.SPARKLE}",
                icon_url=user.avatar_url,
            )

        self.set_thumbnail(url=IMAGE.ICON_URL)
