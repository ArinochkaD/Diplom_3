import allure

from pages.main_page import MainPage
from pages.orders_feed_page import OrdersFeedPage
from utils.constants import TEST_CREDENTIALS, Urls

class TestOrdersFeedPage:
    @allure.feature('Функциональность создания нового заказа.')
    @allure.description('При создании нового заказа счётчик «Выполнено за всё время» увеличивается.')
    def test_change_all_orders_count(self, driver):
        orders_feed_page = OrdersFeedPage(driver)
        main_page = MainPage(driver)
        main_page.open_page()
        main_page.make_login(TEST_CREDENTIALS)
        orders_feed_page.open_page()
        old_count = orders_feed_page.get_all_orders_count()
        main_page.click_constructor_button()
        main_page.add_bun_to_order()
        main_page.make_order()
        main_page.wait_overlay_order()
        main_page.close_modal_order()
        orders_feed_page.open_page()
        orders_feed_page.wait_for_order_count_changed(old_count)
        new_count = orders_feed_page.get_all_orders_count()
        assert new_count > old_count

    @allure.feature('Функциональность создания нового заказа.')
    @allure.description('При создании нового заказа счётчик «Выполнено за сегодня» увеличивается.')
    def test_change_today_orders_count(self, driver):
        orders_feed_page = OrdersFeedPage(driver)
        main_page = MainPage(driver)
        main_page.open_page()
        main_page.make_login(TEST_CREDENTIALS)
        orders_feed_page.open_page()
        old_count = orders_feed_page.get_today_orders_count()
        main_page.click_constructor_button()
        main_page.add_bun_to_order()
        main_page.make_order()
        main_page.wait_overlay_order()
        main_page.close_modal_order()
        orders_feed_page.open_page()
        orders_feed_page.wait_for_today_order_count_changed(old_count)
        new_count = orders_feed_page.get_today_orders_count()
        assert new_count > old_count

    @allure.feature('Функциональность создания нового заказа.')
    @allure.description('При создании нового заказа номер этого заказа появляется в разделе «В работе».')
    def test_order_in_progress(self, driver):
        orders_feed_page = OrdersFeedPage(driver)
        main_page = MainPage(driver)
        main_page.open_page()
        main_page.make_login(TEST_CREDENTIALS)
        orders_feed_page.open_page()
        main_page.click_constructor_button()
        main_page.add_bun_to_order()
        main_page.make_order()
        main_page.wait_overlay_order()
        order_number = main_page.wait_order_number()
        main_page.close_modal_order()
        orders_feed_page.open_page()
        assert orders_feed_page.wait_for_order_in_progress_changed(order_number)
