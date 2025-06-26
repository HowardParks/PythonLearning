import requests
import json

def check_server(cid=None):
# returns True or False;
# when invoked without arguments simply checks if server responds;
# invoked with car ID checks if the ID is present in the database;


def print_menu():
# prints user menu - nothing else happens here;

def read_user_choice():
# reads user choice and checks if it's valid;
# returns '0', '1', '2', '3' or '4'


def print_header():
# prints elegant cars table header;

def print_car(car):
# prints one car's data in a way that fits the header;

def list_cars():
# gets all cars' data from server and prints it;
# if the database is empty prints diagnostic message instead;


def name_is_valid(name):
# checks if name (brand or model) is valid;
# valid name is non-empty string containing
# digits, letters and spaces;
# returns True or False;

def enter_id():
# allows user to enter car's ID and checks if it's valid;
# valid ID consists of digits only;
# returns int or None (if user enters an empty line);


def enter_production_year():
# allows user to enter car's production year and checks if it's valid;
# valid production year is an int from range 1900..2000;
# returns int or None  (if user enters an empty line);


def enter_name(what):
# allows user to enter car's name (brand or model) and checks if it's valid;
# uses name_is_valid() to check the entered name;
# returns string or None  (if user enters an empty line);
# argument describes which of two names is entered currently ('brand' or 'model');

def enter_convertible():
# allows user to enter Yes/No answer determining if the car is convertible;
# returns True, False or None  (if user enters an empty line);

def delete_car():
# asks user for car's ID and tries to delete it from database;


def input_car_data(with_id):
# lets user enter car data;
# argument determines if the car's ID is entered (True) or not (False);
# returns None if user cancels the operation or a dictionary of the following structure:
# {'id': int, 'brand': str, 'model': str, 'production_year': int, 'convertible': bool }


def add_car():
# invokes input_car_data(True) to gather car's info and adds it to the database;


def update_car():
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
