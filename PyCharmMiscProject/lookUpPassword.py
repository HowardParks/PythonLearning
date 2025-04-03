from codemachine import CodeMachine
import json
import re
import random

def binary_search_regex(arr, regex):
    low = 0
    high = len(arr) - 1
    rx = regex.lower()
    rc = re.compile(f"^{rx}.*$")
    arrl = list(map(str.lower, arr))
    arrl.sort()
    while low <= high:
        mid = (low + high) // 2
        holdr = arrl[mid]
        if re.search(rc, arrl[mid]):
            return mid  # Regex found in the middle element
        elif arrl[mid] < rx:
            low = mid + 1
        else:
            high = mid - 1
    return -1  # Regex not found in the list

def f(title):
    a = input(f"{title}: ")
    return title,a


with open("C://Users/hparks/OneDrive - Werner Enterprises/Documents/psafe.fil") as infile:
    contents = infile.read()
while True:
    try:
        key = input("Enter the secret key: ")
        cm = CodeMachine(key)
        js = cm.cypher(contents)
        psafe = json.loads(js)
        break
    except json.decoder.JSONDecodeError:
        continue
keylist = list(psafe.keys())
example = random.choice(keylist)
rando = psafe[example]
titles = list(rando.keys())
group = input("Enter the password name: ")
if group == '':
    answer = input("New or Fix entry? ")
    if answer.lower() == 'new':
        deets = {}
        for t in titles:
            deets[t] = input(f"{t}: ")
        group = deets['Group/Title']
        psafe[group] = deets
        js = json.dumps(psafe)
        output = cm.cypher(js)
        with open('C://Users/hparks/OneDrive - Werner Enterprises/Documents/psafe.fil', 'w') as outfile:
            outfile.write(output)
        keylist = list(psafe.keys())
    elif answer.lower() == 'fix':
        oldval = input("Enter old value: ")
        newval = input("Enter new value: ")
        psafe[newval] = psafe[oldval]
        psafe.pop(oldval)
        group = newval
        js = json.dumps(psafe)
        output = cm.cypher(js)
        with open('C://Users/hparks/OneDrive - Werner Enterprises/Documents/psafe.fil', 'w') as outfile:
            outfile.write(output)
        keylist = list(psafe.keys())
while group != '':
    try:
        record = psafe[group]
        print(f"Key:{group}\tUser:{record['Username']}\tPwd:{record['Password']}\tURL:{record['URL']}")
    except KeyError:
        print(f"Did not find key {group}")
        ind = binary_search_regex(keylist, group[0:2])
        if ind >= 0:
            print(f"Did you maybe mean {keylist[ind:ind+5]}?")
    group = input("Enter the password name: ")