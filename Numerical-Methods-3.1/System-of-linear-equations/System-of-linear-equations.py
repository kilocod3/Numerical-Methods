def gauss_metod(A, b):
    n = len(A)
    
    for i in range(n):
        for j in range(i+1, n):
            ratio = A[j][i]/A[i][i]
            
            for k in range(n):
                A[j][k] = A[j][k] - ratio * A[i][k]
                
            b[j] = b[j] - ratio * b[i]
    
    x = [0 for i in range(n)]
    
    x[n-1] = b[n-1]/A[n-1][n-1]
 
    for i in range(n-2,-1,-1):
        summ = b[i]
        
        for j in range(i+1, n):
            summ = summ - A[i][j]*x[j]
            
        x[i] = summ/A[i][i]
    return x
    
def simple_iteration(A, b):
    n = len(A)
    x = [0 for i in range(n)]
    x_new = [0 for i in range(n)]
    epsilon = 0.0001
    max_diff = epsilon + 1
    iter_col = 0
    
    while max_diff > epsilon:
        max_diff = 0
        
        for i in range(n):
            summ = b[i]
            
            for j in range(n):
                if j != i:
                    summ = summ - A[i][j]*x[j]
            
            x_new[i] = summ / A[i][i]
            
            diff = abs((x_new[i] - x[i]) / x_new[i])
            
            if diff > max_diff:
                max_diff = diff
        
        x = x_new.copy()
        iter_col += 1
    
    print("Количество итераций:", iter_col)
    return x
    
def metod_seidel(A, b):
    n = len(A)
    x = [0 for i in range(n)]
    x_new = [0 for i in range(n)]
    epsilon = 0.0001
    max_diff = epsilon + 1
    iter_col = 0
    
    while max_diff > epsilon:
        max_diff = 0
        
        for i in range(n):
            summ = b[i]
            
            for j in range(n):
                if j != i:
                    summ = summ - A[i][j]*x_new[j]
            
            x_new[i] = summ / A[i][i]
            
            diff = abs((x_new[i] - x[i]) / x_new[i])
            
            if diff > max_diff:
                max_diff = diff
        
        x = x_new.copy()
        iter_col += 1
    
    print("Количество итераций:", iter_col)
    return x
    
def relax_metod(A, b, w):
    n = len(A)
    x = [0 for i in range(n)]
    x_new = [0 for i in range(n)]
    epsilon = 0.0001
    max_diff = epsilon + 1
    iter_col = 0
    
    while max_diff > epsilon:
        max_diff = 0
        
        for i in range(n):
            summ = b[i]
            
            for j in range(n):
                if j != i:
                    summ = summ - A[i][j]*x_new[j]
            
            x_new[i] = ((1 - w) * x[i]) + (w * summ / A[i][i])
            
            diff = abs((x_new[i] - x[i]) / x_new[i])
            
            if diff > max_diff:
                max_diff = diff
        
        x = x_new.copy()
        iter_col += 1
    
    print("Количество итераций:", iter_col)
    return x
    
A = [[6, 0.5, 0.4], [0.5, 5, 0.3], [0.4, 0.3, 4]]
b = [40.1, 29.2, 19.9]
 
# Метод Гаусса
gauss_solution = gauss_metod(A, b)
print("Метод Гаусса:", gauss_solution)
 
# Метод простой итерации
si_solution = simple_iteration(A, b)
print("Метод простой итерации:", si_solution)
 
# Метод Зейделя
gs_solution = metod_seidel(A, b)
print("Метод Зейделя:", gs_solution)
 
# Метод верхней релаксации с w=1.3
sor_solution = relax_metod(A, b, 1.3)
print("Метод верхней релаксации (w=1.3):", sor_solution)
