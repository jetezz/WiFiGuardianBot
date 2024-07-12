import requests
from enum import Enum

class States(Enum):
    OK = 1
    REQUEST_ERROR = 2
    TIMEOUT_ERROR = 3
    SERVIDOR_ERROR = 4

def fetch_server_data(url):   
    
    try:
        # Realiza la solicitud HTTP GET con un tiempo límite de 5 segundos
        response = requests.get(url, timeout=5)
        
        # Comprueba si la solicitud fue exitosa
        if response.status_code == 200:
            # Convierte la respuesta JSON a un diccionario de Python
            data = response.json()
            data["code"] = "OK"           
            
            # Retorna el diccionario tal cual
            return data
        else:
            # Retorna un mensaje de error si la API no responde correctamente
            return {"error": States.SERVIDOR_ERROR , "code": "error"}
    
    except requests.exceptions.Timeout:
        # Maneja el caso de timeout
        return {"error": States.TIMEOUT_ERROR, "code": "error"}
    
    except requests.exceptions.RequestException as e:
        # Maneja otros posibles errores de solicitud
        return {"error": States.REQUEST_ERROR, "code": "error"}
