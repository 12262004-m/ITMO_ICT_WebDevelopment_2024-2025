### Работа приложения:

1. Сервер прослушивает сокет _localhost:14902_
2. Сервер считывает первый байт - тип операции
    * В случае, если первый байт расшифровывается не в ожидаемый тип операции, код выводит ошибку в консоль и закрывает соединение
3. Сервер читает следующие байты в размере и порциями, зависящими от первого байта.
4. Сервер выполняет математическую операцию и возвращает ответ
5. Сервер закрывает соединение
    * Также при любой ошибке во время выполнения операций сервер закрывает соединение

Сервер может заблокироваться, если клиент установил соединение и отправляет данные в размерах меньше ожидаемых