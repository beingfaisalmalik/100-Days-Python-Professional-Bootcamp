import pandas as pd

# with open('Day-25/226 weather-data.csv', 'r') as f:
#     data = [line[:-1] for line in f]
# print(data)
import pandas as pd

df = pd.read_csv('Day-25/226 weather-data.csv')
print(type(df['temp']))

col = df.columns
for i in col:
    print(i)
df.condition
templist = df['temp'].max()
print(templist)

mon = df[df.day=="Monday"]
print(mon)
print(mon.temp%273)
maxtemp = df[df.temp == df.temp.max()]
print(maxtemp)


#Create a dataframe from sctrach

datadict = {
    "student": ["Faisal", "ALi","nasir"],
    "score": [1,2,3]
}
df2 = pd.DataFrame(datadict)
df2.to_csv("faisal")
