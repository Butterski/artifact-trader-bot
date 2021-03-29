import discord
from discord.ext import commands
import json
import time
from datetime import date
import random
import requests

with open('artifacts.json') as artifact_file:  # open file as data variable
    data = json.load(artifact_file)


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
            price_modify = random.randrange((mod_range * -1), mod_range)
            price = price + price_modify
            return price

        rarity = random.randrange(1, 100)

        if 1 <= rarity <= 40:
            random_artifact = random.choice(data["artifacts"]["rarity"]["common"])

        elif 41 <= rarity <= 70:
            random_artifact = random.choice(data["artifacts"]["rarity"]["rare"])

        elif 71 <= rarity <= 90:
            random_artifact = random.choice(data["artifacts"]["rarity"]["epic"])

        elif 91 <= rarity <= 100:
            random_artifact = random.choice(data["artifacts"]["rarity"]["legendary"])

        price = random_artifact["price"]
        price = price_modifier(price)
        name = random_artifact["name"]
        curse = random_artifact["curse"]
        effect = random_artifact["effect"]
        return name, price, effect, curse


client = commands.Bot(command_prefix='$')


@client.event
async def on_ready():
    print('Logged on as ', client.user.name, client.user.id)
    print("Date: ", date.today())
    print('-----------------------------------------------')
    await client.change_presence(status=discord.Status.online, activity=discord.Game('stall'))


@client.command()
async def gen_offer(ctx, how_many):
    if int(how_many) > 5:
        how_many = 5
    for i in range(int(how_many)):
        name, price, effect, curse = generate_random_artifact()
        embed = discord.Embed(title='Here is my offer for you today',
                              color=0x654321
                              )
        embed.add_field(name="Name:", value=f'**{name}**', inline=True)
        embed.add_field(name="Price:", value=f'**{price}**', inline=True)
        embed.add_field(name="Description:", value=f'{effect}', inline=False)
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/721846941926817924/825500010174480384/avatar.png')
        await ctx.send(embed=embed)


client.run('ODI0OTcwOTEyMzgyMTg5NTcx.YF3ICA.xpeeRYRiLaA24YZw1TgxSWRh5Uo')

