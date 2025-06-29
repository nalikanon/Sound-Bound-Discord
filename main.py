import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="/", intents=discord.Intents.all())

TOKEN = 'MTM4ODgyOTc3MzAzNTIwODc3Ng.G9kK5M.7IUnU2pmetfVTQDaFYzZsegRfOTSYXjgkHv6-s'

@bot.event
async def on_ready():
    print('Bot Online')

bot.run(TOKEN)