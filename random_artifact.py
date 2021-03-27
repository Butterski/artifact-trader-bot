import json
import random


with open('artifacts.json') as artifact_file:  # open file as data variable
    data = json.load(artifact_file)


def price_modify():
    price_modifier = random.randrange(-100, 100)
    return price_modifier


def generate_random_artifact(price_modifier):
    if __name__ == "__main__":
        random_artifact = random.choice(data["artifacts"])   # save items informations
        price = random_artifact["price"] + price_modifier
        if price < 1:
            price = random_artifact["price"]
        print(f'ID: {random_artifact["id"]}, Name: {random_artifact["name"]}, Price: {price}')  # prints item id and name


for i in range(5):
    price_modificator = price_modify()
    generate_random_artifact(price_modificator)
