
import discord
import random
from discord.ext import commands
import os

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.lower().startswith('!atlas'):    
            while True:
                pregunta= random.choice(preguntas)
                if pregunta not in preguntas_enviadas:
                    preguntas_enviadas.append(pregunta)
                    await message.channel.send(pregunta)
                    break               
                
                check= [ pregunta in preguntas for pregunta in preguntas]
                if all(check):
                    preguntas_enviadas.clear()


preguntas_enviadas=[]  
with open("preguntas.txt","r", encoding="utf-8") as f:
    preguntas= f.read().splitlines()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)
TOKEN= os.environ["TOKEN_BOT_DISCORD"]
client = MyClient(intents=intents)
client.run(TOKEN)