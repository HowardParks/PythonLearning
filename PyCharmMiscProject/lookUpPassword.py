from codemachine import CodeMachine
import json
import re


def read_psafe():
    with open("C://Users/hparks/OneDrive - Werner Enterprises/Documents/psafe.fil") as infile:
        contents = infile.read()
    psafe = {}
    while True:
        try:
            key = input("Enter the secret key: ")
            cm = CodeMachine(key)
            js = cm.cypher(contents)
            psafe = json.loads(js)
            break
        except json.decoder.JSONDecodeError:
            continue
    return psafe, cm

def write_psafe(ps, cm):
    js = json.dumps(ps)
    output = cm.cypher(js)
    with open('C://Users/hparks/OneDrive - Werner Enterprises/Documents/psafe.fil', 'w') as outfile:
        outfile.write(output)

def regex_search(arr, regex):
    possibles = []
    for k in arr:
        if re.search(regex, k, re.IGNORECASE):
            possibles.append(k)
    if len(possibles) > 0:
        print(f"Did you maybe mean {possibles}?")


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

def titles():
    import random
    example = random.choice(keylist)
    rando = psafe[example]
    return list(rando.keys())

(psafe, cm) = read_psafe()
keylist = list(psafe.keys())
keylist.sort()
group = input("Enter the password name (or END): ")
while group != 'END':
    if group == '':
        answer = input("New or Fix entry? ")
        if answer.lower() == 'new':
            deets = {}
            for t in titles():
                deets[t] = input(f"{t}: ")
            group = deets['Group/Title']
            psafe[group] = deets
            write_psafe(psafe, cm)
        elif answer.lower() == 'fix':
            oldval = input("Enter old value: ")
            newval = input("Enter new value: ")
            psafe[newval] = psafe[oldval]
            psafe.pop(oldval)
            group = newval
            write_psafe(psafe, cm)
        keylist = list(psafe.keys())
    else:
        try:
            record = psafe[group]
            print(f"Key:{group}\tUser:{record['Username']}\tPwd:{record['Password']}\tURL:{record['URL']}")
        except KeyError:
            print(f"Did not find {group}")
            # ind = binary_search_regex(keylist, group[0:2])
            # if ind >= 0:
            #     ind = max(0,ind-3,ind-2,ind-1)
            #     print(f"Did you maybe mean {keylist[ind:ind+5]}?")
            regex_search(keylist, group)
    group = input("Enter the password name (or END): ")
