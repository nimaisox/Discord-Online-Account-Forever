import discord, os, keep_alive, asyncio, datetime, requests
from colorama import Fore
from discord.ext import tasks, commands

client = commands.Bot(
  command_prefix=':',
  self_bot=False
)

async def on_ready():
    client.remove_command('help')
    await client.change_presence(status=discord.Status.online, activity=discord.Game("WATCHING"))

keep_alive.keep_alive()
client.run(os.getenv("TOKEN"), bot=False)

print(Fore.GREEN + f'logged in as {client.user}')