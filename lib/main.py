import time as tiempo
from timeit import timeit
import string

#text = input("ingrese el texto aqui: ")
#texto = text + " "
i = 0
palabra = []
#variable que guarda todo
arregloPalabras = []
letras = ""
palabras = ""
word = ""
words = ""
y = 0
contador = 0
tiempoEvio = 0
secs = 0.2
dos = ""
unolocal = ""


def palRec(text):
    i = 0
    texto = ""
    texto2 = text + " "
    palabra = []
    palabras = ""

    for x in texto2:
        if x != "\n":
            texto = texto + x
            #print(x)
        else:
            texto = texto + " "

    while i < len(texto):
        
        letras = texto[i]

        if texto[i] != string.whitespace:
            palabra.append(letras)

        if texto[i] == " " or texto[i] == "\n":
            for x in palabra:
                if x != "\n" or x != ".":
                    palabras = palabras + x
                else:
                    print("es un espacio")
            arregloPalabras.append(palabras)
            palabras = ""

        if texto[i] == " ":
            palabra = []
            
        
        i += 1


def SendPal(ar, label):
    
    contador = 0
    y = 0
    while y < len(ar):
        print(ar[contador])
        label.configure(text=f"{ar[contador]}")
        if contador >= len(ar):
            break
        tiempo.sleep(secs)
        contador = contador + 1
        y = contador
        








