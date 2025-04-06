from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from conftest import driver

class TestLogout:
    EMAIL = "anatoly_chemulov_20_123@yandex.ru"
    PASSWORD = "123456"

    def test_logout(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.go_to_login()

        login_page = LoginPage(driver)
        login_page.login(self.EMAIL, self.PASSWORD)

        main_page.go_to_personal_account()

        profile_page = ProfilePage(driver)
        profile_page.logout()

        assert login_page.is_login_page_opened(), "После выхода не открылась страница входа"