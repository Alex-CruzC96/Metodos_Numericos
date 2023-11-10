import sympy as sp
from sympy.plotting import plot
import matplotlib.pyplot as plt
import numpy as np

X=sp.Symbol("x")
while(True):
    try:
        func=input("Ingrese la función en términos de X: ")
        function=sp.sympify(func)
        break
    except ValueError:
        pass
f=sp.lambdify(X,function)
x1=float(input("Ingrese el límite inferior: "))
xf=float(input("Ingrese el límite superior: "))
n=int(input("Ingrese el número de intervalos: "))
h=(xf-x1)/n
pares=0
impares=0
xi=x1
for i in range(1,n+1):
    print(f"x{i} = {xi}")
    if(i % 2 == 0):
        pares+=f(xi)
    elif(i!=1):
        impares+=f(xi)
    xi+=h

I=(h/3)*(f(x1)+(4*(pares))+(2*(impares))+f(xi))
print(f"Área encontrada: {I}")

x_val=np.linspace(x1,xf,400)
y_val=f(x_val)
plt.figure(figsize=(8,6))
plt.plot(x_val,y_val,label=f"Funcion = {function}")
plt.scatter([x1,xf],[f(x1),f(xf)],color='red')
plt.fill_between(x_val,y_val,color='lightblue',alpha=0.5,label=f"Área encontrada = {I}")
plt.title('Grafica')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.legend()
plt.show()
