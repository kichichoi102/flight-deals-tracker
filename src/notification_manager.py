import os
import smtplib
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

mail = os.getenv("SOURCE_MAIL_ADDRESS")
password = os.getenv("PASSWORD")

ACCOUNT_SID = os.getenv("ACCOUNT_SID")
AUTH_TOKEN = os.getenv("AUTH_TOKEN")
FROM_NUMBER = os.getenv("FROM_NUMBER")
TO_NUMBER = os.getenv("TO_NUMBER")

class NotificationManager:
    """Notification Manager Class
    Manager class that sends sms and email notification
    when triggered
    
    Attributes
    ----------
    self.client : twilio.rest.Client
        Twilio Client Object
    
    Methods
    ----------
    def send_message(self, text)
        sends sms with `text` to phone number
    def send_email(self, email, text)
        sends email with `text` to `email`
    """

    def __init__(self):
        self.client = Client(ACCOUNT_SID, AUTH_TOKEN)

    def send_message(self, text):
        message = self.client.messages \
        .create(
            body=text,
            from_=FROM_NUMBER,
            to=TO_NUMBER
        )

        return message.sid

    def send_emails(self, email, message):
        with smtplib.SMTP("smtp.gmail.com", 587, "YOUR_USERNAME", timeout=120) as connection:
            connection.starttls()
            connection.login(user=mail, password=password)
            connection.sendmail(
                from_addr=mail, 
                to_addrs=email, 
                msg=message
            )

