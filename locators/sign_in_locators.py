from selenium.webdriver.common.by import By

class SignInLocators:
    """Локаторы страницы Авторизации"""
    NAME_TEXTFIELD = (By.XPATH, "//label[text()='Имя']/following-sibling::input") # Текстфилд "Имя".
    EMAIL_TEXTFIELD = (By.XPATH, "//label[text()='Email']/following-sibling::input") # Текстфилд "Email".
    PASS_TEXTFIELD = (By.XPATH, "//label[text()='Пароль']/following-sibling::input") # Текстфилд "Пароль".
    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']") # Кнопка "Войти".
    AUTH_FORM = (By.CLASS_NAME, "Auth_login__3hAey") # Форма авторизации.
    REGISRATION_TEXT = (By.LINK_TEXT, "Зарегистрироваться") # Кнопка с текстом "Зарегистрироваться".
