from discord.ext import commands

class TestCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content == "Pong":
            await message.channel.send("Ping")


def setup(bot: commands.Bot):
    bot.add_cog(TestCog(bot))