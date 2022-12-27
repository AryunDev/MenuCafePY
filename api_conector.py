import requests

class Api():   
    
    def __init__(self, url):
        self.url = url        
    
    def mostrar_productos():
        url = "http://localhost:5000/productos"
        response = requests.get(url)
        try:
            if response.status_code == 200:
                print(f"El status_code para 'GET' es:\n---->", response.status_code)
                data = response.json()
                data_ord = sorted(data, key=lambda x: x['id']) 
                for dic in data_ord:
                    print(dic)
                print('Los datos de la lista de productos se muestran correctamente')    
        except:
            print("Error!, no se puede mostrar productos en este momento")

    def mostrar_producto(id):
        url = f"http://localhost:5000/productos/{id}" 
        response = requests.get(url)  
        try:
            if response.status_code == 200:
                print(f"El status_code para 'GET' es:\n---->", response.status_code)
                data = response.json()
                print(data)
                print('Los datos del producto que seleccionaste se muestran correctamente')
        except:
            print('Error!, no se pudo mostrar los datos de este producto')  

    def crear_producto(json_data):
        headers = {'Content-Type': 'application/json'}                
        url = "http://localhost:5000/productos"
        response = requests.post(url, data=json_data, headers=headers)
        try:
            if response.status_code == 200:
                print(f"El status_code para 'POST' es:\n---->", response.status_code)
                data = response.json()
                data_ord = sorted(data, key=lambda x: x['id']) 
                for dic in data_ord:
                    print(dic)
                print('Los datos del producto que creaste fueron ingresados correctamente')
        except:
            print('Error!, no se pudo crear el nuevo producto')        

    def actualizar_producto(id, json_data):
        headers = {'Content-Type': 'application/json'}
        url= f"http://localhost:5000/productos/{id}"
        response = requests.put(url, data=json_data, headers = headers)            
        try:
            if response.status_code == 200:
                print(f"El status_code para 'PUT' es:\n---->", response.status_code)
                data = response.json()
                print(data)
                print('Los datos del producto que seleccionaste fueron actualizados correctamente')
        except:
            print('Error al actualizar los datos')

    def eliminar_producto(id):
        url= f"http://localhost:5000/productos/{id}"      
        response = requests.delete(url)
        try:            
            if response.status_code == 200:
                print(f"El status_code para 'DELETE' es:\n---->", response.status_code)
                data = response.json()
                data_ord = sorted(data, key=lambda x: x['id']) 
                for dic in data_ord:
                    print(dic)
                print('Los datos del producto que seleccionaste fueron eliminados correctamente y ya no aparecen en la lista')
        except:
            print('Error al eliminar los datos')