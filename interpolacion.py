import sympy as sp

def newton_interpolation(x_data, y_data):
    n = len(y_data)
    a=[]
    x = sp.symbols('x')
    f = sp.sympify(y_data)
    for i in range(n):
        for j in range(n-1, i, -1):
            f[j] = (f[j] - f[j-1]) / (x_data[j] - x_data[j-i-1])
        a.append(f[i])
    for i in a:
        print(f"Los valores de a son: {i}")
    p = a[n-1]
    for k in range(n-2, -1, -1):
        p = a[k] + (x - x_data[k])*p
    return sp.expand(p)

x_data=[0.6,0.7,0.8,1]
y_data=[-0.176,0.013,0.223,0.658]

p = newton_interpolation(x_data, y_data)
print(f"El polinomio interpolante es {p}")

