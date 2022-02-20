import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
from src.data_manager import DataManager
from src.flight_search import FlightSearch
from src.notification_manager import NotificationManager

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()
sheet_data = data_manager.get_destination_data()

load_dotenv()

START_LOCATION = os.getenv("START_LOCATION")
START_CITY = os.getenv("START_CITY")

# first_name = input("What is your first name? ")
# last_name = input("What is your last name? ")
# email = input("What is your email? ")

# data_manager.post_user_info(first_name, last_name, email)
# data_manager.get_user_info

if sheet_data[0]["iataCode"] == "":
    data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
last_date = tomorrow.now() + timedelta(days=180)

for destination in sheet_data:
    flight_data = flight_search.find_flights(
        START_LOCATION, 
        destination["iataCode"],
        tomorrow,
        last_date
    )
    if flight_data is not None and flight_data.price < destination["lowestPrice"]:
        text = f"""
            Low price alert! Only ${flight_data.price} to fly from 
            {START_CITY}-{flight_data.origin_airport} to {flight_data.destination_city}-{flight_data.destination_airport}, 
            from {flight_data.out_date} to {flight_data.return_date}
        """
        print(text)
        notification_manager.send_message(text)
        user_info = data_manager.get_user_info()
        for email in user_info["sheet"]["email"]:
            notification_manager.send_emails(email, text)
