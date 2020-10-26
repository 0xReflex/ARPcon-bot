import discord
import asyncio
from discord.ext.commands import Bot
 
token = "NzYyMTkzNzkzMjU2MjU5NTg2.X3lmSQ.N4hE2oY4N-OMVAFopNbh5SmYcEs"
client = Bot(command_prefix = '.')

@client.event
async def on_ready():
	print(f'Bot connected as {client.user}')
	await client.change_presence(activity = discord.Game('Pubg'))

@client.command(name='server', help='Gives Server Information')

async def fetchServerInfo(ctx):
	await ctx.send(f'Server Name: {ctx.guild.name}')
	await ctx.send(f'Server Size: {ctx.guild}')
	await ctx.send(f'Active People:{len(ctx.guild.member_count)}')

# async def on_message(message):
# 	if message.content == 'test':
# 		await message.channel.send('Testing 1 2 3!')




@client.command(name='ping', help='Tells you about your ping')
async def ping(ctx):
    await ctx.send(f'Pong! {round (client.latency * 1000)}ms ')




#client = discord.Client()
# @client.event
# async def on_ready():print(ctx.guild.member_count)print(ctx.guild.member_count)
# 	print(f'{client.user} has connected to Discord!')

# @client.event
# async def on_member_join(member):
# 	await member.create_dm()
# 	await member.dm_channel.send(
# 		f'Hi {member.name}, welcome to my Discord server!'
# 	)
    
# @client.event
# async def on_message(message):
# 	if message.author == client.user:
# 		return
 
# 	if message.content.startswith('$hello'):
# 	    await message.send('Hello!')

client.run(token)