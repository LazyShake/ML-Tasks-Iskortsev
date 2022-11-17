# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
s = 'Сезон'
Month = int(input('Введите номер месяца: '))
def season(Month):
    global s
    s = 'Весна' if Month > 2 and Month < 6 \
        else 'Лето' if Month > 5 and Month < 9 \
        else 'Осень' if Month > 8 and Month < 12 \
        else 'Зима' if Month == 12 or Month < 3 \
        else 'Неверный номер месяца'
    return None
season(Month)
print(s)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
