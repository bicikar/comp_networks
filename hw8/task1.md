### Протокол Stop and Wait

Запускаем сервер `python3 src/server.py`

Запускаем клиент `python3 src/client.py`

Тесты `pytest`

Клиент отправляет серверу файл `alice.txt` из папки `texts` используя класс `StopAndWait`. 
Сервер сохраняет результат в `copy_alice.txt`. 
Можно менять:
  * RECEIVE_TIMEOUT - время, через которое сервер считает, что клиент закончил отправку сообщений.
  * SEND_TIMEOUT - время, через которое клиент считает, что пакет доставить невозможно и бросает `StopAndWaitTimeOutException`.
  * RESEND_TIMEOUT - время, через которое клиент считает, что пакет не дошел до получателя.

Клиент считает и отправляет серверу на проверку контрольные суммы.