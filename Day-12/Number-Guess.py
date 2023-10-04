import random
print('Welcome To The Guessign Game! ')


def eeasy():
    return  10
def hhard():
    return  5

easy = eeasy()
hard = hhard()

print(hard)
print(easy)
numberslist =[]


for i in range(1,101):
    numberslist.append(i)

guessednumbr = random.choice(numberslist)
print(f'Guessed Number:{guessednumbr}')

choice = input('Enter Your Level ')
if choice == 'easy':
    print(f'you Have {easy} attepmts remaining to guess the number')
    while(easy>0):
        guess = int(input('Make a guess '))
        if (guess == guessednumbr):
            print('YOu Won')
        elif (guess > guessednumbr):
            print('Too High')
        else:
            print('Too Low')
        easy -=1
        print(f'you have {easy} attepmts remaining to guess the number')
        

if choice == 'hard':
    while(hard>0):
        guess = int(input('Make a guess '))
        if (guess == guessednumbr):
            print('YOu Won')
        elif (guess > guessednumbr):
            print('Too High')
        else:
            print('Too Low')
        hard -=1
        print(f'you have {hard} attepmts remaining to guess the number')
        

if easy or hard == 0:
    print("You've ran out of guesses you loose!")