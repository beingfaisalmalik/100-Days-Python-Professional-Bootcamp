import requests

response =requests.get(url='http://api.open-notify.org/iss-now.json')
r = response.json()

longitude = r['iss_position']['longitude']
latitude = r['iss_position']['latitude']
iss_postion = (longitude,latitude)
print(iss_postion)

