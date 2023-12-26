from src.api_client import ApiClient
from src.data import create_courier_path
import src.data
import pytest


class TestCreateCourier:

    def test_create_new_courier_success_code_and_status(self, new_courier_data):
        api = ApiClient()
        response = api.post(create_courier_path, new_courier_data)
        assert response.status_code == 201
        assert response.text == src.data.success_creating_message

    def test_creating_same_courier_is_prohibited(self, new_courier_data):
        new_courier = new_courier_data
        api = ApiClient()
        api.post(create_courier_path, new_courier)
        response = api.post(create_courier_path, new_courier)
        assert response.status_code == 409
        assert response.text == src.data.same_login_error

    @pytest.mark.parametrize('wrong_data', ['courier_data_without_login', 'courier_data_without_password'])
    def test_mandatory_fields_are_missing(self, wrong_data):
        api = ApiClient()
        response = api.post(create_courier_path, wrong_data)
        assert response.status_code == 400
        assert response.text == src.data.not_enough_data_error
