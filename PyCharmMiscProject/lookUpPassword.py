import re
from datetime import datetime
from passphrase import PassPhrase
from passwordsafefile import PassWordSafeFile

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
    rando = passwordsafe[example]
    return list(rando.keys())

def getnewpassword():
    pp = PassPhrase()
    ### "8umBocphhq$g"
    comp = pp.get_composition()
    while True:
        if comp['raw'] == 'words':
            newpassword = pp.passphrase(comp)
        else:
            newpassword = pp.password(comp)
        presp = input(f"Password: {newpassword}  Okay(y/n/e)? ").lower()
        if presp[0] == 'y':
            return newpassword
        elif presp[0] == 'e':
            newpassword = input("Enter new password: ")
            return newpassword

passwordsafe =  None
while passwordsafe is None:
    key = input("Enter Secret Key: ")
    passwordsafefile = PassWordSafeFile(key)
    passwordsafe = passwordsafefile.read()
keylist = list(passwordsafe.keys())
keylist.sort()
option = input("[1] Lookup\n2 New\n3 Edit\n4 List\nEND Exit: ")
while option != 'END':
    if option == '' or option == '1': ### Lookup
        group = ' '
        try:
            group = input("Enter the password title: ")
            record = passwordsafe[group]
            print(f"Key:{group}\tUser:{record['Username']}\tPwd:{record['Password']}\tURL:{record['URL']}")
        except KeyError:
            print(f"Did not find {group}")
            regex_search(keylist, group)
    elif option == '2': ### New
        ### Add automatic fill in of date fields
        deets = {}
        now = datetime.now()
        deets['Created Date'] = now
        deets['Record Modified Time'] = now
        deets['Last Access Time'] = now
        deets['Password Modified Time'] = now
        for t in titles():
            deets[t] = input(f"{t}: ")
            if t == "Password" and deets[t]=='':
                deets[t] = getnewpassword()
        group = deets['Group/Title']
        passwordsafe[group] = deets
        passwordsafefile.write(passwordsafe)
    elif option == "3": ## Edit
        ### Add automatic fill in of date fields, including making the distinction
        ### between access date and update and pwd change date and pwd change due date
        group = ''
        now = datetime.now()
        try:
            group = input("Enter the password name: ")
            pdict = passwordsafe[group]
        except KeyError:
            print(f"Did not find {group}")
            regex_search(keylist, group)
            continue
        changemade = False
        groupchange = False
        for field, value in pdict.items():
            if value != '':
                print(f"    {field}: {value} ", end='')
                newval = ''
                if field == 'Password':
                    passwordsafe[group]['Password Modified Time'] = now
                    resp = input("R)eplace or G)enerate password? ").lower()
                    if resp != '' and resp[0] == 'g':
                        newval = getnewpassword()
                        print(f"    {newval}")
                    elif resp != '' and resp[0] == 'r':
                        newval = input(f"New {field}: ")
                elif field == 'Group/Title':
                    newval = input(f"New {field}: ")
                    if newval != '':
                        groupchange = True
                else:
                    newval = input(f"New {field}: ")
            else:
                newval = input(f"    {field}: ")
            if newval != '':
                passwordsafe[group][field] = newval
                passwordsafe[group]['Record Modified Time'] = now
                changemade = True
        if changemade:
            passwordsafefile.write(passwordsafe)
    elif option == "4":
        groups = list(passwordsafe.keys())
        groups.sort()
        last = len(groups) - 1
        counter = 0
        group = groups[counter]
        option = 'c'
        while option != 'e' and counter <= last:
            group = groups[counter]
            while group == '':
                counter += 1
                group = groups[counter]
            print(f"GROUP:{group}")
            for field, value in passwordsafe[group].items():
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
        passwordsafefile = PassWordSafeFile(newkey)
        passwordsafefile.write(passwordsafe)
    option = input("[1] Lookup\n 2  New\n 3  Edit\n 4  List\nEND Exit: ")
