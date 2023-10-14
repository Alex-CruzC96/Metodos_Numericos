from sympy import symbols, expand

def lagrange(points):
    x = symbols('x')
    L = 0
    for i in range(len(points)):
        p = 1
        for j in range(len(points)):
            if i != j:
                p *= (x - points[j][0]) / (points[i][0] - points[j][0])
        L += p * points[i][1]
    return expand(L)

points=[(0.6,-0.176),(0.7,0.013),(0.8,0.223),(1,0.658)]
polynomial = lagrange(points)
print(polynomial)

