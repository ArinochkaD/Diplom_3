import allure

from pages.main_page import MainPage

class TestMainPage:
    @allure.feature('Функциональность перехода «Лента заказов».')
    @allure.description('При нажатии на кнопку «Лента заказов», открывается соответствующая страница ленты заказов.')
    def test_open_orders_page(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        main_page.click_orders_button()
        assert main_page.check_orders_url()

    @allure.feature('Функциональность перехода «Конструктор».')
    @allure.description('При нажатии на кнопку «Конструктор», открывается соответствующая страница конструктора.')
    def test_open_constructors_page(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        main_page.click_orders_button()
        main_page.click_constructor_button()
        assert main_page.check_constructor_url()

    @allure.feature('Функциональность открытия попапа ингредиента.')
    @allure.description('При нажатии на ингредиент Флюоресцентной булки, открывается соответствующий попап ингредиента.')
    def test_open_ingredient_popup(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        main_page.click_bun_ingredient()
        assert main_page.check_bun_ingredient_popup()

    @allure.feature('Функциональность проверки закрытия попапа ингредиента.')
    @allure.description('При нажатии на крестик попапа ингредиента, соответствующий попап закрывается.')
    def test_close_ingredient_popup(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        main_page.click_bun_ingredient()
        main_page.close_ingredient_popup()
        assert main_page.check_ingredient_popup_closed()

    @allure.feature('Функциональность проверки счетчика добавления ингредиента в заказ.')
    @allure.description('При перетаскивании ингреиента Spicy-X в заказ, его счетчик увеличивается.')
    def test_add_ingredient_to_order(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        old_count = main_page.get_spicy_x_ingredient_counter()
        main_page.add_cpicy_x_to_order()
        new_count = main_page.get_spicy_x_ingredient_counter()
        assert new_count > old_count
