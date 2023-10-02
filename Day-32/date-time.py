import datetime as dt

now = dt.datetime .now()
year = [now.year, now.month, now.day, now.hour, now.minute]

for y in year:
    print(y)
    
date_of_birth = dt.datetime(year=2001,month=8,day=2)
print(date_of_birth)