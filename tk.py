
from select import select
from tkinter import Button, Entry, Label, Tk, Radiobutton, IntVar
import tkinter
import tkinter.messagebox



def comprasT():
    compra = float(cajatxt1.get())* float(cajatxt2.get())

    if rbd2.select():
        descuento1 = compra * 0.20
        total1 = compra - descuento1
        tkinter.messagebox.showinfo(title=f"FACTURA", message = f"Total: ${compra}  \n Descuento 20% : ${descuento1} \n Total a pagar: ${total1}")



    elif  rbd1.select() and compra <20:
        descuento2 = 0
        tkinter.messagebox.showinfo(title=f"FACTURA", message = f"Total: ${compra}  \n Descuento : ${descuento2} \n Total a pagar: ${compra}")



    elif rbd1.select() and compra > 20:
        descuento3=compra*0.10
        total2=compra-descuento3
        tkinter.messagebox.showinfo(title=f"FACTURA", message = f"Total: ${compra}  \n Descuento 10% :${descuento3} \n Total a pagar: ${total2}")



interfaz=Tk()
interfaz.geometry("400x300")
radio=IntVar()


#Aqui van todos los textbox, label, buttons que ocupamos y sus caracteristicas, sus textos y sus medidas.
txt1=Label(interfaz,text="Bienvenido a supermercado el pollo feliz",bg="#BDC3C7")
interfaz.configure(bg='#AED6F1')
cajatxt1=Entry(interfaz)
cajatxt2=Entry(interfaz)
txt1.place(x=100,y=20)
txt2=Label(interfaz,text="Escriba el producto",bg='#AED6F1')
txt3=Label(interfaz,text="Escriba la cantidad",bg='#AED6F1')
txt2.place(x=100, y=80)
txt3.place(x=100, y=50)
cajatxt1.place(x=180, y=50)
cajatxt2.place(x=180, y=80)
txt4=Label(interfaz,text="Metodo de pago",bg='#AED6F1')
txt4.place(x=140,y=100,width=100,height=50)
rbd1=Radiobutton(interfaz, text="Efectivo",value=1,variable=radio,bg="#FDFEFE")
rbd2=Radiobutton(interfaz, text="Tarjeta",value=2,variable=radio,bg="#FDFEFE")
rbd1.place(x=150,y=140)
rbd2.place(x=150,y=180)

btn=Button(interfaz, text="Comprar",command=comprasT, bg="#E74C3C")
btn.place(x=140,y=220,width=100,height=50)


interfaz.mainloop()
#Aqui llamamos los objetos que antes especificamos para que aparezcan en la pantalla.
txt1.pack()
txt2.pack()
btn.pack()
rbd1.pack()
rbd2.pack()
cajatxt1.pack()
cajatxt2.pack()
