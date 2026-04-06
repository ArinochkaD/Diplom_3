import allure

from locators.base_locators import BaseLocators
from locators.constructor_locators import ConstructorLocators
from locators.sign_in_locators import SignInLocators
from pages.base_page import BasePage
from utils.constants import Urls

class MainPage(BasePage):
    @allure.step('Перейти по адресу.')
    def open_page(self, url=Urls.BASE_URL):
        return self.open_url(url)

    @allure.step('Нажать на кнопку «Лента заказов».')
    def click_orders_button(self):
        return self.find_element_and_click_wait(BaseLocators.ORDERS_BUTTON)

    @allure.step('Проверить соответствие url «Лента заказов».')
    def check_orders_url(self):
        return self.check_url(Urls.ORDERS_FEED_URL)

    @allure.step('Нажать на кнопку «Конструктор».')
    def click_constructor_button(self):
        return self.force_click_element(BaseLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Проверить соответствие url «Конструктор».')
    def check_constructor_url(self):
        return self.check_url(Urls.BASE_URL)

    @allure.step('Нажать на ингредиент Флюоресцентной булки.')
    def click_bun_ingredient(self):
        return self.find_element_and_click_wait(BaseLocators.BUN_INGREDIENT)

    @allure.step('Проверить успешное открытие попапа Флюоресцентной булки.')
    def check_bun_ingredient_popup(self):
        return self.find_element_wait(BaseLocators.BUN_INGREDIENT_POPUP)

    @allure.step('Нажать на крестик попапа ингредиента.')
    def close_ingredient_popup(self):
        return self.find_element_and_click_wait(BaseLocators.POPUP_CLOSE_BUTTON)

    @allure.step('Проверить успешное закрытие попапа Флюоресцентной булки.')
    def check_ingredient_popup_closed(self):
        return self.check_invisibility_element_wait(BaseLocators.BUN_INGREDIENT_POPUP)

    @allure.step('Получить значение счетчика ингредиента Spicy-X.')
    def get_spicy_x_ingredient_counter(self):
        return self.get_actual_text(BaseLocators.SPICY_X_INGREDIENT_COUNTER)

    @allure.step('Добавить ингредиент Spicy-X в заказ.')
    def add_cpicy_x_to_order(self):
        return self.drag_and_drop_element(BaseLocators.SPICY_X_INGREDIENT, BaseLocators.ORDER_BASKET)

    @allure.step('Добавить ингредиент Флюоресцентную булку в заказ.')
    def add_bun_to_order(self):
        return self.drag_and_drop_element(BaseLocators.BUN_INGREDIENT, BaseLocators.ORDER_BASKET)

    @allure.step('Нажать на кнопку оформить заказ.')
    def make_order(self):
        return self.force_click_element(BaseLocators.MAKE_ORDER_BUTTON)

    @allure.step("Нажать на крестик окна оформленного заказа.")
    def close_modal_order(self):
        self.check_invisibility_element_wait(ConstructorLocators.OVERLAY)
        return self.force_click_element(BaseLocators.MODAL_ORDER_CLOSE_BUTTON)

    @allure.step("Дождаться номера заказа.")
    def wait_order_number(self):
        self.check_invisibility_element_wait(ConstructorLocators.OVERLAY)
        return self.find_element_wait(ConstructorLocators.ORDER_NUMBER_IN_MODAL).text

    @allure.step("Авторизоваться.")
    def make_login(self, credentials):
        self.find_element_and_click_wait(BaseLocators.ENTER_IN_ACCOUNT_BUTTON)
        email = self.find_element_wait(SignInLocators.EMAIL_TEXTFIELD)
        email.send_keys(credentials.email)
        password = self.find_element_wait(SignInLocators.PASS_TEXTFIELD)
        password.send_keys(credentials.password)
        login_button = self.find_element_wait(SignInLocators.LOGIN_BUTTON)
        login_button.click()
        return self.find_element_wait(ConstructorLocators.PLACE_AN_ORDER_BUTTON)

    @allure.step("Подождать пока пройдет оверлей загрузки оформления заказа.")
    def wait_overlay_order(self):
        return self.check_invisibility_element_wait(ConstructorLocators.OVERLAY)
