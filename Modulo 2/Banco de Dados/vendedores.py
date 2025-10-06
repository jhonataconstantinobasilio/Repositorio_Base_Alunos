from coneccao import Session
from aleatorio import Vendedor



with Session () as session:

    # session.get(lojas.id)
    vendedores=Vendedor(nome='guilherme',lojaid=1)
    session.add(vendedores)
    session.commit()
    print('essa uotra bagaça tbm funcionou')