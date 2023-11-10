import sympy as sp
from sympy.plotting import plot
import matplotlib.pyplot as plt
import numpy as np

X=sp.Symbol("x")
while(True):
    try:
        func=input("Ingrese la función en términos de X: ")
        function=sp.sympify(func)
        derivada=sp.diff(function,X)
        derivada2=sp.diff(derivada,X)
        break
    except ValueError:
        pass

f=sp.lambdify(X,function)
f2=sp.lambdify(X,derivada2)
a=float(input("Ingrese el límite inferior: "))
b=float(input("Ingrese el límite superior: "))
media=(b-a)/2
eval1=f(a)
eval2=f(b)
error=(-1*(1/12))*(f2((b-a)))*(b-a)**3
resultado=(media*(f(a)+f(b)))+error
print(f"El resultado es: {resultado}")

x_val=np.linspace(a,b,400)
y_val=f(x_val)

plt.figure(figsize=(8,6))
plt.plot(x_val,y_val,label=f"Funcion = {function}")
plt.scatter([a,b],[f(a),f(b)],color='red')
plt.fill_between(x_val,y_val,color='lightblue',alpha=0.8,label=f"Área encontrada = {resultado}")
plt.fill_between([a, b], [f(a), f(b)], color='orange', alpha=0.3, label='Trapecio')
plt.title('Grafica')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.legend()
plt.show()
