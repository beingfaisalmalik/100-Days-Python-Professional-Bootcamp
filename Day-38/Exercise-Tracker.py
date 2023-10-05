import requests

exercise_headers = {
    'x-app-id':'995fdf3e',
    'x-app-key':'21f50e8536615841f78ba8a3e19b75d5',
    "Content-Type": "application/json"
}

url = 'https://trackapi.nutritionix.com/v2/natural/exercise'

exercise_text = input("Tell Me About The Exercise You Did")
exercise_params = {
 "query":f"{exercise_text}",
}

response = requests.post(url=url,json=exercise_params,headers=exercise_headers)
duration = (response.json()['exercises'][0]['duration_min'])
exercise = (response.json()['exercises'][0]['user_input'])
calories = (response.json()['exercises'][0]['calories'])
Id = (response.json()['exercises'][0]['tag_id'])
print(f"{duration} {exercise} {calories} {Id}")
#calories, exercise, duration,


response = requests.get('https://api.sheety.co/22295796e504d19ea2d8376677342995/copyOfMyWorkouts/workouts')
print(response.json())

exercise_data = {"workout": {
    'date': '21/07/2020', 
    'time': '15:00:00', 
    'exercise': calories, 
    'duration': duration, 
    'calories': calories, 
    'id': Id
 }}
basic_auth_headers = {
    "Authorization": "Bearer dsjdsdhsd12322"
}


sheet_response = requests.post(
        url='https://api.sheety.co/22295796e504d19ea2d8376677342995/copyOfMyWorkouts/workouts',
        json=exercise_data,
    )