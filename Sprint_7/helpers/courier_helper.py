import requests
import random
import string
import allure
from data.urls import Urls

class CourierHelper:
    
    @allure.step("Генерация случайной строки длиной {length}")
    def generate_random_string(self, length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    @allure.step("Регистрация нового курьера")
    def register_new_courier(self):
        login = self.generate_random_string(10)
        password = self.generate_random_string(10)
        first_name = self.generate_random_string(10)

        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        response = requests.post(Urls.BASE_URL + Urls.CREATE_COURIER, data=payload)
        return response, login, password, first_name
    
    @allure.step("Удаление курьера с ID {courier_id}")
    def delete_courier(self, courier_id):
        response = requests.delete(Urls.BASE_URL + Urls.DELETE_COURIER.format(id=courier_id))
        return response
    
    @allure.step("Логин курьера")
    def login_courier(self, login, password):
        payload = {
            "login": login,
            "password": password
        }
        response = requests.post(Urls.BASE_URL + Urls.LOGIN_COURIER, data=payload)
        return response