# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
import numpy as np
import pandas as pd
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


df = pd.DataFrame({
    'имя': ['Петя', 'Вася', 'Аня', 'Света'],
    'возраст': [45, 26, 41 , 21],
    'доход': [100000, 80000, 150000, 60000],
    'надежность клиента (0..1)': [0.65, 0.74, 0.87, 0.68],
    'пол': ['муж', 'муж', 'жен', 'жен']},
    index=[0, 1, 2, 3])

print("Все кто старше 40")
print(df[df['возраст']>40])
dfsum = 0.
dfcount = 0.
for i in df['доход']:
    dfsum += i
    dfcount +=1.
dfmiddle = dfsum/dfcount

dfagesum = 0
dfagemiddlecount = 0
for i in df['возраст']:
    dfagesum += i
    dfagemiddlecount +=1.
dfagemiddle = dfagesum/dfagemiddlecount

print("Все чей доход выше среднего")
print(df[df['доход']>dfmiddle])

dfsum_nad = 0.
dfcount_nad = 0.
for i in df['надежность клиента (0..1)']:
    dfsum_nad += i
    dfcount_nad +=1.
dfmiddle_nad = dfsum_nad/dfcount_nad
print("Все чей доход выше среднего, но надежность ниже среднего")
print(df[(df['надежность клиента (0..1)']<dfmiddle_nad)&(df['доход']>dfmiddle)])
vazh = []
ind = 0
strings, colums = df.shape
for i in range(strings):
    vazh.append(df.iloc[i][2]*df.iloc[i][3])
    ind+=1
df['важность'] = vazh
print(df)

dolg = []
for i in range(strings):
    dolg.append(df.iloc[i][5]*(dfagemiddle - df.iloc[i][1]))
df['возможная долгосрочность клиента'] = dolg

print(df)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
