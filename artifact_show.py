import json

def print_artifacts():
    if __name__ == "__main__":
        with open('artifacts.json') as artifact_file:
          data = json.load(artifact_file)

        print("List of all Artifacts:")
        for i in data["artifacts"]:
            print(f'ID: {i["id"]}, Name: {i["name"]} , Price: {i["price"]}, ')

print_artifacts()