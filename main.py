import pandas as pd
import csv
df = pd.read_csv('total_stars.csv')
print(df.shape)
del df['Luminosity']
del df['temp_Star_name']
del df['temp_Distance']
del df['temp_Mass']
del df['temp_Radius']
print(df.shape)
df.dropna(axis=0)
df.to_csv('final.csv')
