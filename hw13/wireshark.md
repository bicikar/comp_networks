## Wireshark

1. Сообщения отправляются поверх протокола UDP.

![](imgs/lab13_0.jpg)

2. Адрес 30:9c:23:29:03:b4

![](imgs/lab13_1.jpg)

3. Transaction ID: 0x24e20da5. Позволяет клиенту распознать, какому DCHP запросу какой
   соответствует ответ.
   
![](imgs/lab13_2.jpg)

4. До присвоения IP исходящий хост имеет IP-адрес, равный 0.0.0.0,
принимающий хост имеет IP, равный 255.255.255.255.
   
![](imgs/lab13_3.jpg)

5. Source Address: 192.168.88.1

6. DHCP-сервер назначает ip адрес на определенный срок, после чего адрес освобождается, 
если срок не был продлен. В моем случае: 10 минут
   
![](imgs/lab13_4.jpg)