import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = MainPageLocators
        self.go_to_site()

    @allure.step("Получить все вопросы из FAQ")
    def get_faq_questions(self):
        return self.find_elements(self.locators.FAQ_QUESTIONS)

    @allure.step("Кликнуть на вопрос FAQ с индексом {index}")
    def click_faq_question(self, index):
        questions = self.get_faq_questions()
        if index < len(questions):
            question = questions[index]
            self.scroll_to_element(question)
            self.wait_for_element_to_be_clickable(question)
            question.click()
            
            self.wait_for_faq_answer_to_be_displayed(index)
        else:
            raise IndexError(f"FAQ question with index {index} not found")

    @allure.step("Дождаться отображения ответа FAQ")
    def wait_for_faq_answer_to_be_displayed(self, index):
        """Явное ожидание отображения конкретного ответа"""
        def is_answer_displayed(driver):
            answers = self.find_elements(self.locators.FAQ_ANSWERS)
            if index < len(answers):
                return answers[index].is_displayed()
            return False
        
        WebDriverWait(self.driver, 10).until(is_answer_displayed)

    @allure.step("Получить ответ FAQ с индексом {index}")
    def get_faq_answer(self, index):
        answers = self.find_elements(self.locators.FAQ_ANSWERS)
        if index < len(answers):
            return answers[index]
        else:
            raise IndexError(f"FAQ answer with index {index} not found")

    @allure.step("Получить текст ответа FAQ")
    def get_faq_answer_text(self, index):
        answer = self.get_faq_answer(index)
        return answer.text

    @allure.step("Проверить отображение ответа FAQ")
    def is_faq_answer_displayed(self, index):
        try:
            answer = self.get_faq_answer(index)
            return answer.is_displayed()
        except:
            return False

    @allure.step("Кликнуть на кнопку 'Заказать' в хедере")
    def click_header_order_button(self):
        button = self.find_element(self.locators.ORDER_BUTTON_HEADER)
        self.scroll_to_element(button)
        button.click()

    @allure.step("Кликнуть на кнопку 'Заказать' в футере")
    def click_footer_order_button(self):
        button = self.find_element(self.locators.ORDER_BUTTON_FOOTER)
        self.scroll_to_element(button)
        button = self.wait_for_element_to_be_clickable(self.locators.ORDER_BUTTON_FOOTER)
        button.click()

    @allure.step("Кликнуть на логотип Самоката")
    def click_scooter_logo(self):
        self.find_element(self.locators.SCOOTER_LOGO).click()

    @allure.step("Кликнуть на логотип Яндекса")
    def click_yandex_logo(self):
        self.find_element(self.locators.YANDEX_LOGO).click()