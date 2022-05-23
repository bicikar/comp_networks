### Задание 1.

1. Мой адрес: 192.168.88.211

2. В поле протокола указано ICMP (1)

3. В IP заголовке - 20 байт, на полезную нагрузку приходится оставшиеся 36 байт.

![](imgs/lab10_0.jpg)

4.  * Изменяемые поля: `TTL`, `identification`, `checksum`
    *  Не изменяемые поля: `IP адреса`, `размер пакета`, `флаги`, 
       `differentiated services field`, `версия протокола`
       
    * Поле `identification` при каждом следующем запросе увеличивается.
    
![](imgs/lab10_1.jpg)

![](imgs/lab10_2.jpg)

![](imgs/lab10_3.jpg)

5. Поле `identification` занимает 2 байта и используется для распознавания пакета.
Поле `TTL` содержит время жизни для него. Например, `TTL = 15` и `identification = 0x62c9`
   
![](imgs/lab10_4.jpg)
![](imgs/lab10_5.jpg)

6. В такой ситуации поле `TTL` остается неизменным, поле `identification` меняется.

![](imgs/lab10_6.jpg)
![](imgs/lab10_7.jpg)

7. `TTL = 60` и `identification = 0xc9bb`

![](imgs/lab10_8.jpg)

8. * Да, сообщение было фрагментировано на 3 ip-датаграммы
![](imgs/lab10_9.jpg)

   * Меняются поля: `Checksum`, `Fragment offset`. Теоретически может меняться и `Total length`.
    
![](imgs/lab10_10.jpg)

![](imgs/lab10_11.jpg)

