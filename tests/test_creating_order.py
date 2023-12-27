from src.api_client import ApiClient
from src.data import new_order_path, orders_with_limit_3
import pytest


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

    @pytest.mark.parametrize("color", [("BLACK", "GREY"),
                                       ("BLACK"),
                                       ("GREY"),
                                       ()])
    def test_optional_colour_in_order_success(self, color):
        api = ApiClient()
        response = api.post(new_order_path, data_for_creating_order(list(color)))
        assert response.status_code == 201
        assert 'track' in response.json()

    def test_response_has_list_of_orders(self, color="BLACK"):
        api = ApiClient()
        api.post(new_order_path, data_for_creating_order(list(color)))
        response = api.get(orders_with_limit_3)
        assert response.json()["orders"] is not None


