print("Welocme to the roller coaster")

height = int(input("Enter your height in cm? "))

if height >= 120:
    print("Can Ride the roller coaster")
    age = int(input("Enter your age "))
    if age <12:
        print("Your ticket price is 5$")
    elif age <=18:
        print("Your ticket price is 7$")
    else :
        print("Your ticket price is 12$")
else:
    print("Can't Ride")