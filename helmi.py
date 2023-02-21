# author @andrwclnln
# v1.0
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
    'sqeuaksqueaksqueak',
    '*chatter*',
    '*bite*',
    '*bites toe*',
    '*angry noises*',
    ]

    response = random.choice(helmiMessages)
    await ctx.send(response)

client.run(TOKEN)