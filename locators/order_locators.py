from selenium.webdriver.common.by import By


class OrderLocators:
    SEARCH_TITLE = (By.XPATH, "//*[normalize-space()='Поиск машины']")
    COUNTDOWN = (By.CSS_SELECTOR, ".order-header-time, [class*='timer'], [class*='countdown']")
    CANCEL_BUTTON = (By.XPATH, "//div[div[normalize-space()='Отменить']]/button | //div[div[normalize-space()='Отмена']]/button")
    DETAILS_BUTTON = (By.XPATH, "//div[div[normalize-space()='Детали']]/button | //button[./img[@alt='burger']]")
    DETAILS_TITLE = (By.XPATH, "//*[normalize-space()='Еще про поездку']")
    PICKUP_ADDRESS = (By.XPATH, "//*[contains(normalize-space(),'Адрес подачи')]")
    DESTINATION_ADDRESS = (By.XPATH, "//*[contains(normalize-space(),'Адрес назначения')]")
    PAYMENT_INFO = (By.XPATH, "//*[contains(normalize-space(),'Способ оплаты')]")
    PRICE_INFO = (By.XPATH, "//*[contains(normalize-space(),'Стоимость')]")
    COMPLETED_ORDER_TITLE = (By.XPATH, "//*[contains(normalize-space(),'приедет')]")
    DRIVER_INFO = (By.CSS_SELECTOR, "[class*='driver']")
