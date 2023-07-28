total = float(input("What was the total bill? "))
per = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
tp = (per/100)*total
split = round((total/people)*tp,2)
print(split)
print("Bill Percent",(per/100))