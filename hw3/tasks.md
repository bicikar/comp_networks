### Задание 1
После создания бита из аналогового сигнала хосту $A$ нужно накопить 56 байт (448 бит)
Т.к. скорость потока 126 мбит/c, то весь пакет накопится за $\frac{448}{128 * 1024}$.
Задержка распространения 0.005 c. Время передачи $\frac{448}{1024^2}$. Итого:
$$
T = \frac{448}{128 * 1024} + 0.005 + \frac{448}{1024^2} = 0.0088 \text{ c.} = 8.8 \text{ мс.}
$$

### Задание 2

$N = \text{ среднее число пакетов в буффере} + 1 = 11$.  Задержка $d = d_{\text{отправки}} + d_{\text{передачи}}$. 

За 1 секунду передается 100 пакетов, значит один пакет передается за 10мс, т.е.
средняя задержка передачи равна 10с. Средняя задержка ожидания тоже равна 10мс.
Тогда по формуле Литтла $a = \frac{N}{d} = \frac{11}{20} = 0.55 \text{пакетов/мс} = 550 \text{пакетов/c}$

### Задание 3

1 пакет окажется на центральном узле через $\frac{L}{R_S} + d_{\text{распр}}$ секунд,
соответственно уйдет целиком с центрального узла через
$t_1 = \frac{L}{R_S} + d_{\text{распр}} + \frac{L}{R_C}$.

2 пакет начнет передаваться через $\frac{L}{R_S}$ секунд с запуска системы (когда первый
пакет с хоста уйдет). Окажется на центральном узле через $t_2 = \frac{2L}{R_S} + d_{\text{распр}}$.


Т.о. необходимо сравнивать $t_1$ и $t_2$. Если $t_1 \leq t_2$, то задержки ожидания не будет
и первый пакет уйдет с центрального узла раньше, чем на узел попадет второй.
Иначе появится задержка для второго пакета $t_1 - t_2$

1. В пункте а. $R_S < R_C$, поэтому $t_1 - t_2 = \frac{L}{R_C} - \frac{L}{R_S} < 0$ 
и задержек не появится. Поэтому разница постоянная и равна $\frac{L}{R_S}$
   
2. В пункте б. $R_S > R_C$. Тогда $t_1 - t_2 = \frac{L}{R_C} - \frac{L}{R_S} > 0$, т.е. 
второй пакет будет находиться во входном буфере, пока не отправится первый пакет.
   Если добавить задержку $T$ к $t_2$, то минимум $T$ будет достигаться при $t_1 = t_2$ и
   равен исходной разности $t_1 - t_2 = \frac{L}{R_C} - \frac{L}{R_S}$
   
### Задание 4
Отправляемый объект в среднем появляется каждые $\frac{1000}{16} = 62.5 \text{мс}$, 
а отправляется за $\frac{850000 \text{бит}}{100 \text{Мбит/c}} = 8.5 \text{мс}$, так что нет задержки
ожидания. 

Задержка передачи $\Delta$ равна как раз $8.5 \text{мс}$. Тогда средняя задержка доступа равна
$\frac{8.5}{1-8.5\cdot \frac{16}{1000}} \approx 10 \text{мс}$, а средняя задержка ответа $\approx 3010 \text{мс}$.

При добавлении кэширующего сервера среднее общее время ответа равно $0.4 \cdot 3010 + 0.6 \cdot 10 = 2010 \text{мс}$