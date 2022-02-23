import json
from  difflib import get_close_matches
data = json.load(open("data.json"))

def translate(word):
    w = word.lower()
    if word in data:
        return(data[word])
    elif w in data:
        return(data[w])
    else:
        poss = get_close_matches(w,data.keys(),n=5)
        poss.reverse()
        while len(poss) > 0:
            p = poss.pop()
            choice = input("Did you mean %s? Y or N: " % p).upper()
            if choice == "Y":
                return(data[p])
        return "%s does not exist. Please check it again!" % word

word = input("Enter word: ")
results = translate(word)
if type(results) == list:
    for r in results:
        print(r)
else:
    print(results)
