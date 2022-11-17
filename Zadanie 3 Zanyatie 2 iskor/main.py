# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
import numpy as np
import pandas as pd
import random as rnd

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

d = [{"Name": "Виктор", "Age": 18},
     {"Name": "Мария", "Age": 21},
     {"Name": "Иван", "Age": 19},
     {"Name": "Иван", "Age": 25},
     {"Name": "Алексей", "Age": 20}]

df = pd.DataFrame(d)

phone = []
for i in d:
    phone.append("+7({}{}{}){}{}{} {}{} {}{}".format(rnd.randint(0, 9), rnd.randint(0, 9), rnd.randint(0, 9), rnd.randint(0, 9), rnd.randint(0, 9), rnd.randint(0, 9), rnd.randint(0, 9), rnd.randint(0, 9), rnd.randint(0, 9), rnd.randint(0, 9)))
print(phone)

df['Phone'] = phone

print(df)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
