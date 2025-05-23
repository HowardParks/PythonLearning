class PassPhrase:
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

    def passphrase(self,joiner=' '):
        import random
        random.seed()
        wordlist = self.words
        while True:
            candidates = random.choices(wordlist, k=3)
            for _ in range(0,3):
                l = random.randint(0,2)
                w = self.insertdigit(candidates[l])
                if w != candidates[l]:
                    candidates[l] = w
                    l = (l + 2) % 3
                    candidates[l] = candidates[l].capitalize()
                    return joiner.join(candidates)

if __name__ == "__main__":
    pp = PassPhrase()
    print(pp.passphrase())
    print(pp.passphrase())
    print(pp.passphrase())
    print(pp.passphrase())
    print(pp.passphrase())
