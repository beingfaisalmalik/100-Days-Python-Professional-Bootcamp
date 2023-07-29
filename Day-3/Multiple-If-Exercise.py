print("Welcome To Python Pizza Deliveries")
size = input('what size pizza do you want? S, M, or L ')
add_pepperoni = input("Do want extra pepperoni Y or N ")
extra_cheese = input("Do want extra cheese Y or N ")

Small_pizaa = 15
Medium_pizza = 20
Large_pizza = 25
cheese = 1
pepperoni_small = 2
pepperoni_LM = 3
bill = 0

if size == "S":
    if add_pepperoni == "Y":
        if extra_cheese =="Y":
            bill+=cheese
            bill+= pepperoni_small
            bill+=Small_pizaa
        else:
            bill+= pepperoni_small
            bill+=Small_pizaa
    elif add_pepperoni =="N":
        if extra_cheese =="Y":
            bill+=cheese
            bill+=Small_pizaa
        else:
             bill+=Small_pizaa
elif size == "M":
    if add_pepperoni == "Y":
        if extra_cheese =="Y":
            bill+=cheese
            bill+= pepperoni_LM
            bill+=Medium_pizza
        else:
            bill+= pepperoni_LM
            bill+=Medium_pizza
    elif add_pepperoni =="N":
        if extra_cheese =="Y":
            bill+=cheese
            bill+=Medium_pizza
        else:
             bill+=Medium_pizza
    
elif size == "L":
    if add_pepperoni == "Y":
        if extra_cheese =="Y":
            bill+=cheese
            bill+= pepperoni_LM
            bill+=Large_pizza
        else:
            bill+= pepperoni_LM
            bill+=Large_pizza
    elif add_pepperoni =="N":
        if extra_cheese =="Y":
            bill+=cheese
            bill+=Large_pizza
        else:
             bill+=Large_pizza


print(f"Your final bill is:${bill}")
