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

Vec = np.array([1,2,3,4,5], int)
NewVec = np.zeros((17))
k = 0
for i in range(len(NewVec)):
    if i%4 == 0:
        NewVec[i] = Vec[k]
        k+=1
print(NewVec)