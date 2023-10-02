import requests
import datetime
time = datetime.datetime.now()

LAT=  51.507351
LONG= -0.127758
parameters = {
    "lat": LAT,
    "long": LONG,
    "formatted": 0,
    
}
response = requests.get('http://api.sunrise-sunset.org/json?',params=parameters)
sunset = response.json()['results']['sunset']
sunrise = response.json()['results']['sunrise']
sunrise = sunrise.split('T')[1].split(':')[0]
sunset = sunset.split('T')[1].split(':')[0]
print(sunrise)
