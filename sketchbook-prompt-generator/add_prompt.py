import os
import json
'''
When run adds new prompt to prompt file and adds to data file.
'''
directory = "prompts/"
promptfiles = os.listdir(directory)
print("The prompt files are: ")
print('\n'.join(promptfiles))
filename = input("Which file would you like to add a prompt to? \nEnter in the format 'filename.json': ")
prompt = input("What prompt would you like to add?: ")

# update prompt list file
jsonFile = open(directory+filename, "r+")
data = json.load(jsonFile)
if prompt not in data:
    prompt.lower()
    data.append(prompt)
    data = sorted(data)
    jsonFile = open(directory+filename, "w+")
    jsonFile.write(json.dumps(data, indent=2))

    # update data file
    dataFile = open("data.json", "r+")
    data = json.load(dataFile)
    data[filename[:-5]].append(prompt)
    data[filename[:-5]] = sorted(data[filename[:-5]])
    jsonFile = open("data.json", "w+")
    jsonFile.write(json.dumps(data, indent=2))
    print(f"{prompt} has been added to '{filename}'.")
else:
    print(f"{prompt} is already in '{filename}'.")
