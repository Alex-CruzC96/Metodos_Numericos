import tkinter as tk
from tkinter import messagebox

def calcular():
    #metodo de gauss seidel métodos numéricos
    try:
        a1=float(text_box1.get())
        b1=float(text_box2.get())
        a2=float(text_box3.get())
        b2=float(text_box4.get())
        c1=float(text_box5.get())
        c2=float(text_box6.get())
        matriz=[[],[]]
        matriz[0].append(a1)
        matriz[0].append(b1)
        matriz[0].append(c1)
        matriz[1].append(a2)
        matriz[1].append(b2)
        matriz[1].append(c2)
   
        vector=[]
        vector2=[]
        for i in range(2):        
            vector.append(0)
            vector2.append(0)

        for i in range(5):
            vector2[0]=(matriz[0][2]+((matriz[0][1]*-1)*vector[1]))/matriz[0][0]
            vector2[1]=(matriz[1][2]+((matriz[1][0]*-1)*vector2[0]))/matriz[1][1]
            vector[0]=vector2[0]
            vector[1]=vector2[1]
            cadena=""            
            cadena += ("El costo de las gasolinas cuando un barril cuesta\n" + str(c1) + " y "+str(c2) + " dólares son:\n"+"Costo de la gasolina prempium {:.6f}".format(abs(vector[0]))+"\n"+" Costo de la gasoliina regular:  {:.6f}".format(abs(vector[1])))
                        
        messagebox.showinfo("Resultado",cadena)
    except ValueError:
        messagebox.showerror("Error","Ingrese un valor numérico adecuado")

root = tk.Tk()

lbl_titulo = tk.Label(root,text="Cálculo de precio de la gasolina premium y regular")
lbl_premium1 = tk.Label(root,text="Litros de gasolina premium 1er periodo")
lbl_premium2 = tk.Label(root,text="Litros de gasolina premium 2do periodo")
lbl_regular1 = tk.Label(root,text="Litros de gasolina regular 1er periodo")
lbl_regular2 = tk.Label(root,text="Litros de gasolina regular 2do periodo")
lbl_petroleo1 = tk.Label(root,text="Precio de1 barril de petróleo 1er periodo")
lbl_petroleo2 = tk.Label(root,text="Precio del barril de pretróleo 2do periodo")
text_box1 = tk.Entry(root)
text_box2 = tk.Entry(root)
text_box3 = tk.Entry(root)
text_box4 = tk.Entry(root)
text_box5 = tk.Entry(root)
text_box6 = tk.Entry(root)

btn_calcular = tk.Button(root,text="Calcular precio de gasolinas por costo de 1 barrril ",command=calcular)
lbl_premium1.place(x=75,y=55)
lbl_premium2.place(x=75,y = 125)
lbl_regular1.place(x=300,y=55)
lbl_regular2.place(x=300,y=125)
lbl_petroleo1.place(x= 515,y=55)
lbl_petroleo2.place(x=515,y=125)
text_box1.place(x=100, y=80)
text_box2.place(x=350, y=80)
text_box3.place(x=100, y=150)
text_box4.place(x=350, y=150)
text_box5.place(x=550, y=80)
text_box6.place(x=550, y=150)
btn_calcular.place(x=280, y = 200)


root.geometry("750x300")

root.mainloop()