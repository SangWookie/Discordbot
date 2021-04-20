import discord
import os
import emoji
from keep_alive import keep_alive
import re

client = discord.Client()

@client.event
async def on_ready():
    print("다음으로 로그인합니다")
    print(client.user.name)
    print(client.user.id)
    print("================")
    await client.change_presence(activity=discord.Game(name="I can counter MinJae 딱대~"))

@client.event
async def on_message(message):
    danger_cnt = 0
    custom_emojis = re.findall(r'<:\w*:\d*>', message.content)
    custom_emojis = [int(e.split(':')[1].replace('>', '')) for e in custom_emojis]
    custom_emojis = [discord.utils.get(client.get_all_emojis(), id=e) for e in custom_emojis]
    danger_cnt += len(custom_emojis)
    print(danger_cnt)

    if message.author.bot: # 메세지를 보낸 사람이 봇일 경우 무시한다
        return None
    
    if any(str(emoji) in message.content for emoji in message.guild.emojis):
      danger_cnt = danger_cnt + 1
      print("custom emoji detected")
      if(danger_cnt > 1) :
        message.delete()
    

    if message.content.rfind('민재') != -1:
        msg = "Hazardous word detected! Choose your words carefully!"
        channel = message.channel
        await channel.send(msg)
        return None

    if message.content.startswith('!hi'):
        channel = message.channel
        await channel.send('Hello world!')
    
    
    print(custom_emojis)
    
    print(message.content)

keep_alive()
client.run(os.environ['TOKENs'])

