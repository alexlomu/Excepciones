# Excepciones
El link de este repositorio es: [Github](https://github.com/alexlomu/Excepciones)
https://github.com/alexlomu/Excepciones.
Para esta entrega hemos tenido que programar un código que introducida una entrada nos diga si este es un correo electrónico o no.
El UML correspondiente es el siguiente:

![uml excepciones](https://user-images.githubusercontent.com/91721507/161435859-0ed2e7f1-3c5e-4697-b615-210a067a666c.PNG)

El código propuesto es el siguiente:
```
import re

def comprobar():
    entrada = input("Introduce tu correo: ")
    if entrada == "":
        print("'' es una entrada incorrecta. Introduzca una dirección de correo")
        comprobar()
    elif re.search(". * @. * \ .. *", entrada):
        print("Una dirección de correo electrónico debe tener el formato xxx@xxx.xx")
        comprobar()
    else:
        lista = re.split( "@", entrada)
        nombre = lista [0]
        print("Bienvenido ", nombre)
comprobar()
```
