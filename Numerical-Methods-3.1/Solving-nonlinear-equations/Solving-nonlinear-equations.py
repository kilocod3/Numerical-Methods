import math
 
def simple_iteration(x0, epsilon):
    x = x0
    count = 0
    xn = math.log(10*x0 - math.log(x0))
    while abs(( xn - x ) / xn) >= epsilon:
        x = xn
        xn = math.log(10*x - math.log(x))
        count += 1
    nevyazka = xn - math.log(10*xn - math.log(xn))
    pogeshnost = abs(( xn - x ) / xn)
    return xn, nevyazka, count, pogeshnost
x0 = 3.4
epsilon = 0.0001
 
xn, nevyazka, count, pogeshnost = simple_iteration(x0, epsilon)
print("Простая итерация: ", xn)
print("Невязка: ", nevyazka)
print("Количество итераций: ", count)
print("Погрешность: ", pogeshnost)
