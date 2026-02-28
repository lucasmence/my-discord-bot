import discord
from discord.ext import commands, tasks
import os
import re
import ffmpeg
import asyncio
from pytube import YouTube
import yt_dlp
import requests

FOLDER_DOWNLOADS = "./downloads"
token = os.getenv('DISCORD_TOKEN')
prefix = os.getenv('PREFIX')
cooldownMediaCommand = os.getenv('COOLDOWN_MEDIA')
limitFilesizeMb = os.getenv('LIMIT_FILESIZE_MB')
diskClearMinutes = os.getenv('DISK_CLEAR_MINUTES')

userId = ''

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=prefix, intents=intents)

async def load_extensions():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')

async def main():
    async with bot:
        await load_extensions()
        await bot.start(token)

if __name__ == "__main__":
    asyncio.run(main())