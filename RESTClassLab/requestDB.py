import requests
import json

URL = "http://localhost:3000/cars"
key_names = ["id", "brand", "model", "production_year", "convertible"]
key_widths = [10, 15, 10, 20, 15]
h_content = {'Content-Type': 'application/json'}

def yn2s(conv):
    if type(conv) is bool:
        if conv:
            return 'y'
        else:
            return 'n'
    else:
        return conv

def check_server(cid=None):
# returns True or False;
# when invoked without arguments simply checks if server responds;
# invoked with car ID checks if the ID is present in the database;
# entries disappear from the database after this function when using head
    try:
        if cid is not None:
            reply = requests.get(f"{URL}/{cid}")
        else:
            reply = requests.get(URL)
    except Exception  as e:
        print(e)
        return False
    else:
        return reply.status_code == requests.codes.ok

def print_menu():
    print("""+-----------------------------------+
|       Vintage Cars Database       |
+-----------------------------------+
M E N U
=======
1. List cars
2. Add new car
3. Delete car
4. Update car
0. Exit""")

# prints user menu - nothing else happens here;

def read_user_choice():
# reads user choice and checks if it's valid;
# returns '0', '1', '2', '3' or '4'
    choice = input("Enter your choice (0..4): ")
    if len(choice) == 1 and choice in "01234":
        return choice
    print("Invalid choice")

def print_header():
    for (n, w) in zip(key_names, key_widths):
        print(n.ljust(w), end='| ')
    print()
# prints elegant cars table header;

def print_car(car):
    for (n, w) in zip(key_names, key_widths):
        print(str(car[n]).ljust(w), end='| ')
    print()
# prints one car's data in a way that fits the header;

def list_cars():
    reply = requests.get(URL+"?_sort=id")
    if reply.status_code != 200:
        return

    print_header()
    json = reply.json()
    if type(json) is list:
        for car in json:
            print_car(car)
    elif type(json) is dict:
        if json:
            print_car(json)
# gets all cars' data from server and prints it;
# if the database is empty prints diagnostic message instead;


def name_is_valid(name):
    if name != '':
        return name.replace(' ', '').isalnum()
    return False
# checks if name (brand or model) is valid;
# valid name is non-empty string containing
# digits, letters and spaces;
# returns True or False;

def enter_id():
    id = input("Car ID (empty string to exit): ")
    if id == '' or not id.isdigit():
        return None
    return id
# allows user to enter car's ID and checks if it's valid;
# valid ID consists of digits only;
# returns int or None (if user enters an empty line);

def enter_production_year():
# allows user to enter car's production year and checks if it's valid;
# valid production year is an int from range 1900..2000;
# returns int or None  (if user enters an empty line);
    year = input("Car production year: ")
    if year == '' or not year.isnumeric() or not 1900 <= int(year) <= 2000:
        return None
    return int(year)

def enter_name(what):
    name = input(f"Car {what}: ")
    if name_is_valid(name):
        return name
    return None
# allows user to enter car's name (brand or model) and checks if it's valid;
# uses name_is_valid() to check the entered name;
# returns string or None  (if user enters an empty line);
# argument describes which of two names is entered currently ('brand' or 'model');

def enter_brand():
    return enter_name('brand')

def enter_model():
    return enter_name('model')

def enter_convertible():
    yn = input("Is this car convertible? (y/n): ").lower()
    if yn != '' and yn[0] in 'yn':
        return yn[0] == 'y'
    return None
# allows user to enter Yes/No answer determining if the car is convertible;
# returns True, False or None  (if user enters an empty line);

def delete_car():
    id = enter_id()
    if id is not None:
        if check_server(id):
            reply = requests.delete(f"{URL}/{id}")
            if reply.status_code == requests.codes.ok:
                print("Deleted")
        else:
            print("Car id not found")
# asks user for car's ID and tries to delete it from database;


def input_car_data(with_id):
    car = {}
    r = None
    for f in key_names:
        if f != 'id' or with_id:
            r = eval(f"enter_{f}()")
            if r is None:
                break
            car[f] = r
    if r is not None:
        return car
    return r
# lets user enter car data;
# argument determines if the car's ID is entered (True) or not (False);
# returns None if user cancels the operation or a dictionary of the following structure:
# {'id': int, 'brand': str, 'model': str, 'production_year': int, 'convertible': bool }


def add_car():
    car = input_car_data(True)
    if car is not None:
        try:
            reply = requests.post(URL, headers=h_content, data=json.dumps(car))
            if reply.status_code == requests.codes.ok:
                print("Added")
        except Exception as e:
            print(e)
# invokes input_car_data(True) to gather car's info and adds it to the database;


def update_car():
    id = enter_id()
    if id is None:
        return
    if check_server(id):
        car = input_car_data(False)
        if car != None:
            car['id'] = id
            reply = requests.put(f"{URL}/{id}", headers=h_content, data=json.dumps(car))
            if reply.status_code == 2001:
                print("Updated")
    else:
        print("Car not in database")
# invokes enter_id() to get car's ID if the ID is present in the database;
# invokes input_car_data(False) to gather new car's info and updates the database;

while True:
    if not check_server():
        print("Server is not responding - quitting!")
        exit(1)
    print_menu()
    choice = read_user_choice()
    if choice == '0':
        print("Bye!")
        exit(0)
    elif choice == '1':
        list_cars()
    elif choice == '2':
        add_car()
    elif choice == '3':
        delete_car()
    elif choice == '4':
        update_car()
