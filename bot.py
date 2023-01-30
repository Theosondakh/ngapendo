from email.message import EmailMessage, Message
from importlib.resources import path
import discord
from discord.ext import commands
import requests
import os
from os import system
import subprocess
import shutil

token = "MTA0ODEyMjE3NDkwMjM3MDQxNA.GH5Sl8.CRka6UM2dOS3qZ8NXSBXMQlspnSf4WidQA1-_A"
category_id = 1033369766448082944

file_path = os.path.abspath(os.path.dirname(__file__))

bot = commands.Bot(command_prefix="+")
bot.remove_command("help")

def obfuscation(path, filename, author):
    copy = f"{file_path}\\obfuscated\\{filename}"

    #removing duplicates
    if os.path.exists(copy):
        os.remove(copy)

    #copying uploaded one to make operations on it
    shutil.copyfile(path, copy)

    #copying obfuscate file to copied one
    text_file = open(f"{file_path}\\obfuscate.lua", "r")
    data = text_file.read()
    text_file.close()
    f = open(copy, "a")
    f.truncate(0)
    f.write(data)
    f.close()

    #writing upload file into obfuscation script
    originalupload = open(path, "r")
    originalupload_data = originalupload.read()
    originalupload.close()

    with open(copy, "r") as in_file:
        buf = in_file.readlines()

    with open(copy, "w") as out_file:
        for line in buf:
            if line == "--SCRIPT\n":
                line = line + originalupload_data + '\n'
            out_file.write(line)

    #executing script and making new file with obfuscated output
    output = subprocess.getoutput(f'lua {copy}')

    if os.path.exists(f"{file_path}\\obfuscated\\Encrypted_{filename}"):
        os.remove(f"{file_path}\\obfuscated\\Encrypted_{filename}")

    f = open(f"{file_path}\\obfuscated\\Encrypted_{filename}", "a")
    f.write(output)
    f.close()

    os.remove(copy)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="TSSK SERVICE", url="https://www.twitch.tv/theosondakh"))
    print(f"{bot.user} is online ✔️")
    

@bot.listen('on_message') 
async def on_message(message):
        if message.content == "-help":
            await message.channel.send('```UPLOAD YOUR FILE IN HERE AND BOT AUTOMATIC TO ENC YOUR FILE \n[ NOTE!!! : Only .lua ]``` ', reference=message,delete_after=10.0)

@bot.listen('on_message') 
async def stuff(message):
    if message.channel.category.id == category_id:
        if message.content.startswith("prefix"):
            msg = await message.channel.send( '**_my prefix is_ `-`**',delete_after=5.0)
@bot.event
async def on_message(message):
    channel = str(message.channel)
    author = str(message.author)
    channel = bot.get_channel(message.channel.id)
    
    try:
        url = message.attachments[0].url
        filename = str(message.attachments[0].filename)
        if not message.author.bot:
            if message.channel.category is not None:
                if message.channel.category.id == category_id:
                    if message.attachments[0].url:
                        if '.lua' not in url:
                            embed=discord.Embed(title=f"***Wrong file extension!***", description=f"only ``.lua`` allowed", color=0xFF3357)
                            message = await channel.send(embed=embed)
                        else:
                            uploads_dir = f"{file_path}\\uploads\\"
                            obfuscated_dir = f"{file_path}\\obfuscated\\"

                        if not os.path.exists(uploads_dir):
                            os.makedirs(uploads_dir)
                        if not os.path.exists(obfuscated_dir):
                            os.makedirs(obfuscated_dir)
                            
                        print(f'\nNew lua script received from {author}.')
                        print(f'Attachment Link: {message.attachments[0].url}\n')
                        response = requests.get(url)
                        path = f"{file_path}\\uploads\\{filename}"

                        if os.path.exists(path):
                            os.remove(path)

                        open(path, "wb").write(response.content)
                        obfuscation(path, filename, author)
                        embed=discord.Embed(title="_File has been obfuscated By TSSK#2005_", description=f"THANKS FOR USE MY SERVICE \n 👑 {author} 👑 ", color=0xFF3357)
                        await channel.send(embed=embed, file=discord.File(f"{file_path}\\obfuscated\\Encrypted_{filename}"))
    except:
        pass

bot.run(token)

 