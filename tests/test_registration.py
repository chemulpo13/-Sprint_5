from pages.register_page import RegisterPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from utils.generators import generate_email, generate_password, generate_name
from conftest import driver

class TestRegistration:

    def test_successful_registration(self, driver):
        name = generate_name()
        email = generate_email(cohort_number=5)
        password = generate_password(length=8)

        register_page = RegisterPage(driver)
        register_page.open()
        register_page.register(name, email, password)

        login_page = LoginPage(driver)
        login_page.wait_for_page_to_load()

        login_page.login(email, password)

        main_page = MainPage(driver)
        assert main_page.is_main_page_opened(), "После входа не открылась главная страница"

    def test_registration_with_short_password(self, driver):
        name = generate_name()
        email = generate_email(cohort_number=5)
        password = generate_password(length=5)

        register_page = RegisterPage(driver)
        register_page.open()
        register_page.register(name, email, password)

        assert register_page.is_password_error_displayed(), "Не отобразилась ошибка о некорректном пароле"