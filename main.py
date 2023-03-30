# This example requires the 'message_content' privileged intents

import os
import discord
from discord.ext import commands

import numexpr

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def calc(ctx, expr):
    try:
        await ctx.reply(f"{expr} = {numexpr.evaluate(expr)}")
    except KeyError:
        await ctx.reply("Invalid expression.")


bot.run(os.environ["DISCORD_TOKEN"])
