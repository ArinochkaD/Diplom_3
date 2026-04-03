import allure

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class BasePage():
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открыть url {url}.')
    def open_url(self, url):
        return self.driver.get(url)

    @allure.step('Дождаться появления элемента {locator}.')
    def find_element_wait(self, locator):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Дождаться отсутствия элемента {locator}.')
    def check_invisibility_element_wait(self, locator):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(expected_conditions.invisibility_of_element_located(locator))

    @allure.step('Форс клик на элемент {locator}.')
    def force_click_element(self, locator):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(expected_conditions.element_to_be_clickable(locator))
        return self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Дождаться появления элемента {locator} и кликнуть.')
    def find_element_and_click_wait(self, locator):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(expected_conditions.element_to_be_clickable(locator)).click()

    @allure.step('Проверка url {url}.')
    def check_url(self, url):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(expected_conditions.url_to_be(url))

    @allure.step('Получить текст элемента {locator}.')
    def get_actual_text(self, locator):
        return self.find_element_wait(locator).text

    @allure.step('Перетащить один элемент на другой и отпустить.')
    def drag_and_drop_element(self, first, second):
        first = self.find_element_wait(first)
        second = self.find_element_wait(second)
        # ActionChains не корректно работает с Firefox.
        self.driver.execute_script("""
            var source = arguments[0];
            var target = arguments[1];
            var dataTransfer = new DataTransfer();
            source.dispatchEvent(new DragEvent('dragstart', {dataTransfer: dataTransfer, bubbles: true}));
            target.dispatchEvent(new DragEvent('dragover', {dataTransfer: dataTransfer, bubbles: true}));
            target.dispatchEvent(new DragEvent('drop', {dataTransfer: dataTransfer, bubbles: true}));
            source.dispatchEvent(new DragEvent('dragend', {dataTransfer: dataTransfer, bubbles: true}));
        """, first, second)
        return
