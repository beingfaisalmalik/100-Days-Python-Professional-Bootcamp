
flag = False

while(not flag):
    first_name = input('Enter Your First Name ')
    lastt_name = input('Enter Your Last Name ')
    email = input('Enter Your Email ')
    emailagain = input('Enter YOur Email Again ')
    if email != emailagain:
        print('emails do not matched')
    else:
        flag = True
        print(first_name)
        print(lastt_name)
        print(email)
        
import requests
url = 'https://api.sheety.co/962c9a731a19b4170b1fb74786c6c945/untitledSpreadsheet/sheet1'
params = {
   'sheet1': {
    'First Name':'f',
    'Last Name': 'f',
    'Email': 'f'
    }
}
repsonse = requests.post(url=url,json=params)
print(repsonse.text)


