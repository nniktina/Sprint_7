from src.api_client import ApiClient
from src.data import Pathes, ResponseTexts
import allure


class TestLoginCourier:

    @allure.title('Проверка успешного логина курьера')
    @allure.description(
        'Проверка получения корректного кода и текста в случае передачи корректных данных для логина')
    def test_login_courier_success(self, data_for_login):
        api = ApiClient()
        response = api.post(Pathes.login_courier_path, data_for_login)
        assert response.status_code == 200
        assert 'id' in response.json()

    @allure.title('Проверка логина без заполненного поля login')
    @allure.description(
        'Проверка получения ошибки в случае, когда не заполнено поле login в форме логина')
    def test_login_without_login_error(self, register_new_courier_and_return_login_password):
        api = ApiClient()
        registered_courier = register_new_courier_and_return_login_password
        login_data = {"login": "",
                      "password": registered_courier[1]}
        response = api.post(Pathes.login_courier_path, login_data)
        assert response.status_code == 400
        assert response.text == ResponseTexts.missing_data_for_login_error

    @allure.title('Проверка логина без заполненного поля password')
    @allure.description(
        'Проверка получения ошибки в случае, когда не заполнено поле password в форме логина')
    def test_login_without_password_error(self, register_new_courier_and_return_login_password):
        api = ApiClient()
        registered_courier = register_new_courier_and_return_login_password
        login_data = {"login": registered_courier[0],
                      "password": ""}
        response = api.post(Pathes.login_courier_path, login_data)
        assert response.status_code == 400
        assert response.text == ResponseTexts.missing_data_for_login_error

    @allure.title('Проверка логина под несуществующим пользователем')
    @allure.description(
        'Проверка получения ошибки если в форму логина передаем данные незарегистрированного курьера')
    def test_login_nonexistent_courier_error(self, login_data_nonexistent_courier):
        api = ApiClient()
        response = api.post(Pathes.login_courier_path, login_data_nonexistent_courier)
        assert response.status_code == 404
        assert response.text == ResponseTexts.nonexistent_courier_login_error

    @allure.title('Проверка логина с некорректным логином')
    @allure.description(
        'Проверка получения ошибки если в форму логина передаем измененный логин зарегистрированного курьера')
    def test_login_with_incorrect_login(self, data_for_login):
        new_courier = data_for_login
        api = ApiClient()
        new_courier["login"] += '1'
        response = api.post(Pathes.login_courier_path, new_courier)
        assert response.status_code == 404
        assert response.text == ResponseTexts.nonexistent_courier_login_error

    @allure.title('Проверка логина с некорректным паролем')
    @allure.description(
        'Проверка получения ошибки если в форму логина передаем измененный пароль зарегистрированного курьера')
    def test_login_with_incorrect_password(self, data_for_login):
        new_courier = data_for_login
        api = ApiClient()
        new_courier["password"] += '1'
        response = api.post(Pathes.login_courier_path, new_courier)
        assert response.status_code == 404
        assert response.text == ResponseTexts.nonexistent_courier_login_error
