
import requests




lista = requests.get('https://68ca9f3f430c4476c34a3b5f.mockapi.io/Restaurante').json()

print(lista)


def publicar(local,pedido,bebida):
   
    cliente = {
    'prato':pedido,
    'bebida':bebida,
    'mesa':local
    }

    requests.post(f"https://68ca9f3f430c4476c34a3b5f.mockapi.io/Restaurante/",cliente)




for item in lista:
    # print(f'Me acompanhe até a mesa {local}. Irei trazer seu pedido {pedido}, com a bebida {bebida} de acompanhamento: ')
    break
