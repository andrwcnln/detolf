# author @andrwclnln
# v1.1
# feb 2023
# a lil discord bot so that our hamster can join the fun

import os
import random

import discord
from discord.ext import commands

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = commands.Bot(command_prefix='!',intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.command(name='helmi')
async def helmi(ctx):
    helmiMessages = [
    'squeak!',
    'squeaksqueak',
    'squeaksqueaksqueak',
    '*chatter*',
    '*bite*',
    '*bites toe*',
    '*angry noises*',
    ]

    response = random.choice(helmiMessages)
    await ctx.send(response)

@client.command(name='give')
async def give(ctx,arg):
    if arg == 'coriander':
        with open('images/coriander.gif', "rb") as file:
            fileToSend = discord.File(file, filename='images/coriander.gif')
        await ctx.send(file=fileToSend)
    elif arg == 'water':
        with open('images/water.gif', "rb") as file:
            fileToSend = discord.File(file, filename='images/water.gif')
        await ctx.send(file=fileToSend)
    elif arg == 'cucumber':
        with open('images/cucumber.gif', "rb") as file:
            fileToSend = discord.File(file, filename='images/cucumber.gif')
        await ctx.send(file=fileToSend)
    elif arg == 'cheddars':
        with open('images/cheddars.gif', "rb") as file:
            fileToSend = discord.File(file, filename='images/cheddars.gif')
        await ctx.send(file=fileToSend)

client.run(TOKEN)