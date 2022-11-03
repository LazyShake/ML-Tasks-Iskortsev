# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
number = int(input("Введите число от 1 до 9: "))
temp = 1
otvet = "Результат "
while number>0:
    otvet += str(temp)
    temp += 1
    number -= 1
print(otvet)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
