import discord
from discord.ext import commands
from password_gen import pass_gen
from os import listdir
from random import choice

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Cześć, jestem bot{bot.user}!')

@bot.command()
async def password(ctx, length = 10):
    await ctx.send("Wygnerowane hasło: " + pass_gen(length))

@bot.command()
async def mem(ctx):
    files_in_dir = listdir("memy")
    chosen_file = choice(files_in_dir)
    with open(rf"memy\{chosen_file}", "rb") as file:
        image = discord.File(file)
        await ctx.send("Oto twój mem:", file=image)


bot.run("")