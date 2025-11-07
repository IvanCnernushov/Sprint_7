import pytest
import requests
import random
from helpers.courier_helper import CourierHelper

class TestOrderCreation:
    
    BASE_URL = "https://qa-scooter.praktikum-services.ru"
    
    @pytest.mark.parametrize("color", [
        ["BLACK"],
        ["GREY"], 
        ["BLACK", "GREY"],
        []
    ])
    def test_create_order_with_different_colors(self, color):
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
        
        response = requests.post(f'{self.BASE_URL}/api/v1/orders', json=payload)
        
        assert response.status_code == 201
        assert "track" in response.json()
        
        # Отменяем заказ
        track = response.json()["track"]
        cancel_payload = {"track": track}
        requests.put(f'{self.BASE_URL}/api/v1/orders/cancel', json=cancel_payload)

    def test_create_order_returns_track(self):
        payload = {
            "firstName": "Test",
            "lastName": "User",
            "address": "Test Address, 123",
            "metroStation": "1",
            "phone": "+7 900 123 45 67",
            "rentTime": 3,
            "deliveryDate": "2024-06-07",
            "comment": "Test comment",
            "color": ["BLACK"]
        }
        
        response = requests.post(f'{self.BASE_URL}/api/v1/orders', json=payload)
        
        assert response.status_code == 201
        assert "track" in response.json()
        
        # Отменяем заказ
        track = response.json()["track"]
        cancel_payload = {"track": track}
        requests.put(f'{self.BASE_URL}/api/v1/orders/cancel', json=cancel_payload)


class TestOrdersList:
    
    BASE_URL = "https://qa-scooter.praktikum-services.ru"
    
    def test_get_orders_list_returns_orders(self):
        response = requests.get(f'{self.BASE_URL}/api/v1/orders')
        
        assert response.status_code == 200
        assert "orders" in response.json()
        assert "pageInfo" in response.json()
        assert "availableStations" in response.json()
        
        orders = response.json()["orders"]
        assert isinstance(orders, list)
        
        if len(orders) > 0:
            order = orders[0]
            assert "id" in order
            assert "firstName" in order
            assert "lastName" in order
            assert "address" in order

    def test_get_orders_list_with_limit(self):
        limit = 5
        response = requests.get(f'{self.BASE_URL}/api/v1/orders?limit={limit}')
        
        assert response.status_code == 200
        orders = response.json()["orders"]
        page_info = response.json()["pageInfo"]
        
        assert len(orders) <= limit
        assert page_info["limit"] == limit

    def test_get_orders_list_with_courier_id(self, courier_helper):
        # Создаем курьера
        courier_data = courier_helper.register_new_courier_and_return_login_password()
        login, password, first_name = courier_data
        
        # Логинимся чтобы получить ID
        payload_login = {"login": login, "password": password}
        login_response = requests.post(f'{self.BASE_URL}/api/v1/courier/login', data=payload_login)
        courier_id = login_response.json()["id"]
        
        # Запрашиваем заказы для этого курьера
        response = requests.get(f'{self.BASE_URL}/api/v1/orders?courierId={courier_id}')
        
        # Может вернуть 200 с пустым списком или 404 если курьер не найден
        assert response.status_code in [200, 404]
        
        if response.status_code == 200:
            assert "orders" in response.json()
        
        # Удаляем курьера
        courier_helper.delete_courier(courier_id)