import re

def tagdata(tag, html):
    rc = re.compile(f"<{tag}>([\\w\\s\\.]+)</{tag}>",re.A)
    m = re.search(rc, html)
    try:
        return m.group(1)
    except AttributeError:
        return ""

with open('tbcedi.xml') as infile:
    contents = infile.read()
lines = contents.split("\n")
lines.pop()
results = {}
cn = ""
ws = ""
ps = ""
for line in lines:
    line = line.strip()
    if cn == "":
        cn = tagdata('ConsigneeName',line)
        if cn != "" and cn not in results:
            results[cn] = {'pieces':0, 'weight':0.0}
    if cn != "":
        if ps == "":
            ps = tagdata('Pieces',line)
            if ps != "":
                results[cn]['pieces'] += int(float(ps))
        if ws == '':
            ws = tagdata('Weight',line)
            if ws != '':
                results[cn]['weight'] += float(ws)
                cn = ""
                ps = ""
                ws = ""
print(results)
