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

a = np.array([1., 1., 1., 7., 8., 5.])
b = np.array([7., 7., 7., 7., 8., 5.])
c = np.array([1., 1., 1., 1., 8., 5.])

NumberOfMax = int(input("Введите количество максимумов: "))

def Maxim(a, NumberOfMax):
    Answer = np.zeros((NumberOfMax))
    for i in range(NumberOfMax):
        Max = -1
        Max_index = -1
        for j in range(len(a)):
            if a[j]>=Max:
                Max = a[j]
                Max_index = j
        Answer[i]= Max
        a[Max_index] = np.NaN
    return Answer

print(Maxim(a, NumberOfMax))
print(Maxim(b, NumberOfMax))
print(Maxim(c, NumberOfMax))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
