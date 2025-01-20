import pandas as pd

list_of_rows = []
list_of_charcodes = ["BYR","USD","EUR","KZT","UAH","AZN","KGS","UZS","GEL"]

for year in range(2003, 2024 + 1):
    for month in range(1, 12 + 1 if year != 2024 else 12 + 1):
        url = f"http://www.cbr.ru/scripts/XML_daily.asp?date_req=01/{month:02}/{year}&d=0"
        df = pd.read_xml(url, encoding='cp1251')
        df = df[['CharCode', 'VunitRate']]
        df['VunitRate'] = df['VunitRate'].str.replace(',', '.').astype(float)
        df = df[df['CharCode'].isin(list_of_charcodes)].set_index('CharCode').T
        df.insert(0, 'date', f"{year}-{month:02}")
        list_of_rows.append(df.to_dict(orient='records')[0])

result = pd.DataFrame(list_of_rows)
result.to_csv("currency.csv", index=False)