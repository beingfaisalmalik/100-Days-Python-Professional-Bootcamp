def facchecker(func):
    def wrapper(*args, **kwargs):
        print('There is something happening')
        result = func(*args, **kwargs)
        print('Nothing is happening')
        return result
    return wrapper
    
@facchecker
def fac(num):
    fact = 1
    for i in range(1,num):
        fact *= i
    return fact

print(fac(5))