from flask import Flask

app = Flask(__name__)
print(__name__)

@app.route('/')
def hellow_world():
    return '<p>Faisal Malik<p>'

if __name__ == '__main__':
    app.run()