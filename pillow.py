from PIL import Image,ImageTk, ImageFilter,Image,ImageEnhance
from tkinter import Tk,Label,Button, filedialog
import tkinter.messagebox

#Aqui estan todas las funciones que utilizare para los diferentes filtros
def cargar():
    archivo=filedialog.askopenfilename()
    imagen=Image.open(archivo)
    imagenres=imagen.resize((180,200),Image.Resampling.LANCZOS)
    render=ImageTk.PhotoImage(imagenres)
    label1.configure(image=render)
    label1.image=render

def blanco():
    tkinter.messagebox.showinfo(message="Elija la imagen que le desea aplicar el filtro")
    archivo1=filedialog.askopenfilename()
    imagen1=Image.open(archivo1)
    imagenblack= imagen1.convert('1') 
    imagenres1=imagenblack.resize((180,200),Image.Resampling.LANCZOS)
    render1=ImageTk.PhotoImage(imagenres1)
    label1.configure(image=render1)
    label1.image=render1

def desenfocar():
    tkinter.messagebox.showinfo(message="Elija la imagen que le desea aplicar el filtro")
    archivo2=filedialog.askopenfilename()
    imagen2=Image.open(archivo2)
    imagenblur=imagen2.filter(ImageFilter.BoxBlur(20))
    imagenres2=imagenblur.resize((180,200),Image.Resampling.LANCZOS)
    render=ImageTk.PhotoImage(imagenres2)
    label1.configure(image=render)
    label1.image=render
    
def resaltar():
    tkinter.messagebox.showinfo(message="Elija la imagen que le desea aplicar el filtro")
    archivo2=filedialog.askopenfilename()
    imagen2=Image.open(archivo2)
    imagenblur=ImageEnhance.Brightness(imagen2).enhance(2)
    imagenres2=imagenblur.resize((180,200),Image.Resampling.LANCZOS)
    render=ImageTk.PhotoImage(imagenres2)
    label1.configure(image=render)
    label1.image=render
    
def contorno():
    tkinter.messagebox.showinfo(message="Elija la imagen que le desea aplicar el filtro")
    archivo2=filedialog.askopenfilename()
    imagen2=Image.open(archivo2)
    imagenblur=imagen2.filter(ImageFilter.CONTOUR)
    imagenres2=imagenblur.resize((180,200),Image.Resampling.LANCZOS)
    render=ImageTk.PhotoImage(imagenres2)
    label1.configure(image=render)
    label1.image=render

    
#Las configuraciones de la ventana, tamaños, colores localizaciones de 'x' y 'y'
#CREACION DE MI VENTANA
ventana=Tk()
ventana.geometry("550x400")

txt1=Label(ventana,text="FILTROS DE IMAGENES",bg="#F00019")
txt1.place(x=0,y=0)
label1=Label(ventana ,image="")
boton=Button(ventana,text="Cargar Imagen", command=cargar,bg='#AED6F1')
boton.place(x=400,y=110,width=100,height=50)
label1.place(x=100, y=50)
boton1=Button(ventana,text="Blanco/Negro",command=blanco,bg='#AED6F1')
boton1.place(x=25,y=300,width=100,height=50)
boton2=Button(ventana,text="Desenfocar",command=desenfocar,bg='#AED6F1')
boton2.place(x=155,y=300,width=100,height=50)
boton3=Button(ventana,text="Contorno",command=contorno,bg='#AED6F1')
boton3.place(x=275,y=300,width=100,height=50)
boton4=Button(ventana,text="Resaltar",command=resaltar,bg='#AED6F1')
boton4.place(x=400,y=300,width=100,height=50)



ventana.mainloop()
#FIN DE MI VENTANA
#Aqui es donde llamo a mis labels y botones
txt1.pack()
label1.pack()
boton.pack()