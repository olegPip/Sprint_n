import allure
import pytest

from data.test_data import ORIGIN, DESTINATION, ROUTE_TYPES, TRANSPORT_TYPES


@allure.feature("Подготовка к заказу такси")
class TestRoutePreparation:
    @allure.title("Переключение между оптимальным и быстрым маршрутами меняет активную вкладку")
    def test_route_tabs_switch(self, routes_page):
        routes_page.build_route(ORIGIN, DESTINATION)
        routes_page.select_route_type("Оптимальный")
        assert "Оптимальный" in routes_page.active_route_name()
        routes_page.select_route_type("Быстрый")
        assert "Быстрый" in routes_page.active_route_name()

    @allure.title("В режиме Свой доступны типы передвижения")
    def test_custom_route_enables_transport_types(self, routes_page):
        routes_page.build_route(ORIGIN, DESTINATION)
        routes_page.select_route_type("Свой")
        assert routes_page.transport_options_are_visible()

    @allure.title("Для быстрого маршрута доступна кнопка вызова такси")
    def test_fast_route_has_enabled_taxi_button(self, routes_page):
        routes_page.build_route(ORIGIN, DESTINATION)
        routes_page.select_route_type("Быстрый")
        assert routes_page.taxi_button_is_enabled()

    @allure.title("Для Драйва доступна кнопка бронирования")
    def test_drive_transport_has_booking_button(self, routes_page):
        routes_page.build_route(ORIGIN, DESTINATION)
        routes_page.select_route_type("Свой")
        routes_page.select_transport("Драйв")
        assert routes_page.drive_button_is_enabled()
