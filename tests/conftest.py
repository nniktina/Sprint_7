import requests
import random
import string
import pytest
from faker import Faker


@pytest.fixture
def new_courier_data():
    fake = Faker(locale="ru_RU")
    user_data = {"login": fake.lexify('???????'),
                 "password": fake.lexify('???????'),
                 "firstName": fake.lexify('???????')
                 }
    return user_data


@pytest.fixture
def courier_data_without_login():
    fake = Faker(locale="ru_RU")
    user_data = {"password": fake.lexify('???????'),
                 "firstName": fake.lexify('???????')
                 }
    return user_data


@pytest.fixture
def courier_data_without_password():
    fake = Faker(locale="ru_RU")
    user_data = {"login": fake.lexify('???????'),
                 "firstName": fake.lexify('???????')
                 }
    return user_data

@pytest.fixture
def login_data_nonexistent_courier():
    fake = Faker(locale="ru_RU")
    user_data = {"login": fake.lexify('????????'),
                 "password": fake.lexify('???????')
                 }
    return user_data

@pytest.fixture
def register_new_courier_and_return_login_password():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    login_pass = []

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)

    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)

    return login_pass


@pytest.fixture
def data_for_login(register_new_courier_and_return_login_password):
    registered_courier = register_new_courier_and_return_login_password
    login_data = {"login": registered_courier[0],
                  "password": registered_courier[1]}
    return login_data


@pytest.fixture
def data_for_login_without_login(register_new_courier_and_return_login_password):
    registered_courier = register_new_courier_and_return_login_password
    login_data = {"login": "",
                  "password": registered_courier[1]}
    return login_data


@pytest.fixture
def data_for_login_without_password(register_new_courier_and_return_login_password):
    registered_courier = register_new_courier_and_return_login_password
    login_data = {"login": registered_courier[0],
                  "password": ""}
    return login_data
