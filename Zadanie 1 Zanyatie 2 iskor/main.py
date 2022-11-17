# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
import numpy as np
import pandas as pd

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


r = np.random.RandomState(1)
s = pd.Series(r.uniform(0, 10, 100))

Answer = pd.Series(s[s>5])
for i in Answer.index:
    print("Первый элемент больше 5 имеет индекс", i)
    break

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
