import requests
# from flask import Flask
# import pprint 
# import json

class Api():

    def __init__(self,url):
        self.url = url   
      
    def mostrar_producto():
        url = "http://localhost:5000/productos"
        response = requests.get(url)

        # print(response)

        print(response.text)
        # esto sirve para hacer validaciones segun el julio
        print(response.status_code)


    def crear_producto(self, data):    
        headers = {'Content-Type': 'application/json'}
        data = '{"id": 10, "nombre": "Pié De Limón", "descripcion": "Masa, Azucar, Limó", "valor": 2500}'    
        
        url = "http://localhost:5000/productos"
        response = requests.post(self, url, data=data, headers=headers)
        
        # print(response)
        print(response.text)
        print(response.status_code)
        
obj = Api()


    

