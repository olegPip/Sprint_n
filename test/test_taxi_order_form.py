import allure
import pytest
from locators.taxi_locators import TaxiLocators
from data.test_data import TAXI_TARIFFS
import time

@allure.feature("Заказ тарифа Такси")
class TestTaxiOrderForm:
    @allure.title("Форма заказа содержит все шесть тарифов")
    def test_all_taxi_tariffs_are_displayed(self, taxi_page):
        assert set(taxi_page.tariff_names()) == set(TAXI_TARIFFS)

    @allure.title("Подсказка тарифа «{tariff}» содержит описание из требований")
    @pytest.mark.parametrize("tariff, expected_description", [
        ("Рабочий", "Для деловых особ, которых отвлекают"),
        pytest.param(
            "Сонный",
            "Для тех, кто не выспался",
            marks=pytest.mark.xfail(reason="Баг на стенде: текст описания перепутан с тарифом 'Разговорчивый'")
        ),
        ("Отпускной", "Если пришла пора отдохнуть"),
        pytest.param(
            "Разговорчивый",
            "Если мысли не выходят из головы",
            marks=pytest.mark.xfail(reason="Баг на стенде: текст описания перепутан с тарифом 'Сонный'")
        ),
        ("Утешительный", "Если хочется свернуться калачиком"),
        ("Глянцевый", "Если нужно блистать"),
    ])
    def test_tariff_tooltip_description(self, taxi_page, tariff, expected_description):
        tooltip = taxi_page.hover_tariff_info(tariff)
        assert expected_description in tooltip

    @allure.title("В форме заказа отображаются поля заказа")
    def test_order_form_fields_are_displayed(self, taxi_page):
        time.sleep(1)

        assert taxi_page.is_phone_field_visible(), "Поле 'Телефон' не отображается на форме"
        assert taxi_page.is_payment_method_visible(), "Поле 'Способ оплаты' не отображается на форме"
        assert taxi_page.is_comment_field_visible(), "Поле 'Комментарий водителю' не отображается"
        assert taxi_page.is_requirements_block_visible(), "Блок 'Требования к заказу' не отображается"

