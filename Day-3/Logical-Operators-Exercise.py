name1 = input("Enter Your Name ")
name2 = input("Enter Your Second Name ")

name1 , name2 = name1.lower(), name2.lower()
truecount = name1.count("t")+name1.count("r")+name1.count("u")+name1.count("e")
truecount2= name2.count("t")+name2.count("r")+name2.count("u")+name2.count("e")

name1count = truecount+truecount2

print(" ")

lovecount2 = name2.count("l")+name2.count("o")+name2.count("v")+name2.count("e")
lovecount = name1.count("l")+name1.count("o")+name1.count("v")+name1.count("e")
name2count = lovecount+lovecount2


total = int(str(name1count)+str(name2count))
if total<10 or total> 90:
    print(f"your score is {total}% you go together like coke and mentos")
elif total>=40 or total<=50:
    print(f"your score is {total}% you are alright together")
else:
    print(f"your score is {total}%" )
    
    
    