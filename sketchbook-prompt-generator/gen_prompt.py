'''
Program that randomly selects a prompt from a category.
The categories are cycled through in the order:
    - person
    - object
    - drink
    - animal
    - food
    - plant
    - person
    - scenery
    - animal
The person category is made up of sub categories that are cycled through in the order:
    - anatomy
    - characterdesign
    - pose
If the subcat is characterdesign then two emotions are also generated with it.
'''
import json
from os import listdir
from os.path import isfile, join
import random
import webbrowser

person_subcat = ["anatomy","characterdesign","pose"]
prompt_order = ["person", "object", "drink", "animal", "food", "plant", "plant",
                "person", "scenery", "animal"]
'''
Function that resets the unused prompts to the orignal list.
Parameters: listname(str)
Return: {
    "prev_prompts":[]
    "prev_person": "str",
    "anatomy": [],
    "animal": [],
    "characterdesign": [],
    "drink": [],
    "emotion": [],
    "food": [],
    "object": [],
    "plant": [],
    "pose": [],
    "scenery": [],
    }
'''
def reset_prompt_list(listname):
    dir = "prompts/"
    ogListFile = open(dir+listname+".json", "r+")
    original_list = json.load(ogListFile)
    dataFile = open("data.json", "r+")
    data = json.load(dataFile)
    data[listname] = original_list
    jsonFile = open("data.json", "w+")
    jsonFile.write(json.dumps(data, indent=2))
    return data

'''
Function that resets the unused prompts to the orignal list.
Parameters: listname(str)
Return: None
'''
def reset_all():
    prompt_file_names = [f[:-5] for f in listdir("prompts/") if isfile(join("prompts/", f))]
    for l in prompt_file_names:
        reset_prompt_list(l)
'''
Function that brings up reference images based on prompt and prompt category
Parameters: prompt(str), listname(str)
Return: None
'''
def search_reference(prompt, category):
    base_url = "https://www.pinterest.com.au/search/pins/?q="
    prompt = prompt.replace(" ", "%20")
    prompt = prompt.replace("''", "%27")
    url = base_url + prompt + "%20" + category + "%20" + "reference"
    webbrowser.open(url)
'''
Function which cycles to the next prompt category and randomly selects a prompt.
Parameters: None
Return: None
'''
def main():
    # get previous 2 prompts
    dataFile = open("data.json", "r+")
    data = json.load(dataFile)
    prev_prompt = data["prev_prompts"]
    next_prompt = None

    # get the next prompt
    if len(prev_prompt) == 0:
        # if there isn't anything start with person prompt
        next_prompt = "person"
        data["prev_prompts"].append("person")
    elif len(prev_prompt) < 1:
        next_prompt = "object"
        data["prev_prompts"].append("object")
    else:
        # find location in the prompt order and generate next prompt
        for i in range(1, len(prompt_order)):
            if prompt_order[i-1] == prev_prompt[0] and prompt_order[i] == prev_prompt[1]:
                if i == len(prompt_order)-1:
                    next_prompt = prompt_order[0]
                else:
                    next_prompt = prompt_order[i+1]
                break
            elif i == len(prompt_order)-1:
                next_prompt = "object"
        data["prev_prompts"][0] = prev_prompt[1]
        data["prev_prompts"][1] = next_prompt

    if (next_prompt == "person"):
        # get previous person subcat
        i = person_subcat.index(data["prev_person"])
        if i == len(person_subcat)-1:
            p = person_subcat[0]
        else:
            p = person_subcat[i+1]

        data["prev_person"] = p
        if len(data[p]) < 1: data = reset_prompt_list(p)
        prompt = random.choice(data[p])
        data[p].remove(prompt)

        if p == "characterdesign":
            if len(data["emotion"]) < 2: data = reset_prompt_list("emotion")
            emote = random.choices(data["emotion"], k=2)
            for e in emote: data["emotion"].remove(e)
            prompt = f"{prompt} experiencing {emote[0]} and {emote[1]}"
    else:
        if len(data[next_prompt]) < 1: data = reset_prompt_list(next_prompt)
        prompt = random.choice(data[next_prompt])
        data[next_prompt].remove(prompt)

    # update data file
    jsonFile = open("data.json", "w+")
    jsonFile.write(json.dumps(data, indent=2))

    # print prompt and bring up reference images
    print(f"Today's prompt is: {prompt}.")
    search_reference(prompt, next_prompt)

main()
