import pandas as pd

df_currency = pd.read_csv('currency.csv', index_col='date')
df = pd.read_csv('vacs.csv')


def to_rub(df):
    salary, currency, date = df["salary"], df["salary_currency"], df["published_at"][:7]
    if currency == "RUR":
        return salary
    if salary > 0 and currency is not None and any(df_currency.index.isin([date])):
        value = df_currency[df_currency.index == date][currency].values[0]
        if value > 0:
            return salary * value
    return None


df_copy = df[df['name'].str.contains('c\+\+', case=False, na=False)]
df_copy['salary'] = df[['salary_from','salary_to']].mean(axis=1)
df_copy['salary'] = df_copy.apply(to_rub, axis=1)

dynamicOfCity = (df_copy.groupby("area_name", as_index=False)[["area_name", "name", "salary"]]
        .agg({"area_name": "first", "name": "count", "salary": "mean"})
        .sort_values("name", ascending=False)
        .dropna(subset=['salary']))
dynamicOfCity["salary"] = dynamicOfCity["salary"].round().astype(int)
dynamicOfCity["name"] = (dynamicOfCity["name"] / len(df) * 100).round(2)
salaries = dynamicOfCity.sort_values("name", ascending=False)[['area_name', 'salary']]

salaries = salaries[:14].sort_values("salary", ascending=False)


import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

cities_name = salaries['area_name'].values
x = salaries['salary'].values
y = np.arange(len(cities_name))
ax.barh(y, x, align='center')
ax.set_yticks(y, labels=cities_name)
ax.invert_yaxis()
ax.grid(axis='x')
ax.set_title('Уровень зарплат по городам для выбранной профессии')
ax.set_xlabel('Зарплаты')
ax.set_ylabel('Города')


