import pytest
from src.flight_search import FlightSearch

class TestFlightSearch:

    @pytest.fixture(scope='module')
    def flight_search(self):
        self.flight_search = FlightSearch()
        return self.flight_search

    def test_it_can_get_airport_codes(self, flight_search):
        airport_code = "YYZ"
        test_airport_code = flight_search.get_airport_codes("Toronto")
        assert test_airport_code == airport_code