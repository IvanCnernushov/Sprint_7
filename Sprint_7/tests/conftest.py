import pytest
from helpers.courier_helper import CourierHelper

@pytest.fixture
def courier_helper():
    return CourierHelper()

@pytest.fixture
def create_courier_data():
    helper = CourierHelper()
    return helper.register_new_courier_and_return_login_password()

@pytest.fixture
def login_courier(courier_helper, create_courier_data):
    login, password, first_name = create_courier_data
    payload = {
        "login": login,
        "password": password
    }
    response = courier_helper.login_courier(payload)
    return response.json()["id"]