#metodo de gauss seidel métodos numéricos

matriz=[[],[]]

for i in range(3):
    matriz[0].append(int(input("Ingrese los coeficientes de la primer ecuación: ")))
print(str(matriz[0][0])+"x1"+"{}{}".format("+" if matriz[0][1] > 0 else "", matriz[0][1])+"x2"+"="+str(matriz[0][2]))

for i in range(3):
    matriz[1].append(int(input("Ingrese los coeficientes de la segunda ecuación: ")))
print(str(matriz[1][0])+"x1"+"{}{}".format("+" if matriz[1][1] > 0 else "", matriz[1][1])+"x2"+"="+str(matriz[1][2]))

print("x1 = "+"("+str(matriz[0][2])+"{}{}".format("-" if matriz[0][1] > 0 else "+",abs(matriz[0][1]))+"x2)"+"/"+str(matriz[0][0]))
print("x2 = "+"("+str(matriz[1][2])+"{}{}".format("-" if matriz[1][0] > 0 else "+",abs(matriz[1][0]))+"x1)"+"/"+str(matriz[1][1]))

vector=[]
vector2=[]
for i in range(2):
    num=int(input("Ingrese el valor del vector inicial: "))
    vector.append(num)
    vector2.append(num)

for i in range(10):
    errorX1=100
    errorX2=100
    vector2[0]=(matriz[0][2]+((matriz[0][1]*-1)*vector[1]))/matriz[0][0]
    vector2[1]=(matriz[1][2]+((matriz[1][0]*-1)*vector2[0]))/matriz[1][1]
    errorX1=(abs((vector2[0]-vector[0])/vector2[0]))*100
    errorX2=(abs((vector2[1]-vector[1])/vector2[1]))*100
    vector[0]=vector2[0]
    vector[1]=vector2[1]
    print(f"|  {i}  ||"+"  {:.6f}".format(vector[0])+"  ||"+" {:.{}f}".format(errorX1,1 if errorX1 >= 100 else 3)+"% ||"+"  {:.6f}".format(vector[1])+" ||"+"  {:.{}f}".format(errorX2,1 if errorX2 >= 100 else 3)+"%  ||")