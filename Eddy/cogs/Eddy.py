# -*- coding: utf-8 -*-

from discord.ext import commands
import discord


class Eddy(commands.Cog):
    """The description for Eddy goes here."""

    def __init__(self, bot):
        self.bot: commands.Bot = bot
        self.bot.remove_command("help")

    @commands.command(name="ping")
    async def ping(self, ctx: commands.Context):
        """PONG

        Args:
            ctx (commands.Context): [description]
        """
        await ctx.send(f"Pong! {round(self.bot.latency * 1000)}ms ")

    @commands.command(name="help")
    async def help_command(self, ctx: commands.Context):
        """Bot Help Command"""

        help_em = discord.Embed(
            title="Help :orange_heart:",
            description="Use **pls ed help** for this menu :white_check_mark:",
        )

        help_em.add_field(
            name="Eddy",
            value="**ping** : pOng!\n**help** : Hi, its me!\n**set-status-to** : to change the BOT status!",
        )

        await ctx.send(embed=help_em)

    @commands.command(name="set-status-to")
    async def set_status(self, ctx: commands.Context, *, text: str):
        """Set the BOT STATUS

        Args:
            ctx (commands.Context): bot context
            text (str): status text
        """

        await self.bot.change_presence(activity=discord.Game(name=text))
        await ctx.send(f"Set status to **{text}** - :white_check_mark:")


def setup(bot):
    bot.add_cog(Eddy(bot))
