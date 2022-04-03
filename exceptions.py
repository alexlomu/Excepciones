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

