from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.register_page import RegisterPage
from conftest import driver
from data.user_data import EMAIL, PASSWORD

class TestLogin:

    def test_login_from_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.go_to_login()

        login_page = LoginPage(driver)
        login_page.login(EMAIL, PASSWORD)

        assert main_page.is_main_page_opened(), "После входа не открылась главная страница"

    def test_login_from_personal_account_button(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.go_to_personal_account()

        login_page = LoginPage(driver)
        login_page.login(EMAIL, PASSWORD)

        assert main_page.is_main_page_opened(), "После входа не открылась главная страница"

    def test_login_from_register_form(self, driver):
        register_page = RegisterPage(driver)
        register_page.open()
        register_page.go_to_login()

        login_page = LoginPage(driver)
        login_page.login(EMAIL, PASSWORD)

        main_page = MainPage(driver)
        assert main_page.is_main_page_opened(), "После входа не открылась главная страница"

    def test_login_from_forgot_password_form(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.go_to_forgot_password()

        driver.get("https://stellarburgers.nomoreparties.site/login")

        login_page.login(EMAIL, PASSWORD)

        main_page = MainPage(driver)
        assert main_page.is_main_page_opened(), "После входа не открылась главная страница"