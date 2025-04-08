import allure
from .base_page import BasePage
from locators.profile_locators import ProfilePageLocators

class ProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, url="https://stellarburgers.nomoreparties.site/profile")

    @allure.step("Выход из аккаунта пользователя")
    def logout(self):
        self.find_and_click(ProfilePageLocators.LOGOUT_BUTTON)

    @allure.step("Проверка открытия страницы профиля")
    def is_profile_page_opened(self):
        return self.is_element_visible(ProfilePageLocators.PROFILE_HEADER)