height = float(input('height: '))
wight = float(input('width: '))

if height > 3:
    raise ValueError('height must be greater than 3')
raise KeyError
bmi = wight/height **2
print(bmi)