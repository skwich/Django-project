import pandas as pd

df = pd.read_csv('vacs.csv')


def format_cell(x):
    if isinstance(x, str):
        return x.split('\n')


df_copy = df.copy()
df_copy['year'] = df_copy['published_at'].str[:4].astype(int)
skills = df_copy[df_copy['key_skills'].notna()][['year', 'key_skills']]

skills_list = list(map(format_cell, skills['key_skills']))
years_list = skills['year'].values

result = [(year,skill) for (year, skill_list) in zip(years_list, skills_list) for skill in skill_list]

df_skills = pd.DataFrame(result, columns=['year', 'skill'])

mosttop = df_skills.groupby('year').value_counts()


import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

year = 2024
skills_name = mosttop[year][:20].index
x = mosttop[year][:20].values
y = np.arange(len(skills_name))
ax.barh(y, x, align='center')
ax.set_yticks(y, labels=skills_name)
ax.invert_yaxis()
ax.grid(axis='x')
ax.set_title(f'ТОП-20 навыков в {year} году')
ax.set_xlabel('Заинтересованость')
ax.set_ylabel('Скиллы')