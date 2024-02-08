def well(e, x):
    k = 0
    a = 1
    S = a
    while (abs(a / S) > e):
        q = (-x**2)/(4*((2*k+1))*(2*k+2))
        a *= q
        S += a
        k += 1
    return S, k
def wellp(e, x):
    k = 1
    a = (-0.1)/4
    S = a
    while (abs(a / S) > e):
        q = (-k*(x**2))/(4*(2*k+1)*(2*k+2))
        a *= q
        S += a
        k += 1
    return S
def poli(x, y, e):
    xi = []
    yi = []
    yip = []
    z = []
    h = 0.1
    print('Значения функции в интервалах:\n')
    for i in range(0,4):
        xi.append(round((x[i] + h / 2),2))
        yi.append(well(e,xi[i]))
        print('x =', xi[i],', y = ',yi[i][0],', шаг ', yi[i][1])
    print('\nЗначения функции в интервалах по полиному:\n')
    for i in range(0,4):
        yip.append(y[i][0]+((y[i+1][0]-y[i][0])/2))
        z.append(abs(yi[i][0] - yip[i]))
        print('x =', xi[i],', y = ',round(yip[i],6), ', погрешность:', z[i])
def left(x, ypr, e):
    h = 0.1
    q = [x-h, x]
    y = [well(e, q[0]), well(e, q[1])]
    yp = (y[1][0]-y[0][0])/h
    z = abs(yp - ypr)
    print('x =', round(x,2),', yp  = ',ypr,', yx  = ',yp,', погрешность:', z)
def right(x, ypr, e):
    h = 0.1
    q = [x, x+h]
    y = [well(e, q[0]), well(e, q[1])]
    yp = (y[1][0]-y[0][0])/h
    z = abs(yp - ypr)
    print('x =', round(x,2),', yp  = ',ypr,', yx  = ',yp,', погрешность:', z)
def central(x, ypr, e):
    h = 0.1
    q = [x-h, x+h]
    y = [well(e, q[0]), well(e, q[1])]
    yp = (y[1][0]-y[0][0])/(2*h)
    z = abs(yp - ypr)
    print('x =', round(x,2),', yp  = ',ypr,', yxo  = ',yp,', погрешность:', z)
print('Точность: ')
e = float(input())
x = []
y = []
ypr = []
print('\nДля заданной функции:\n')
for i in range(0, 5):
    x.append(round(((i + 1) * 0.1),1))
    y.append(well(e, x[i]))
for i in range(0, 5):
    ypr.append(wellp(e, x[i]))
for i in range(0,5):
    print('x =', x[i],', y = ',y[i][0],', шаг ', y[i][1])
print("\nДля полинома:\n")
poli(x, y, e)
print('\nЛевый, Правый и Центральный:\n')
for i in range(1,4):
    left(x[i], ypr[i], e)
print('\n')
for i in range(1,4):
    right(x[i], ypr[i], e)
print('\n')
for i in range(1,4):
    central(x[i], ypr[i], e)