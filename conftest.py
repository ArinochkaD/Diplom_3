import allure
import pytest
import sys
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from utils.constants import Credentials

# Добавляем текущую директорию в sys.path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

@pytest.fixture(params=['Chrome', 'Firefox'])
def driver(request):
    with allure.step(f'Запуск браузера {request.param}.'):
        if request.param == 'Chrome':
            service = Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service)
        else:
            driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def test_credentials():
    return Credentials('Arina', 'arinakhugaeva3637000@bk.ru', '123456')
