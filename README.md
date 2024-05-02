# Sprint_7

*Проект автоматизации тестирования api сайта заказа самокатов https://qa-scooter.praktikum-services.ru/*


1. Основа для написания автотестов — фреймворк pytest, selenium, модуль hhtp
2. Для отчетов используется Allure
3. Автотесты написаны в соответствии паттерна POM
4. Установить зависимости — `pip install -r requirements.txt`
5. Команда для запуска — `pytest -v`
6. Команда для запуска с записью отчета в allure_results: `pytest --alluredir=allure_results`
7. Генерация отчета в html страницу (находясь в дирректории allure_results): _`allure serve allure_results`_ 

### Директория проекта:

* `allure_results` - сожержит отчеты alure
 * `tests` - дирректория тестов
 * * `test_mcreate_courier.py` - тесты создания курьера
 * * `test_create_order.py` - тесты создания заказа\
 * * `test_get_list_orders.py` - тест получения списка заказов
 * * `test_login_courier.py` - тесты авторизации курьера
 * `conftest.py` -  фикстуры
 * `date.py` - данные для параметризации
 * `README.md` - описание проекта
 * `requirements` - файл с внешними зависимостями
 *  `helpers` - файл с вспомогательными функциями
 * `pytest.ini` - файл конфигурации pytest 