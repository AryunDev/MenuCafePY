import requests
from flask import Flask
import pprint
import json

class Api():

    def __init__(self):     
      

        url = "http://localhost:5000/productos"
        response = requests.get(url)

        print(response)
        print(response.text)
        print(response.status_code)


    def __init__(self):     
        pepinho = {'Content-Type': 'application/json'}
        pepito = {"id": 10, "nombre": "Pié De Limón", "descripcion": "Masa, Azucar, Limó", "valor": 2500}         
        
        url = "http://localhost:5000/productos"
        response = requests.post(url, data=pepito, headers=pepinho)

        print(response)
        print(response.text)
        print(response.status_code)
        
obj = Api()


    

