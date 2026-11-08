from selenium.webdriver.common.by import By


class RoutesLocators:
    # Использование стабильных ID элементов вместо сложных XPath
    FROM_INPUT = (By.ID, "from")
    TO_INPUT = (By.ID, "to")

    SUGGESTIONS = (By.CSS_SELECTOR, "[class*='suggest'], [role='option']")
    MAP_MARKERS = (By.CSS_SELECTOR, "[class*='map'] [class*='marker'], [class*='map'] [class*='placemark']")
    TRIP_INFO = (By.XPATH, "//*[contains(., 'В пути') or contains(., 'Бесплатно')]")
    CALL_TAXI_BUTTON = (By.CSS_SELECTOR, ".results-container button")
    BOOK_DRIVE_BUTTON = (By.CSS_SELECTOR, ".results-container button")
    ACTIVE_TAB = (By.CSS_SELECTOR, "[aria-selected='true'], [class*='active']")

    # Весь блок с иконками транспорта (Машина, Пешком, Такси...)
    ROUTE_PANEL = (By.CSS_SELECTOR, ".type-picker.shown")
    ACTIVE_ROUTE_TAB = (By.CSS_SELECTOR, ".mode.active")
    TRANSPORT_PANEL = (By.CSS_SELECTOR, ".types-container")
    # Списки вкладок (если они используются в find_all)
    ROUTE_TABS = (By.XPATH, "//div[contains(@class, 'route') or contains(@class, 'panel')]//button")
    TRANSPORT_TABS = (By.XPATH, "//div[contains(@class, 'transport-tabs') or contains(@class, 'types-select')]//button")
