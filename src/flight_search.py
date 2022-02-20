import os
import requests
from dotenv import load_dotenv
from src.flight_data import FlightData

load_dotenv()

SEARCH_KEY = os.getenv("SEARCH_KEY")
SEARCH_ENDPOINT = os.getenv("SEARCH_ENDPOINT")

class FlightSearch:
    """Flight Search Class
    Class that outlines the methods to search
    airport codes and flights
    
    Attributes
    ----------
    None
    
    Methods
    ----------
    get_airport_codes
        takes in city as a parameter, and returns the 
        "closest" airport's code
    find_flights
        from the given parameters, origin_city_code, 
        destination_city_code, from and to dates, create and
        return a new "Flight Data" object.
    """

    def __init__(self):
        pass

    def get_airport_codes(self, city):
        additional = "/locations/query/"
        header = {"apikey": SEARCH_KEY}
        params = {
            "term":city,
            "locale": "en-US",
            "location_types": "airport",
            "limit": 1,
            "active_only": "true",
        }

        endpoint = SEARCH_ENDPOINT+additional
        response = requests.get(endpoint, params=params, headers=header)

        if response.json()["locations"]:
            return response.json()["locations"][0]["id"]
        else:
            raise Exception(f"{city} is not a valid airport city")

    def find_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        additional = "/v2/search/"
        endpoint = SEARCH_ENDPOINT + additional
        header = {"apikey": SEARCH_KEY}

        params = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "CAD"
        }

        response = requests.get(endpoint, params=params, headers=header)
        # print(response.json())
        
        try:
            response.json()["data"][0]
        except IndexError:
            params["max_stopovers"] = 1
            response = requests.get(endpoint, params=params, headers=header)
            try:
                response.json()["data"][0]
            except IndexError:
                print(f"No flights found for {destination_city_code}")
                return None
            else:
                data = response.json()["data"][0]
                flight_data = FlightData(
                    price = data["price"],
                    origin_city = data["route"][0]["cityFrom"],
                    origin_airport = data["route"][0]["flyFrom"],
                    destination_city = data["route"][0]["cityTo"],
                    destination_airport = data["route"][0]["flyTo"],
                    out_date = data["route"][0]["local_departure"].split("T")[0],
                    return_date = data["route"][1]["local_departure"].split("T")[0]
                )
        else:
            data = response.json()["data"][0]
            flight_data = FlightData(
                price = data["price"],
                origin_city = data["route"][0]["cityFrom"],
                origin_airport = data["route"][0]["flyFrom"],
                destination_city = data["route"][0]["cityTo"],
                destination_airport = data["route"][0]["flyTo"],
                out_date = data["route"][0]["local_departure"].split("T")[0],
                return_date = data["route"][1]["local_departure"].split("T")[0]
            )
        
        return flight_data


# fs = FlightSearch()
# fs.find_flights()


    