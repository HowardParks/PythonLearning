import csv

with open('contacts.csv') as csvfile:
    fnames = ['Name','Phone','Nice']
    reader = csv.DictReader(csvfile, fieldnames=fnames)
    for row in reader:
        print(f"{row['Name']:20} {row['Phone']:12} {row['Nice']}")

