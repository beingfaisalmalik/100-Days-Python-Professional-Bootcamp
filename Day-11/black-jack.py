## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def startingusercards():
    ucards = random.choice(cards)
    return ucards

def startingpccards():
    pcards = random.choice(cards)
    return pcards

blackjackpc = False
pcards = []
pcards.append(startingpccards())
pcards.append(startingpccards())
if pcards[0] == 11 and pcards[1] == 10 :
    blackjackpc = True
    
blackjackuser = False
userards = []
userards.append(startingusercards())
userards.append(startingusercards())
if userards[0] == 11 or 10 and userards[1] == 10 or 11:
    blackjackuser = True

def user_score(userards):
    userscore =0
    for i in range(0, len(userards)):     
        userscore += userards[i]
        if userards[i] == 11 in userards and userscore >21:
            userscore -=11
            userscore += 1
    return userscore
def pc_score(pcards):
    pcscore =0
    for i in range(0, len(pcards)):
        pcscore += pcards[i]
        if pcards[i] == 11 in userards and pcscore >21:
            pcscore -= 11
            pcscore += 1 
    return pcscore
            
userscore = user_score(userards=userards)
pcscore = pc_score(pcards=pcards)

stop = False
while(not stop):
    print(f"your cards {userards}, cureent score {userscore}")
    print(f"Computer's first hand {pcards}")
    chocie =    int(input(f"type 'y to get another card or type n to pass "))
    if chocie == 1:
        if(userscore < 21):
            userards.append(startingusercards())
            userscore = user_score(userards=userards)
            print(f"your cards {userards}, cureent score {userscore}")
            print(f"Computer's first hand {pcards}")
    elif chocie == 2:
        if(pcscore < 16):
          pcards.append(startingpccards())
          pcscore = pc_score(pcards=pcards)
          print(pc_score)
    if blackjackpc or userscore>21:
        print(f'Your final hand{userards}, final score {userscore}')
        print(f'Pc final hand{pcards}, final score {pcscore}')
        print("You lose!")
        break
    if blackjackuser or pc_score > 21:
        print(f'Your final hand{userards}, final score {userscore}')
        print(f'Pc final hand{pcards}, final score {pcscore}')
        print("You Won!")
        break
    else:
        print(f'Your final hand{userards}, final score {userscore}')
        print(f'Pc final hand{pcards}, final score {pcscore}')
        print("Draw!")
        break
        
        
