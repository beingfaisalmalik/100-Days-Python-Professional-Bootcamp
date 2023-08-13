from art import logo,vs
from game_data import data
import random
import os




def randompersons():
    person1 = random.randrange(1,50)
    person2 = random.randrange(1,50)
    if person1 == person2:
        person2 = random.randrange(person1-1,50)
    return person1,person2



def person1info(pr1):
    print(f"Compare A: {data[pr1]['name']} a {data[pr1]['description']} from {data[pr1]['country']}")
def person2info(pr2):
    print(f"Compare B: {data[pr2]['name']} a {data[pr2]['description']} from {data[pr2]['country']}")



def person1follower(p1):
    person1followers = data[p1]['follower_count']
    return person1followers
def person2follower(p2):
    person1followers = data[p2]['follower_count']
    return person1followers




def  highlow():
    flag = False
    # Clearing the Screen
    
    person1 , person2 = randompersons()
    print(logo)
    person1info(person1)
    print(vs)
    person2info(person2)
    
    person1followers = person1follower(person1)
    
    person2followers = person1follower(person2)
    choice = input("Who has more followers? Type 'A' and 'B:' ")
    if choice == 'A' and person1followers > person2followers:
        flag = True
    elif choice == 'B' and person2followers > person1followers:
        flag = True
    elif choice == 'A' and person1followers < person2followers:
        return flag
    elif choice == 'B' and person2followers < person1followers:
        return flag
    else: return flag
    return flag

while True:
    
    score =0
    answer = highlow()
    if answer == False:
        print(f"That's Wrong your current score {score}")
        break
    else:
        score +=1
    print(f"That's Right your current score {score}")