### Задание А.

1. ip адресов достаточно много, например 49.7.37.133

![](pics/lab4_1.png)

2. Для Оксфордского университета:

![](pics/lab4_2.png)


3. Подойдет сайт `sina.com.cn` из пункта 1. Адреса моего учебного заведения:

![](pics/lab4_3.png)


### Задание Б.

1. Запрос отправлен по UDP.
2. Порт 53

![](pics/lab4_4.png)

3. Запрос был отправлен на адрес 192.168.88.1. Локальный адрес такой же.

![](pics/lab4_5.png)

4. Запрашивается запись типа А на ip адреса. Ответов нет.

![](pics/lab4_6.png)
   
5. В ответном сообщении содержатся ответы - ip адреса, их классы, размер данных и время которое ответ будет правильным.

![](pics/lab4_7.png)

6. Следующий TCP запрос с флагом SYN действительно отправляется на один из IP адресов, указанных в ответе (третий)

![](pics/lab4_8.png)

7. Выполняется еще один запрос DNS следом за первым. Но судя по всему, выполняется он не из-за картинок
 и запрашивается как будто бы то же самое.

![](pics/lab4_9.png)   

### Задание В.

1. В DNS запросе порт назначения и в DNS ответе порт источника один и тот же - 53
2. Запрос отправлены на 192.168.88.1. Это адрес локального DNS сервера.
3. В сообщении-запросе запрашивается тип АААА, ответов нет.

![](pics/lab4_10.png)

4. В ответе пришло много информации о сервере. Самих по себе "ответов", "answers", нет.

![](pics/lab4_11.png)

### Задание Г.

1. Запросы опять идут на локальный DNS сервер. 
2. Запрашивается запись типа NS. Ответов нет.

![](pics/lab4_12.png)

3. В ответе имена nameserver-ов, при этом их ip адреса не указаны.

![](pics/lab4_13.png)

### Задание Д.

1. Сначала происходит 2 запроса типа А и АААА, адрес совпадает с адресом ip сервера по умолчанию.
   Затем еще 2 запроса на адрес 195.70.196.210, это адрес спбгу.
2. В запросах типа A и AAAA, отправленных на адрес спбгу, ответов нет.
3. В ответе типа А есть 2 ответа, CNAME и A, в ответе типа АААА ответов нет, но есть Authoritative nameservers

![](pics/lab4_14.png)

![](pics/lab4_15.png)

### Задание Е.

1. WHOIS — сетевой протокол прикладного уровня, базирующийся на протоколе TCP. Основное применение — получение регистрационных данных о владельцах доменных имён, IP-адресов и автономных систем. 
2. Используем [www.nic.ru](www.nic.ru) и [whois.ru](whois.ru)

[yandex.ru](yandex.ru):

![](pics/lab4_16.png)

![](pics/lab4_17.png)

[spbu.ru](spbu.ru):

![](pics/lab4_18.png)

3. Запросы в nslookup:

![](pics/lab4_19.png)