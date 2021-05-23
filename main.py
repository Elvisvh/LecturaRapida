from sys import api_version
import tkinter as tk
import time as tiempo
import asyncio
import itertools
from typing import Iterable, Text
from lib import secs
from lib import var

from asyncio.tasks import sleep
from lib import main as func


y = 0
verdadero = False


ventana = tk.Tk()
ventana.geometry("600x580+400+100")
ventana.maxsize(height=580, width=600)
ventana.minsize(height=580, width=600)
lableTexto = tk.StringVar()
lableTexto.set("hola")




def MinVen(ven, secds):
    secs.segundos = secds
    print("Los segundos son: ", secs.segundos)
    ven.state(newstate="withdraw")

def Funtion():
    otra_ventana = tk.Toplevel(ventana)
    otra_ventana.title("Palabra por minuto")
    otra_ventana.geometry("250x300+400+100")
    oBtn1 = tk.Button(otra_ventana, text="150 palabras por minuto", command= lambda: MinVen(otra_ventana, secs.palabras150))
    oBtn1.pack()
    oBtn2 = tk.Button(otra_ventana, text="200 palabras por minuto", command= lambda: MinVen(otra_ventana, secs.palabras200))
    oBtn2.pack()
    oBtn3 = tk.Button(otra_ventana, text="250 palabras por minuto", command= lambda: MinVen(otra_ventana, secs.palabras250))
    oBtn3.pack()
    oBtn4 = tk.Button(otra_ventana, text="300 palabras por minuto", command= lambda: MinVen(otra_ventana, secs.palabras300))
    oBtn4.pack()
    oBtn5 = tk.Button(otra_ventana, text="350 palabras por minuto", command= lambda: MinVen(otra_ventana, secs.palabras350))
    oBtn5.pack()
    oBtn6 = tk.Button(otra_ventana, text="400 palabras por minuto", command= lambda: MinVen(otra_ventana, secs.palabras400))
    oBtn6.pack()
    oBtn7 = tk.Button(otra_ventana, text="450 palabras por minuto", command= lambda: MinVen(otra_ventana, secs.palabras450))
    oBtn7.pack()
    oBtn8 = tk.Button(otra_ventana, text="500 palabras por minuto", command= lambda: MinVen(otra_ventana, secs.palabras500))
    oBtn8.pack()
    oBtn9 = tk.Button(otra_ventana, text="600 palabras por minuto", command= lambda: MinVen(otra_ventana, secs.palabras600))
    oBtn9.pack()

def getTexto(x):
    func.arregloPalabras = []
    obj = ""
    texto = x.get("1.0","end")
    func.palRec(texto)
    #print(func.arregloPalabras)
    
    

def iterables():
    for x in func.arregloPalabras: 
        print(x)
        lableTexto.set(f"{x}")
        if var.stop == True:
            var.stop = False
            break
        tiempo.sleep(secs.segundos)
        ventana.update()
    print("Has leido un total de:", len(func.arregloPalabras) - 1, "palabras")
      
        
def StopBucle():
    if var.stop == True:
        var.stop = False
    else:
        var.stop = True


def BorrarCajaDeTexto():
    cajadetexto.delete("1.0","end")



etiqueta = tk.Label(ventana, textvariable = lableTexto, font="Georgia 30", height="3")
cajadetexto = tk.Text(ventana, width="70", height="10")
btn1 = tk.Button(ventana, text="get", command=lambda:getTexto(cajadetexto))
btn2 = tk.Button(ventana, text="Tiempo", command=Funtion)
btn3 = tk.Button(ventana, text="empezar", command=iterables)
btn4 = tk.Button(ventana, text="stop", command=StopBucle)
btn5 = tk.Button(ventana, text="Borrar", command=BorrarCajaDeTexto)


etiqueta.pack()
cajadetexto.pack()
btn1.pack()
btn3.pack()
btn2.pack()
btn4.pack()
btn5.pack()

ventana.mainloop()