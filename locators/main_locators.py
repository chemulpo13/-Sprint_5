from selenium.webdriver.common.by import By


class MainPageLocators:
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")  # Кнопка "Конструктор"
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")  # Кнопка "Личный кабинет"
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")  # Кнопка "Войти в аккаунт"
    LOGO = (By.XPATH, "//div[contains(@class, 'AppHeader_header__logo')]")  # Логотип Stellar Burgers

    # Разделы конструктора
    BUNS_TAB = (By.XPATH, "//span[text()='Булки']/parent::div")  # Вкладка "Булки"
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']/parent::div")  # Вкладка "Соусы"
    FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']/parent::div")  # Вкладка "Начинки"

    BUNS_SECTION = (By.XPATH, "//h2[text()='Булки']")  # Секция булок
    SAUCES_SECTION = (By.XPATH, "//h2[text()='Соусы']")  # Секция соусов
    FILLINGS_SECTION = (By.XPATH, "//h2[text()='Начинки']")  # Секция начинок

    PAGE_TITLE = (By.XPATH, "//h1[contains(text(), 'Соберите бургер')]")  # Заголовок страницы