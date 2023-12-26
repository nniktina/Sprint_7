BASE_URL = 'https://qa-scooter.praktikum-services.ru/'

create_courier_path = 'api/v1/courier'
login_courier_path = 'api/v1/courier/login'

success_creating_message = '{"ok":true}'

same_login_error = '{"code":409,"message":"Этот логин уже используется. Попробуйте другой."}'
not_enough_data_error = '{"code":400,"message":"Недостаточно данных для создания учетной записи"}'

missing_data_for_login_error = '{"code":400,"message":"Недостаточно данных для входа"}'
nonexistent_courier_login_error = '{"code":404,"message":"Учетная запись не найдена"}'
