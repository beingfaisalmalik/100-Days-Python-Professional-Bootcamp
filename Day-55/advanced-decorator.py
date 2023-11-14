def decorator(function):
    def wrapper(*args, **kwargs):
        print("Before calling the function")
        print(args[0])
        square = function(args[0])
        print(square)
        print("After calling the function")
    return wrapper

@decorator
def add(num):
    return num**2

add(2)