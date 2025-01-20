import pandas as pd

df = pd.read_csv('vacs.csv')

df_copy = df[df['name'].str.contains('c\+\+', case=False, na=False)]
df_copy['year'] = df_copy['published_at'].str[:4].astype(int)
dynamicOfYear = df_copy.groupby('year').agg('count')['name']


import matplotlib.pyplot as plt

x = dynamicOfYear.index
y = dynamicOfYear.values
plt.bar(x, y)
plt.xticks(x, rotation=90)
plt.grid(axis='y')
plt.suptitle('Динамика количества вакансий по годам для выбранной профессии')
plt.xlabel('Года')
plt.ylabel('количество')


