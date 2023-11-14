import sympy as sp
from sympy.plotting import plot
import matplotlib.pyplot as plt
import numpy as np

def factorial(var):
    if var == 0:
        return 1
    else:
        return var * factorial(var-1)
X=sp.Symbol("x")
while(True):
    try:
        func=input("Ingrese la función en términos de X: ")
        function=sp.sympify(func)
        break
    except ValueError:
        pass
x0=float(input("Ingrese el valor de X0: "))
evaluaciones=[]
derivada=func
serie=0
i=0
while(True):
    if derivada == 0:
        break
    else:
        f=sp.lambdify(X,derivada)
        evaluaciones.append(f(x0))
        derivada=sp.diff(function,X)
        function=derivada
    serie+=(evaluaciones[i]/factorial(i))*(X-x0)**i
    i+=1
print(f"La serie resultante es: {serie}")
grafica=plot(serie,show=False)
grafica.tittle="Gráfica!"
grafica.xlabel="X"
grafica.ylabel="Y"
grafica.show()