print("Welocme to the roller coaster")

height = int(input("Enter your height in cm? "))
bill=0
if height >= 120:
    print("Can Ride the roller coaster")
    age = int(input("Enter your age "))
    if age <12:
        print("Children ticket price is 5$")
        bill+=5
    elif age <=18:
        print("Youths ticket price is 7$")
        bill+=7
    else :
        print("Adults ticket price is 12$")
        bill+=12
    wantsphoto = input("Enter Y or N  For Photo ")
    if wantsphoto == "Y":
        bill+=3
    print(f"Your Final Bill is {bill}")   
else:
    print("Can't Ride")