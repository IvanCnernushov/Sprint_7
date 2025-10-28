from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = MainPageLocators
        self.go_to_site()

    def get_faq_questions(self):
        """Получить все вопросы из FAQ"""
        return self.find_elements(self.locators.FAQ_QUESTIONS)

    def click_faq_question(self, index):
        """Кликнуть на вопрос по индексу"""
        questions = self.get_faq_questions()
        question = questions[index]
        self.scroll_to_element(question)
        question.click()

    def get_faq_answer_text(self, index):
        """Получить текст ответа по индексу"""
        answers = self.find_elements(self.locators.FAQ_ANSWERS)
        answer = answers[index]
        return answer.text

    def is_faq_answer_displayed(self, index):
        """Проверить, отображается ли ответ"""
        answers = self.find_elements(self.locators.FAQ_ANSWERS)
        answer = answers[index]
        return answer.is_displayed()

    def click_header_order_button(self):
        """Кликнуть на кнопку заказа в хедере"""
        button = self.find_element(self.locators.ORDER_BUTTON_HEADER)
        self.scroll_to_element(button)
        button.click()

    def click_footer_order_button(self):
        """Кликнуть на кнопку заказа в футере"""
        button = self.find_element(self.locators.ORDER_BUTTON_FOOTER)
        self.scroll_to_element(button)
        button.click()

    def click_scooter_logo(self):
        """Кликнуть на логотип Самоката"""
        self.find_element(self.locators.SCOOTER_LOGO).click()

    def click_yandex_logo(self):
        """Кликнуть на логотип Яндекса"""
        self.find_element(self.locators.YANDEX_LOGO).click()

    def get_current_url(self):
        """Получить текущий URL"""
        return self.driver.current_url