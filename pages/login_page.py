from .base_page import BasePage
from locators.login_locators import LoginPageLocators


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, url="https://stellarburgers.nomoreparties.site/login")

    def login(self, email, password):
        self.find_and_input(LoginPageLocators.EMAIL_INPUT, email)
        self.find_and_input(LoginPageLocators.PASSWORD_INPUT, password)
        self.find_and_click(LoginPageLocators.LOGIN_BUTTON)

    def go_to_register(self):
        self.find_and_click(LoginPageLocators.REGISTER_LINK)

    def go_to_forgot_password(self):
        self.find_and_click(LoginPageLocators.FORGOT_PASSWORD_LINK)

    def is_login_page_opened(self):
        return self.is_element_visible(LoginPageLocators.LOGIN_HEADER)

    def wait_for_page_to_load(self):
        self.wait_for_element_visible(LoginPageLocators.EMAIL_INPUT)
        self.wait_for_element_visible(LoginPageLocators.PASSWORD_INPUT)
        self.wait_for_element_visible(LoginPageLocators.LOGIN_BUTTON)