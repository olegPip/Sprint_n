import allure
import pytest

from data.test_data import ORIGIN, DESTINATION, SAME_ADDRESS


@allure.feature("Отрисовка блока с выбором маршрута")
class TestRouteSelection:
    @allure.title("После ввода разных адресов отображается блок выбора маршрута")
    def test_route_selection_panel_for_different_addresses(self, routes_page):
        routes_page.build_route(ORIGIN, DESTINATION)
        assert routes_page.route_panel_is_visible()

    @allure.title("Для одинаковых адресов отображается бесплатный маршрут с нулевым временем")
    @pytest.mark.xfail(reason="Известный дефект: некорректный результат для одинаковых адресов")
    def test_route_selection_panel_for_same_addresses(self, routes_page):
        routes_page.build_route(SAME_ADDRESS, SAME_ADDRESS)
        assert "Авто Бесплатно В пути 0 мин." in routes_page.text(
            routes_page.find_route_summary_locator()
        )
