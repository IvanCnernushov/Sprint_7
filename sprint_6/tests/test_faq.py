import pytest
import allure
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class TestFAQ:
    @allure.title("Проверка раскрытия ответов в FAQ - вопрос {question_index + 1}")
    @allure.description("Проверяем, что при клике на вопрос отображается соответствующий текст")
    @pytest.mark.parametrize("question_index,expected_text", [
        (0, "Сутки — 400 рублей. Оплата курьеру — наличными или картой."),
        (1, "Пока что у нас так: один заказ — один самокат."),
        (2, "Допустим, вы оформляете заказ на 8 мая."),
        (3, "Только начиная с завтрашнего дня."),
        (4, "Пока что нет!"),
        (5, "Самокат приезжает к вам с полной зарядкой."),
        (6, "Да, пока самокат не привезли."),
        (7, "Да, обязательно. Всем самокатов!")
    ])
    def test_faq_questions_expand(self, main_page, driver, question_index, expected_text):
        with allure.step(f"Кликаем на вопрос №{question_index + 1}"):
            main_page.click_faq_question(question_index)
            time.sleep(2)  # Пауза для полного раскрытия
        
        with allure.step("Проверяем, что ответ отображается"):
            # Ждем пока ответ станет видимым
            try:
                WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.CSS_SELECTOR, f"[data-accordion-component='AccordionItemPanel']:nth-child({question_index + 1})"))
                )
            except:
                pass
            
            assert main_page.is_faq_answer_displayed(question_index), f"Ответ на вопрос {question_index + 1} не отображается"
        
        with allure.step("Проверяем текст ответа"):
            answer_text = main_page.get_faq_answer_text(question_index)
            assert expected_text in answer_text, f"Текст ответа не совпадает для вопроса {question_index + 1}. Получено: {answer_text}"