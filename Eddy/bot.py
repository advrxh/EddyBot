# -*- coding: utf-8 -*-

from discord.ext import commands
import discord
import config

from Embeds import *


class Bot(commands.Bot):
    def __init__(self, **kwargs):

        super().__init__(command_prefix=commands.when_mentioned_or("pls ed "), **kwargs)
        for cog in config.cogs:
            try:
                self.load_extension(cog)
            except Exception as exc:
                print(
                    "Could not load extension {0} due to {1.__class__.__name__}: {1}".format(
                        cog, exc
                    )
                )

    async def on_ready(self):
        await self.change_presence(
            activity=discord.Game(
                name="pls ed",
                url="https://github.com/AadilVarsh/EddyBot",
            )
        )

        print("Logged on as {0} (ID: {0.id})".format(self.user))

    async def on_command_error(self, context: commands.Context, exception):
        await context.send(embed=ErrorEmbed(exception))


bot = Bot()

# write general commands here
bot.remove_command("help")


@bot.command(name="help", aliases=["welp"])
async def help_command(ctx: commands.Context):

    await ctx.send(embed=HelpEmbed(ctx.author))


@bot.command(name="ping", aliases=["reply"])
async def ping_command(ctx: commands.Context):
    ping_em = discord.Embed(
        title="Ping", description=f"Pong! {round(bot.latency * 100)}ms"
    )

    await ctx.send(embed=ping_em)


@bot.command(name="invite")
async def invite_command(ctx: commands.Context):

    await ctx.send(embed=InviteEmbed(ctx.author))


@bot.event
async def on_message(message: discord.Message):
    if "pls ed" in message.content.lower():
        await message.channel.send(embed=HelpEmbed(message.author))


bot.run(config.token)
