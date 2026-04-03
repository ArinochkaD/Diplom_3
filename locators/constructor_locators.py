from selenium.webdriver.common.by import By

class ConstructorLocators:
    """Локаторы страницы Конструктора"""
    PLACE_AN_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']") # Кнопка "Оформить заказ".
    OVERLAY = (By.XPATH, "//div[contains(@class, 'Modal_modal_opened__3ISw4 Modal_modal__P3_V5')]") # Локатор оверлея загрузки оформления заказа.
    ORDER_NUMBER_IN_MODAL = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title')]") # Локатор номера заказа в модальном окне.
