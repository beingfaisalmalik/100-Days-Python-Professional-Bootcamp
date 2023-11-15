from flask import Flask,render_template
import random
import datetime,requests
app = Flask(__name__)
date = datetime.datetime.now()
y = date.year
import json

@app.route('/')
def home():
    random_number = random.randint(1,10)
    return render_template('index.html',random_number=random_number,year= y)

@app.route('/guess/<name>')
def guess(name):
    agejson = requests.get(f'https://api.agify.io/?name={name}')
    agifydic = json.loads(agejson.text)
    genderjson = requests.get(f'https://api.genderize.io/?name={name}')
    genderfydic = json.loads(genderjson.text)
    
    name = agifydic['name']
    age = agifydic['age']
    gender = genderfydic['gender']
    return render_template('name.html',name=name,gender=gender,age=age)
    
if __name__ == '__main__':
    app.run(debug=True)
