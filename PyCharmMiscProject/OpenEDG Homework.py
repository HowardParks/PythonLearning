# def big_container(collective_material):
#     def wrapper(our_function):
#         def internal_wrapper1(*args):
#             print(f'f1 {our_function.__name__}')
#             our_function(*args)
#             print('<strong>*</strong> The whole order would be packed with', collective_material)
#             print()
#         print('f2 in big_container.wrapper')
#         return internal_wrapper1
#     print('f3 in big_container')
#     return wrapper
#
# def warehouse_decorator(material):
#     def wrapper(our_function):
#         def internal_wrapper2(*args):
#             print('f4')
#             our_function(*args)
#             print('<strong>*</strong> Wrapping items from {} with {}'.format(our_function.__name__, material))
#         print('f5 in warehouse wrapper')
#         return internal_wrapper2
#     print('f6 in warehouse')
#     return wrapper
#
# @big_container('plain cardboard')
# @warehouse_decorator('bubble foil')
# def pack_books(*args):
#     print("We'll pack books:", args)
#
#@big_container('colourful cardboard')
#@warehouse_decorator('foil')
#def pack_toys(*args):
#    print("We'll pack toys:", args)
from tkinter.ttk import Label


#@big_container('strong cardboard')
#@warehouse_decorator('cardboard')
#def pack_fruits(*args):
#    print("We'll pack fruits:", args)


# print("stuff about to go down. word.")
# pack_books('Alice in Wonderland', 'Winnie the Pooh')
#pack_toys('doll', 'car')
#pack_fruits('plum', 'pear')

# f3 in big_container
# f6 in warehouse
# f5 in warehouse wrapper
# f2 in big_container.wrapper
# stuff about to go down. word.
# f1 internal_wrapper2
# f4
# We'll pack books: ('Alice in Wonderland', 'Winnie the Pooh')
# <strong>*</strong> Wrapping items from pack_books with bubble foil
# <strong>*</strong> The whole order would be packed with plain cardboard


class Example:
    __internal_counter = 0

    def __init__(self, value):
        self.value = value
        Example.__internal_counter += 1

    @classmethod
    def get_internal(cls):
        return f"# of objects created: {cls.__internal_counter}"

print(Example.get_internal())
example1 = Example('One')
print(Example.get_internal())
example2 = Example('Two')
print(Example.get_internal())

print("blah")

#2.6.1.8 Lab
from abc import ABC, abstractmethod
import random


class Device:
    def __init__(self):
        self.power_on = False

    def hit_switch(self):
        self.power_on = not self.power_on


class PrinterClass(Device):
    @abstractmethod
    def print_document(self):
        pass

    @abstractmethod
    def get_printer_status(self):
        pass


class ScannerClass(Device):
    @abstractmethod
    def scan_document(self):
        pass

    @abstractmethod
    def get_scanner_status(self):
        pass


class MFD1(ScannerClass, PrinterClass):
    def __init__(self):
        super().__init__()
        self.queue = []
        self.papertray = 20

    def scan_document(self):
        if self.power_on:
            print("Scanning ...")
            size = random.randint(5, 70)
            text = 'a' * size
            pagecount = size // 8
            self.queue.append({'text': text, 'pages': pagecount})

    def get_scanner_status(self):
        print(f"Device is {'On' if self.power_on else 'Off'}")
        print(f"There are {len(self.queue)} documents in the queue.")

    def print_document(self):
        if self.power_on:
            while len(self.queue) > 0:
                print("Printing ...")
                doc = self.queue.pop()
                print(doc['text'])
                self.papertray -= doc['pages']

    def get_printer_status(self):
        print(f"Device is {'On' if self.power_on else 'Off'}")
        print(f"There are {self.papertray} pages left for printing.")


m1 = MFD1()
m1.hit_switch()
m1.scan_document()
m1.scan_document()
m1.get_scanner_status()
m1.print_document()
m1.scan_document()
m1.print_document()
m1.get_scanner_status()
m1.get_printer_status()
