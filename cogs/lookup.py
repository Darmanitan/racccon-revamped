# imports
import nextcord, asyncio, aiohttp
from nextcord.ext import commands


class lookup(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['lookup'])
    async def anime(self, ctx, anime):
        anime = '%20'.join(anime)    
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://api.jikan.moe/v4/anime?letter={anime}") as api:
                data = await api.json()
                embed = nextcord.Embed(
                    title=(data['data'][0]['title']),
                    url=(data['data'][0]['url']),
                    description=(data['data'][0]['synopsis'])
                )
                embed.set_thumbnail(url=(data['data'][0]['images']['jpg']['large_image_url'])) # sets image
                embed.add_field(name="⭐ Average Rating", value=(data['data'][0]['score'])) # sets rating
                embed.add_field(name="💽 Type", value=(data['data'][0]['type'])) # sets type
                embed.add_field(name="⁉️ Genres", value=(", ".join([g['name'] for g in data['data'][0]['genres']]))) # sets genres
                embed.add_field(name="⏳ Status", value=(data['data'][0]['status'])) # sets status
                embed.add_field(name="🕛 Aired", value=f"Aired from {(data['data'][0]['aired']['string'])}") # sets aired
                embed.add_field(name="🏆 Rank", value=f"Top {(data['data'][0]['rank'])}") # sets rank
                await ctx.send(embed=embed)
    
    @commands.command()
    async def manga(self, ctx, *args):
        anime = '%20'.join(args)    
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://api.jikan.moe/v4/manga?letter={anime}") as api:
                data = await api.json()
                embed = nextcord.Embed(
                    title=(data['data'][0]['title']),
                    url=(data['data'][0]['url']),
                    description=(data['data'][0]['synopsis'])
                )
                embed.set_thumbnail(url=(data['data'][0]['images']['jpg']['large_image_url'])) # sets image
                embed.add_field(name="⭐ Average Rating", value=(data['data'][0]['score'])) # sets rating
                embed.add_field(name="💽 Type", value=(data['data'][0]['type'])) # sets type
                embed.add_field(name="⁉️ Genres", value=(", ".join([g['name'] for g in data['data'][0]['genres']]))) # sets genres
                embed.add_field(name="⏳ Status", value=(data['data'][0]['status'])) # sets status
                embed.add_field(name="🕛 Aired", value=f"Aired from {(data['data'][0]['aired']['string'])}") # sets aired
                embed.add_field(name="🏆 Rank", value=f"Top {(data['data'][0]['rank'])}") # sets rank
                await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(lookup(bot))