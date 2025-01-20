import pandas as pd


df = pd.read_csv('vacs.csv')

df_copy = df[df['name'].str.contains('c\+\+', case=False, na=False)]

dynamicOfCity = (df_copy.groupby("area_name", as_index=False)[["area_name", "name"]]
        .agg({"area_name": "first", "name": "count"})
        .sort_values("name", ascending=False))
dynamicOfCity["rate"] = (dynamicOfCity["name"] / len(df) * 100).round(2)
rate = dynamicOfCity[['area_name', 'rate']]

result = rate[:10]
result.loc[len(rate), ['area_name', 'rate']] = 'Другие', sum(rate['rate'].values[10:])


import matplotlib.pyplot as plt

fig, ax = plt.subplots()

labels = result['area_name'].values
rates = result['rate'].values
ax.pie(rates, labels=labels)
ax.set_title('Доля вакансий по городам для выбранной профессии')


