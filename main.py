#Las importaciones de las librerias que ocuparemos
from cgitb import text
from os import environ
from source import email
from dotenv import load_dotenv
from tkinter import Tk,Label,Button,Entry
import tkinter.messagebox

load_dotenv()

#Funcion para poder enviar mi correo 
def enviar():
    tkinter.messagebox.showinfo(title="Informacion",message="Su mensaje ha sido enviado con exito!")
    texto=str(cajatxt3.get())
    texto1=str(cajausu.get())
    texto2=str(cajadestino.get())
    mensaje_html=texto
    environ["STMP_USER"]=texto1
    destinatario=texto2
    Correo = email.Email()
    Correo.mandar_email([destinatario],"Hola desde python", message_format=mensaje_html.format(texto1,texto), format="html")


ventana=Tk()
#Ventana que me permitira poder enviar un correo y mi programa en si
ventana.geometry("400x300")

txt1=Label(ventana,text="Gestion de correos",bg="#BDC3C7")
txt1.place(x=0,y=0)
txt2=Label(ventana,text="Enviar a:",bg='#AED6F1')
txt3=Label(ventana,text="Usuario:",bg='#AED6F1')
txt2.place(x=100, y=80)
txt3.place(x=100, y=50)
cajausu=Entry(ventana)
cajadestino=Entry(ventana)
cajausu.place(x=180, y=50,width=200)
cajadestino.place(x=180, y=80,width=200)
cajatxt3=Entry(ventana)
cajatxt3.place(x=100, y=120, width=200,height=100)
btn=Button(ventana, text="Comprar",command=enviar, bg="#E74C3C")
btn.place(x=140,y=230,width=100,height=50)






ventana.mainloop()



