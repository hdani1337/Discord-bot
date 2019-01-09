@client.event
async def on_message(message):
    print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")
    if message.author == client.user: #Ne válaszoljon magának
        return

    if f"danibot.member_count()" == message.content.lower():
        await message.channel.send(f"{dani_guild.member_count} ember van a szerveren.")

    if f"hi there" in message.content.lower():
        await message.channel.send(f"Hi {message.author.name}!")

    if f"hello" in message.content.lower():
        await message.channel.send(f"Szia {message.author.name}!")

    if f"szia" in message.content.lower():
        await message.channel.send(f"Hali {message.author.name}!")

    if f"hi" in message.content.lower():
        await message.channel.send(f"Hello {message.author.name}!")

    if f"kurva anyád" in message.content.lower():
        await message.channel.send(f"A tiédet.")

    if f"szeretlek" in message.content.lower():
        await message.channel.send(f"Én is téged.")

    if f"dáh" in message.content.lower():
        await message.channel.send(f"Úgybiza")

    if f"játszani?" in message.content.lower():
        await message.channel.send(f"Faszt játszol. Inkább tanulj egy kis hálózatot: http://tuskeb.duckdns.org/halozatok/")

    if f"cyka" in message.content.lower():
        await message.channel.send(f"BLYAAAAAAAAAAAT")

    if f"morgen" in message.content.lower():
        await message.channel.send(f"Dáh.")

    if f"dugnálak" in message.content.lower():
        await message.channel.send(f"Én is téged.")

    if f"alexa, play despacito" in message.content.lower():
        await message.channel.send(f"https://www.youtube.com/watch?v=kJQP7kiw5Fk")

    if f"Volt házi?" in message.content.lower():
        await message.channel.send(f"A kérdést sem értem.")

    if f"xd" in message.content.lower():
        await message.channel.send(f"Nevetel?\nNe neveteljé.")

    elif f"danibot.logout()" in message.content.lower():
        await client.close()

