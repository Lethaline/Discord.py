from discord.ext import commands
from dotenv import load_dotenv
from discord_slash import SlashCommand, SlashContext
from Functions.Randomize import *
import os

def main():
    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')
    PREFIX = os.getenv('DISCORD_PREFIX')
    bot = commands.Bot(command_prefix=PREFIX)
    for files in os.listdir('./Commands'):
        if files.endswith('.py'):
           bot.load_extension(f'Commands.{files[:-3]}')
    for listeners in os.listdir('./Listeners'):
        if listeners.endswith('.py'):
           bot.load_extension(f'Listeners.{listeners[:-3]}')
    bot.run(TOKEN)
    
if __name__ == '__main__':
    main()