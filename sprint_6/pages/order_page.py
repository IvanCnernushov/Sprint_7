from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = OrderPageLocators

    def fill_first_step_form(self, name, last_name, address, phone):
        """Заполнить первую часть формы заказа"""
        self.find_element(self.locators.NAME_INPUT).send_keys(name)
        self.find_element(self.locators.LAST_NAME_INPUT).send_keys(last_name)
        self.find_element(self.locators.ADDRESS_INPUT).send_keys(address)
        
        # Выбор станции метро
        self.find_element(self.locators.METRO_STATION_INPUT).click()
        self.find_element(self.locators.METRO_STATION_OPTION).click()
        
        self.find_element(self.locators.PHONE_INPUT).send_keys(phone)
        self.find_element(self.locators.NEXT_BUTTON).click()

    def fill_second_step_form(self, date, period, color, comment):
        """Заполнить вторую часть формы заказа"""
        # Ждем загрузки второй части
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.locators.DATE_INPUT)
        )
        
        # Выбор даты
        self.find_element(self.locators.DATE_INPUT).click()
        self.find_element(self.locators.DATE_OPTION).click()
        
        # Выбор периода аренды
        self.find_element(self.locators.RENTAL_PERIOD_INPUT).click()
        if period == "сутки":
            self.find_element(self.locators.RENTAL_PERIOD_OPTION).click()
        elif period == "двое суток":
            self.find_element(self.locators.RENTAL_PERIOD_OPTION_TWO_DAYS).click()
        
        # Выбор цвета
        if color == "black":
            self.find_element(self.locators.COLOR_BLACK_CHECKBOX).click()
        elif color == "grey":
            self.find_element(self.locators.COLOR_GREY_CHECKBOX).click()
        
        # Комментарий
        if comment:
            self.find_element(self.locators.COMMENT_INPUT).send_keys(comment)
        
        # Заказ - кликаем на кнопку Заказать во второй части
        order_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.locators.ORDER_BUTTON)
        )
        order_button.click()

    def confirm_order(self):
        """Подтвердить заказ"""
        # Ждем появления кнопки подтверждения
        confirm_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.locators.CONFIRM_ORDER_BUTTON)
        )
        confirm_button.click()

    def get_success_message(self):
        """Получить сообщение об успешном заказе"""
        return self.find_element(self.locators.SUCCESS_MESSAGE).text

    def is_success_message_displayed(self):
        """Проверить, отображается ли сообщение об успехе"""
        try:
            return self.find_element(self.locators.SUCCESS_MESSAGE).is_displayed()
        except:
            return False