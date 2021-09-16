from discord.ext import commands
import discord


class Eddy(commands.Cog):
    """The description for Eddy goes here."""

    def __init__(self, bot):
        self.bot: commands.Bot = bot


def setup(bot):
    bot.add_cog(Eddy(bot))
