from selenium.webdriver.common.by import By

class ProfilePageLocators:
    PROFILE_LINK = (By.XPATH, "//a[text()='Профиль']")  # Ссылка "Профиль"
    ORDER_HISTORY_LINK = (By.XPATH, "//a[text()='История заказов']")  # Ссылка "История заказов"
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")  # Кнопка "Выход"
    PROFILE_HEADER = (By.XPATH, "//a[text()='Профиль']")  # Заголовок профиля