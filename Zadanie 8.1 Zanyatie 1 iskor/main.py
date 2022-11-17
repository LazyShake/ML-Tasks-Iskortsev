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

a = np.random.randint(0, 10, (16, 16))
b = np.random.randint(0, 10, (16, 16))
c = np.random.randint(0, 10, (16, 16))

def Four_Summ(a):
    Summ = np.zeros((4,4))
    for i in range(4):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    Summ[i][j]+= a[k+i*4][l+j*4]
    return Summ
print(a)
print(b)
print(c)
print(Four_Summ(a))
print(Four_Summ(b))
print(Four_Summ(c))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
