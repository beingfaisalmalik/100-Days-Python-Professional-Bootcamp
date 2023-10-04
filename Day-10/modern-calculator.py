#Caclulator


def add(num1, num2):
    return num1 + num2
def minus(num1, num2):
    return num1 - num2
def div(num1, num2):
    return num1 / num2
def mul(num1, num2):
    return num1 * num2

calc = {'+': add,'-': minus, '*': mul,'/': div}


def calculation():
    num1 = float(input('Enter The First Number? '))


    for fun in calc:
        print(fun)
    symbol = input('Pick an operation from the above list: ')
    num2 = float(input('Enter The Second Number? '))

    answer1 = calc[symbol](num1, num2)
    print(f"{num1} {symbol} {num2} = {answer1}")

    flag = True
    while flag == True:
        choice = input("Type 'y' to continue calculating with {answer1} or type 'n' to exit: ")
        if choice == 'y':
            symbol = input('Pick an operation from the above list: ')
            num3 = float(input('Enter The Second Number? '))
            answer2 = calc[symbol](num3, answer1)
            print(f"{answer1} {symbol} {num3} = {answer2}")
        else:
            flag = False
            calculation()
            
calculation()

