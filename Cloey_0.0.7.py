import discord
import asyncio


client = discord.Client()

@client.event
async def on_ready():
    print("login")
    print(client.user.name)
    print(client.user.id)
    print("-----------")
    await client.change_presence(game=discord.Game(name='DM me for help!', type=0))


@client.event
async def on_message(message):
    if message.channel.is_private and message.author.id != "536552480834715658":
        await client.send_message(client.get_channel("569107894843211776"), message.author.name + "(" + message.author.id + ") : " + message.content)

    if message.content.startswith('!dm'):
        member = discord.utils.get(client.get_all_members(), id=message.content[4:22])
        embed = discord.Embed(color=0x5aaeff)
        embed.add_field(name="답변", value=message.author.name)
        embed.add_field(name="내용", value=message.content[23:])
        embed.set_thumbnail(url=message.author.avatar_url)
        await client.send_message(member, embed=embed)
        

        
client.run('NTM2NTUyNDgwODM0NzE1NjU4.XLr1mg.QsDCYd1xEIWyPxC38zWKBWGJGWQ')
