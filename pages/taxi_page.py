from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import time
from data.test_data import ORIGIN, DESTINATION, TAXI_TARIFFS
from locators.taxi_locators import TaxiLocators
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data.test_data import BASE_URL
from pages.routes_page import RoutesPage

class TaxiPage(BasePage):
    def open(self):
        self._driver.get(BASE_URL)
        return self

    def build_route(self):
        RoutesPage(self._driver).build_route(ORIGIN, DESTINATION)
        return self

    def open_taxi_order(self):
        RoutesPage(self._driver).open_taxi_order()
        self.find(TaxiLocators.TARIFF_CARDS)
        return self

    def tariff_names(self):
        elements = self._driver.find_elements(*TaxiLocators.TARIFF_CARDS)

        return [el.text.split('\n')[0].strip() for el in elements if el.text]

    def hover_tariff_info(self, tariff_name):
        card = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located(
                TaxiLocators.TARIFF_BY_NAME(tariff_name)
            )
        )

        self._driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            card
        )

        info_button = card.find_element(
            By.CSS_SELECTOR,
            "button.i-button.tcard-i"
        )

        # Проверяем, есть ли у кнопки видимая область
        button_size = self._driver.execute_script("""
            const rect = arguments[0].getBoundingClientRect();
            return {
                width: rect.width,
                height: rect.height
            };
        """, info_button)

        if button_size["width"] > 0 and button_size["height"] > 0:
            ActionChains(self._driver).move_to_element(info_button).perform()
        else:
            # Если кнопка невидима, наводим курсор на карточку
            ActionChains(self._driver).move_to_element(card).perform()

        description = WebDriverWait(card, 5).until(
            lambda element: element.find_element(
                By.CSS_SELECTOR,
                ".i-floating .i-dPrefix"
            )
        )

        return self._driver.execute_script(
            "return arguments[0].textContent.trim();",
            description
        )

    def select_tariff(self, name):
        tariff_title = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located(TaxiLocators.TARIFF_BY_NAME(name))
        )
        # 2. Скроллим к нему
        self._driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", tariff_title)
        time.sleep(0.5)

        tariff_title.click()
        time.sleep(1)

    def enable_laptop_table(self):
        req_header = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located(TaxiLocators.REQUIREMENTS)
        )
        self._driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", req_header)
        time.sleep(0.5)

        try:
            arrow = req_header.find_element(By.CSS_SELECTOR, ".reqs-arrow")
            if "open" not in arrow.get_attribute("class"):
                req_header.click()
                time.sleep(0.5)
        except Exception:
            req_header.click()
            time.sleep(0.5)

        slider = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located(TaxiLocators.LAPTOP_TABLE_CHECKBOX)
        )
        self._driver.execute_script("arguments[0].click();", slider)

    def submit_order(self):
        self.click(TaxiLocators.SUBMIT_ORDER)

    def is_phone_field_visible(self):
        try:
            WebDriverWait(self._driver, 5).until(
                EC.visibility_of_element_located(TaxiLocators.PHONE_INPUT)
            )
            return True
        except Exception:
            return False

    def is_payment_method_visible(self):
        return self.is_visible(TaxiLocators.PAYMENT_FIELD)

    def is_comment_field_visible(self):
        return self.is_visible(TaxiLocators.DRIVER_COMMENT)

    def is_requirements_block_visible(self):
        return self.is_visible(TaxiLocators.REQUIREMENTS)
