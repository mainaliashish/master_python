import json
from difflib import get_close_matches
data = json.load(open("/home/ashish/pythonprograms/Dictionary/data.json"))

def tanslate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yesorno =  input("Did you mean %s instead ? Enter Y if Yes or N if No : " % get_close_matches(w, data.keys())[0])
        if yesorno == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yesorno == "N":
            return "No close matches found!"
        else:
            return "We didn't understand your query!"
    else:
        return "The Word does not exist! Please double check it!"

word = input("Enter a Word : ")

output = tanslate(word)

if(type(output) == list):
    for meaning in output:
        print("---> " + meaning)
else:
    print(output)