# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

df = pd.read_csv("H1N1_Flu_Vaccines.csv")
df.dropna(axis=0, how='all')

print(df.hhs_geo_region.unique())

df_filter = df['education'].isin(['Some College'])
df[df_filter]
print(df[df_filter])

max_children = df[df_filter]['household_children'].max()
mean_children = df[df_filter]['household_children'].mean()
SKO_children = np.std(df[df_filter]['household_children'])

print(max_children)
print(mean_children)
print(SKO_children)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
