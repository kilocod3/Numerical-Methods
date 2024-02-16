g, n, m = 1, 10, 14
 
def U(Xi, y0):
    return (m * Xi - y0) / Xi #Дифференциальное уравнение
def Ux(Xi):
    return (m / 2) * Xi + (g / Xi) #Точное решение
 
zmax = 0
h = 1 / n
y0 = (m / 2) + g #Начальное условие
for i in range(n):
    Xi = 1 + i * h
    yn1 = y0 + h * U(Xi, y0)
    y0 = yn1
    zi = abs(yn1 - Ux(Xi))
    if zi > zmax:
        zmax = zi
        
print('Метод Эйлера: {:.1f}'.format(yn1))
print('Точное решение: {:.1f}'.format(Ux(Xi)))
print('Погрешность: {:.1f}'.format(zi))
print(f'Норма: {zmax:.1f}')
