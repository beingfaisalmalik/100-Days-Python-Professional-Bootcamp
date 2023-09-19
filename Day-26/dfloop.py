import pandas as pd 
import numpy as np
df = pd.read_csv('Day-26/50_states.csv')
l =[]
for key,values in df.iterrows():
    l.append(values.state)
print(l)
for row in df.itertuples(index=True):
    if row.Index == 48:
        print(row)
# --->      0      1        2     3     4   5    6
names = ['Asif',"Kashif",'Hamza',1000,1000,3000,True]
# <---     -7     -6       -5     -4   -3   -2   -1

a = [*set(names[::-1])]
print(a)

data = [[1,2,3],
       [4,5,6],
       [7,8,9]]


for row in range(len(data)):
    for col in range(len(data)):
        print(data[row][col], end=" ")
    print()
    
l = [[1,'a','Z'],
    [2,'b','Y'],
    [3,'c',"X"]]

a = lambda x:x[2]

print(a([1,2,3,4]))

b = np.array([[1,2,3,4]])

print(b)