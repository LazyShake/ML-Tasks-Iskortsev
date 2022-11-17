# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
Spisok = [0,1,2,3,4,5,6,7,8,9]
Odd = []
Even = []
def Split(Spisok):
    global Odd
    global Even
    for i in range(len(Spisok)):
        if i%2 == 1:
            Odd.append(Spisok[i])
        else:
            Even.append(Spisok[i])
    return None
Answer = []
Split(Spisok)
print(Odd, Even)
Odd.reverse()
k = 0
x = 0
for i in range(len(Spisok)):
    if i % 2 == 1:
        Answer.append(Odd[k])
        k+=1
    else:
        Answer.append(Even[x])
        x += 1
print(Answer)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
