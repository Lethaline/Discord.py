from discord.ext import commands
from dotenv import load_dotenv
from discord import Intents
from discord_slash import SlashCommand, SlashContext
from Functions.Randomize import *
import os

def main():
    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')
    PREFIX = os.getenv('DISCORD_PREFIX')
    bot = commands.Bot(command_prefix=PREFIX, intents=Intents.all())
    slash = SlashCommand(bot, sync_commands=True)
    for files in os.listdir('./Commands'):
        if files.endswith('.py'):
           bot.load_extension(f'Commands.{files[:-3]}')
    for listeners in os.listdir('./Listeners'):
        if listeners.endswith('.py'):
           bot.load_extension(f'Listeners.{listeners[:-3]}')
    for slashcommands in os.listdir('./Slash_Commands'):
        if slashcommands.endswith('.py'):
           bot.load_extension(f'Slash_Commands.{slashcommands[:-3]}')
    bot.run(TOKEN)
    
if __name__ == '__main__':
    main()