# imports
import nextcord, typing
from nextcord.ext import commands

class misc(commands.Cog):
    def __init__(self, bot):    
        self.bot = bot

    @commands.command(aliases=['latency'])
    async def ping(self, ctx):
        await ctx.send(f"**Pong!** Latency: ~{round(self.bot.latency * 1000, 3)}ms")

    @commands.command(aliases=['av', 'pfp'])
    async def avatar(self, ctx, member: nextcord.Member):
        embed = nextcord.Embed(
            title = f"{member.name}'s avatar",
        )
        embed.set_author(name = member, icon_url = member.avatar.url)
        embed.set_image(url=member.avatar.url)
        await ctx.send(embed=embed)
    
    @commands.command(alises=['clear', 'delete', 'clean'])
    @commands.has_permissions(manage_messages = True)
    async def purge(self, ctx, messages: typing.Optional[int] = 10):
        await ctx.channel.purge(limit = messages)
        await ctx.send(f"successfuly purged `{messages}` messages", delete_after = 3)

def setup(bot):
    bot.add_cog(misc(bot))