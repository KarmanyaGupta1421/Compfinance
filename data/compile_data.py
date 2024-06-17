import pandas as pd
import json

df = pd.DataFrame()

for month in range(1,13):
  mnth = str(month)
  if month < 10:
    mnth = '0' + mnth
  
  file_name = 'data-' + '2023' + '-'+ mnth + '.json'
  # print(file_name)
  with open(file_name, 'r') as f:
    time_series = json.load(f)
    time_series = time_series[f"Time Series (1min)"]

    # print(time_series)

    df_temp = pd.DataFrame.from_dict(time_series, orient="index")
    
    df_temp.columns = ["Open", "High", "Low", "Close", "Volume"]
    df_temp.index = pd.to_datetime(df_temp.index)
    # print(df_temp)
    df_temp = df_temp.astype(float)

    # print(df_temp.head())

    df = pd.concat([df, df_temp])


df.to_csv('full_data.csv', sep=',', index=True)