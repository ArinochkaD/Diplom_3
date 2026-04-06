from selenium.webdriver.common.by import By

class BaseLocators:
    """Общие локаторы"""
    PERSONAL_CABINET_BUTTON = (By.LINK_TEXT, "Личный Кабинет") # Кнопка с текстом "Личный Кабинет".
    ENTER_IN_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']") # Кнопка "Войти в аккаунт".
    LOGIN_TEXT = (By.LINK_TEXT, "Войти") # Кнопка с текстом "Войти".
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']") # Кнопка с текстом "Конструктор" для перехода в "Конструктор".
    LOGO_BUTTON = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2") # Кнопка-логотип "stellar burgers" для перехода в "Конструктор".
    ORDERS_BUTTON = (By.XPATH, '//p[contains(text(), "Лента Заказов")]') # Кнопка лента заказов.
    BUN_INGREDIENT = (By.XPATH, "//p[contains(text(), 'Флюоресцентная булка')]") # Айтем Флюоресцентной булки.
    SPICY_X_INGREDIENT = (By.XPATH, "//p[contains(text(), 'Соус Spicy-X')]") # Айтем Соус Spicy-X.
    SPICY_X_INGREDIENT_COUNTER = (By.XPATH, "//p[text()='Соус Spicy-X']/preceding-sibling::div//p[contains(@class, 'counter_counter__num')]") # Счетчик айтема Соус Spicy-X.
    BUN_INGREDIENT_POPUP = (By.XPATH, "//div[contains(@class, 'Modal_modal__container')]//p[text()='Флюоресцентная булка R2-D3']") # Попап Флюоресцентной булки.
    POPUP_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]") # Крестик закрытия попапа ингредиента.
    ORDER_BASKET = (By.CLASS_NAME, "BurgerConstructor_basket__list__l9dp_") # Корзина для перетаскивания ингредиента.
    MAKE_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']") # Кнопка оформить заказ.
    MODAL_ORDER_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")
    ENTER_IN_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']") # Кнопка "Войти в аккаунт".
