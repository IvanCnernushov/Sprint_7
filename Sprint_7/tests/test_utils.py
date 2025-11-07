import pytest
import requests

class TestUtils:
    
    BASE_URL = "https://qa-scooter.praktikum-services.ru"
    
    def test_ping_server(self):
        response = requests.get(f'{self.BASE_URL}/api/v1/ping')
        
        assert response.status_code == 200
        assert response.text == "pong;"

    def test_search_stations(self):
        station_name = "Сокол"
        response = requests.get(f'{self.BASE_URL}/api/v1/stations/search?s={station_name}')
        
        assert response.status_code == 200
        stations = response.json()
        assert isinstance(stations, list)
        
        if len(stations) > 0:
            station = stations[0]
            assert "number" in station
            assert "name" in station
            assert "color" in station