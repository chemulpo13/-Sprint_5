import allure
from .base_page import BasePage
from locators.main_locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, url="https://stellarburgers.nomoreparties.site/")

    @allure.title("Переход к форме входа")
    def go_to_login(self):
        self.find_and_click(MainPageLocators.LOGIN_BUTTON)

    @allure.title("Переход в личный кабинет")
    def go_to_personal_account(self):
        self.find_and_click(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.title("Проверка открытия главной страницы")
    def is_main_page_opened(self):
        return self.is_element_visible(MainPageLocators.PAGE_TITLE)

    @allure.title("Проверка видимости конструктора")
    def is_constructor_visible(self):
        return self.is_element_visible(MainPageLocators.PAGE_TITLE)

    @allure.title("Переход на страницу конструктора")
    def go_to_constructor(self):
        self.find_and_click(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.title("Переключение на вкладку 'Булки'")
    def switch_to_buns_tab(self):
        self.find_and_click(MainPageLocators.BUNS_TAB)

    @allure.title("Переключение на вкладку 'Соусы'")
    def switch_to_sauces_tab(self):
        self.find_and_click(MainPageLocators.SAUCES_TAB)

    @allure.title("Переключение на вкладку 'Начинки'")
    def switch_to_fillings_tab(self):
        self.find_and_click(MainPageLocators.FILLINGS_TAB)

    @allure.title("Проверка активности раздела 'Булки'")
    def is_buns_section_active(self):
        return self.is_element_visible(MainPageLocators.BUNS_SECTION)

    @allure.title("Проверка активности раздела 'Соусы'")
    def is_sauces_section_active(self):
        return self.is_element_visible(MainPageLocators.SAUCES_SECTION)

    @allure.title("Проверка активности раздела 'Начинки'")
    def is_fillings_section_active(self):
        return self.is_element_visible(MainPageLocators.FILLINGS_SECTION)

    @allure.title("Клик по логотипу 'Stellar Burgers'")
    def click_logo(self):
        self.find_and_click(MainPageLocators.LOGO)