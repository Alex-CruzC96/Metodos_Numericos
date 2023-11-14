import sympy as sp

X,Y=sp.symbols('x y')
while(True):
    try:
        func=input("Ingrese la diferencial en términos de X,Y: ")
        function=sp.sympify(func)
        break
    except ValueError:
        pass
f=sp.lambdify((X,Y),function)
x0=float(input("Ingrese el valor de x0: "))
y0=float(input("Ingrese el valor de y0: "))
xf=float(input("Ingrese el valor de xf: "))
n=int(input("Ingrese el número de intervalos: "))
h=(xf-x0)/n
print(h)
yi=0
print("||   X  ||    Y    ||   f(x,y)   ||")
for i in range(n+1):
    print("|| "+"{:.2f}".format(x0)+" ||  "+"{:.3f}".format(y0)+"  ||    "+"{:.3f}".format(f(x0,y0))+"   ||")
    yi=(y0+(h*f(x0,y0)))
    x0+=h
    y0=yi