# import libraries
import nextcord, logging, os, asyncio, wavelink
from nextcord.ext import commands
from dotenv import load_dotenv


load_dotenv()
token = os.environ.get("token")
bot = commands.Bot(command_prefix=commands.when_mentioned_or('$'), case_insensitive=True, activity = nextcord.Game("raccoon | $help"), status=nextcord.Status.dnd)

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

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f"cogs.{extension}")
    await ctx.send(f"successfuly loaded {extension}")

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f"cogs.{extension}")
    await ctx.send(f"successfuly unloaded {extension}")

@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(f"cogs.{extension}")
    await ctx.send(f"successfuly reloaded {extension}")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f"You do not have the required permissions to execute this command! {ctx.message.author.mention}", delete_after=3)
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"Please input a required argument", delete_after=3)
    elif isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f"This command is on cooldown. Please try again after {round(error.retry_after, 1)} seconds.", delete_after=3)
    else:
        raise error


bot.run(token)