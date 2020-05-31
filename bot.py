import discord
import os
from mcstatus import MinecraftServer
from datetime import datetime
from discord.ext import tasks

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
MC_SERVER_ADDRESS = os.getenv('MC_SERVER_ADDRESS')

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
        self.check_server.start()

    @tasks.loop(seconds=5.0)
    async def check_server(self):
        await self.wait_until_ready()
        online = False
        try:
            server = MinecraftServer.lookup(MC_SERVER_ADDRESS)
            server_status = server.status()
            online = True
        except:
            pass

        await self.update_server_presence(online)
    
    async def update_server_presence(self, online):
        status = (discord.Status.dnd, discord.Status.online)[online]
        emoji = ('\U000026D4', '\U00002705')[online]
        activity = discord.Game(name='Minecraft Server ' + emoji)
        await self.change_presence(status=status, activity=discord.Game(name=activity))

client = MyClient()

client.run(DISCORD_TOKEN)