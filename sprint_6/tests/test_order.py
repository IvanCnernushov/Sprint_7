import pytest
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class TestOrder:
    @allure.title("Позитивный сценарий заказа самоката через {order_button}")
    @allure.description("Проверяем полный флоу заказа самоката")
    @pytest.mark.parametrize("order_button,test_data", [
        ("header", {
            "name": "Иван",
            "last_name": "Иванов",
            "address": "Москва, Красная площадь, 1",
            "phone": "+79991234567",
            "date": "10.12.2024",
            "period": "сутки",
            "color": "black",
            "comment": "Тестовый заказ через верхнюю кнопку"
        }),
        ("footer", {
            "name": "Петр",
            "last_name": "Петров",
            "address": "Санкт-Петербург, Невский проспект, 100",
            "phone": "+79997654321",
            "date": "15.12.2024",
            "period": "двое суток",
            "color": "grey",
            "comment": "Тестовый заказ через нижнюю кнопку"
        })
    ])
    def test_scooter_order_positive_flow(self, main_page, driver, order_button, test_data):
        from pages.order_page import OrderPage
        
        with allure.step(f"Нажимаем кнопку 'Заказать' в {order_button}"):
            if order_button == "header":
                main_page.click_header_order_button()
            else:
                main_page.click_footer_order_button()

        order_page = OrderPage(driver)

        with allure.step("Заполняем первую часть формы"):
            order_page.fill_first_step_form(
                test_data["name"],
                test_data["last_name"],
                test_data["address"],
                test_data["phone"]
            )

        with allure.step("Заполняем вторую часть формы"):
            order_page.fill_second_step_form(
                test_data["date"],
                test_data["period"],
                test_data["color"],
                test_data["comment"]
            )

        with allure.step("Подтверждаем заказ"):
            order_page.confirm_order()

        with allure.step("Проверяем сообщение об успешном заказе"):
            assert order_page.is_success_message_displayed(), "Сообщение об успешном заказе не отображается"
            success_text = order_page.get_success_message()
            assert "Заказ оформлен" in success_text, f"Неверный текст успешного заказа: {success_text}"

    @allure.title("Проверка перехода на главную через логотип Самоката")
    def test_scooter_logo_redirect(self, main_page):
        with allure.step("Кликаем на логотип Самоката"):
            main_page.click_scooter_logo()
        
        with allure.step("Проверяем, что находимся на главной странице"):
            current_url = main_page.get_current_url()
            assert current_url == main_page.base_url, f"Неверный URL после клика на логотип: {current_url}"

    @allure.title("Проверка перехода на Дзен через логотип Яндекса") 
    def test_yandex_logo_redirect(self, main_page, driver):
        with allure.step("Кликаем на логотип Яндекса"):
            main_window = driver.current_window_handle
            main_page.click_yandex_logo()
        
        with allure.step("Переключаемся на новую вкладку"):
            WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
            windows = driver.window_handles
            new_window = [window for window in windows if window != main_window][0]
            driver.switch_to.window(new_window)
        
        with allure.step("Проверяем, что открылась страница Дзена"):
            WebDriverWait(driver, 10).until(EC.url_contains("dzen.ru"))
            current_url = driver.current_url
            assert "dzen.ru" in current_url, f"Неверный URL после клика на логотип Яндекса: {current_url}"