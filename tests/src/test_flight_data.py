import pytest
from src.flight_data import FlightData

class TestFlightData:

    @pytest.fixture(scope='module')
    def flight_data(self):
        self.flight_data = FlightData(
            "test_price",
            "test_origin_city",
            "test_origin_airport",
            "test_destination_city",
            "test_destination_airport",
            "test_out_date",
            "test_return_date",
            "test_stop_overs",
            "test_via_city"
        )
        return self.flight_data
    
    def test_instantiate_class(self, flight_data):
        assert flight_data.price == "test_price"
        assert flight_data.origin_city == "test_origin_city"
        assert flight_data.origin_airport == "test_origin_airport"
        assert flight_data.destination_city == "test_destination_city"
        assert flight_data.destination_airport == "test_destination_airport"
        assert flight_data.out_date == "test_out_date"
        assert flight_data.return_date == "test_return_date"
        assert flight_data.stop_overs == "test_stop_overs"
        assert flight_data.via_city == "test_via_city"
