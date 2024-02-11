def f(x, a):
    k=0
    return (-x**2)/(4*((2*k+1))*(2*k+2)) # Полином для функции f(x)
 
def F(x):
    k=0
    return (-k*(x**2))/(4*(2*k+1)*(2*k+2)) # Первообразная для функции f(x)
 
# Границы интегрирования
a = 0.1
b = 0.5
E = 1e-4  
 
# Значение точного интеграла J(f) по первообразной функции
J = F(b) - F(a)
 
# Функция для вычисления значения Jₙ(f) по методу прямоугольников
def rectangle_method(a, b, n):
    h = (b - a) / n
    J_n = h * sum(f(a + (i + 0.5)*h, a) 
    for i in range(n))
    return J_n
 
# Функция для вычисления значения Jₙ(f) по методу трапеций
def trapezoid_method(a, b, n):
    h = (b - a) / n
    J_n = h/2 * (f(a, a) + f(b, a) + 2*sum(f(a + i*h, a) 
    for i in range(1, n)))
    return J_n
 
# Функция для вычисления значения Jₙ(f) по методу Симпсона
def simpson_method(a, b, n):
    h = (b - a) / n
    J_n = h/3 * (f(a, a) + f(b, a) + 4*sum(f(a + i*h, a) 
    for i in range(1, n, 2)) + 2*sum(f(a + i*h, a) 
    for i in range(2, n, 2)))
    return J_n
 
# Вычисление значений интегралов с заданной точностью
ε = 0.001  # Заданная точность
 
n = 1
J_n = rectangle_method(a, b, n)
J_2n = rectangle_method(a, b, 2*n)
while abs((J_n - J_2n) / J_2n) >= ε:
    n *= 2
    J_n = J_2n
    J_2n = rectangle_method(a, b, 2*n)
R_2n = abs((J_n - J_2n) / J_2n)
print("Метод прямоугольников:")
print("J =", J_2n)
print("n =", n)
print("R2n =", R_2n)
 
n = 1
J_n = trapezoid_method(a, b, n)
J_2n = trapezoid_method(a, b, 2*n)
while abs((J_n - J_2n) / J_2n) >= ε:
    n *= 2
    J_n = J_2n
    J_2n = trapezoid_method(a, b, 2*n)
R_2n = abs((J_n - J_2n) / J_2n)
print("Метод трапеций:")
print("J =", J_2n)
print("n =", n)
print("R2n =", R_2n)
 
n = 1
J_n = simpson_method(a, b, n)
J_2n = simpson_method(a, b, 2*n)
while abs((J_n - J_2n) / J_2n) >= ε:
    n *= 2
    J_n = J_2n
    J_2n = simpson_method(a, b, 2*n)
R_2n = abs((J_n - J_2n) / J_2n)
print("Метод Симпсона:")
print("J =", J_2n)
print("n =", n)
print("R2n =", R_2n)
