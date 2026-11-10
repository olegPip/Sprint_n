import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.routes_page import RoutesPage
from pages.taxi_page import TaxiPage
from pages.order_page import OrderPage
from data.test_data import BASE_URL

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--window-size=1440,1000")
    options.add_argument("--disable-notifications")
    browser = webdriver.Chrome(options=options)

    # ПЕРЕХОД НА САЙТ: Добавляем открытие целевой страницы
    browser.get(BASE_URL)

    yield browser
    browser.quit()


@pytest.fixture
def routes_page(driver):
    page = RoutesPage(driver)
    page.open()
    return page


@pytest.fixture
def taxi_page(driver, routes_page):
    page = TaxiPage(driver)
    page.open()
    page.build_route()
    page.open_taxi_order()
    return page


@pytest.fixture
def order_page(driver, taxi_page):
    return OrderPage(driver)
