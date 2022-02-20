import pytest
from src.data_manager import DataManager


class TestDataManager:

    @pytest.fixture(scope='module')
    def data_manager(self):
        self.data_manager = DataManager()
        return self.data_manager

    def test_it_can_get_destination_data(self, data_manager):
        destination_data = [
            {
                'city': 'Paris', 
                'iataCode': 'CDG', 
                'lowestPrice': 54, 
                'id': 2
            }, 
            {
                'city': 'Berlin', 
                'iataCode': 'BER', 
                'lowestPrice': 42,
                'id': 3
            }, 
            {
                'city': 'Tokyo', 
                'iataCode': 'NRT', 
                'lowestPrice': 485, 
                'id': 4
            }, 
            {
                'city': 'Sydney', 
                'iataCode': 'SYD', 
                'lowestPrice': 551, 
                'id': 5
            }, 
            {
                'city': 'Istanbul', 
                'iataCode': 'SAW', 
                'lowestPrice': 95, 
                'id': 6
            }, 
            {
                'city': 'Kuala Lumpur', 
                'iataCode': 'KUL', 
                'lowestPrice': 414, 
                'id': 7
            }, 
            {
                'city': 'New York', 
                'iataCode': 'JFK', 
                'lowestPrice': 240, 
                'id': 8
            }, 
            {
                'city': 'San Francisco', 
                'iataCode': 'SFO', 
                'lowestPrice': 260, 
                'id': 9
            }, 
            {
                'city': 'Cape Town', 
                'iataCode': 'CPT', 
                'lowestPrice': 378, 
                'id': 10
            }
        ]
        test_destination_data = data_manager.get_destination_data()
        assert destination_data == test_destination_data

    def test_it_can_get_user_info(self, data_manager):
        user_info = {
            'sheet2': [
                {
                    'firstName': 'daniel', 
                    'lastName': 'dsds', 'email': 
                    'dsds@gmail.com', 
                    'id': 2
                }, 
                {
                    'firstName': 'dsdsdssd', 
                    'lastName': 'dsaADsdfsa', 
                    'email': 'sdffdsf@gmail.com', 
                    'id': 3
                }, 
                {
                    'firstName': 'daniel', 
                    'lastName': 'choi', 
                    'email': 'kichichoi102@gmail.com', 
                    'id': 4
                }
            ]
        }
        test_user_info = data_manager.get_user_info()
        assert test_user_info == user_info
