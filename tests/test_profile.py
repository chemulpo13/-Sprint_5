from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from conftest import driver
from data.user_data import EMAIL, PASSWORD

class TestProfile:

    def test_go_to_profile(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.go_to_login()

        login_page = LoginPage(driver)
        login_page.login(EMAIL, PASSWORD)

        main_page.go_to_personal_account()

        profile_page = ProfilePage(driver)
        assert profile_page.is_profile_page_opened(), "Не открылась страница личного кабинета"

    def test_go_to_constructor_from_profile(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.go_to_login()

        login_page = LoginPage(driver)
        login_page.login(EMAIL, PASSWORD)

        main_page.go_to_personal_account()

        profile_page = ProfilePage(driver)
        profile_page.go_to_constructor()

        assert main_page.is_main_page_opened(), "Не открылась главная страница с конструктором"

    def test_go_to_main_page_by_logo(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.go_to_login()

        login_page = LoginPage(driver)
        login_page.login(EMAIL, PASSWORD)

        main_page.go_to_personal_account()

        profile_page = ProfilePage(driver)
        profile_page.click_logo()

        assert main_page.is_main_page_opened(), "Не открылась главная страница после клика по логотипу"