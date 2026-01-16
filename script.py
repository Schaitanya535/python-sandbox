# This is a sample Python script.


# Press ⌃F5 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import io

from second_script import adding_numbers


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f"Hi, {name}")  # Press F9 to toggle the breakpoint.


def print_hello(name):
    print(f"Hello, {name}")


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    print_hi("Chaitanya")
    print_hello("Chaitanya")
    print_hello(adding_numbers(1, 2))
    file_name = io.open("./second_script.py").buffer
    print_hi(file_name)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
