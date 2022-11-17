# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
import numpy as np

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
lst = [16, 71, 34, 2, 7, -30, -6, 0]
def more_than_five(lst):
    Answer = []
    for i in lst:
        if i>10 or i < -10:
            Answer.append(i)
    return Answer
Answer = more_than_five(lst)
print(lst)
print(Answer)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
