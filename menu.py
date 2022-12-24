from api_conector import Api


import os
def limpiarpantalla():
    os.system('cls')

class Menu:
    def __init__():

        print('''
        ====================MENU=================
        = a) Crear un nuevo producto            =
        = b) Mostrar los productos disponibles  =
        = c) Mostrar un producto en especifico  =
        = d) Editar un producto                 =
        = e) Eliminar un producto               =
        = f) Para salir del programa presione   =
        =        cualquier tecla !!!            =
        =========================================
        ''')

        op = input("Ingrese una opcion:\n").capitalize()
        print('\n')
        limpiarpantalla()

        if op == 'A':
            # id = int(input("Asigne un id a su nuevo producto:\n"))
            # nombre = input("Ingrese el nombre del producto:\n")
            # descripcion = input("Ingrese una descripcion para su producto:\n")
            # precio = int(input("Ingrese el valor de este producto:\n"))
                pass

        elif op == 'B':
            Api.mostrar_productos()
        elif op == 'C':

            id = int(input("Ingrese el id del producto que desea mostrar:\n"))
            Api.mostrar_producto(id)
        elif op == 'D':
            id = int(input("Ingrese el id del producto que desea modificar:\n"))
            nombre = input("Ingrese el nuevo nombre o mantenga el anterior:\n")
            descripcion = input("Ingrese nueva descripción o mantenga la anterior:\n")
            valor = int(input("Ingrese un nuevo valor o mantenga el anterior:\n"))

            # data = data.append(nombre, descripcion, valor)
            data = {
            "id": {id},
            "nombre": {nombre},
            "descripcion": {descripcion},
            "valor": {valor}
            }

            Api.actualizar_producto(data)

        elif op == 'E':
            id = int(input("Ingrese el id del producto que quiere eliminar:\n"))
            Api.eliminar_producto(id)
        else:
            pass

        

Menu.__init__()