import os
import time
from pathlib import Path
import re
from datetime import datetime as dt
import xml.dom.minidom

def search_pathlib(path, target):
    path = Path(path)
    lsst = []
    for item in path.rglob(target):
        lsst.append(str(item))
    return lsst

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
    with open(file) as infile:
        contents = infile.read()
    if ext == ".edi":
        term = contents[105]
        delim = contents[3]
        segments = contents.split(term)
        segments.pop()
        output = ''
        doctype = ''
        fileparts=[]
        for seg in segments:
            elems = seg.split(delim)
            prefix = elems[0]
            if prefix == "ISA":
                fileparts.append(elems[6].rstrip()+'-'+elems[8].rstrip())
            elif prefix == 'GS':
                fileparts.append(elems[1])
            elif prefix == 'ST':
                fileparts.append(elems[1])
            elif prefix == 'B3':
                fileparts.append(elems[2])
            output += seg + term + "\n"
        filename = '_'.join(fileparts) + '.txt'
    elif ext == ".xml":
        fileparts = []
        dom = xml.dom.minidom.parseString(contents)
        lgk = dom.getElementsByTagName('LoadGroupKey')
        if len(lgk)>0:
            sc = dom.getElementsByTagName('ShipperCode')[0]
            fileparts.append(sc.firstChild.nodeValue)
            fileparts.append(lgk[0].firstChild.nodeValue)
        else:
            as400BillToCode = dom.getElementsByTagName('as400-bill-to-code')[0].firstChild.nodeValue
            fileparts.append(as400BillToCode)
            invoiceNum = dom.getElementsByTagName('invoice-num')[0].firstChild.nodeValue
            fileparts.append(invoiceNum)
            tourNum = dom.getElementsByTagName('tour-num')[0].firstChild.nodeValue
            fileparts.append(tourNum)
        filename = "_".join(fileparts) + ".xml"
        output = dom.toprettyxml()
    elif ext == ".csv":
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
                        c2ns = str(c2n.days).rjust(3) + " days old"
                        if words[i+3][0:11] == 'Incident - ':
                            words[i+3] = words[i+3][11:]
                    else:
                        c2ns = 'Age'
                    output += f"{words[i]:8} {words[i+1]:17} {words[i+3][0:40]:40} {words[i+4]:17} {c2ns:12} {words[i+6]:12}\n"
    else:
        continue
    print(write_file(filename, output))