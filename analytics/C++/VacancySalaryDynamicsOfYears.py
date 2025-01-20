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

result = df_copy[df_copy['salary'] <= 10_000_000]
result['year'] = result['published_at'].str[:4].astype(int)

dynamicOfYear = result.groupby('year')['salary'].agg('mean').round().astype(int)


import matplotlib.pyplot as plt

x = dynamicOfYear.index
y = dynamicOfYear.values
plt.bar(x, y)
plt.xticks(x, rotation=90)
plt.grid(axis='y')
plt.suptitle('Динамика уровня зарплат по годам для выбранной профессии')
plt.xlabel('Года')
plt.ylabel('Зарплаты')