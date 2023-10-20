# ##################### Normal Starting Project ######################

# # 1. Update the birthdays.csv with your friends & family's details. 
# # HINT: Make sure one of the entries matches today's date for testing purposes. e.g.
# #name,email,year,month,day
# #YourName,your_own@email.com,today_year,today_month,today_day

import pandas as pd
import datetime as dt
import smtplib, ssl
import random
now = dt.datetime.now()
now.month
df = pd.read_csv("Day-32/birthdays.csv")
csdict = df.to_dict()
letters = []

for i in range(1,4):    
    with open(f"Day-32/letter_templates/letter_{i}.txt", "r") as f:
         
            cont = [x.strip() for x in f.readlines()]
            letters.append(cont)

persons = {}
text = ''
subject = random.choice(letters)
for item in subject:
    text += item

for i in range(len(csdict)-2):
    print(f"Name : {csdict['name'][i]} Email : {csdict['email'][i]} Year : {csdict['year'][i]} Month : {csdict['month'][i]} Day : {csdict['day'][i]}")
    persons[f'person{i+1}'] =  [csdict['name'][i],csdict['email'][i],csdict['year'][i] ,csdict['month'][i] , csdict['day'][i]]
    print(" ")
print(persons.values())
count =0;
for person in persons.values():

        if now.day == person[4]:
            smtp_server = "smtp.gmail.com"
            port = 587  # For starttls
            sender_email = "email"
            password = 'password'

            # Create a secure SSL context
            context = ssl.create_default_context()

            # Try to log in to server and send email

            server = smtplib.SMTP(smtp_server,port)
            server.ehlo() # Can be omitted
            server.starttls(context=context) # Secure the connection
            server.ehlo() # Can be omitted
            server.login(sender_email, password)
            # TODO: Send email here
            text = text.replace("[NAME],",f"{person[0]} ")
            server.sendmail(sender_email, f"{person[1]}", msg=f"Subject:Happy Birthday Dear: {person[0]}: \n\n {text}")
            server.quit()

         


