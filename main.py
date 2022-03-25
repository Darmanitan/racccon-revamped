# import libraries
import nextcord, logging, os, asyncio
from nextcord.ext import commands
from dotenv import load_dotenv


load_dotenv()
token = os.environ.get("token")
bot = commands.Bot(command_prefix=commands.when_mentioned_or('$'), case_insensitive=True)
logging.basicConfig(level=logging.ERROR)

@bot.event
async def on_ready():
    print(f"successfuly logged in as {bot.user}")
    for fn in os.listdir("./cogs"):
        if fn.endswith(".py"):
            bot.load_extension(f"cogs.{fn[:-3]}")
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You don't have the permissions to run this command.", delete_after=4)
        await ctx.message.delete(delay=3)
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please enter missing required argument", delete_after=4)
        await ctx.message.delete(delay=3)
    elif isinstance(error, commands.BotMissingPermissions):
        await ctx.send("Please give bot sufficiant permissions.", delete_after=4)
        await ctx.message.delete(delay=3)
    elif isinstance(error, commands.CommandNotFound):
        await ctx.send("Command not found.", delete_after=4)
        await ctx.message.delete(delay=3)
    elif isinstance(error, commands.DisabledCommand):
        await ctx.send(f'{ctx.command} has been disabled.', delete_after=4)
        await ctx.message.delete(delay=3)

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

bot.run(token)