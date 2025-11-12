import pytest
import requests
import allure
from data.urls import Urls

class TestOrderCreation:
    
    @allure.title("Создание заказа с разными цветами")
    @pytest.mark.parametrize("color", [
        ["BLACK"],
        ["GREY"], 
        ["BLACK", "GREY"],
        []
    ])
    def test_create_order_with_different_colors(self, color):
        with allure.step("Создание заказа"):
            payload = {
                "firstName": "Naruto",
                "lastName": "Uzumaki",
                "address": "Konoha, 142 apt.",
                "metroStation": "4",
                "phone": "+7 800 355 35 35",
                "rentTime": 5,
                "deliveryDate": "2024-06-06",
                "comment": "Saske, come back to Konoha",
                "color": color
            }
            
            response = requests.post(Urls.BASE_URL + Urls.CREATE_ORDER, json=payload)
        
        with allure.step("Проверка создания заказа"):
            assert response.status_code == 201
            assert "track" in response.json()
            
        with allure.step("Отмена заказа"):
            track = response.json()["track"]
            cancel_payload = {"track": track}
            requests.put(Urls.BASE_URL + Urls.CANCEL_ORDER, json=cancel_payload)


class TestOrdersList:
    
    @allure.title("Получение списка заказов")
    def test_get_orders_list_returns_orders(self):
        with allure.step("Запрос списка заказов"):
            response = requests.get(Urls.BASE_URL + Urls.GET_ORDERS)
        
        with allure.step("Проверка ответа"):
            assert response.status_code == 200
            assert "orders" in response.json()