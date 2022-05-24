from discord.ext import commands

@commands.command()
async def Test(ctx):
    print("Bonjour")
    
def setup(bot):
 	bot.add_command(Test)