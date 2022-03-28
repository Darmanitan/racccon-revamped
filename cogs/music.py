# imports
import nextcord, asyncio, aiohttp, wavelink
from nextcord.ext import commands

class music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='join', description='racccon joins the voice channel youre in')
    async def join(self, ctx):
        await ctx.author.voice.channel.connect()

    @commands.command(aliases=['disconnect'], name='leave', description='disconnect from voice channel')
    async def leave(self, ctx):
        vc = wavelink.Player = ctx.voice_client
        await vc.stop()
        await vc.disconnect()

    @commands.command(name='play', description='plays music (only supports youtube at the moment)')
    async def play(self, ctx, search: wavelink.YouTubeTrack):
        if not ctx.voice_client:
            vc: wavelink.Player = await ctx.author.voice.channel.connect(cls=wavelink.Player)
        elif not ctx.author.voice_client:
            await ctx.send("You are not currently connected to a voice channel!")
        else:        
            await vc.play(search)
            await ctx.send(f"Now Playing: `{search.title}`")
    
    @commands.command(name='pause', description='pauses current song playing')
    async def pause(self, ctx):
        if not ctx.voice_client:
            await ctx.send("You're not playing any music!")
        elif not getattr(ctx.author.voice, "channel", None):
            await ctx.send("You are not current connected to a voice channel!")
        else:
            vc = wavelink.Player = ctx.voice_client
        
        await vc.pause()
        await ctx.send("`Paused.`")

    @commands.command(name='resume', description='resumes paused music')
    async def resume(self, ctx):
        if not ctx.voice_client:
            await ctx.send("You're not playing any music!")
        elif not getattr(ctx.author.voice, "channel", None):
            await ctx.send("You are not current connected to a voice channel!")
        else:
            vc = wavelink.Player = ctx.voice_client
        
        await vc.resume()
        await ctx.send("`Resumed your music!.`")
    
    @commands.command(name='stop', description='stops music currently playing')
    async def stop(self, ctx):
        if not ctx.voice_client:
            await ctx.send("You're not playing any music!")
        elif not getattr(ctx.author.voice, "channel", None):
            await ctx.send("You are not current connected to a voice channel!")
        else:
            vc = wavelink.Player = ctx.voice_client
        
        await vc.stop()
        await ctx.send("successfuly stopped music")
    

def setup(bot):
    bot.add_cog(music(bot))