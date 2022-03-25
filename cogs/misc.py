# imports
import nextcord
from nextcord.ext import commands


class misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['latency'])
    async def ping(self, ctx):
        await ctx.send(f"**Pong!** Latency: ~{round(self.bot.latency, 3)}ms")

def setup(bot):
    bot.add_cog(misc(bot))