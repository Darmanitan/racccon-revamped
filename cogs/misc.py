# imports
import nextcord, typing
from nextcord.ext import commands

class misc(commands.Cog):
    def __init__(self, bot):    
        self.bot = bot

    @commands.command(aliases=['latency'], description="ping from raccon to discord", name='ping')
    async def ping(self, ctx):
        await ctx.send(f"**Pong!** Latency: ~{round(self.bot.latency * 1000, 3)}ms")

    @commands.command(aliases=['av', 'pfp'], description='sends the avatar of the given user', name='avatar')
    async def avatar(self, ctx, member: nextcord.Member):
        embed = nextcord.Embed(
            title = f"{member.name}'s avatar",
        )
        embed.set_author(name = member, icon_url = member.avatar.url)
        embed.set_image(url=member.avatar.url)
        await ctx.send(embed=embed)
    
    @commands.command(alises=['clear', 'delete', 'clean'], description='deletes the amount of messages given', name='purge')
    @commands.has_permissions(manage_messages = True)
    async def purge(self, ctx, messages: typing.Optional[int] = 10):
        await ctx.channel.purge(limit = messages)
        await ctx.send(f"successfuly purged `{messages}` messages", delete_after = 3)
    
    @commands.command(aliases=['serverinfo'], name='info', description='shows various information about the server')
    async def info(self, ctx):
        member_count = ctx.guild.member_count
        owner = f"{ctx.guild.owner.name}#{ctx.guild.owner.discriminator}"
        channels = len(ctx.guild.text_channels)
        voice = len(ctx.guild.voice_channels)
        roles = len(ctx.guild.roles)
        categories = len(ctx.guild.categories)
        created_at = str(ctx.guild.created_at).split(" ")

        embed = nextcord.Embed()
        embed.set_author(name=f"{ctx.guild.name} | server info", icon_url=(ctx.guild.icon.url))
        embed.set_thumbnail(url=ctx.guild.icon.url)
        embed.set_footer(text=f"server id: {ctx.guild.id} | created at: {created_at[0]}")
        embed.add_field(name="owner", value=owner)
        embed.add_field(name="members", value=member_count)
        embed.add_field(name="channel count", value=channels)
        embed.add_field(name="voice channels", value=voice)
        embed.add_field(name="roles", value=roles)
        embed.add_field(name="categories", value=categories)
        
        await ctx.send(embed=embed)
    
def setup(bot):
    bot.add_cog(misc(bot))