# imports
import nextcord, asyncio, aiohttp, humanfriendly, datetime, typing
from humanfriendly import parse_timespan
from nextcord.ext import commands

class moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='kick', description='kicks member')
    @commands.has_permissions(kick_members = True)
    async def kick(self, ctx, member: nextcord.Member, reason: typing.Optional[str] = "None"):
        await ctx.guild.kick(member)
        await ctx.send(f"successfuly kicked {member.mention} because of {reason} :thumbsup:")
    
    @commands.command(name='ban', description='bans member')
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, member: nextcord.Member, reason: typing.Optional[str] = "None"):
        await ctx.guild.ban(member)
        await ctx.send(f"successfuly banned {member.mention} becuase of {reason} :thumbsup:")
    
    @commands.command(name='unban', description='unbans member')
    @commands.has_permissions(ban_members = True)
    async def unban(self, ctx, member: nextcord.Member, reason: typing.Optional[str] = "None"):
        await ctx.guild.unban(member)
        await ctx.send(f"successfuly unbanned {member.mention} because of {reason} 👍")
    
    @commands.command(name='mute', description='mutes a member', aliases=['timeout'])
    @commands.has_permissions(moderate_members = True)
    async def mute(self, ctx, member: nextcord.Member, time, reason: typing.Optional[str] = "None"):
        time = humanfriendly.parse_timespan(time)
        await member.edit(timeout=nextcord.utils.utcnow()+datetime.timedelta(seconds=time))
        await ctx.send(f"successfuly muted {member.mention} for {time} because of {reason}")
    
    @commands.command(name='unmute', description='unmutes a member', aliases=['untimeout'])
    @commands.has_permissions(moderate_members = True)
    async def unmute(self, ctx, member: nextcord.Member, reason: typing.Optional[str] = "None"):
        await member.edit(timeout=None)
        await ctx.send(f"successfuly unmuted {member.mention} because of {reason}")
    
def setup(bot):
    bot.add_cog(moderation(bot))