g, n, m = 1, 10, 14
h = 1 / n
def f(X, y0, m): #Дифференциальное уравнение
    return (m * X - y0) / X
def exact_solution(X, m, g): # Точное решение
    return (m / 2) * X + (g / X)

def euler_method(h, m, g): # Метод Эйлера
    y0 = [(m / 2) + g]
    for i in range(1, n + 1):
        X = 1 + i * h
        y0.append(y0[i-1] + h * f(X, y0[i-1], m))
        X += h
    return y0

def runge_kutta_2(h, m, g): # Метод Рунге-Кутта 2-го порядка
    y0 = [(m / 2) + g]
    for i in range(1, n + 1):
        X = 1 + i * h
        k1 = h * f(X, y0[i-1], m)
        k2 = h * f(X + h, y0[i-1] + k1, m)
        y0.append(y0[i-1] + 0.5 * (k1 + k2))
        X += h
    return y0

def runge_kutta_4(h, m, g): # Метод Рунге-Кутта 4-го порядка
    y0 = [(m / 2) + g]
    for i in range(1, n + 1):
        X = 1 + i * h
        k1 = h * f(X, y0[i-1], m)
        k2 = h * f(X + 0.5*h, y0[i-1] + 0.5*k1, m)
        k3 = h * f(X + 0.5*h, y0[i-1] + 0.5*k2, m)
        k4 = h * f(X + h, y0[i-1] + k3, m)
        y0.append(y0[i-1] + (k1 + 2*k2 + 2*k3 + k4) / 6)
        X += h
    return y0

print('Метод Эйлера: ', euler_method(h, m, g)[-1])
print('Метод Рунге-Кутта 2: ', runge_kutta_2(h, m, g)[-1])
print('Метод Рунге-Кутта 4: ', runge_kutta_4(h, m, g)[-1])
print('Точное решение: ', exact_solution(h, m, g))


def calculate_error(approximate, exact): # Функция для вычисления погрешности
    return [abs(a - e) for a, e in zip(approximate, exact)]

def max_error(errors): # Функция для нахождения максимальной погрешности
    return max(errors)

h_values = [1 / n,  1 / (n * 10)] # Параметры и шаги 10 и 100

for h in h_values: #Ошибки
    x_values = [1 + i * h for i in range(n + 1)]
    
    U_euler = euler_method(h, m, g) # Получение значений при различных методах
    U_rk2 = runge_kutta_2(h, m, g)
    U_rk4 = runge_kutta_4(h, m, g)
    
    exact_values = [exact_solution(X, m, g) for X in x_values] # Точное решение
    
    errors_euler = calculate_error(U_euler, exact_values) # Вычисление ошибок
    errors_rk2 = calculate_error(U_rk2, exact_values)
    errors_rk4 = calculate_error(U_rk4, exact_values)
    
    max_error_euler = max_error(errors_euler) # Нахождение максимальных ошибок
    max_error_rk2 = max_error(errors_rk2)
    max_error_rk4 = max_error(errors_rk4)
    
    print("Шаг h =", h) # Вывод результатов
    print("Максимальная погрешность для метода Эйлера:", max_error_euler)
    print("Максимальная погрешность для метода Рунге-Кутта 2-го порядка:", max_error_rk2)
    print("Максимальная погрешность для метода Рунге-Кутта 4-го порядка:", max_error_rk4)