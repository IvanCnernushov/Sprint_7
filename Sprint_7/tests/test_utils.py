import pytest
import requests
import allure
from data.urls import Urls

class TestUtils:
    
    @allure.title("Пинг сервера")
    def test_ping_server(self):
        with allure.step("Пинг сервера"):
            response = requests.get(Urls.BASE_URL + Urls.PING)
        
        with allure.step("Проверка ответа"):
            assert response.status_code == 200
            assert response.text == "pong;"

    @allure.title("Поиск станций метро")
    def test_search_stations(self):
        with allure.step("Поиск станций"):
            station_name = "Сокол"
            response = requests.get(Urls.BASE_URL + Urls.SEARCH_STATIONS, params={"s": station_name})
        
        with allure.step("Проверка ответа"):
            assert response.status_code == 200
            stations = response.json()
            assert isinstance(stations, list)