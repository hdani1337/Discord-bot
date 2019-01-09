import discord
import asyncio
import json
from discord.ext import commands

client = discord.Client()

@client.event
async def on_ready():
    print("Level bot kész.")

@client.event
async def on_member_join(member):
    with open("users.json", "r") as f:
            users = json.load(f)

            await update_data(users, member)

            with open("users.json", "w") as f:
                json.dump(users, f)
@client.event
async def on_message(message):
    with open("users.json", "r") as f:
        users = json.load(f)

    await update_data(users, message.author)
    await add_experience(users, message.author, 5)
    await level_up(users, message.author, message.channel)

    with open("users.json", "w") as f:
        json.dump(users, f)

async def update_data(users, user):
    if user == client.user:
        return
    
    if user.id in users:
        return

    if not user.id in users:
        users[user.id] = {}
        users[user.id]["experience"] = 0
        users[user.id]["level"] = 1
        users[user.id] = "\n"
    
async def add_experience(users, user, exp):
    if user == client.user:
        return
    
    if user.id in users:
        xp = users[user.id]["experience"] + exp
        users[user.id]["experience"] = xp

    if not user.id in users:
        return

async def level_up(users, user, message):
    experience = users[user.id]["experience"]
    lvl_start = users[user.id]["level"]
    lvl_end = int(experience * (1/4))

    if lvl_start < lvl_end:
        await message.channel.send("{} elérte a {} szintet.".format(user.mention, lvl_end))
        users[user.id]["level"] = lvl_end

client.run("NTA0MjM0ODQxMTEwMjE2NzA0.DrCH5w.JBOZwiY-nxqV8JUpZD3QKog3ZOk")