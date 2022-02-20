import os
import requests
from dotenv import load_dotenv
from src.flight_search import FlightSearch

load_dotenv()

SHEET_ENDPOINT = os.getenv("SHEET_ENDPOINT")
DESTINATION_SHEET = os.getenv("DESTINATION_SHEET")
USER_SHEET = os.getenv("USER_SHEET")

class DataManager:
    """Data Manager Class
    Manager class that gets and manipulates destination and user data
    
    Attributes
    ----------
    self.destination_data : Dict
        Contains destination data as a dict, NULL
    self.user_data : Dict
        Contains user data as a dict, NULL
    
    Methods
    ----------
    def get_destination_data(self)
        gets data from db and returns self.destination_data
    def write_destination_data(self)
        writes new cities to the db
    def update_destination_codes(self)
        dev QOL method. gets and writes airport (IATA codes) codes to db
    def get_user_info(self)
        self explantory, gets user info from user table
    def post_user_info(self, first, last, email)
        posts a new user to db
    """
    def __init__(self):
        self.destination_data = {}
        self.user_data = {}

    def get_destination_data(self):
        response = requests.get(f"{SHEET_ENDPOINT}/{DESTINATION_SHEET}/")
        data = response.json()
        # print(data)
        self.destination_data = data[DESTINATION_SHEET]
        return self.destination_data

    def write_destination_data(self):
        cities = []
        list = input("Cities you want to add (seperate by spaces): ")
        cities = list.split(" ")
        for city in cities:
            city_code = FlightSearch.get_airport_codes(self, city)
        data = {
            DESTINATION_SHEET: {
                "city": city.Title(),
                "iataCode": city_code,
                "lowestPrice": ""
            }
        }
        response = requests.post(f"{SHEET_ENDPOINT}/{DESTINATION_SHEET}/", json=data)

    def update_destination_codes(self):
        id = 2
        for city in self.get_destination_data():

            city_name = city["city"]
            city_code = FlightSearch.get_airport_codes(self, city_name)
            
            params = {
                DESTINATION_SHEET: {
                    "iataCode":city_code
                }
            }

            response = requests.put(f"{SHEET_ENDPOINT}/{DESTINATION_SHEET}/{id}/", json=params)
            id += 1

    def get_user_info(self):
        response = requests.get(f"{SHEET_ENDPOINT}/{USER_SHEET}")
        self.user_data = response.json()
        return self.user_data

    def post_user_info(self, first, last, email):
        payload = {
            USER_SHEET : {
                "firstName": first,
                "lastName": last,
                "email" : email
            }
        }
        response = requests.post(f"{SHEET_ENDPOINT}/{USER_SHEET}/", json=payload)
        print(response.text)

    """
    def edit_user_info(self, email, **kwargs):
        # What the fuck
        user_info = self.get_user_info()
        for user in user_info["sheet2"]:
            if email == user["email"]:
                id = user["id"]
                for key in ("first", "last", "email"):
                    if key in kwargs:
                        # params = 
                        requests.put(f"{SHEET_ENDPOINT}/sheet2/{id}")
    """
        
        

dm = DataManager()
# dm.edit_user_info("dsds@gmail.com")
# dm.post_user_info("Daniel", "Choi", "kichichoi102@gmail.com")
# dm.update_destination_codes()
# dm.write_destination_data()

