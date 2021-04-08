import discord
from discord.ext import commands
import json
import time
from datetime import date
import random
import requests


with open('artifacts.json') as artifact_file:  # open file as data variable
    data = json.load(artifact_file)

msg_dump_channel = 828717938231476285
testing_guild = 825400163504750593

"""
1-40 - common
41-70 - rare
71-90 - epic
91-100 - legendary 
"""


def generate_random_artifact():
    if __name__ == "__main__":
        def price_modifier(price):
            mod_range = price * 0.35
            price_modify = random.randrange(int(-mod_range), int(mod_range))
            price = price + price_modify
            return price

        rarity = random.randrange(1, 100)

        if 1 <= rarity <= 40:
            random_artifact = random.choice(data["artifacts"]["general"]["rarity"]["common"])
            embed_color = 0x1eff00

        elif 41 <= rarity <= 70:
            random_artifact = random.choice(data["artifacts"]["general"]["rarity"]["rare"])
            embed_color = 0x0070dd

        elif 71 <= rarity <= 90:
            random_artifact = random.choice(data["artifacts"]["general"]["rarity"]["epic"])
            embed_color = 0xa335ee

        elif 91 <= rarity <= 100:
            random_artifact = random.choice(data["artifacts"]["general"]["rarity"]["legendary"])
            embed_color = 0xff8000

        price = int(random_artifact["price"])
        price_after = price_modifier(price)
        name = random_artifact["name"]
        description = random_artifact["description"]
        return name, price_after, description, embed_color


client = commands.Bot(command_prefix='$', intents=discord.Intents.all(), help_command=None)


@client.event
async def on_ready():
    print('Logged on as ', client.user.name, client.user.id)
    print("Date: ", date.today())

    await client.change_presence(status=discord.Status.online, activity=discord.Game('$help - for commands'))


@client.command()
async def help(ctx):
    author = ctx.message.author
    embed = discord.Embed(title="General ", color=0x491fe0)
    embed.set_author(name="Help")
    embed.add_field(name="`$help`", value="Shows you this message :)", inline=True)
    embed.add_field(name="-",
                    value="-", inline=False)
    embed.add_field(name="`$gen_offer [x]`",
                    value="Generates your offers where [x] is how many offers should it generate", inline=True)
    embed.add_field(name="-",
                    value="-", inline=False)
    embed.add_field(name="`$s [suggestion]`, `$sugg [suggestion]`, `$suggestion [suggestion]`",
                    value="Send this command as private message and submit your suggestion :)", inline=True)
    embed.set_footer(text="Please send suggestions ")
    await ctx.send(embed=embed)


@client.command()
async def gen_offer(ctx, how_many=1):
    if int(how_many) > 15:
        how_many = 15
    for i in range(int(how_many)):
        name, price, description, embed_color = generate_random_artifact()
        embed = discord.Embed(title='Here is my offer for you today',
                              color=embed_color
                              )
        embed.add_field(name="Name:", value=f'**{name}**', inline=True)
        embed.add_field(name="Price:", value=f'**{price}**', inline=True)
        embed.add_field(name="Description:", value=f'{str(description)}', inline=False)
        embed.set_thumbnail(
            url='https://cdn.discordapp.com/attachments/721846941926817924/825500010174480384/avatar.png')
        embed.set_footer(text="Please DM me any sugestions about the bot")
        await ctx.send(embed=embed)


# tylko rzeczy pisane po $suggestion są wkładane do sugesti
@client.command(pass_context=True, aliases=['s', 'sugg'])
async def suggestion(ctx, *, sugg):
    channel = client.get_channel(msg_dump_channel)
    if ctx.guild is None and not ctx.author.bot:
        # if the channel is public at all, make sure to sanitize this first
        embed_sugg = discord.Embed(title="Sugestia ⚠", description=sugg)
        embed_sugg.set_thumbnail(
            url=ctx.author.avatar_url)
        embed_sugg.set_author(name=ctx.author.name)
        message = await channel.send(embed=embed_sugg)
        emojis = ['📨', '🗑️']
        for emoji in emojis:
            react = await message.add_reaction(emoji)
        await ctx.send("Thank you for your suggestion! :blush: It will be send to our dev team :man_technologist:")


@client.event
async def on_reaction_add(reaction, user):
    if reaction.message.channel.id == 828717938231476285:
        reactions = reaction.message.reactions
        reaction_message_id = reaction.message.id
        for reacts in reactions:
            if reacts.emoji == '📨' and reacts.count > 1:
                await reaction.remove(user)
                todo_channel = client.get_channel(826401709798588436)
                channel = client.get_channel(828717938231476285)
                msg = await channel.fetch_message(reaction_message_id)
                await todo_channel.send(embed=msg.embeds[0])
            if reacts.emoji == '🗑️' and reacts.count > 1:
                await reaction.message.delete()


"""
Wszystko co jest pisane jest wkładane jako sugestia

@client.event
async def on_message(message: discord.Message):
    channel = client.get_channel(msg_dump_channel)
    if message.guild is None and not message.author.bot:
        # if the channel is public at all, make sure to sanitize this first
        embed_sugg = discord.Embed(title="Sugestia ⚠", description=message.content)
        embed_sugg.set_thumbnail(
            url=message.author.avatar_url)
        embed_sugg.set_author(name=message.author.name)
        await channel.send(embed=embed_sugg)
    await client.process_commands(message)
    """

client.run('ODI0OTcwOTEyMzgyMTg5NTcx.YF3ICA.xpeeRYRiLaA24YZw1TgxSWRh5Uo')

