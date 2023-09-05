import os
from modelos.persona import Person
from arbol import ArbolBinario
import json
import csv

os.system("cls")

jsonArbol = ArbolBinario()

menu = ""

while(menu != None):
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
                    jsonArbol.insertar(jsonPersona)
                elif fila[0] == "PATCH":
                    if ((jsonArbol.buscar(jsonPersona))!= None):
                        jsonPersonaPatch = jsonArbol.buscar(jsonPersona)
                        jsonPersonaPatch.datebirth = jsonPersona.datebirth
                        jsonPersonaPatch.address = jsonPersona.address
                        jsonArbol.eliminar(jsonPersona)
                        jsonArbol.insertar(jsonPersonaPatch)
                    else:
                        print("No se encontro a la persona")
                elif fila[0] == "DELETE":
                    jsonArbol.eliminar(jsonPersona)
                else:
                    print("No es una instruccion valida")
        os.system("cls")
        print("Se cargo el archivo correctamente")
    elif(menu == "2"):
        print("Buscar por nombre")
        print("Coloque el nombre de las personas que quiere buscar:")
        nombre = input()
        lista = jsonArbol.buscar_por_nombre(nombre)
        i =0
        while i < len(lista):
            print("Nombre:" + lista[i].name)
            print("Dpi:" + lista[i].dpi)
            print("Fecha de nacimiento:" + lista[i].datebirth)
            print("Direccion:" + lista[i].address)
            print('\n')
            i += 1
        print("Se encontraron:" + str(i+1) +" resultados.")
    elif(menu == "3"):
        print("Buscar por dpi")

    elif(menu == "4"):
        print("Eliminar por dpi")

    elif(menu == "5"):
        menu = None