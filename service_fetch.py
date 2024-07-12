import requests
from enum import Enum

class States(Enum):
    OK = 1
    REQUEST_ERROR = 2
    TIMEOUT_ERROR = 3
    SERVIDOR_ERROR = 4

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

def fetch_server_data(url):   
    global headers
    try:
        # Realiza la solicitud HTTP GET con un tiempo límite de 5 segundos
        response = requests.get(url,headers = headers, timeout=5)

        print(response)
        
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
