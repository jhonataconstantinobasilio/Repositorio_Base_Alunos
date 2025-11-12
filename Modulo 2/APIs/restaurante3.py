
import requests



passo1 = requests.get(f'https://68ca9f3f430c4476c34a3b5f.mockapi.io/Restaurante/')
print(passo1.json())

s = input('Vai ficar, ou vai embora? Por favor, digite (ficar/sair) apenas: ')

if s == 'sair':
    pedidoId=input('digite o id que sera deletado')
    passo2 = requests.delete(f'https://68ca9f3f430c4476c34a3b5f.mockapi.io/Restaurante/{pedidoId}')
    


elif s == 'ficar':
    pedidoId_0=input('digite o id que sera alterado: ')
    local = input('Qual mesa vão se sentar? ')
    pedido = input ('Qual será seu pedido? ')
    bebida = input('Bebida pra acompanhamento? ')
    pedidoCliente={
        'prato':pedido,
        'bebida':bebida,
        'mesa':local
    }


    passo2_0 = requests.put(f'https://68ca9f3f430c4476c34a3b5f.mockapi.io/Restaurante/{pedidoId_0}',pedidoCliente)



    
