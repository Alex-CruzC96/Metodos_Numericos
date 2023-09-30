#metodo de gauss seidel métodos numéricos

matrizA=[]
vectorX=[]
vectorX2=[]
vectorB=[]
n=int(input("Cuantas ecuaciones desea agregar?: "))

for i in range(n):
    ecuacion=[]
    for j in range(n):
        ecuacion.append(int(input(f"Ingrese los coeficientes de la ecuacion {i+1}: ")))
    matrizA.append(ecuacion)

for i in range(n):
    num=int(input("Ingrese los terminos independiendes: "))
    vectorX.append(num)
    vectorX2.append(num)

for i in range(n):
    vectorB.append(int(input("Ingrese el valor del vector inicial: ")))

for l in range(7):  
    for i in range(n):
        vectorX[i]=(vectorB[i]-sum(matrizA[i][j] * vectorX[j] for j in range(n) if j != i))/matrizA[i][i]
        error=(abs(vectorX[i]-vectorX2[i])/vectorX[i])*100
        vectorX2[i]=vectorX[i]
        print(f"El valor de X{i+1} es: {vectorX[i]}\nCon un error de: "+"{:.{}}".format(error,4 if error <= 100 else 2)+"%\n")


