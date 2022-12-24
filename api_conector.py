import requests
from flask import Flask
import pprint 
import json



class Api():
    
    
    def __init__(self, url):
        self.url = url
        
      
    def mostrar_productos(self):
        url = "http://localhost:5000/productos"
        response = requests.get(url)

        print(response)

        print(response.text)
        # esto sirve para hacer validaciones segun el julio
        print(response.status_code)

    def mostrar_producto(self, id):
        url = f"http://localhost:5000/productos/{id}"
        response = requests.get(url)
        print(response.text)



    # def crear_producto(self, data):    
    #     headers = {'Content-Type': 'application/json'}
    #     data = '{"id": 10, "nombre": "Pié De Limón", "descripcion": "Masa, Azucar, Limó", "valor": 2500}'    
        
    #     url = "http://localhost:5000/productos"
    #     response = requests.post(self, url, data=data, headers=headers)
        
    #     print(response)
    #     print(response.text)
    #     print(response.status_code)

    def actualizar_producto(self, id):
        url= f"http://localhost:5000/productos/{id}" 
        data = f"{'id': 1,'nombre': 'Donuts','descripcion': 'rellenas de chocolate','valor': 2500}"

        response = requests.put(url, data)
        print(response.text)

    def eliminar_producto(self, id):
        
        url= f"http://localhost:5000/productos/{id}" 
        response = requests.delete(url)

        if response.status_code == 204:
                print('Datos eliminados correctamente')
        else:
                print('Error al eliminar los datos')

        


url = "http://localhost:5000/productos"    
obj = Api(url)

obj.eliminar_producto(8)
obj.mostrar_productos()
data = '{"id": 10, "nombre": "Pié De Limón", "descripcion": "Masa, Azucar, Limó", "valor": 2500}'

# obj.mostrar_productos()
#data.crear_producto()


    

