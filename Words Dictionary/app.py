import json
from difflib import get_close_matches

with open("data.json") as file:
    data = json.load(file)

def value_returning(k):
    if k in data.keys():
        return data[k]
    elif get_close_matches(k,data.keys())[0]:
        answer = input("did you ment this word "+ get_close_matches(k,data.keys())[0]+ " ? Please answer Y or N: ")
        if answer.lower() == 'y':
            return data[get_close_matches(k,data.keys())[0]]
        elif answer.lower() == 'n':
            return "The word does not exists, please double check it."
        else:
            return "We did not understand your query."
    else:
        return "This word seems to does not exists, please double check it."

output = value_returning(input("Please Enter a word: ").lower())
if type(output) == list:
    for item in output:
        print(item)
else:
    print (output)
