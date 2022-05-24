from discord.ext import commands

@commands.command()
async def UserInfos(ctx):
    print(ctx.author)

def setup(bot):
    bot.add_command(UserInfos)