#!/usr/bin/python3
# bot.py

import discord
import bot_functions

client = discord.Client()
tokenFile = open("../vitaminarm.txt")
tokenString = tokenFile.readline()


@client.event
async def on_ready():
    print('logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('$password'):
        password = bot_functions.passwordgen()
        await message.channel.send(password)

    if message.content.startswith('$dice'):
        diceMessage = message.content.split(" ")
        diceInput = diceMessage[1]
        roll = bot_functions.diceroll(diceInput)
        await message.channel.send(roll)

print("using Token:" + tokenString)
client.run(tokenString)
