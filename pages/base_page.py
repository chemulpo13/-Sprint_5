import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, url=None):
        self.driver = driver
        self.url = url

    @allure.step("Открытие страницы")
    def open(self):
        self.driver.get(self.url)

    @allure.step("Ожидание видимости элемента {locator}")
    def wait_for_element_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step("Ожидание кликабельности элемента {locator}")
    def wait_for_element_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    @allure.step("Ожидание URL, содержащего '{text}'")
    def wait_for_url_contains(self, text, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.url_contains(text)
        )

    @allure.step("Проверка видимости элемента {locator}")
    def is_element_visible(self, locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except:
            return False

    @allure.step("Поиск элемента {locator}")
    def find_element(self, locator, timeout=10):
        return self.wait_for_element_visible(locator, timeout)

    @allure.step("Найти и кликнуть по элементу {locator}")
    def find_and_click(self, locator, timeout=10):
        element = self.wait_for_element_clickable(locator, timeout)
        element.click()
        return element

    @allure.step("Найти элемент {locator} и ввести текст: {text}")
    def find_and_input(self, locator, text, timeout=10):
        element = self.wait_for_element_visible(locator, timeout)
        element.clear()
        element.send_keys(text)
        return element