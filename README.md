## Проект  с framework Flask

работает  docker_compose.yml
3 контейнера база , приложение и тесты

Запуск приложения  main.py   
Переменные в config.py  
Тесты лежат в  tests/test_api.py

Создать БД можно через docker-compose.yml. Все параметры для БД будут взяты из .env.
В проекте реализованы методы REST API (backend) для сайта объявлений с системой прав.  
В файле  requests_flask.http  лежат запросы для тестирования через VScode
Также реализованы тесты на базе  pytest

### Примеры запросов:
 - регистрация нового пользователя(POST): http://127.0.0.1:5001/users json={'email': 'ttt@mail.rr',password': 'ef;s_hp5'}

 - вход в систему (POST): http://127.0.0.1:5001/users?email=ttt@mail.rr&password=ef;s_hp5
 - выход из системы (POST): http://127.0.0.1:5001/logout
 - разместить объявления (POST): http://127.0.0.1:5001/advs json={"title": "Продам шкаф","description": "Почти новый"}
 - редактировать объявление (PATCH): http://127.0.0.1:5001/advs/int:adv_id json={"title": "Продам шкаф","description": "Почти новыйб Срочно!"}
 - получить объявление (GET): http://127.0.0.1:5001/advs/int:adv_id
 - удалить объявление (DELETE): http://127.0.0.1:5001/advs/int:adv_id

Создавать объявление может только авторизованный пользователь. Удалять/редактировать может только владелец объявления.