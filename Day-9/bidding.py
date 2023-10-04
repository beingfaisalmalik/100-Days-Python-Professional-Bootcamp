import os
from art import logo

bid_log = []

def addbid(name,bidamount):
    dic = {}
    dic['name'] = name
    dic['bid_amount'] = bidamount
    bid_log.append(dic)

def showbids():
    print("All Bids")
    for bid in bid_log:
        print(bid['name'] +' bid '+ str(bid['bid_amount']))
    print(" ")
def max_bid(bid_log):
    bidwinner = ""
    maxbid = 0
    for i in range(0,len(bid_log)):
        if bid_log[i]['bid_amount'] > maxbid:
            maxbid = bid_log[i]['bid_amount']
            bidwinner+=bid_log[i]['name']
    print(" The maximum bid is " + str(maxbid))
    print(" The bid winner is " + str(bidwinner))

print(logo)
flag= True
while(flag):
    name = input("What is your name? ")
    bid = int(input("What's your bid?: "))
    addbid(name,bid)
    print("type 'yes if you want to continue otherwise 'no")
    choice = input()
    if choice == 'yes':
        os.system('cls')
        flag = True
        
    else:
        max_bid(bid_log=bid_log)
        flag = True
        
    
    
    