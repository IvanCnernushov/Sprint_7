from selenium.webdriver.common.by import By


class MainPageLocators:
    # Локаторы для FAQ
    FAQ_QUESTIONS = (By.CSS_SELECTOR, "[data-accordion-component='AccordionItemButton']")
    FAQ_ANSWERS = (By.CSS_SELECTOR, "[data-accordion-component='AccordionItemPanel']")
    
    # Локаторы для кнопок заказа - правильные
    ORDER_BUTTON_HEADER = (By.XPATH, "//div[@class='Header_Nav__AGCXC']//button[text()='Заказать']")
    ORDER_BUTTON_FOOTER = (By.XPATH, "//div[@class='Home_FinishButton__1_cWm']//button[text()='Заказать']")
    
    # Локаторы логотипов
    SCOOTER_LOGO = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    YANDEX_LOGO = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")