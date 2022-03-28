# import libraries
import nextcord, logging, os, asyncio, wavelink
from nextcord.ext import commands
from dotenv import load_dotenv


load_dotenv()
token = os.environ.get("token")
intents = nextcord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix=commands.when_mentioned_or('$'), case_insensitive=True, activity = nextcord.Game("raccoon | $help"), status=nextcord.Status.dnd, intents=intents)
logging.basicConfig(level=logging.ERROR)

@bot.event
async def on_ready():
    print(f"successfuly logged in as {bot.user}")
    for fn in os.listdir("./cogs"):
        if fn.endswith(".py"):
            bot.load_extension(f"cogs.{fn[:-3]}")
    bot.loop.create_task(connect_node())


async def connect_node():
    await bot.wait_until_ready()
    await wavelink.NodePool.create_node(bot = bot,  host = "lavalink.oops.wtf" , port = 443, password = "www.freelavalink.ga", https = "True")

@bot.command(name='load', description='loads cog')
async def load(ctx, extension):
    if ctx.message.author.id == 855586334005002270:
        bot.load_extension(f"cogs.{extension}")
        await ctx.send(f"successfuly loaded {extension}")
    else:
        await ctx.send("seriously? why would you even try.")

@bot.command(name='unload', description='unloads cog')
async def unload(ctx, extension):
    if ctx.message.author.id == 855586334005002270:
        bot.unload_extension(f"cogs.{extension}")
        await ctx.send(f"successfuly unloaded {extension}")
    else:
        await ctx.send("seriously? why would you even try")

@bot.command(name='reload', description='reloads cog')
async def reload(ctx, extension):
    if ctx.message.author.id == 855586334005002270:
        bot.reload_extension(f"cogs.{extension}")
        await ctx.send(f"successfuly reloaded {extension}")
    else:
        await ctx.send("seriously? why would you even try")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f"You do not have the required permissions to execute this command! {ctx.message.author.mention}", delete_after=3)
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"Please input a required argument", delete_after=3)
    elif isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f"This command is on cooldown. Please try again after {round(error.retry_after, 1)} seconds.", delete_after=3)
    elif isinstance(error, commands.CommandNotFound):
        await ctx.send(f"This command does not exist! {ctx.message.author.mention}", delete_after=3)
    else:
        raise error


bot.run(token)