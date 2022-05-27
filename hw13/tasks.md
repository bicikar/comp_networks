## Теория
### Задача 1
1. Найдем производную по $p$ и приравняем к нулю:
$$
\left( Np(1-p)^{N-1} \right)' = N \cdot (1-p)^{N-1} - Np\cdot(N-1)(1-p)^{N-2} = 
N\cdot(1-p)^{N-2} \cdot (1-Np) = 0
$$

Очевидно экстремум - либо 1, либо $\frac{1}{N}$. При четных и нечетных $N$ точка 
$\frac{1}{N}$ является точкой максимума, при $p = \frac{1}{N}$ получаем $\left(
1-\frac{1}{N}\right)^{N-1}$

2. В пределе просто получаем:
$$
\lim\limits_{N\rightarrow\infty} N\cdot\frac{1}{N}\cdot\left( 1-\frac{1}{N} \right)^{N-1} =
\lim\limits_{N\rightarrow\infty} \left( 1-\frac{1}{N} \right)^{N} \cdot \frac{1}{1-\frac{1}{N}} = \frac{1}{e}
$$
   

### Задача 3

Цикл опроса длится $t = N\left( \frac{Q}{R} + d_{\text{опрос}} \right)$. Максимальная пропускная способность
широковещательного канала равна
$$
\frac{NQ}{t} = \frac{Q}{\frac{Q}{R} + d_{\text{опрос}}} = \frac{QR}{Q + R\cdot d_{\text{опрос}}}
$$