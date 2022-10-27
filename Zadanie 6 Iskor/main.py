# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
Number = 522005
print(Number)
MultiNumber = 1
while Number > 0:
    if Number%10 != 0:
        MultiNumber *= Number%10
        Number = Number//10
    else :
        Number = Number // 10

print(MultiNumber)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
