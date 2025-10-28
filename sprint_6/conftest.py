import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
import os


@pytest.fixture
def driver():
    firefox_options = Options()
    firefox_options.add_argument("--width=1920")
    firefox_options.add_argument("--height=1080")
    firefox_options.add_argument("--disable-blink-features=AutomationControlled")
    firefox_options.set_preference("dom.webdriver.enabled", False)
    firefox_options.set_preference("useAutomationExtension", False)
    
    # Используем системный Firefox если webdriver-manager не работает
    try:
        from webdriver_manager.firefox import GeckoDriverManager
        service = Service(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=firefox_options)
    except:
        # Альтернативный способ - используем системный драйвер
        driver = webdriver.Firefox(options=firefox_options)
    
    driver.implicitly_wait(10)
    
    yield driver
    driver.quit()


@pytest.fixture
def main_page(driver):
    from pages.main_page import MainPage
    return MainPage(driver)