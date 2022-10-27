# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from random import random
from random import randint


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
Number = randint(0, 100) + random()
print(Number)

print("{0:.2f}".format(Number))
print("{0:.0f}".format(Number))
Number=round(Number, 3)
print("{0:=011}".format(Number))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
