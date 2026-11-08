from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from locators.order_locators import OrderLocators
from pages.base_page import BasePage


class OrderPage(BasePage):
    def search_window_is_visible(self):
        return self.is_visible(OrderLocators.SEARCH_TITLE)

    def countdown_is_visible(self):
        try:
            WebDriverWait(self._driver, 5).until(
                EC.visibility_of_element_located(OrderLocators.COUNTDOWN)
            )
            return True
        except TimeoutException:
            return False

    def wait_for_search_to_complete(self, timeout=40):

        WebDriverWait(self._driver, timeout).until(
            EC.invisibility_of_element_located(OrderLocators.SEARCH_TITLE)
        )
        return self

    def open_details(self):
        btn = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located(OrderLocators.DETAILS_BUTTON)
        )

        self._driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", btn)
        self._driver.execute_script("arguments[0].click();", btn)
        return self

    def details_are_visible(self):
        return self.is_visible(OrderLocators.DETAILS_TITLE)

    def price_text(self):
        return self.text(OrderLocators.PRICE_INFO)

    def cancel_order(self):
        btn = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located(OrderLocators.CANCEL_BUTTON)
        )
        self._driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", btn)
        self._driver.execute_script("arguments[0].click();", btn)

    def completed_order_is_visible(self):
        return self.is_visible(OrderLocators.COMPLETED_ORDER_TITLE)

    def driver_info_is_visible(self):
        return self.is_visible(OrderLocators.DRIVER_INFO)
