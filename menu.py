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
        limpiarpantalla()

        if op == 'A':
            id = int(input("Asigne un id a su nuevo producto:\n"))
            nombre = input("Ingrese el nombre del producto:\n")
            descripcion = input("Ingrese una descripcion para su producto:\n")
            precio = int(input("Ingrese el valor de este producto:\n"))

        elif op == 'B':
            pass
        elif op == 'C':
            pass
        elif op == 'D':
            pass
        elif op == 'E':
            pass
        else:
            pass

        

Menu.__init__()