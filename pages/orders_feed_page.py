import allure

from selenium.webdriver.support.wait import WebDriverWait
from locators.orders_feed_page_locators import OrdersFeedPageLocators
from pages.base_page import BasePage
from utils.constants import Urls

class OrdersFeedPage(BasePage):
    @allure.step('Перейти по адресу.')
    def open_page(self, url=Urls.ORDERS_FEED_URL):
        return self.open_url(url)

    @allure.step('Получить значение счетчика всех заказов.')
    def get_all_orders_count(self):
        return self.get_actual_text(OrdersFeedPageLocators.ORDERS_COUNT)

    @allure.step('Ожидаем пока счетчик общих заказов не изменится.')
    def wait_for_order_count_changed(self, old_count):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(lambda driver: self.get_all_orders_count() != old_count)

    @allure.step('Получить значение счетчика заказов сегодня.')
    def get_today_orders_count(self):
        return self.get_actual_text(OrdersFeedPageLocators.ORDERS_TODAY_NUMBER)

    @allure.step('Ожидаем пока счетчик общих заказов не изменится.')
    def wait_for_today_order_count_changed(self, old_count):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(lambda driver: self.get_today_orders_count() != old_count)

    @allure.step('Ожидаем пока заказ не появится в списке заказов.')
    def wait_for_order_in_progress_changed(self, order_number):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(lambda d: order_number in self.find_element_wait(OrdersFeedPageLocators.ORDERS_IN_PROGRESS).text)
