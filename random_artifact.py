import json
import random


with open('artifacts.json') as artifact_file:  # open file as data variable
    data = json.load(artifact_file)


def price_modify():
    price_modifier = random.randrange(-100, 100)
    return price_modifier


"""
1-40 - common
41-70 - rare
71-90 - epic
91-100 - legendary 
"""


def generate_random_artifact(price_modificator):
    if __name__ == "__main__":
        rarity = random.randrange(1, 100)
        if 1 <= rarity <= 40:
            random_artifact = random.choice(data["artifacts"]["rarity"]["common"])

        elif 41 <= rarity <= 70:
            random_artifact = random.choice(data["artifacts"]["rarity"]["rare"])

        elif 71 <= rarity <= 90:
            random_artifact = random.choice(data["artifacts"]["rarity"]["epic"])

        elif 91 <= rarity <= 100:
            random_artifact = random.choice(data["artifacts"]["rarity"]["legendary"])

        price = random_artifact["price"] + price_modificator
        if price < 1:
            price = random_artifact["price"]
        print(f'Name: {random_artifact["name"]}, Price: {price}')  # prints item id and name

        """
        random_artifact = random.choice(data["artifacts"])   # save items informations
        
        print(f'ID: {random_artifact["id"]}, Name: {random_artifact["name"]}, Price: {price}')  # prints item id and name
        """


for i in range(100):
    price_modificator = price_modify()
    generate_random_artifact(price_modificator)
