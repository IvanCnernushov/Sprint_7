import pytest
import requests
from helpers.courier_helper import CourierHelper

class TestCourierCreation:
    
    BASE_URL = "https://qa-scooter.praktikum-services.ru"
    
    def test_create_courier_success(self, courier_helper):
        courier_data = courier_helper.register_new_courier_and_return_login_password()
        login, password, first_name = courier_data
        
        assert len(courier_data) == 3
        assert login is not None
        assert password is not None
        assert first_name is not None
        
        # Удаляем курьера после теста
        payload_login = {"login": login, "password": password}
        login_response = requests.post(f'{self.BASE_URL}/api/v1/courier/login', data=payload_login)
        if login_response.status_code == 200:
            courier_id = login_response.json()["id"]
            courier_helper.delete_courier(courier_id)

    def test_create_duplicate_courier_returns_error(self, courier_helper):
        courier_data = courier_helper.register_new_courier_and_return_login_password()
        login, password, first_name = courier_data
        
        # Пытаемся создать такого же курьера
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        response = requests.post(f'{self.BASE_URL}/api/v1/courier', data=payload)
        
        assert response.status_code == 409
        assert "Этот логин уже используется" in response.json()["message"]
        
        # Удаляем курьера
        payload_login = {"login": login, "password": password}
        login_response = requests.post(f'{self.BASE_URL}/api/v1/courier/login', data=payload_login)
        if login_response.status_code == 200:
            courier_id = login_response.json()["id"]
            courier_helper.delete_courier(courier_id)

    def test_create_courier_without_login_returns_error(self):
        payload = {
            "password": "password123",
            "firstName": "John"
        }
        response = requests.post(f'{self.BASE_URL}/api/v1/courier', data=payload)
        
        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для создания учетной записи"

    def test_create_courier_without_password_returns_error(self):
        payload = {
            "login": "testuser",
            "firstName": "John"
        }
        response = requests.post(f'{self.BASE_URL}/api/v1/courier', data=payload)
        
        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для создания учетной записи"

    def test_create_courier_returns_correct_response(self, courier_helper):
        # Создаем нового уникального курьера для этого теста
        login = courier_helper.generate_random_string(10)
        password = courier_helper.generate_random_string(10)
        first_name = courier_helper.generate_random_string(10)
        
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        response = requests.post(f'{self.BASE_URL}/api/v1/courier', data=payload)
        
        # Проверяем успешное создание
        assert response.status_code == 201
        assert response.json()["ok"] == True
        
        # Удаляем курьера
        payload_login = {"login": login, "password": password}
        login_response = requests.post(f'{self.BASE_URL}/api/v1/courier/login', data=payload_login)
        if login_response.status_code == 200:
            courier_id = login_response.json()["id"]
            courier_helper.delete_courier(courier_id)


class TestCourierLogin:
    
    BASE_URL = "https://qa-scooter.praktikum-services.ru"
    
    def test_login_courier_success(self, courier_helper):
        courier_data = courier_helper.register_new_courier_and_return_login_password()
        login, password, first_name = courier_data
        
        payload = {
            "login": login,
            "password": password
        }
        response = requests.post(f'{self.BASE_URL}/api/v1/courier/login', data=payload)
        
        assert response.status_code == 200
        assert "id" in response.json()
        
        # Удаляем курьера
        courier_id = response.json()["id"]
        courier_helper.delete_courier(courier_id)

    def test_login_without_login_returns_error(self, courier_helper):
        courier_data = courier_helper.register_new_courier_and_return_login_password()
        login, password, first_name = courier_data
        
        payload = {
            "password": password
        }
        response = requests.post(f'{self.BASE_URL}/api/v1/courier/login', data=payload)
        
        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для входа"
        
        # Удаляем курьера
        payload_login = {"login": login, "password": password}
        login_response = requests.post(f'{self.BASE_URL}/api/v1/courier/login', data=payload_login)
        if login_response.status_code == 200:
            courier_id = login_response.json()["id"]
            courier_helper.delete_courier(courier_id)

    def test_login_without_password_returns_error(self, courier_helper):
        courier_data = courier_helper.register_new_courier_and_return_login_password()
        login, password, first_name = courier_data
        
        payload = {
            "login": login
        }
        response = requests.post(f'{self.BASE_URL}/api/v1/courier/login', data=payload)
        
        
        assert response.status_code in [400, 504] 
        if response.status_code == 400:
            assert response.json()["message"] == "Недостаточно данных для входа"
        
        # Удаляем курьера
        payload_login = {"login": login, "password": password}
        login_response = requests.post(f'{self.BASE_URL}/api/v1/courier/login', data=payload_login)
        if login_response.status_code == 200:
            courier_id = login_response.json()["id"]
            courier_helper.delete_courier(courier_id)

    def test_login_with_wrong_password_returns_error(self, courier_helper):
        courier_data = courier_helper.register_new_courier_and_return_login_password()
        login, password, first_name = courier_data
        
        payload = {
            "login": login,
            "password": "wrongpassword"
        }
        response = requests.post(f'{self.BASE_URL}/api/v1/courier/login', data=payload)
        
        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"
        
        # Удаляем курьера
        payload_login = {"login": login, "password": password}
        login_response = requests.post(f'{self.BASE_URL}/api/v1/courier/login', data=payload_login)
        if login_response.status_code == 200:
            courier_id = login_response.json()["id"]
            courier_helper.delete_courier(courier_id)

    def test_login_nonexistent_courier_returns_error(self):
        payload = {
            "login": "nonexistentuser",
            "password": "password123"
        }
        response = requests.post(f'{self.BASE_URL}/api/v1/courier/login', data=payload)
        
        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"