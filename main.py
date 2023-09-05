from modelos.persona import Person
from arbol import ArbolBinario
import json
import csv

jsonArbol = ArbolBinario()

def insertar(jsonPersona):
    jsonArbol.insertar(jsonPersona)

def patch(jsonPersona):
    if ((jsonArbol.buscar(jsonPersona))!= None):
        jsonPersonaPatch = jsonArbol.buscar(jsonPersona)
        jsonPersonaPatch.datebirth = jsonPersona.datebirth
        jsonPersonaPatch.address = jsonPersona.address
        eliminar(jsonPersona)
        insertar(jsonPersonaPatch)
    else:
        print("No se encontro a la persona")

def eliminar(jsonPersona):
    if ((jsonArbol.buscar(jsonPersona))!= None):
        eliminar(jsonPersona)
    else:
        print("No se encontro a la persona")

menu = None

while(menu == None):
    print("1. Cargar archivo")
    print("2. Buscar por nombre")
    print("3. Buscar por dpi")
    print("4. Eliminar por dpi")
    print("5. Salir")
    menu = input()

    if(menu == "1"):
        print("Cargando archivo...")
        with open('input.csv') as archivo:
            reader = csv.reader(archivo, delimiter=";")
            for fila in reader:
                jsonPersona = Person.from_json(str(fila[1]))
                if fila[0] == "INSERT":
                    insertar(jsonPersona)
                elif fila[0] == "PATCH":
                    patch(jsonPersona)
                elif fila[0] == "DELETE":
                    eliminar(jsonPersona)
                else:
                    print("No es una instruccion valida")
        print("Se cargo el archivo correctamente")
    elif(menu == "2"):
        print("")
    elif(menu == "3"):
        print("")
    elif(menu == "4"):
        print("")
    elif(menu == "5"):
        menu = None