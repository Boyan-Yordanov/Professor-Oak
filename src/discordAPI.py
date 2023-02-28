import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    print("The bot is ready.")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    try:
        num = int(message.content)
        result = num * num
        await message.channel.send(str(result))
    except ValueError:
        pass

    await bot.process_commands(message)


@bot.command()
async def wake_up_professor(ctx):
    await ctx.send("THE PROFESSOR IS AWAKE")


bot.run("DISCORD_API_KEY")
