import allure

from data.test_data import ORIGIN, DESTINATION
from locators.routes_locators import RoutesLocators


@allure.feature("Отрисовка маршрута")
class TestRouteRendering:
    @allure.title("На карте отображаются начало и конец построенного маршрута")
    def test_map_displays_two_route_points(self, routes_page):
        routes_page.build_route(ORIGIN, DESTINATION)
        assert routes_page.map_marker_count() >= 2
