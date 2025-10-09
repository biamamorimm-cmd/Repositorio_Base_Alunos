
import requests 

dados=requests.get('https://68e543ff21dd31f22cc13300.mockapi.io/Api/Restaurante').json()

for item in dados:
    Prato=item.get('Prato')
    id = item.get('id')

    if 'pizza' in Prato:
        requests.delete(f'https://68e543ff21dd31f22cc13300.mockapi.io/Api/Restaurante/{id}')
        print ('Odeio pizza 😝')


