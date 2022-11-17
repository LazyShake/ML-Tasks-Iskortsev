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

a = np.random.randint(0, 10, (10, 10))
b = np.random.randint(0, 10, (5, 10))
c = np.random.randint(0, 10, (4, 2))
print(a)
print(b)
print(c)
def Zamena(a):
    rows, colums = a.shape
    print(rows)
    for i in range(colums):
        b = a[(rows//2)-1][i]
        a[(rows//2)-1][i] = a[(rows // 2)][i]
        a[(rows // 2)][i] = b
    return a

print(Zamena(a))
print(Zamena(b))
print(Zamena(c))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
