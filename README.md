# Sprint_7
Проверка учебного сервиса https://qa-scooter.praktikum-services.ru/ 
Документация API - https://qa-scooter.praktikum-services.ru/docs/ 

test_create_courier.py
    покрытие требований:
        1) test_create_new_courier_success_code_and_status:
            * курьера можно создать 
            * запрос возвращает правильный код ответа;
            * успешный запрос возвращает {"ok":true};
        2) test_creating_same_courier_is_prohibited:
            * нельзя создать двух одинаковых курьеров;
            * если создать пользователя с логином, который уже есть, возвращается ошибка
        3) test_mandatory_fields_are_missing:
            * чтобы создать курьера, нужно передать в ручку все обязательные поля;
            * если одного из полей нет, запрос возвращает ошибку;


test_login_courier.py
    покрытие требований:
        1) test_login_courier_success:
            * курьер может авторизоваться;
            * успешный запрос возвращает id
        2) test_login_without_login_error, test_login_without_password_error:
            * для авторизации нужно передать все обязательные поля;
            * если какого-то поля нет, запрос возвращает ошибку;
        3) test_login_nonexistent_courier_error:
            * если авторизоваться под несуществующим пользователем, запрос возвращает ошибку;
        4) test_login_with_incorrect_login, test_login_with_incorrect_password:
            * система вернёт ошибку, если неправильно указать логин или пароль;

test_order_create_and_list.py
    data_for_creating_order - вспомогательная функция для создания заказа
    покрытие требований:
        1) test_optional_colour_in_order_success:
            * можно указать один из цветов — BLACK или GREY;
            * можно указать оба цвета;
            * можно совсем не указывать цвет;
            * тело ответа содержит track
        2) test_response_has_list_of_orders:
            * проверь, что в тело ответа возвращается список заказов
