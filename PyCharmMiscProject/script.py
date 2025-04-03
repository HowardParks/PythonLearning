import json

class CodeMachine:
    def __init__(self,key):
        self.key = key

    def cypher(self, text):
        result = ''
        for i in range(len(text)):
            result += chr(ord(text[i]) ^ ord(self.key[i % len(self.key)]))
        return result


with open('C://Users/hparks/Downloads/pwsafe_2017_home.txt') as infile:
    contents = infile.read()

lines = contents.split("\n")
titles = lines[0].split("\t")
psafe = []
for i in range(1,10):
    line = lines[i]
    fields = line.split("\t")
    psafe.append({fields[0]:{titles[j]:fields[j] for j in range(len(fields))}})
js = json.dumps(psafe)
key = input("Enter secret key: ")
coder = CodeMachine(key)
output = coder.cypher(js)
with open('C://Users/hparks/OneDrive - Werner Enterprises/Documents/psafe.fil','w') as outfile:
    outfile.write(output)
