from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, timeout=15):
        self._driver = driver
        self._wait = WebDriverWait(driver, timeout)

    def find(self, locator):
        return self._wait.until(EC.visibility_of_element_located(locator))

    def find_all(self, locator):
        return self._wait.until(EC.visibility_of_all_elements_located(locator))

    def click(self, locator):
        self._wait.until(EC.element_to_be_clickable(locator)).click()

    def type_text(self, locator, value):
        element = self.find(locator)
        element.clear()
        element.send_keys(value)

    def text(self, locator):
        return self.find(locator).text

    def is_visible(self, locator):
        try:
            self.find(locator)
            return True
        except Exception:
            return False

    def wait_until_invisible(self, locator):
        self._wait.until(EC.invisibility_of_element_located(locator))
