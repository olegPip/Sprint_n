import allure
import pytest

from locators.order_locators import OrderLocators


@allure.feature("Полный флоу заказа Такси")
class TestTaxiOrderFlow:
    @allure.title("После отправки заказа открывается окно поиска машины")
    def test_car_search_window_is_displayed(self, taxi_page, order_page):
        taxi_page.select_tariff("Рабочий")
        taxi_page.enable_laptop_table()
        taxi_page.submit_order()
        assert order_page.search_window_is_visible()
        assert order_page.countdown_is_visible()

    @allure.title("После завершения поиска отображается совершенный заказ")
    @pytest.mark.xfail(reason="Проверка зависит от завершения серверного таймера; дефект стенда требует подтверждения")
    def test_completed_order_is_displayed(self, taxi_page, order_page):
        taxi_page.select_tariff("Рабочий")
        taxi_page.enable_laptop_table()
        taxi_page.submit_order()
        assert order_page.completed_order_is_visible()
        assert order_page.driver_info_is_visible()

    @allure.title("В деталях отображается стоимость выбранного тарифа")
    def test_order_details_show_price(self, taxi_page, order_page):
        taxi_page.select_tariff("Рабочий")
        taxi_page.enable_laptop_table()
        taxi_page.submit_order()

        order_page.wait_for_search_to_complete(timeout=45)
        order_page.open_details()

        assert order_page.details_are_visible()
        assert order_page.price_text()

    @allure.title("Отмена закрывает окно заказа")
    def test_cancel_closes_order_window(self, taxi_page, order_page):
        taxi_page.select_tariff("Рабочий")
        taxi_page.enable_laptop_table()
        taxi_page.submit_order()
        order_page.cancel_order()
        assert not order_page.search_window_is_visible()
