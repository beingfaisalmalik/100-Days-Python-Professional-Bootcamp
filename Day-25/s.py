import pandas as pd

df = pd.read_csv('Day-25/ss.csv')
grey = df[df["Primary Fur Color"] == 'Gray']
red = df[df["Primary Fur Color"] == 'Cinnamon']
black = df[df["Primary Fur Color"] == 'Black']
count =[]
count.append(len(grey))
count.append(len(red))
count.append(len(black))
datadict = {
    "Fur Color": ['grey','red','black'],
    "Count": count
}
df2 = pd.DataFrame(datadict)
df2.to_csv("Day-25/squirell.csv")