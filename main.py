from modelos.persona import Person
from arbol import ArbolBinario
import json
import csv

jsonArbol = ArbolBinario()

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




#persona = Person.from_json(el string de json)