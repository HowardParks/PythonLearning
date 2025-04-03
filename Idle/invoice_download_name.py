import glob
import os
import re
import time


def isThere(k,d):
    if (k in d):
        return True
    else:
        return False


def decomp(x):
    x = x.strip()
    m = re.match("<([^>]+)>([^<]+)<", x)
    if m != None:
      return [m.group(1), m.group(2)]
    return [None, None]


now = time.time()
iteration = 0
skipped = 0
processed = 0
#destination = 'C:/Users/hparks/Desktop/Pretty'
os.chdir('C:/Users/hparks/Downloads/')
for f in glob.glob('*.xml'):
    age = now - os.stat(f).st_mtime
    if (age > 1800):
        skipped += 1
        continue

    (dir, name) = os.path.split(f)
    fh = open(f, 'r')
    for line in fh:
        (tag,value) = decomp(line)
        if tag == 'customer-id':
            customer = value
        if tag == 'invoice-num':
            invoice = value
            break
        if tag == 'inv-purpose-code':
            purpose = value + ".xml"
    filename = "_".join([customer, invoice, purpose])
    fh.close()
    os.rename(f, filename)
    print(filename)

"""    processed += 1
    iteration += 1
    (dir,name) = os.path.split(f)
    outfile = open(destination+proNum+'_'+eventType+'.xml','w')
    outfile.write(pretty_xml_as_string)
    outfile.close()
"""
print("Skipped " + str(skipped) + " Processed " + str(processed))
