import os
import time
from pathlib import Path
import re
from datetime import datetime as dt

def search_pathlib(path, target):
    path = Path(path)
    lsst = []
    for item in path.rglob(target):
        lsst.append(str(item))
    return lsst

def tagdata(tag, html):
    rc = re.compile(f"<{tag}>(\\w+)</{tag}>",re.A)
    m = re.search(rc, html)
    try:
        return m.group(1)
    except AttributeError:
        return ""

def get_file_age_in_seconds(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    modification_time = os.path.getmtime(file_path)
    current_time = time.time()
    file_age_seconds = current_time - modification_time
    return file_age_seconds

def write_file(filename, outstuff):
    counter = 0
    basefile, xtn = os.path.splitext(filename)
    pdir = 'C:/Users/hparks/OneDrive - Werner Enterprises/Desktop/Pretty/'
    while os.path.exists(pdir + filename) and xtn != '.csv':
        counter += 1
        filename = f"{basefile}_{counter:02}{xtn}"
    outfile = open(pdir + filename, 'w')
    outfile.write(outstuff)
    return filename

def parsecsv(text):
    results = []
    inside_string = False
    word = ''
    for l in text:
        if l == '\"':
            inside_string = not inside_string
        elif l == '\n':
            if inside_string:
                continue
            else:
                results.append(word)
                word = ''
        elif l == ',':
            if inside_string:
                word += l
            else:
                results.append(word)
                word = ''
        else:
            if l.isascii():
                word += l
    if len(word) > 0:
        results.append(word)
    return results

def dateconvert(datestring):
    cd = dt.strptime(datestring, '%m/%d/%Y %I:%M:%S %p')
    return cd.strftime('%x %X'), cd


files = search_pathlib('C:/Users/hparks/Downloads/', "*.*")
for file in files:
    basename, ext = os.path.splitext(file)
    if ext == ".pdf":
        continue
    age = get_file_age_in_seconds(file)
    if age > 3600:
        continue
    try:
        with open(file) as infile:
            contents = infile.read()
    except UnicodeError:
        print(f"Trouble reading {file}")
        continue
    if ext == ".edi":
        term = contents[105]
        delim = contents[3]
        segments = contents.split(term)
        segments.pop()
        output = ''
        doctype = ''
        filename = ''
        for seg in segments:
            elems = seg.split(delim)
            prefix = elems[0]
            if prefix == "ISA":
                filename = elems[6].rstrip()+'-'+elems[8].rstrip()
            elif prefix == 'GS':
                filename = elems[1] + '-' + filename
            elif prefix == 'ST':
                doctype = elems[1]
            elif prefix == 'B3':
                filename += '-' + elems[2]
            output += seg + term + "\n"
        filename = filename + '.txt'
    elif ext == ".xml":
        fileparts = []
        isItTBC = len(tagdata('LoadGroupKey', contents)) > 0
        if isItTBC:
            fileparts.append(tagdata('LoadGroupKey',contents))
            fileparts.append(tagdata('ShipperCode',contents))
        else:
            fileparts.append(tagdata('as400-bill-to-code', contents))
            fileparts.append(tagdata('invoice-num', contents))
            fileparts.append(tagdata('tour-num', contents))
        filename = "_".join(fileparts) + ".xml"
        ptr = 0
        tags = []
        while ptr < len(contents):
            tagst = contents.find('<',ptr)
            tagen = contents.find('>',ptr)+1
            tag = contents[tagst:tagen]
            tags.append({'tag':tag, 'st':tagst,'en':tagen})
            ptr = tagen
        output = ""
        tab = '    '
        depth = 0
        skip = False
        rctagOnly = re.compile("^<[^>/]+>")
        rcendGroup = re.compile("^</[^>]+>")
        for i in range(len(tags)):
            if skip:
                skip = False
                continue
            tag1 = tags[i]
            try:
                tag2 = tags[i+1]
            except IndexError:
                tag2 = tag1
            if tag1['en'] < tag2['st']:
                output += f"{tab*depth}{tag1['tag']}{contents[tag1['en']:tag2['st']]}{tag2['tag']}\n"
                skip = True
            elif re.fullmatch(rctagOnly, tag1['tag']):
                output += f"{tab*depth}{tag1['tag']}\n"
                depth += 1
            elif re.fullmatch(rcendGroup, tag1['tag']):
                depth -= 1
                output += f"{tab*depth}{tag1['tag']}\n"
            else:
                output += f"{tab*depth}{tag1['tag']}\n"
    elif ext == ".csv":
            from datetime import datetime as dt
            words = parsecsv(contents)
            output = ''
            filename = "Issues.csv"
            n = dt.now()
            for i in range(0,len(words)-8,8):
                if words[i+5] == "Howard Parks <hparks@werner.com>" or words[i] == 'ID':
                    if words[i] != 'ID':
                        words[i+1],d1 = dateconvert(words[i+1])
                        words[i+4],d2 = dateconvert(words[i+4])
                        u2n = n - d1
                        c2n = n - d2
                        c2ns = str(c2n.days) + " days old"
                        if words[i+3][0:11] == 'Incident - ':
                            words[i+3] = words[i+3][11:]
                    else:
                        c2ns = ''
                    output += f"{words[i]:8} {words[i+1]:17} {words[i+3][0:40]:40} {words[i+4]:17} {c2ns}\n"
    else:
        continue
    print(write_file(filename, output))