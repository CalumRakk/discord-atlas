

import discord
from discord import app_commands
from discord.ext import commands
from googlesearch import search

import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    synced= await bot.tree.sync()
    print("yay",len(synced))

@bot.tree.command(name="python")
@app_commands.describe(busqueda="buscar el termino de python")
async def hello(interaction: discord.Interaction, busqueda:str):

    resultados= search(f"{busqueda} AND python", num_results=5, advanced=True, lang="es")

    for index, resultado in enumerate(resultados):
        if index==0:
            embed=discord.Embed(title=resultado.title, url=resultado.url, description=resultado.description, color=0xFF5733)
        else:
            embed.add_field(name=str(index),value=f"[{resultado.title}]({resultado.url})", inline=False)

    await interaction.channel.send(embed=embed)

@bot.tree.command(name="javascript")
@app_commands.describe(busqueda="buscar el termino de javascript")
async def hello(interaction: discord.Interaction, busqueda:str):

    resultados= search(f"{busqueda} AND javascript", num_results=5, advanced=True, lang="es")

    for index, resultado in enumerate(resultados):
        if index==0:
            embed=discord.Embed(title=resultado.title, url=resultado.url, description=resultado.description, color=0xFF5733)
        else:
            embed.add_field(name=str(index),value=f"[{resultado.title}]({resultado.url})", inline=False)

    await interaction.channel.send(embed=embed)


TOKEN = os.environ["TOKEN_BOT_DISCORD"]
bot.run(TOKEN)
    
