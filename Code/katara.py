import discord
from discord.ext import commands
import numpy as np
import logging

logging.basicConfig(level=logging.INFO)

token = bytearray.fromhex('4f4449774d5441784d54457a4e6a41774e6a63784e7a51302e5945775172672e346b45796d6359313850684d4162494c686f6a706f764168435863').decode()
owner = int('0x1ba105773420000', 0)
prefix = '.'
client = commands.Bot(command_prefix = prefix)
with open('C:\\Google Drive\\Coursera\\Data-driven Astronomy\\Code\\Resources\\bakamitai.txt', 'r') as file:
    bakamitai = file.read()

def connect():
	
	@client.event
	async def on_ready():
		print('We have logged in as {0.user}'.format(client))


def comds():
	
	@client.listen()
	async def on_message(message):
		if message.content.startswith(prefix + 'hello'):
			await message.channel.send('Hello! ' + message.author.mention)
			print('Hello')
			print(message.author)
			reply = message.author.mention
			with open("reply.txt", "w") as file:
				file.write(reply)

		if message.content.startswith(prefix + 'who'):
				with open("reply.txt", "r") as file:
					reply = file.readline()
					print(file.readline())
				await message.channel.send('Its that nigga! ' + reply)
				print('Nigga')
				print(reply)


	@client.listen()
	async def on_message(message):
		if message.content.startswith('Bakamitai'):
			await message.channel.send(bakamitai)	
			print('bakamitai')
			print(message.author)


def close():

	@client.listen()
	async def on_message(message):
		if message.author.id == owner:
			if message.content.startswith('close'):
				await client.close()
				print('close')
				print(message.author)


	

def main():
	connect()
	comds()
	close()
	client.run(token)



if __name__ == '__main__':

	main()

		
