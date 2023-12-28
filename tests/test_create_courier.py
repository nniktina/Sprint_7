from src.api_client import ApiClient
from src.data import Pathes, ResponseTexts
import pytest
import allure


class TestCreateCourier:

    @allure.title('Проверка создания нового курьера')
    @allure.description(
        'Проверка возможности создания нового курьера, проверка кода и текста успешного ответа')
    def test_create_new_courier_success_code_and_status(self, new_courier_data):
        api = ApiClient()
        response = api.post(Pathes.create_courier_path, new_courier_data)
        assert response.status_code == 201
        assert response.text == ResponseTexts.success_creating_message

    @allure.title('Проверка невозможности создания одинаковых курьеров')
    @allure.description(
        'Проверка невозможности создания курьеров с одинаковыми данными, а также проверка кода и текста ошибки')
    def test_creating_same_courier_is_prohibited(self, new_courier_data):
        new_courier = new_courier_data
        api = ApiClient()
        api.post(Pathes.create_courier_path, new_courier)
        response = api.post(Pathes.create_courier_path, new_courier)
        assert response.status_code == 409
        assert response.text == ResponseTexts.same_login_error

    @allure.title('Проверка обязательности заполнения полей')
    @allure.description(
        'Проверяем что поля логина и пароля обязательны для заоплнения, а также проверка кода и текста ошибки')
    @pytest.mark.parametrize('wrong_data', ['courier_data_without_login', 'courier_data_without_password'])
    def test_mandatory_fields_are_missing(self, wrong_data):
        api = ApiClient()
        response = api.post(Pathes.create_courier_path, wrong_data)
        assert response.status_code == 400
        assert response.text == ResponseTexts.not_enough_data_error
