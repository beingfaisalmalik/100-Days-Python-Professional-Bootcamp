numbers = []
#Range Can Be Done With Steps
for i in range(2,101,2):
    numbers.append(i)
total =0
for number in numbers:
    total += number
print(total)