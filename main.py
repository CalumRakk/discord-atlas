import discord
import random
import os


class MyClient(discord.Client):
    async def on_ready(self):
        print(f"Logged in as {self.user} (ID: {self.user.id})")
        print("------")

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return
        channel_id= message.channel.id
        print(channel_id)
        if preguntas_enviadas.get(channel_id) is None:
            preguntas_enviadas[channel_id] = []

        if message.content.lower().startswith("!atlas"):
            while True:
                pregunta = random.choice(preguntas)
                if pregunta not in preguntas_enviadas[channel_id]:
                    preguntas_enviadas[channel_id].append(pregunta)
                    await message.channel.send(pregunta)
                    break

                check = [pregunta in preguntas for pregunta in preguntas]
                if all(check):
                    preguntas_enviadas[channel_id].clear()


preguntas_enviadas = {}
with open("preguntas.txt", "r", encoding="utf-8") as f:
    preguntas = f.read().splitlines()

intents = discord.Intents.default()
intents.message_content = True

TOKEN = os.environ["TOKEN_BOT_DISCORD"]
client = MyClient(intents=intents)
client.run(TOKEN)
