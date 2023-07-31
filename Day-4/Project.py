rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
userchoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))
pcchoice = random.randint(0,2)
print("---User Choice---")

if userchoice == 0:
  print(rock)
elif userchoice == 1:
  print(paper)
elif userchoice == 2:
  print(scissors)
  
print("---Pc Choice---")

if pcchoice == 0:
  print(rock)
elif pcchoice == 1:
  print(paper)
elif pcchoice == 2:
  print(scissors)

if userchoice == 0 and pcchoice == 0 or userchoice == 1 and pcchoice == 1 or userchoice == 2 and pcchoice == 2:
    print("Its Draw")
elif userchoice == 2 and pcchoice == 0 or userchoice == 0 and pcchoice == 1 or userchoice == 1 and pcchoice == 2:
    print("Pc Won")
elif userchoice == 0 and pcchoice == 2 or userchoice == 1 and pcchoice == 0 or userchoice == 2 and pcchoice == 1:
    print("User Won")   