import pandas as pd 
df = pd.read_csv('Day-26/50_states.csv')
l =[]
for key,values in df.iterrows():
    l.append(values.state)
print(l)
    