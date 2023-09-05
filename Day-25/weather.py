# with open('Day-25/226 weather-data.csv', 'r') as f:
#     data = [line[:-1] for line in f]
# print(data)
import pandas as pd

df = pd.read_csv('Day-25/226 weather-data.csv')
print(df['temp'])

