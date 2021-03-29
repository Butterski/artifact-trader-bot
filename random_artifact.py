import json
import random


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
        print(f'Name: {random_artifact["name"]}, Price: {price}')  # prints item id and name


for i in range(100):
    generate_random_artifact()
