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

a = np.array([1., 1., 1., 2., 3., 2.])
b = np.array([1., 2., 3., 4., 5., 6.])
c = np.array([1., 1., 1., 1., 3., 2.])
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
def Moda(a):
    max = -1
    max_count = -1
    tempmax = 0
    tempmax_count = 0
    for j in range(len(a)):
        if a[j]!= np.NaN:
            tempmax = a[0]
            for i in range(len(a)):
                if tempmax==a[i]:
                    tempmax_count +=1
                    a[i] = np.NaN
            if tempmax_count> max_count:
                max = tempmax
                max_count = tempmax_count
    return max, max_count

print(Moda(a))
print(Moda(b))
print(Moda(c))