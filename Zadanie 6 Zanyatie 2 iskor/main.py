# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
import pandas as pd
import matplotlib.pyplot as plt

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

df = pd.read_excel("Olympics 2018.xlsx", sheet_name="Olympics")

df_filter_country = df['Country'].isin(['Soviet Union']) & df['Medal'].isin(['GOLD'])

print(df[df_filter_country])

df.groupby('Year').Age.mean().plot()
plt.show()

df.drop(columns=['City'])
df_filter_season = df['Season'].isin(['Summer'])


df['Born_Year'] = df['Year'] - df['Age']
print(df[df_filter_season])

df[df_filter_season].to_csv('final_base.csv')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
