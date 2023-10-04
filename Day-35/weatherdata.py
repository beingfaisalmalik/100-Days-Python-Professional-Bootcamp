import requests
import smtplib, ssl
API_KEY = '7baccb75e8343bada70f497c3602d32b'
response = requests.get('https://api.openweathermap.org/data/2.5/weather?q=karachi&APPID=dbd3b02d8958d62185d02e944cd5f522')
# response = requests.get('https://pro.openweathermap.org/data/2.5/forecast/hourly?lat=24.9056&lon=67.0822&appid=dbd3b02d8958d62185d02e944cd5f522')
flag = response.json()['weather']

smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = "faisalmalikff.99@gmail.com"
password = 'kzknhrovilvqdoti'

# Create a secure SSL context
context = ssl.create_default_context()

# Try to log in to server and send email
try:
    server = smtplib.SMTP(smtp_server,port)
    server.ehlo() # Can be omitted
    server.starttls(context=context) # Secure the connection
    server.ehlo() # Can be omitted
    server.login(sender_email, password)
    if flag == 'Rain':
        message = 'Bring Umbrella'
    else:
        message= 'Clear'
    # TODO: Send email here
    server.sendmail(sender_email, "faisalmalikfr.99@gmail.com", msg=f"Subject:Weather_Status\n\n {message}")
except Exception as e:
    # Print any error messages to stdout
    print(e)
finally:
    server.quit()

