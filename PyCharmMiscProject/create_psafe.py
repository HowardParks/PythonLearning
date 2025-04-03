import json
from codemachine import CodeMachine

def last(text):
    if "." in text:
        return text.split(".")[-1]
    else:
        return text

with open('C://Users/hparks/Downloads/pwsafe_2017_home.txt') as infile:
    contents = infile.read()

lines = contents.split("\n")
titles = lines[0].split("\t")
psafe = {}
for i in range(1,len(lines)):
    line = lines[i]
    fields = line.split("\t")
    psafe[last(fields[0])] = {titles[j]:fields[j] for j in range(len(fields))}
js = json.dumps(psafe)
key = input("Enter secret key: ")
coder = CodeMachine(key)
output = coder.cypher(js)
with open('C://Users/hparks/OneDrive - Werner Enterprises/Documents/psafe.fil','w') as outfile:
    outfile.write(output)
