import requests
import smtplib, ssl
# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
urlstock = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=IBM&apikey=GQXW7I3YRQD39KG3'
urlnews = ('https://newsapi.org/v2/everything?q=ibm&apiKey=79792340121241d7a0f42f1e7b68a0de')
r = requests.get(urlstock)
response = requests.get(urlnews)
data = r.json()

final_price = data['Global Quote']['05. price']
high_price = data['Global Quote']['03. high']
low_price = data['Global Quote']['04. low']
change_per = data['Global Quote']['10. change percent']
headline = response.json()['articles'][0]['title']
Brief = response.json()['articles'][0]['description']
news = None


print(news)

smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = "email"
password = 'pass'

# Create a secure SSL context
context = ssl.create_default_context()

# Try to log in to server and send email
try:
    server = smtplib.SMTP(smtp_server,port)
    server.ehlo() # Can be omitted
    server.starttls(context=context) # Secure the connection
    server.ehlo() # Can be omitted
    server.login(sender_email, password)
    
    if float(change_per[:-1]) > 0:
        news =f"""Day End Price:{final_price} IBM: 🔺{change_per} Headline: {headline}?. Brief: {Brief[:50]}"""
    else :
        news =f"""Day End Price:{final_price} IBM: 🔻{change_per}% Headline: {headline}?. Brief: {Brief[:50]}"""
    # TODO: Send email here
    server.sendmail(sender_email, "faisalmalikfr.99@gmail.com", msg=f"Subject:Stock Report \n\n {news}")
except Exception as e:
    # Print any error messages to stdout
    print(e)
finally:
    server.quit()