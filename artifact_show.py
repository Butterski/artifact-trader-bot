import json

def print_artifacts():
    if __name__ == "__main__":
        with open('artifacts.json') as artifact_file:
          data = json.load(artifact_file)

        print("List of all Artifacts:")
        for item in data["artifacts"]:
            print(f'ID: {item["id"]}, Name: {item["name"]} ')

print_artifacts()