class Urls:
    BASE_URL = 'https://stellarburgers.education-services.ru/'
    REGISTER_URL = BASE_URL + 'register'
    FOGOT_PASSWORD_URL = BASE_URL + 'forgot-password'
    ORDERS_FEED_URL = BASE_URL + 'feed'

class Credentials:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

TEST_CREDENTIALS = Credentials('Arina', 'arinakhugaeva3637000@bk.ru', '123456')
