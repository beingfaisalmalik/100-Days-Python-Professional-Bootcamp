from flask import Flask

app = Flask(__name__)

def makebold(func):
    def wrapper():
        b = func()
        return '<b>' + b + '</b>'
    return wrapper

def makeem(func):
    def wraaper():
        print('I"m getting executed first')
        a = func()
        return '<em>'+ a + '</em>'
    return wraaper

def makeu(func):
    def wraaper():
        print('I"m getting executed first')
        a = func()
        return '<u>'+ a + '</u>'
    return wraaper

@app.route('/')
@makeu
@makeem
@makebold
def sayhello():
    return f'Bye!'
@app.route('/username/<name>')
def home(name):
    return f'Hello {name}'

if __name__ == '__main__':
    app.run(debug=True)