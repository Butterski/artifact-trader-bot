import json


def print_artifacts():
    if __name__ == "__main__":
        with open('artifacts.json') as artifact_file:               # open file as data variable
          data = json.load(artifact_file)

        print("List of all Artifacts:")
        for item in data["artifacts"]:                              # prints all artifacts id and name
            print(f'ID: {item["id"]}, Name: {item["name"]} ')


print_artifacts()
