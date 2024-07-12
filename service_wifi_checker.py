from service_fetch import fetch_server_data
from service_fetch import States




def check_wifi_connection(url):    
    pokemon_info = fetch_server_data(url)
    print(pokemon_info)

    if 'error' in pokemon_info:
        return pokemon_info['error']   

    if 'code' in pokemon_info:
        return States.OK
   
    return pokemon_info