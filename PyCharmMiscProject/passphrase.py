class PassPhrase:
    DEFAULT_CHARSET = {
        'lowercase': 'abcdefghijkmnopqrstuvwxyz',
        'uppercase': 'ABCDEFGHJKLMNPQRSTUVWXYZ',
        'digit': '23456789',
        'special': '!@#$%&*'}

    def __init__(self):
        with open('C://Users/Owner/PycharmProjects/PythonLearning/PycharmMiscProject/wordlywords.txt') as infile:
#        with open('C://Users/hparks/OneDrive - Werner Enterprises/Python/PyCharmMiscProject/words.txt') as infile:
            contents = infile.read()
        strings = contents.split("\n")
        strings.pop()
        self.words = []
        for word in strings:
            if 3 < len(word) < 10 and word.isalnum():
                self.words.append(word)
        self.table = {'e':'3','i':'1','s':'5','o':'0'}

    def insertdigit(self, word):
        for i in range(len(word)):
            ltr = word[i]
            if ltr in self.table:
                word = word.replace(ltr,self.table[ltr],1)
                return word
        return word

    def passphrase(self,comp):
        import random
        random.seed()
        wordlist = self.words
        candidates = random.choices(wordlist, k=comp['length'])
        l = random.randrange(len(candidates))
        if 'uppercase' in comp:
            candidates[l] = candidates[l].capitalize()
        if 'digit' in comp:
            candidates[l] = self.insertdigit(candidates[l])
        if 'special' in comp:
            spch = random.choice(list(comp['special']['selectfrom']))
            candidates[l] = candidates[l] + spch
        if 'delim' in comp:
            joiner = comp['delim']
        else:
            joiner = ''
        return joiner.join(candidates)

    def get_composition(self):
        ### need to derive this from Password Policy
        composition = {}
        resp = input("What is the total length of the password/phrase and what is it composed of? ")
        if resp == '':
            resp = '12 chars'
        if resp.endswith('words'):
            composition['raw'] = 'words'
            delim = input("Delimiter to use between words? ")
            composition['delim'] = delim
        elif resp.endswith('chars'):
            composition['raw'] = 'chars'
        resp = resp[:-5]
        composition['length'] = int(resp)
        for chtype in ['lowercase', 'uppercase', 'digit', 'special']:
            resp = input(f"Will this password include {chtype}? ").lower()
            if resp == 'y':
                resp = input(f"Minimum number of {chtype}? ")
                composition[chtype] = {}
                composition[chtype]['min'] = int(resp)
                resp = input(f"Use specific {chtype} charset? ").lower()
                if resp == 'y':
                    resp = input("Enter special charset: ")
                else:
                    resp = PassPhrase.DEFAULT_CHARSET[chtype]
                composition[chtype]['selectfrom'] = resp
        return composition

    def get_policy(self, comp: dict) -> str :
        import json
        return json.dumps(comp)

    def password(self, composition):
        import random
        random.seed()
        letters = []
        selectlist = []
        # build a list containing the minimums
        for chtype in ['lowercase', 'uppercase', 'digit', 'special']:
            if chtype in composition:
                slist = list(composition[chtype]['selectfrom'])
                letters.extend(random.choices(slist, k=composition[chtype]['min']))
                selectlist.extend(slist)
        while len(letters) < composition['length']:
            letters.append(random.choice(selectlist))
        random.shuffle(letters)
        return ''.join(letters)

if __name__ == "__main__":
    pp = PassPhrase()
    comp = pp.get_composition()
    if comp['raw'] == 'chars':
        print(pp.password(comp))
    else:
        print(pp.passphrase(comp))
