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

a = np.random.randint(2, 4, (10,3))
b = np.random.randint(2, 4, (10,3))
c = np.random.randint(2, 4, (10,3))
print(a)
def Axis_Check(a):
    amean = np.mean(a, axis=1)
    trans_amean = np.zeros((10,1))
    for i in range(len(amean)):
        trans_amean[i][0] = amean[i]
    newa = a
    newa = newa-trans_amean
    newa = np.sum(newa, axis=1)
    for i in range(10):
        if newa[i]==0:
            print(i, a[i])
    return None

Axis_Check(a)
print(b)
Axis_Check(b)
print(c)
Axis_Check(c)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
