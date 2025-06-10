import re
from passphrase import PassPhrase
from psafefile import PsafeFile

def regex_search(arr, regex):
    possibles = []
    for k in arr:
        if re.search(regex, k, re.IGNORECASE):
            possibles.append(k)
    if len(possibles) > 0:
        print(f"Did you maybe mean {possibles}?")

def f(title):
    a = input(f"{title}: ")
    return title,a

def titles():
    import random
    example = random.choice(keylist)
    rando = psafe[example]
    return list(rando.keys())

def getnewpassword():
    pp = PassPhrase()
    while True:
        newpassword = pp.passphrase()
        resp = input(f"Password: {newpassword}  Okay? ").lower()
        if resp[0] == 'y':
            return newpassword

#(psafe, cm) = read_psafe()
key = input("Enter Secret Key: ")
psafefile = PsafeFile(key)
psafe = psafefile.read()
keylist = list(psafe.keys())
keylist.sort()
option = input("[1] Lookup\n2 New\n3 Edit\n4 List\nEND Exit: ")
while option != 'END':
    if option == '' or option == '1': ### Lookup
        try:
            group = input("Enter the password title: ")
            record = psafe[group]
            print(f"Key:{group}\tUser:{record['Username']}\tPwd:{record['Password']}\tURL:{record['URL']}")
        except KeyError:
            print(f"Did not find {group}")
            regex_search(keylist, group)
    elif option == '2': ### New
        deets = {}
        for t in titles():
            deets[t] = input(f"{t}: ")
            if t == "Password" and deets[t]=='':
                deets[t] = getnewpassword()
        group = deets['Group/Title']
        psafe[group] = deets
        psafefile.write(psafe)
    elif option == "3": ## Edit
        try:
            group = input("Enter the password name: ")
            pdict = psafe[group]
        except KeyError:
            print(f"Did not find {group}")
            regex_search(keylist, group)
            continue
        changemade = False
        groupchange = False
        for field, value in pdict.items():
            if value != '':
                print(f"    {field}: {value} ", end='')
                if field == 'Password':
                    resp = input("Generate new password? ").lower()
                    if resp != '' and resp[0] == 'y':
                        newval = getnewpassword()
                        print(f"    {newval}")
                elif field == 'Group/Title':
                    newval = input(f"New {field}: ")
                    if newval != '':
                        groupchange = True
                else:
                    newval = input(f"New {field}: ")
                if newval != '':
                    psafe[group][field] = newval
                    changemade = True
        if changemade:
            psafefile.write(psafe)
    elif option == "4":
        groups = list(psafe.keys())
        groups.sort()
        last = len(groups) - 1
        counter = 0
        group = groups[counter]
        option = 'c'
        while option != 'e':
            group = groups[counter]
            while group == '':
                counter += 1
                group = groups[counter]
            print(f"GROUP:{group}")
            for field, value in psafe[group].items():
                if value != '':
                    print(f"    {field}: {value}")
            option = input("[c] cont, f fwd 5, b back 5, e end ... ").lower()
            if option == 'f':
                counter += 5
                if counter > last:
                    counter = last
            elif option == 'b':
                counter -= 5
                if counter < 0:
                    counter = 0
            else:
                counter += 1
            print()
    elif option == '5':
        newkey=input("Enter new password safe key: ")
        psafefile = PsafeFile(newkey)
        psafefile.write(psafe)
    option = input("[1] Lookup\n 2  New\n 3  Edit\n 4  List\nEND Exit: ")
