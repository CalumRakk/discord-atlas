import discord
import os
from googlesearch import search

class MyClient(discord.Client):
    async def on_ready(self):
        print(f"Logged in as {self.user} (ID: {self.user.id})")
        print("------")

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.lower().startswith("!atlas"):
            command, text= message.content.split(" ", 1)
            resultados= search(f"{text} AND python", num_results=5, advanced=True, lang="es")

            for index, resultado in enumerate(resultados):
                if index==0:
                    embed=discord.Embed(title=resultado.title, url=resultado.url, description=resultado.description, color=0xFF5733)
                else:
                    embed.add_field(name=str(index),value=f"[{resultado.title}]({resultado.url})", inline=False)

            await message.channel.send(embed=embed)
          
intents = discord.Intents.default()
intents.message_content = True

TOKEN = os.environ["TOKEN_BOT_DISCORD"]
client = MyClient(intents=intents)
client.run(TOKEN)
