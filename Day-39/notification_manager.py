import smtplib,ssl
smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = "faisalmalikff.99@gmail.com"
password = 'kzknhrovilvqdoti'

# Create a secure SSL context
context = ssl.create_default_context()

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        pass
    def email_sender(self,message):
        try:
            server = smtplib.SMTP(smtp_server,port)
            server.ehlo() # Can be omitted
            server.starttls(context=context) # Secure the connection
            server.ehlo() # Can be omitted
            server.login(sender_email, password)
            # TODO: Send email here
            server.sendmail(sender_email, "faisalmalikfr.99@gmail.com", msg=f"Subject:Low Price Alert \n\n {message}")
        except Exception as e:
            # Print any error messages to stdout
            print(e)
        finally:
            server.quit()
        







