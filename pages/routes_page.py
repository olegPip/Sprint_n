import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

from data.test_data import BASE_URL
from locators.routes_locators import RoutesLocators
from pages.base_page import BasePage

class RoutesPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        self._driver.get(BASE_URL)
        return self.find(RoutesLocators.FROM_INPUT)

    def set_address(self, locator, address):
        # Обход ElementClickIntercepted с помощью клика по label
        by_type, element_id = locator
        label_locator = (By.XPATH, f"//label[@for='{element_id}']")
        try:
            self.click(label_locator)
        except Exception:
            self.find(locator).click()

        # Ввод адреса
        element = self.find(locator)
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(address)

        # Ждем саджест и выбираем первую подсказку
        time.sleep(1)
        try:
            first_suggestion = self._wait.until(EC.element_to_be_clickable(RoutesLocators.SUGGESTIONS))
            first_suggestion.click()
        except Exception:
            element.send_keys(Keys.ENTER)
        time.sleep(0.4)

    def build_route(self, origin, destination):
        self.set_address(RoutesLocators.FROM_INPUT, origin)
        self.set_address(RoutesLocators.TO_INPUT, destination)
        self._wait.until(EC.visibility_of_element_located(RoutesLocators.ROUTE_PANEL))

    def route_panel_is_visible(self):
        return self.is_visible(RoutesLocators.ROUTE_PANEL)

    def map_marker_count(self):
        return len(self.find_all(RoutesLocators.MAP_MARKERS))

    def select_route_type(self, name):
        # Ищем строго div с классом mode и нужным текстом
        locator = (By.XPATH, f"//div[contains(@class, 'mode') and text()='{name}']")
        self._wait.until(EC.element_to_be_clickable(locator)).click()

    def select_transport(self, name):
        # Маппинг для поиска правильной картинки транспорта
        transport_mapping = {
            "Машина": "car",
            "Пешком": "walk",
            "Такси": "taxi",
            "Велосипед": "bike",
            "Самокат": "scooter",
            "Драйв": "drive"
        }
        svg_name = transport_mapping.get(name)
        locator = (By.XPATH, f"//div[contains(@class, 'type')]//img[contains(@src, '{svg_name}')]")
        self._wait.until(EC.element_to_be_clickable(locator)).click()

    def active_route_name(self):
        return self.text(RoutesLocators.ACTIVE_ROUTE_TAB)

    def transport_options_are_visible(self):
        return self.is_visible(RoutesLocators.TRANSPORT_PANEL)

    def taxi_button_is_enabled(self):
        try:
            button = self._wait.until(EC.presence_of_element_located(RoutesLocators.CALL_TAXI_BUTTON))
            return button.is_enabled()
        except Exception:
            return False

    def drive_button_is_enabled(self):
        try:
            button = self._wait.until(EC.presence_of_element_located(RoutesLocators.BOOK_DRIVE_BUTTON))
            return button.is_enabled()
        except Exception:
            return False

    def find_route_summary_locator(self):
        return (By.XPATH, "//*[contains(., 'Авто') and contains(., 'В пути')]")

    def open_taxi_order(self):
        self.select_route_type("Быстрый")
        self.click(RoutesLocators.CALL_TAXI_BUTTON)
