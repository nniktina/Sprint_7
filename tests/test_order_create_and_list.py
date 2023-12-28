from src.api_client import ApiClient
from src.data import Pathes
import pytest
import allure

def data_for_creating_order(color):
    order_data = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": color
    }
    return order_data


class TestOrders:

    @allure.title('Проверка опциональности указания цвета самоката')
    @allure.description(
        'Проверка различных опций указания цвета самоката при создании заказа, а также передача пустого поля')
    @pytest.mark.parametrize("color", [("BLACK", "GREY"),
                                       ("BLACK"),
                                       ("GREY"),
                                       ()])
    def test_optional_colour_in_order_success(self, color):
        api = ApiClient()
        response = api.post(Pathes.new_order_path, data_for_creating_order(list(color)))
        assert response.status_code == 201
        assert 'track' in response.json()

    @allure.title('Проверка наличия спсика заказов в ответе ручки просмотра заказов')
    @allure.description(
        'Создаем заказ и проверяем что ручка просмотра всех заказов возвращает данные')
    def test_response_has_list_of_orders(self, color="BLACK"):
        api = ApiClient()
        api.post(Pathes.new_order_path, data_for_creating_order(list(color)))
        response = api.get(Pathes.orders_with_limit_3)
        assert response.json()["orders"] is not None


