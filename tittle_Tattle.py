import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import time
import threading
from threading import Timer

TOKEN = 'NTMwNzEzNzM0NDY1ODQ3MzI3.Dx7sdw.EVibNa0-zQxxzzZPKXhglBg1jPg'

bot = discord.Client()
client = commands.Bot(command_prefix = '!')

global user_ID
global channel_New

@client.event
#Check to see if bot is connected
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    #message to create new channel
    #   enter as "!create @user_ID"
    global channel_New
    global user_ID

    if message.content.upper().startswith('!CREATE'):

        channel = message.channel
        server = message.server
        author = message.author

        try:
            user_Temp = message.mentions[0]
            #If the Tittle creates a channel
            if client.user.mentioned_in(message):
                await client.send_message(channel, "Wow, ok, rude!")
            elif author == user_ID:
                await client.send_message(channel, "Don't be a ninny")
            #if the Tittle is already being talked about
            elif user_Temp == user_ID:
                await client.send_message(channel, "Can't handel that much shit about " + str(user_ID))
            #Anything else
            elif channel_New is not None:
                await client.send_message(channel, "Loose Lips Sink Ships")
            else:
                await channel_create(user_Temp, server, channel)
        #only when channel_New is None
        except NameError as error:
            await channel_create(user_Temp, server, channel)
            #error if author did not mention a user
        except IndexError as error:
                    await client.send_message(channel, 'Who do you wanna gossip about?')

    if message.content.upper().startswith('!DELETE'):
        print(channel_New)
        await client.delete_channel(channel_New)
        await client.send_message(message.channel, 'The tittling on '+ user_ID.mention + " has stopped.")
        channel_New  = None
        user_ID = None
    if message.content.upper().startswith('!TEST'):
        print(channel_New)
        print(user_ID)
    #check to see if a message was heard
    print('Message deteced')
    #checks to see if there is a command to run
    await client.process_commands(message)

#creates the channel
async def channel_create(user, server, channel):
    global user_ID
    global channel_New

    user_ID = user
    overwrite = discord.PermissionOverwrite(read_messages=False, manage_channels=False)
    channel_New =  await client.create_channel(server, 'Tattle about ' + str(user_ID), (user_ID, overwrite))
    await client.send_message(channel, 'Start tattling about ' + user_ID.mention)
    await delete(channel_New)

#deletes the channel
async def delete(channel):
    global channel_New
    global user_ID

    await asyncio.sleep(60)
    print(str(channel))
    await client.send_message(channel, 'just Stahp it!')
    await asyncio.sleep(60)
    await client.send_message(channel, 'The tittling on '+ user_ID.mention + " has stopped.")
    await asyncio.sleep(2)
    await client.delete_channel(channel_New)
    #await client.send_message(bot-spam, 'The tittling on '+user_ID.mention + " has stopped.")


    #reset the channel name and user
    channel_New  = None
    user_ID = None

async def the_Tattle():
    #adding the Tattler to DB
    print()
async def the_Tittle():
    #adding the tittle to DB
    Print()

client.run(TOKEN)
