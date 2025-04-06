import allure
from pages.main_page import MainPage
from conftest import driver

class TestConstructor:

    @allure.title('Проверка переключения на вкладку "Булки"')
    def test_switch_to_buns_tab(self, driver):
        main_page = MainPage(driver)
        main_page.open()

        main_page.switch_to_sauces_tab()

        main_page.switch_to_buns_tab()

        assert main_page.is_buns_section_active(), "Секция 'Булки' не активна"

    @allure.title('Проверка переключения на вкладку "Соусы"')
    def test_switch_to_sauces_tab(self, driver):
        main_page = MainPage(driver)
        main_page.open()

        main_page.switch_to_sauces_tab()

        assert main_page.is_sauces_section_active(), "Секция 'Соусы' не активна"

    @allure.title('Проверка переключения на вкладку "Начинки"')
    def test_switch_to_fillings_tab(self, driver):
        main_page = MainPage(driver)
        main_page.open()

        main_page.switch_to_fillings_tab()

        assert main_page.is_fillings_section_active(), "Секция 'Начинки' не активна"