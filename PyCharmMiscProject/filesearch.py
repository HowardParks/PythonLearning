from pathlib import Path
def search_pathlib(path, target):
    path = Path(path)
    lsst = ''

    for item in path.rglob(target):
        lsst += str(item) + "\n"
    return lsst
# def list_contents(path):
#     path = Path(path)
#     for item in path.iterdir():
#         print(f"{'File ' if item.is_file() else 'Dir '}{str(item)}")
#current_dir = Path.cwd()
current_dir = input("Search directory: ")
while current_dir != 'END':
    if current_dir == '':
        current_dir = 'C://Users/Owner'
    # elif current_dir == 'Git':
    #     current_dir = 'C://Users/hparks/GitHub/WernerEnterprise'
    # elif current_dir == '210':
    #     current_dir = 'C://Users/hparks/GitHub/WernerEnterprise/Mastery/210'
    print(f"Searching in {current_dir}")
    target = input("Search target: ")
    found_list = search_pathlib(current_dir, target)
    print(found_list)
    current_dir = input("Search Directory: ")
