import datetime as dt
import random
import smtplib, ssl
now = dt.datetime.now()


with open("Day-32/quotes.txt", "r") as f:
    content = f.readlines()
qoute = random.choice(content)

year = now.year

if year == 2023:

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
        # TODO: Send email here
        server.sendmail(sender_email, "faisalmalikfr.99@gmail.com", msg=f"Subject:Motivation Of The Day: \n\n {qoute}")
    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        server.quit()
