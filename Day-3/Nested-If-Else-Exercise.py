# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = round(int(weight)/(float(height)**2),1)

if bmi > 35:
    print("clinically obese")
elif bmi > 30:
    print("obese")
elif bmi > 25:
    print("Overweight")
elif bmi > 18.5:
    print("normal weight")
else:
    print("underweight")