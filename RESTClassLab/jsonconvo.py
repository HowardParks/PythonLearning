import json

class Vehicle:
    def __init__(self, registration_number, year_of_manufacture, passenger, mass):
        self.registration_number = registration_number
        self.year_of_manufacture = year_of_manufacture
        self.passenger = passenger
        self.mass = mass

    def __str__(self):
        result = f"Registration number: {self.registration_number}\n"
        result += f"Year of manufacture: {self.year_of_manufacture}\n"
        result += f"Passenger: {'y' if self.passenger else 'n'}\n"
        result += f"Vehicle mass: {self.mass}\n"
        return result

class Vehicle_Encoder(json.JSONEncoder):
    def default(self, v):
        if isinstance(v, Vehicle):
            return v.__dict__
        else:
            return super().default(self, v)

class Vehicle_Decoder(json.JSONDecoder):
    def __init__(self):
        json.JSONDecoder.__init__(self, object_hook=self.decode_v)

    def decode_v(self, v):
        return Vehicle(**v)

# my_subaru = Vehicle("AE0Z", "2020", "y", "1500")
# json_str = json.dumps(my_subaru, cls=Vehicle_Encoder)
# new_car = json.loads(json_str, cls=Vehicle_Decoder)
# print(my_subaru, new_car, type(new_car))
choice = input("1 produce a JSON string or \n2 decode JSON string into vehicle:")
if choice == "1":
    reg = input("Registration number: ")
    year = input("Year of manufacture: ")
    psng = input("Passenger [y/n]: ")
    psng = (psng.lower() == 'y')
    mass = input("Vehicle mass: ")
    car = Vehicle(reg, year, psng, mass)
    json_str = json.dumps(car, cls=Vehicle_Encoder)
    print(json_str)
elif choice == '2':
    json_str = input("Enter JSON string: ")
    car = json.loads(json_str, cls=Vehicle_Decoder)
    print(type(car), car)
