# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
import math



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
x1 = 15
y1 = 27
x2 = 12
y2 = 68

def Distance(x1,y1,x2,y2):
    z = math.sqrt(((x2-x1)**2)+((y2-y1)**2))
    return z
Answer = Distance(x1,y1,x2,y2)
print(Answer)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
