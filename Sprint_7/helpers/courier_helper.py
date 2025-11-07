import requests
import random
import string

class CourierHelper:
    
    BASE_URL = "https://qa-scooter.praktikum-services.ru"
    
    def generate_random_string(self, length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    def register_new_courier_and_return_login_password(self):
        login_pass = []
        
        login = self.generate_random_string(10)
        password = self.generate_random_string(10)
        first_name = self.generate_random_string(10)

        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        response = requests.post(f'{self.BASE_URL}/api/v1/courier', data=payload)

        if response.status_code == 201:
            login_pass.append(login)
            login_pass.append(password)
            login_pass.append(first_name)

        return login_pass
    
    def delete_courier(self, courier_id):
        response = requests.delete(f'{self.BASE_URL}/api/v1/courier/{courier_id}')
        return response
    
    def login_courier(self, payload):
        response = requests.post(f'{self.BASE_URL}/api/v1/courier/login', data=payload)
        return response
  