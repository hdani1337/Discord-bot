import discord
import asyncio
from discord.ext import commands

client = discord.Client()
token = open("token.txt","r").read()

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name="Hello world!"))
    print(f"Kliensbot készen áll.")

@client.event
async def on_message(message):
    print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")
    if message.author == client.user: 
        if f"Ezt nyomatom" in message.content:
            txt = f"{message.content}"
            txt = txt.replace("Ezt nyomatom: ","")
            await client.change_presence(game=discord.Game(name=f"{txt}"))
            #A jelenleg játszott számot írja ki az állapotába

        else:
            return
            #Ne válaszoljon magának

    #Válaszolgatások
    if f"hi there" == message.content.lower():
        await message.channel.send(f"Hi {message.author.name}!")

    if f"teszt" == message.content.lower():
        await message.channel.send(f"Itt vagyok!")

    if f"hello" == message.content.lower():
        await message.channel.send(f"Szia {message.author.name}!")

    if f"szia" == message.content.lower():
        await message.channel.send(f"Hali {message.author.name}!")

    if f"hi" == message.content.lower():
        await message.channel.send(f"Hello {message.author.name}!")

    if f"kurva anyád" in message.content.lower():
        await message.channel.send(f"A tiédet.")

    if f"szeretlek" == message.content.lower():
        await message.channel.send(f"Én is téged.")

    if f"dáh" == message.content.lower():
        await message.channel.send(f"Úgybiza")

    if f"játszani?" in message.content.lower():
        await message.channel.send(f"Inkább tanulj egy kis hálózatot: http://tuskeb.duckdns.org/halozatok/")

    if f"cyka" == message.content.lower():
        await message.channel.send(f"BLYAAAAAAAAAAAT")

    if f"morgen" == message.content.lower():
        await message.channel.send(f"Dáh.")

    if f"dugnálak" == message.content.lower():
        await message.channel.send(f"Én is téged.")

    if f"volt házi?" == message.content.lower():
        await message.channel.send(f"A kérdést sem értem.")

    if f"xd" in message.content.lower():
        await message.channel.send(f"Nevetel?\nNe neveteljé.")

    #Parancsok
    if f"status" in message.content:
        txt = f"{message.content}"
        txt = txt.replace("status: ","")
        await client.change_presence(game=discord.Game(name=f"{txt}"))
        await message.channel.send(f"Mostantól ezzel játszok: {txt}")
        #Egyedi értéket ír ki az állapotba

    if f".stop" == message.content:
        await client.change_presence(game=discord.Game(name="Hello world!"))
        #Playinget rakja vissza ha leállítják a zenét

    if f"alexa, stop" == message.content:
        await client.change_presence(game=discord.Game(name="Hello world!"))
        #Playinget rakja vissza ha leállítják a zenét

    if f"<@!504234841110216704> stop" == message.content:
        await client.change_presence(game=discord.Game(name="Hello world!"))
        #Playinget rakja vissza ha leállítják a zenét

    if f"danibot.help" == message.content.lower():
        await message.channel.send(f"A következő módokon adhatsz nekem parancsokat:\n - Megjelölsz (mention)\n - Egy ponttal (.)\n - Alexa szóval\n\nMik is a parancsok?\n - Termétszetesen válaszolok az üzenetekre, ez a funkcióm bővülni fog idővel egy mesterségeis inteligenciává\n - play szóval zenét játszok le\n - stop szóval kilépek a voice channelből\n - join szóval belépek a voice channelbe\n\nIgyekszem több funkciót beépíteni ebbe a botba, hogy ez az egy kiszolgálhassa az egész szervert (zenelejátszás, képküldés, nsfw, mesterséges intelligencia). Talán eljutok oda, hogy 7/24-ben futhasson, ne csak akkor, amikor foglalkozok vele.")

    if f"danibot.logout()" == message.content.lower():
        await client.close()
        #Kijelentkezés

    if f"danibot.community_report()" == message.content.lower():
        online = 0
        idle = 0
        offline = 0

        for m in client.get_guild(528996170488479798).members:
            if str(m.status) == "online":
                online += 1
            if str(m.status) == "offline":
                offline += 1
            else:
                idle += 1

        await message.channel.send(f"Elérhető: {online}.\nTávol vagy Elfoglalt: {idle}.\nOffline: {offline}")
        #Hány ember online, távol/elfoglalt vagy offline

        
    if f"danibot.member_count()" in message.content.lower():
        await message.channel.send(f"{client.get_guild(528996170488479798).member_count} tagja van a szervernek.")
        #Hány tagja van a szervernek

client.run(token)
