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

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

a = np.random.randint(0,10,(3,3))
amean = a.mean(axis=1)
Transposed_amean = np.zeros((3, 1))
for i in range(len(amean)):
    Transposed_amean[i][0] = amean[i]
print(Transposed_amean)
print(a)
a = a-Transposed_amean
print(a)

