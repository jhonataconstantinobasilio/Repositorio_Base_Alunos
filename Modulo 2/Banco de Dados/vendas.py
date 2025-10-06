from coneccao import Session
from aleatorio import Venda

with Session() as session:
    venda=Venda(carro='fiat uno',valor='2.000,00',comissao='###',vendedor_id=1)
    session.add(venda)
    session.commit()
    print('funcionou essa bagaça')