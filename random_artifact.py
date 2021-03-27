import json
import random


def generate_random_artifact(how_many):
    if __name__ == "__main__":
        with open('artifacts.json') as artifact_file:  # open file as data variable
            data = json.load(artifact_file)

        for i in range(how_many):
            random_artifact = random.choice(data["artifacts"])
            print(f'ID: {random_artifact["id"]}, Name: {random_artifact["name"]}')


generate_random_artifact(3)
