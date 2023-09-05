# Unlimited positionl arguments
def add(*args):
    l = 0
    for i in args:
        l+=i
    return l

print(add(1,2,3,4,5,6))

def calculate(n,**kwargs):
    n+= kwargs["add"]
    n*= kwargs["multiply"]
    print(n)

calculate(2,add=3,multiply=5)