# This is a sample Python script.
import math


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
Number = int(input('Введите число от 0 до 1000: '))

def Is_Prime(Number):
    Primes = [2,3,5,7,11,13,17,19,23,29,31]
    Answer = 'True'
    for i in Primes:
        if(i>math.sqrt(Number)):
           break
        if Number % i == 0:
          Answer = 'False'
    return Answer
Answer = Is_Prime(Number)
print(Answer)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
