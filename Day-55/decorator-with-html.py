def decorator1(func):
    def wraaper():
        print('I"m getting executed first')
        a = func()
        return f'<b>{a}</b>'
    return wraaper

def decorator2(func):
    def wraaper():
        print('I"m getting executed first')
        a = func()
        print(f'<em>{a}</em>')
    return wraaper
@decorator2
@decorator1
def hello():
    return 'Bye!'

hello()