l""""
Written by Madeline Younes
20/11/2020
Quick Python Revision Program with the added benfit of annoying people.
I have not read homestuck and have no idea the autheticity or the accuracy of
the program written.
"""

print(f"""Hey, so you wanna troll with homestuck type quirks\nPick your style.
        Karkat Vantas [kv]
        Terezi Pyrope [tp]
        Tavros Nitram [tn]
        Aradia Megido [am]
        Sollux Captor [sc]
        Nepeta Leijon [nl]
        Kanaya Maryam [km]
        Vriska Serket [vs]
        Gamzee Makara [gm]
        Equius Zahhak [ez]
        Eridan Ampora [ea]
        Feferi Peixes [fp]
        Combination of a couple quirks [cb]""")
style = input("Enter style code: ")
input_type = input("Do you wanna use a file [y/n]?: ")
if input_type == 'y':
    filename = input("Enter text file name: ")
    f = open(filename, "r")
    message = f.read()
else:
    message = input(f"So what do you want to say?\nEnter your message: ")

if style == "kv":
    message = message.upper()
elif style == "tp":
    message = message.upper()
    message = message.replace("A", "4")
    message = message.replace("E", "3")
    message = message.replace("I", "1")
elif style == "tn":
    message = message.upper()
    list = message.split(".")
    newmessage = ''
    if message.endswith('.'):
        list.remove('')
    for word in list:
        stripper = word.strip().capitalize() + ","
        newmessage = newmessage + stripper
    message = newmessage.swapcase()
elif style == "am":
    message = message.replace("o", "0")
    message = message.replace("O", "0")
    no_punct = ''
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for char in message:
        if char not in punctuations:
            no_punct = no_punct + "" + char
    message = no_punct
elif style == "sc":
    #double up the i in a word,
    #replace to and too for two,and substitute s for 2
    message = message.replace("i", "ii")
    message = message.replace("too", "two")
    message = message.replace("to", "two")
    message = message.replace("s", "2")
elif style == "nl":
    if message.startswith(":33 < ") is False:
        message = ":33 < " + message
    message = message.replace("you", "mew")
    message = message.replace("pause", "pawsse")
    message = message.replace("perfect", "purrfect")
    message = message.replace("ee", "33")
elif style == "km":
    message = string.capwords(message)
elif style == "vs":
    # her one is harder and ceebs making it work properly
    print("hmm your message is good but have you throw in a  >::::('  or a :::;) emoticon?")
    message = message.replace("b", "8")
    message = message.replace(".", "!!!!!!!!")
    message = message.replace("!", "!!!!!!!!")
    message = message.replace("?", "????????")
elif style == "gm":
    message = message.lower()
    newmessage = ''
    i = 0
    for char in message:
        if i% 2 == 0:
            newmessage = newmessage + char.upper()
        else:
            newmessage = newmessage + char
        i+=1
    message = newmessage
elif style == "ez":
    if message.startswith("D --> ") is False:
        message = "D --> " + message
    message = message.replace("loo", "100")
    message = message.replace("ool", "001")
elif style == "ea":
    message = message.lower()
    message = message.replace("w", "ww")
    message = message.replace("v", "vv")
    message = message.replace("g", "")
elif style == "fp":
    # ceebs making it work properly with added puns or a pun suggestor thingo
    print("Are you happy with the amount of fish puns in your message?")
    message = message.replace("h", ")(")
    message = message.replace("H", ")(")
    message = message.replace("E", "--E")
elif style == "cb":
    message = message.upper()
    if message.startswith("--> ") is False:
        message = "--> " + message

    message = message.replace("H", ")(")
    message = message.replace("E", "--3")
    message = message.replace("S", "5")
    message = message.replace("A", "4")
    message = message.replace("T", "7")
    message = message.replace("O", "0")
    message = message.replace("!", "!!!!!!!!")
    message = message.replace(".", "!!!!!!!!")
    message = message.replace("?", "????????")

else:
    message = """Dude I want to help you!
                Really, I do but I need a valid style code.
                Please rerun the program and enter a valid code.
                For example for Karkat Vantas enter kv."""

print ("Your message has been exported to the homestuck_output.txt file!\nEnjoy XD")
f = open("homestuck_output.txt", "w")
f.write(message)
if len(message) < 255:
    print (message)
