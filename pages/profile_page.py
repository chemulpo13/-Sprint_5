from .base_page import BasePage
from locators.profile_locators import ProfilePageLocators

class ProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, url="https://stellarburgers.nomoreparties.site/profile")

    def logout(self):
        self.find_and_click(ProfilePageLocators.LOGOUT_BUTTON)

    def is_profile_page_opened(self):
        return self.is_element_visible(ProfilePageLocators.PROFILE_HEADER)

    def go_to_constructor(self):
        from locators.main_locators import MainPageLocators
        self.find_and_click(MainPageLocators.CONSTRUCTOR_BUTTON)

    def click_logo(self):
        from locators.main_locators import MainPageLocators
        self.find_and_click(MainPageLocators.LOGO)