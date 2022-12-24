import requests
# from flask import Flask
import json



class Api():
    
    
    def __init__(self, url):
        self.url = url
        
    
    def mostrar_productos():

        url = "http://localhost:5000/productos"
        response = requests.get(url)

        print(response)

        print(response.text)
        # esto sirve para hacer validaciones segun el julio
        print(response.status_code)



    def mostrar_producto(id):

        url = f"http://localhost:5000/productos/{id}"
        response = requests.get(url)
        response = response.json()        

        try:
            print(response)
        except:
            print('Error al intentar mostrar los datos')



    # def crear_producto(self, data):    
        
    #     headers = {'Content-Type': 'application/json'}
    #     #data = f'{"id": {id}, "nombre": {nombre}, "descripcion": {descripcion}, "valor": {valor}}'

        
    #     # url = "http://localhost:5000/productos"
    #     response = requests.post(self, url, data=data, headers = headers)
        
    #     print(response)
    #     print(response.text)
    #     print(response.status_code)

    def actualizar_producto(id, data):
        url= f"http://localhost:5000/productos/{id}" 
        # data = {"id": 1,"nombre": "Donuts","descripcion": "rellenas de chocolate","valor": 2500}    
        try:
            response = requests.put(url, data=data)
            response = response.json()
            print(response)
            # response.status_code == 200
            print('Datos actualizados correctamente')
        except:
            print('Error al actualizar los datos')

    def eliminar_producto(id):

        url= f"http://localhost:5000/productos/{id}" 
        response = requests.delete(url)

        try:
            response.status_code == 204
            print('Datos eliminados correctamente')
        except:
            print('Error al eliminar los datos')

        


url = "http://localhost:5000/productos"    
obj = Api(url)
# data = '{"nombre": "Papa","descripcion": "rellenas de chocolate"}'

# obj.actualizar_producto(1)
# obj.mostrar_productos()


# obj.mostrar_producto()
# obj.crear_producto()
# obj.mostrar_productos()

    

