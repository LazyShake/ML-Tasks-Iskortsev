# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
Spisok = [1, 2, 3, 4,5,6]

def reverse_list(Spisok):
    Reverse_Spisok = []
    for i in range(len(Spisok)):
        Reverse_Spisok.append(0)
    for i in range(len(Spisok)):
        Reverse_Spisok[len(Spisok)-i-1]= Spisok[i]
    return Reverse_Spisok
Reverse_Spisok = reverse_list(Spisok)
print(Reverse_Spisok)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
