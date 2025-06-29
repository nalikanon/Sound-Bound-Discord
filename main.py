import discord
from discord.ext import commands
import os
import asyncio

intents = discord.Intents.default()
intents.guilds = True
intents.voice_states = True
bot = commands.Bot(command_prefix='/', intents=intents)

TOKEN = 'MTM4ODgyOTc3MzAzNTIwODc3Ng.GkUyqW.c63JIfIDkMIau2M9id9EQPZ4R82gsS-ZCPnXdE'

@bot.event
async def on_ready():
    print("Bot Online")

@bot.command(name='1')
async def play_music(ctx):
    # Check if the user is in a voice channel
    if not ctx.author.voice:
        await ctx.send("คุณต้องเข้าห้องเสียงก่อนใช้คำสั่งนี้!")
        return
    
    # Get the voice channel
    voice_channel = ctx.author.voice.channel
    
    try:
        # Check if the bot is already in a voice channel
        if ctx.voice_client is not None:
            await ctx.voice_client.disconnect()
        
        # Connect to the voice channel
        voice_client = await voice_channel.connect()
        
        # Play the audio file
        audio_source = discord.FFmpegPCMAudio('music/a.mp3')
        
        def after_playing(error):
            if error:
                print(f"Error: {error}")
            asyncio.run_coroutine_threadsafe(ctx.voice_client.disconnect(), bot.loop)
        
        voice_client.play(audio_source, after=after_playing)
        await ctx.send("กำลังเล่นเพลง...")
        
    except Exception as e:
        print(f"Error: {e}")
        await ctx.send("เกิดข้อผิดพลาดในการเล่นเพลง")
        if ctx.voice_client:
            await ctx.voice_client.disconnect()

bot.run(TOKEN)