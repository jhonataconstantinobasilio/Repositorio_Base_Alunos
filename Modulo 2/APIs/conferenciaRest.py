
import requests

resposta = input("Você pediu abacate com mel e fanta na mesa 6? ")

if resposta == 'sim':
    pedido={
        'prato': 'abacate com mel',
        'bebida': 'fanta',
        'mesa': '6'
    }
else:
    prato =input('Digite seu prato:')
    bebida =input('bebida: ')
    local =input('sua mesa: ')

r = requests.put('https://68ca9f3f430c4476c34a3b5f.mockapi.io/Restaurante/1',pedido)

print(r.json())
