import pytest
import allure
from helpers.courier_helper import CourierHelper

@pytest.fixture
def courier_helper():
    return CourierHelper()

@pytest.fixture
def create_and_delete_courier(courier_helper):
    """Фикстура создает курьера и удаляет его после теста"""
    with allure.step("Создание тестового курьера"):
        response, login, password, first_name = courier_helper.register_new_courier()
        
        if response.status_code != 201:
            pytest.skip("Не удалось создать курьера для теста")
    
    yield login, password, first_name
    
    with allure.step("Удаление тестового курьера"):
        login_response = courier_helper.login_courier(login, password)
        if login_response.status_code == 200:
            courier_id = login_response.json()["id"]
            courier_helper.delete_courier(courier_id)