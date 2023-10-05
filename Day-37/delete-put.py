import requests
import datetime

#we give system the data  requests.post()
# we want to update the given data request.put()
# we want to delete the updated data

pixela_endpoint = 'https://pixe.la/v1/users' 
TOKEN = 'wuedwueheh2e223dw'
USERNAME = "fiasal400"
now = datetime.datetime.now()
d = [now.year,now.month,now.day]
date =''
c=''
for i in range(3):
    if len(str(d[i]))==1:
        c +='0'
        c += str(d[i])
        date +=c
       
    else:
        date+=str(d[i])
# user_params = {
#      "token": TOKEN,
#      "username": USERNAME,
#      "agreeTermsOfService": "yes",
#      "notMinor": "yes",
         
#  }
# repsonse = requests.post(url=pixela_endpoint,json=user_params)
# print(repsonse.text)


# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# graph_params = {
#     'id':'graph400',
#     'name':'Cycle Graph',
#     'unit':'Km',
#     'type':'float',
#     'color':'ajisai',
# }

# headers = {
#     "X-USER-TOKEN": TOKEN
# }
# repsonse = requests.post(url=graph_endpoint,json=graph_params,headers=headers)

# print(repsonse.text)

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph400/20231005"

pixel_params = {
    'quantity':'12'
}
headers = {
    "X-USER-TOKEN": TOKEN
}

    

 
repsonse = requests.delete(url=pixel_endpoint,headers=headers)

print(repsonse.text)