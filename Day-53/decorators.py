def decorator_hello(function):
    def wrapper():
        print('Im Getting Executed First')
        function()
    return wrapper





def say_hello():
    print('Hello')
    
wrapper_return = decorator_hello(say_hello)
wrapper_return()