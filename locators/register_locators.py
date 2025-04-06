from selenium.webdriver.common.by import By

class RegisterPageLocators:
    NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")  # Поле ввода имени
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")  # Поле ввода Email
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")  # Поле ввода пароля
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")  # Кнопка "Зарегистрироваться"
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")  # Ссылка "Войти"
    REGISTER_HEADER = (By.XPATH, "//h2[text()='Регистрация']")  # Заголовок "Регистрация"
    PASSWORD_ERROR = (By.XPATH, "//p[text()='Некорректный пароль']")  # Сообщение об ошибке пароля