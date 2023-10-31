# #functions are first class objects you can pass fucntions as well

def subratct(n1,n2):
    return n1-n2
def add(n1,n2):
    return n1+n2

def divide(n1,n2):
    return n1/n2

def calculate(calc_func,n1,n2):
    return calc_func(n1,n2)
    
result = calculate(divide,10,2)
print(result)


# #functions Nesting 
#only accessed from inside the functions

def outer():
    print('I"m Outer Function')
    
    def inner():
        print('I"m Inner Function')
    inner()
outer()


#functions can also be returned from other functions
def outer():
    print("I'm Outer Function")
    def Inner():
        print("I'm Inner Function")
    return Inner
inner_function = outer()
inner_function()