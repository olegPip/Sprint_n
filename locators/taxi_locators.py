from selenium.webdriver.common.by import By


class TaxiLocators:
    # Карточки тарифов и динамический поиск по имени
    TARIFF_CARDS = (By.CSS_SELECTOR, ".tcard, [class*='tariff']")
    # Ищет родительский блок карточки тарифа, внутри которого есть элемент с нужным названием

    TARIFF_BY_NAME = lambda name: (
        By.XPATH,
        f"//div[contains(concat(' ', normalize-space(@class), ' '), ' tcard ')]"
        f"[.//div[contains(concat(' ', normalize-space(@class), ' '), ' tcard-title ')"
        f" and normalize-space()='{name}']]"
    )

    # Иконка информации внутри карточки
    TARIFF_INFO_BUTTONS = (
        By.CSS_SELECTOR,
        "button.i-button.tcard-i"
    )


    TOOLTIP_DESCRIPTION = (
        By.CSS_SELECTOR,
        ".i-floating .i-dPrefix"
    )
    # Кнопка-блок "Телефон" на главной форме заказа
    # Поле ввода/кнопка Блока телефона
    PHONE_INPUT = (By.XPATH, "//*[contains(@class, 'np-text') or contains(normalize-space(), 'Телефон')]")

    # Поле выбора способа оплаты
    PAYMENT_FIELD = (By.XPATH, "//*[contains(@class, 'payment') or contains(normalize-space(), 'Способ оплаты')]")

    # Поле комментария водителю
    DRIVER_COMMENT = (By.CSS_SELECTOR, "input#comment, [name='comment']")

    # Блок требований к заказу
    REQUIREMENTS = (By.CSS_SELECTOR, ".reqs-header, .reqs-head")

    # Элементы внутри модального окна телефона (появляется после клика на PHONE_INPUT)
    PHONE_MODAL_INPUT = (By.CSS_SELECTOR, "input#phone")
    PHONE_MODAL_SUBMIT = (By.CSS_SELECTOR, ".section.active button[type='submit']")

    # Чекбокс опции "Столик для ноутбука"
    LAPTOP_TABLE_CHECKBOX = (By.XPATH, "//*[normalize-space()='Столик для ноутбука']/..//span[contains(@class, 'slider')]")


    SUBMIT_ORDER = (By.CSS_SELECTOR, "button.smart-button, [class*='smart-button']")
