import requests
pedido={
    'Prato':"lasanha",
    'Bebida':'suco de laranja',
    'Mesa':'5',
    'sobremesa':'pudin,sorvete,bolo'
}

r= requests.post('https://68ca9f48430c4476c34a3b81.mockapi.io/restaurante',pedido)

print(r.json())
