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

a = np.random.randint(-10,10,10)
b = np.random.randint(-10,10,10)
c = np.random.randint(-10,10,10)
d = np.random.randint(-10,10,10)
print(a, b, c, d)
def ThreeToEight(ar):
    for i in range(len(ar)):
        if (ar[i]>=3 and ar[i]<=8) or (ar[i]>= -8 and ar[i]<= -3):
            ar[i] = ar[i]* -1
    return ar
print(ThreeToEight(a), ThreeToEight(b), ThreeToEight(c), ThreeToEight(d))