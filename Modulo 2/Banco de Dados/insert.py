from coneccao import Session
from aleatorio import Loja

with Session() as session:
    loja=Loja(nome='carGabriel',endereco='rua padilha',gerente='jhonatã')
    session.add(loja)
    session.commit()
    print('funcionou')

