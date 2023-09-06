from modelos.persona import Person
from arbol import ArbolBinario
import json
import csv

jsonArbol = ArbolBinario()

menu = ""

while(menu != None):
    print("1. Cargar archivo")
    print("2. Buscar por nombre")
    print("3. Buscar por dpi")
    print("4. Eliminar por Nombre")
    print("5. Eliminar por dpi")
    print("6. Actualizar por Nombre")
    print("7. Actualizar por dpi")
    print("8. Salir")
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
        print("Se encontraron:" + str(i) +" resultados.")
    elif(menu == "3"):
        print("Buscar por dpi")
        print("Coloque el dpi de la persona que quiere buscar:")
        dpi = input()
        lista = jsonArbol.buscar_por_dpi(dpi)
        i =0
        while i < len(lista):
            print("Nombre:" + lista[i].name)
            print("Dpi:" + lista[i].dpi)
            print("Fecha de nacimiento:" + lista[i].datebirth)
            print("Direccion:" + lista[i].address)
            print('\n')
            i += 1
        print("Se encontraron:" + str(i) +" resultados.")
    elif(menu == "4"):
        print("Eliminar por Nombre")
        print("Coloque el nombre de las personas que quiere eliminar:")
        nombre = input()
        lista = jsonArbol.buscar_por_nombre(nombre)
        i =0
        while i < len(lista):
            jsonArbol.eliminar(lista[i])
            i += 1
        print("Se eliminaron: " + str(i) +" personas.")

    elif(menu == "5"):
        print("Eliminar por dpi")
        print("Coloque el dpi de la personas que quiere eliminar:")
        nombre = input()
        lista = jsonArbol.buscar_por_dpi(nombre)
        i =0
        while i < len(lista):
            jsonArbol.eliminar(lista[i])
            i += 1
        print("Se eliminaron: " + str(i) +" personas.")
    elif(menu == "6"):
        print("Actualizar por nombre")
        print("Coloque el nombre de las personas que quiere actualizar:")
        nombre = input()
        lista = jsonArbol.buscar_por_nombre(nombre)
        print("Coloque la Fecha de nacimiento (en caso de no querer cambiar dar ENTER):")
        fecha = input()
        print("Coloque la direccion (en caso de no querer cambiar dar ENTER):")
        direccion = input()
        if (fecha != '') & (direccion == ''):
            i =0
            while i < len(lista):
                lista[i].datebirth = fecha
                i += 1
        elif (fecha == '') & (direccion != ''):
            i =0
            while i < len(lista):
                lista[i].address = direccion
                i += 1
        elif (fecha != '') & (direccion != ''):
            i =0
            while i < len(lista):
                lista[i].datebirth = fecha
                lista[i].address = direccion
                i += 1
        else:
            print("No se hacen cambios")
    elif(menu == "7"):
        print("Actualizar por dpi")
        print("Coloque el dpi de la persona que quiere actualizar:")
        dpi = input()
        lista = jsonArbol.buscar_por_dpi(dpi)
        print("Coloque la Fecha de nacimiento (en caso de no querer cambiar dar ENTER):")
        fecha = input()
        print("Coloque la direccion (en caso de no querer cambiar dar ENTER):")
        direccion = input()
        if (fecha != '') & (direccion == ''):
            i =0
            while i < len(lista):
                lista[i].datebirth = fecha
                i += 1
        elif (fecha == '') & (direccion != ''):
            i =0
            while i < len(lista):
                lista[i].address = direccion
                i += 1
        elif (fecha != '') & (direccion != ''):
            i =0
            while i < len(lista):
                lista[i].datebirth = fecha
                lista[i].address = direccion
                i += 1
        else:
            print("No se hacen cambios")

    elif(menu == "8"):
        menu = None