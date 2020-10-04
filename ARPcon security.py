import discord
import asyncio

token = "NzYyMTkzNzkzMjU2MjU5NTg2.X3lmSQ.uDHYR-cmckeDH9ITa637yT5WXeQ"
client = discord.Client()
@client.event
async def on_ready():
	print(f'{client.user} has connected to Discord!')

@client.event
async def on_member_join(member):
	await member.create_dm()
	await member.dm_channel.send(
		f'Hi {member.name}, welcome to my Discord server!'
	)
    
@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if message.content.startswith('$hello'):
	    await message.channel.send('Hello!')

client.run(token)