from selenium.webdriver.common.by import By


class OrderPageLocators:
    # Локаторы для первой части формы заказа
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_STATION_OPTION = (By.XPATH, "//div[text()='Бульвар Рокоссовского']")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    
    # Локаторы для второй части формы
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    DATE_OPTION = (By.XPATH, "//div[contains(@class, 'react-datepicker__day--today')]")
    RENTAL_PERIOD_INPUT = (By.CLASS_NAME, "Dropdown-placeholder")
    RENTAL_PERIOD_OPTION = (By.XPATH, "//div[text()='сутки']")
    RENTAL_PERIOD_OPTION_TWO_DAYS = (By.XPATH, "//div[text()='двое суток']")
    COLOR_BLACK_CHECKBOX = (By.ID, "black")
    COLOR_GREY_CHECKBOX = (By.ID, "grey")
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    
    # Кнопка Заказать во второй части формы
    ORDER_BUTTON = (By.XPATH, "//div[@class='Order_Buttons__1xGrp']//button[text()='Заказать']")
    
    # Локаторы для подтверждения заказа
    CONFIRM_ORDER_BUTTON = (By.XPATH, "//button[text()='Да']")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "Order_ModalHeader__3FDaJ")