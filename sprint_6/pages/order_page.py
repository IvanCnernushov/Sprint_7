import allure
from .base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = OrderPageLocators

    @allure.step("Заполнить первую часть формы заказа")
    def fill_first_step_form(self, name, last_name, address, phone):
        self.find_element(self.locators.NAME_INPUT).send_keys(name)
        self.find_element(self.locators.LAST_NAME_INPUT).send_keys(last_name)
        self.find_element(self.locators.ADDRESS_INPUT).send_keys(address)
        
        self.find_element(self.locators.METRO_STATION_INPUT).click()
        self.find_element(self.locators.METRO_STATION_OPTION).click()
        
        self.find_element(self.locators.PHONE_INPUT).send_keys(phone)
        self.find_element(self.locators.NEXT_BUTTON).click()

    @allure.step("Заполнить вторую часть формы заказа")
    def fill_second_step_form(self, period, color, comment):
        self.wait_for_element_to_be_visible(self.locators.DATE_INPUT)
        self.find_element(self.locators.DATE_INPUT).click()
        self.find_element(self.locators.DATE_OPTION).click()
        
        self.find_element(self.locators.RENTAL_PERIOD_INPUT).click()
        if period == "сутки":
            self.find_element(self.locators.RENTAL_PERIOD_OPTION).click()
        elif period == "двое суток":
            self.find_element(self.locators.RENTAL_PERIOD_OPTION_TWO_DAYS).click()
        
        if color == "black":
            self.find_element(self.locators.COLOR_BLACK_CHECKBOX).click()
        elif color == "grey":
            self.find_element(self.locators.COLOR_GREY_CHECKBOX).click()
        
        if comment:
            self.find_element(self.locators.COMMENT_INPUT).send_keys(comment)
        
        order_button = self.wait_for_element_to_be_clickable(self.locators.ORDER_BUTTON)
        order_button.click()

    @allure.step("Подтвердить заказ")
    def confirm_order(self):
        confirm_button = self.wait_for_element_to_be_clickable(self.locators.CONFIRM_ORDER_BUTTON)
        confirm_button.click()

    @allure.step("Получить сообщение об успешном заказе")
    def get_success_message(self):
        return self.find_element(self.locators.SUCCESS_MESSAGE).text

    @allure.step("Проверить отображение сообщения об успехе")
    def is_success_message_displayed(self):
        try:
            return self.find_element(self.locators.SUCCESS_MESSAGE).is_displayed()
        except:
            return False

    @allure.step("Дождаться сообщения об успехе")
    def wait_for_success_message(self):
        return self.wait_for_element_to_be_visible(self.locators.SUCCESS_MESSAGE)