import csv

class PhoneContact:
    def __init__(self,n,p,c=None):
        self.name = n
        self.phone = p
        self.nice = c

    def __str__(self):
        return f"{self.name} {self.phone} is {self.nice} nice."

    def listfrom(self):
        return [self.name, self.phone, self.nice]

    def dictfrom(self):
        return {'Name':self.name, 'Phone':self.phone, 'Nice':self.nice}

class Phone:
    def __init__(self,number):
        self.contacts = []
        self.mynumber = number

    def load_contacts_from_csv(self,filename):
        with open(filename) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.contacts.append(PhoneContact(row['Name'],row['Phone'],row['Nice']))

    def search_contacts(self,srchstr):
        for pc in self.contacts:
            if srchstr in str(pc):
                return pc
        return None

    def add_contact(self):
        name = input("Name: ")
        phone = input("Phone: ")
        nice = input(f"How nice is {name}: ")
        self.contacts.append(PhoneContact(name, phone, nice))

    def write_contacts(self, filename):
        with open(filename,'w',newline='') as csvfile:
            writer = csv.writer(csvfile,quoting=csv.QUOTE_NONNUMERIC)
            writer.writerow(['Name','Phone','Nice'])
            for row in self.contacts:
                writer.writerow(row.listfrom())

    def writedict_contacts(self,filename):
        with open(filename,'w',newline='') as csvfile:
            first = self.contacts[0].dictfrom()
            headers = list(first.keys())
            writer = csv.DictWriter(csvfile, fieldnames=headers,quoting=csv.QUOTE_NONNUMERIC)
            for row in self.contacts:
                writer.writerow(row.dictfrom())


mynewphone = Phone('2104')
mynewphone.load_contacts_from_csv('contacts.csv')
while True:
    ac = input("Add contact: ")
    if ac != '' and ac[0].lower() == 'y':
        mynewphone.add_contact()
    ss = input("Search text: ")
    if ss == 'break':
        break
    result = mynewphone.search_contacts(ss)
    if result is not None:
        print(result)
    else:
        print(f"{ss} not found")
mynewphone.write_contacts('contacts.csv')
mynewphone.writedict_contacts('dcontacts.csv')