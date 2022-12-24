from api_conector import Api


import os
def limpiarpantalla():
    os.system('cls')

class Menu:
    def __init__():

        print('''
        ====================MENU=================
        = a) Mostrar los productos disponibles  =
        = b) Mostrar un producto en especifico  =
        = c) Crear un nuevo producto            =
        = d) Editar un producto                 =
        = e) Eliminar un producto               =
        = f) Para salir del programa presione   =
        =        cualquier tecla !!!            =
        =========================================
        ''')

        op = input("Ingrese una opcion:\n").capitalize()
        print('\n')
        limpiarpantalla()
        # FUNCIONA
        if op == 'A':
           
             Api.mostrar_productos()
        # FUCNIONA
        elif op == 'B':
            id = int(input("Ingrese el id del producto que desea mostrar:\n"))
            Api.mostrar_producto(id)
        
        elif op == 'C':
            # id = int(input("Ingrese el id del nuevo producto:\n"))
            # nombre = input("Ingrese el nombre del nuevo producto:\n")
            # descripcion = input("Ingrese unda descripcion para el nuevo producto:\n")
            # valor = int(input("Ingrese un valor para el nuevo producto:\n"))

            
            # data = {
            # "id": {id},
            # "nombre": {nombre},
            # "descripcion": {descripcion},
            # "valor": {valor}
            # }

            # Api.crear_producto(data)
            pass

        elif op == 'D':
            # id = int(input("Ingrese el id del producto que desea modificar:\n"))
            # nombre = input("Ingrese el nuevo nombre o mantenga el anterior:\n")
            # descripcion = input("Ingrese nueva descripción o mantenga la anterior:\n")
            # valor = int(input("Ingrese un nuevo valor o mantenga el anterior:\n"))

            # # data = data.append(nombre, descripcion, valor)
            # data = {
            # "id": {id},
            # "nombre": {nombre},
            # "descripcion": {descripcion},
            # "valor": {valor}
            # }

            # Api.actualizar_producto(data)
            pass

        elif op == 'E':
            id = int(input("Ingrese el id del producto que quiere eliminar:\n"))
            Api.eliminar_producto(id)
        else:
            pass

        

Menu.__init__()