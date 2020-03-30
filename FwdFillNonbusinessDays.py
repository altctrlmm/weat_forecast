from datetime import datetime
from datetime import timedelta
import pandas as pd
pd.set_option('display.max_rows', None)
csv_path = 'C:\\Users\\micah\\Desktop\\WEAT.csv'

def fill_in_missing_dates(df, date_col_name = 'date',date_order = 'asc', fill_value = 0, days_back = 3000):
    df.set_index(date_col_name,drop=True,inplace=True)
    df.index = pd.DatetimeIndex(df.index)
    d = df.index.max()
    d2 = df.index.min()
    idx = pd.date_range(d2, d, freq = "D")
    df = df.reindex(idx,fill_value=fill_value)
    df[date_col_name] = pd.DatetimeIndex(df.index)
    return df

df = pd.read_csv(csv_path)

df = fill_in_missing_dates(df, date_col_name = 'date',date_order = 'asc', fill_value = 0, days_back = 30)

cols = ["4. close","1. open","2. high", "3. low", "5. volume"]
df[cols] = df[cols].replace({0:np.nan})

cols2 = ["item_id"]
df[cols2] = df[cols2].replace({0:'WEAT'})

df[cols] = df[cols].replace('', np.nan).fillna(method='ffill')
    
print(df)

df.to_csv(r'C:\\Users\\micah\\Desktop\\WEAT_2.csv', index = False)
