from src.api_client import ApiClient
from src.data import login_courier_path
import src.data
import pytest_check as check


class TestLoginCourier:

    def test_login_courier_success(self, data_for_login):
        api = ApiClient()
        response = api.post(login_courier_path, data_for_login)
        assert response.status_code == 200
        assert 'id' in response.json()

    def test_login_without_login_error(self, data_for_login_without_login):
        api = ApiClient()
        response = api.post(login_courier_path, data_for_login_without_login)
        assert response.status_code == 400
        assert response.text == src.data.missing_data_for_login_error

    def test_login_without_password_error(self, data_for_login_without_password):
        api = ApiClient()
        response = api.post(login_courier_path, data_for_login_without_password)
        assert response.status_code == 400
        assert response.text == src.data.missing_data_for_login_error

    def test_login_nonexistent_courier_error(self, login_data_nonexistent_courier):
        api = ApiClient()
        response = api.post(login_courier_path, login_data_nonexistent_courier)
        assert response.status_code == 404
        assert response.text == src.data.nonexistent_courier_login_error

    def test_login_with_incorrect_data(self, data_for_login):
        new_courier = data_for_login
        api = ApiClient()
        for key, value in new_courier.items():
            new_courier[key] = value + '1'
            response = api.post(login_courier_path, new_courier)
            assert response.status_code == 404
            assert response.text == src.data.nonexistent_courier_login_error

