# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from random import randint


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
Number = -5238


print(Number)
Length = 0
if Number < 2147483647 and Number > -2147483648:
    if Number < 0:
        Number = Number * -1
        TempNumber = Number

        while TempNumber != 0:
            Length += 1
            TempNumber = TempNumber // 10
        NewNumber = 0
        for i in range(Length):
            NewNumber = NewNumber + (Number % 10) * 10 ** (Length - 1 - i)
            Number = Number // 10
        NewNumber = NewNumber * -1
    else:
        TempNumber = Number
        while TempNumber != 0:
            Length += 1
            TempNumber = TempNumber // 10
        NewNumber = 0
        for i in range(Length):
            NewNumber = NewNumber + (Number % 10) * 10 ** (Length - 1 - i)
            Number = Number // 10
else:
    NewNumber = 0


print(NewNumber)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
