import os
import json
directory = "prompts/"

for filename in os.listdir(directory):
    if filename.endswith(".json"):
        jsonFile = open(directory+filename, "r+")
        data = json.load(jsonFile)
        updated_data = [str.lower() for str in data]
        updated_data = sorted(updated_data)
        jsonFile = open(directory+filename, "w+")
        jsonFile.write(json.dumps(updated_data, indent=2))
        continue
