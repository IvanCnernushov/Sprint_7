import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestOrder:
    @allure.title("Позитивный сценарий заказа самоката через верхнюю кнопку")
    @allure.description("Проверяем полный флоу заказа через верхнюю кнопку")
    def test_scooter_order_positive_flow_header(self, driver):
        test_data = {
            "name": "Иван",
            "last_name": "Иванов",
            "address": "Москва, Красная площадь, 1",
            "phone": "+79991234567",
            "period": "сутки",
            "color": "black",
            "comment": "Тестовый заказ через верхнюю кнопку"
        }
        
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        
        with allure.step("Кликаем на кнопку заказа в хедере"):
            main_page.click_header_order_button()
        
        with allure.step("Заполняем первую часть формы"):
            order_page.fill_first_step_form(
                test_data["name"],
                test_data["last_name"],
                test_data["address"],
                test_data["phone"]
            )
        
        with allure.step("Заполняем вторую часть формы"):
            order_page.fill_second_step_form(
                test_data["period"],
                test_data["color"],
                test_data["comment"]
            )
        
        with allure.step("Подтверждаем заказ"):
            order_page.confirm_order()
            order_page.wait_for_success_message()
        
        with allure.step("Проверяем сообщение об успехе"):
            assert order_page.is_success_message_displayed()
            success_text = order_page.get_success_message()
            assert "Заказ оформлен" in success_text

    @allure.title("Позитивный сценарий заказа самоката через нижнюю кнопку")
    @allure.description("Проверяем полный флоу заказа через нижнюю кнопку")
    def test_scooter_order_positive_flow_footer(self, driver):
        test_data = {
            "name": "Петр",
            "last_name": "Петров",
            "address": "Санкт-Петербург, Невский проспект, 100",
            "phone": "+79997654321",
            "period": "двое суток",
            "color": "grey",
            "comment": "Тестовый заказ через нижнюю кнопку"
        }
        
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        
        with allure.step("Кликаем на кнопку заказа в футере"):
            main_page.click_footer_order_button()
        
        with allure.step("Заполняем первую часть формы"):
            order_page.fill_first_step_form(
                test_data["name"],
                test_data["last_name"],
                test_data["address"],
                test_data["phone"]
            )
        
        with allure.step("Заполняем вторую часть формы"):
            order_page.fill_second_step_form(
                test_data["period"],
                test_data["color"],
                test_data["comment"]
            )
        
        with allure.step("Подтверждаем заказ"):
            order_page.confirm_order()
            order_page.wait_for_success_message()
        
        with allure.step("Проверяем сообщение об успехе"):
            assert order_page.is_success_message_displayed()
            success_text = order_page.get_success_message()
            assert "Заказ оформлен" in success_text

    @allure.title("Проверка перехода на главную через логотип Самоката")
    def test_scooter_logo_redirect(self, driver):
        main_page = MainPage(driver)
        main_page.click_scooter_logo()
        
        current_url = main_page.get_current_url()
        assert current_url == main_page.base_url, f"Неверный URL после клика на логотип: {current_url}"

    @allure.title("Проверка перехода на Дзен через логотип Яндекса") 
    def test_yandex_logo_redirect(self, driver):
        main_page = MainPage(driver)
        main_window = driver.current_window_handle
        
        main_page.click_yandex_logo()
        main_page.wait_for_number_of_windows(2)
        
        windows = driver.window_handles
        new_window = [window for window in windows if window != main_window][0]
        driver.switch_to.window(new_window)
        
        main_page.wait_for_url_contains("dzen.ru")
        current_url = driver.current_url
        assert "dzen.ru" in current_url, f"Неверный URL после клика на логотип Яндекса: {current_url}"