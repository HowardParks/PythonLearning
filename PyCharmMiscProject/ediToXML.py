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

def write_file(filename, contents):
    counter = 0
    basefile, ext = os.path.splitext(filename)
    dir = 'C:/Users/hparks/OneDrive - Werner Enterprises/Desktop/Pretty/'
    while os.path.exists(dir + filename):
        counter += 1
        filename = f"{basefile}_{counter:02}{ext}"
    outfile = open(dir + filename, 'w')
    outfile.write(output)
    return filename



files = search_pathlib('C:/Users/hparks/Downloads/', "*.*")
for file in files:
    basename, ext = os.path.splitext(file)
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
