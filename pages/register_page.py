import allure
from .base_page import BasePage
from locators.register_locators import RegisterPageLocators


class RegisterPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, url="https://stellarburgers.nomoreparties.site/register")

    @allure.step("Регистрация пользователя с именем: '{name}', email: '{email}'")
    def register(self, name, email, password):
        self.find_and_input(RegisterPageLocators.NAME_INPUT, name)
        self.find_and_input(RegisterPageLocators.EMAIL_INPUT, email)
        self.find_and_input(RegisterPageLocators.PASSWORD_INPUT, password)
        self.find_and_click(RegisterPageLocators.REGISTER_BUTTON)

    @allure.step("Переход со страницы регистрации на страницу входа")
    def go_to_login(self):
        self.find_and_click(RegisterPageLocators.LOGIN_LINK)

    @allure.step("Проверка открытия страницы регистрации")
    def is_register_page_opened(self):
        return self.is_element_visible(RegisterPageLocators.REGISTER_HEADER)

    @allure.step("Проверка отображения ошибки пароля")
    def is_password_error_displayed(self):
        return self.is_element_visible(RegisterPageLocators.PASSWORD_ERROR)