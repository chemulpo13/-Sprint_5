from .base_page import BasePage
from locators.main_locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, url="https://stellarburgers.nomoreparties.site/")

    def go_to_login(self):
        self.find_and_click(MainPageLocators.LOGIN_BUTTON)

    def go_to_personal_account(self):
        self.find_and_click(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)

    def is_main_page_opened(self):
        return self.is_element_visible(MainPageLocators.PAGE_TITLE)

    def switch_to_buns_tab(self):
        self.find_and_click(MainPageLocators.BUNS_TAB)

    def switch_to_sauces_tab(self):
        self.find_and_click(MainPageLocators.SAUCES_TAB)

    def switch_to_fillings_tab(self):
        self.find_and_click(MainPageLocators.FILLINGS_TAB)

    def is_buns_section_active(self):
        return self.is_element_visible(MainPageLocators.BUNS_SECTION)

    def is_sauces_section_active(self):
        return self.is_element_visible(MainPageLocators.SAUCES_SECTION)

    def is_fillings_section_active(self):
        return self.is_element_visible(MainPageLocators.FILLINGS_SECTION)

    def click_logo(self):
        self.find_and_click(MainPageLocators.LOGO)