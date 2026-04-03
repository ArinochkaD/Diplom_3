from selenium.webdriver.common.by import By

class OrdersFeedPageLocators:
    """Локаторы страницы Ленты заказов"""
    ORDERS_COUNT = (By.XPATH, "//p[contains(@class, 'OrderFeed_number')]") # Локатор счетчика всех заказов.
    ORDERS_TODAY_NUMBER = (By.XPATH, "//p[contains(@class, 'OrderFeed_number')]") # Локатор счетчика сегодняшних заказов.
    ORDERS_IN_PROGRESS = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]//li") # Локатор заказов в работе.
