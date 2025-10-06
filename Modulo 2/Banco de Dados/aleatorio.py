# Todo codigo abaixo serve para criar uma conexao com o banco
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

DATABASE_URL = 'sqlite:///relacoes.db'

engine = create_engine(DATABASE_URL, echo=False, future=True)

Base = declarative_base()

Session = sessionmaker(bind=engine, future=True)

# ============================
# Definição das tabelas
# ============================

class Loja(Base):
    __tablename__ = "lojas"

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    endereco = Column(String)
    gerente = Column(String)

    vendedores = relationship("Vendedor", back_populates="loja")  # corrigido


class Vendedor(Base):
    __tablename__ = "vendedores"

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    lojaid = Column(Integer, ForeignKey("lojas.id"))

    loja = relationship("Loja", back_populates="vendedores")       # corrigido
    vendas = relationship("Venda", back_populates="vendedor")      # corrigido


class Venda(Base):
    __tablename__ = "vendas"

    id = Column(Integer, primary_key=True)
    carro = Column(String, nullable=False)
    valor = Column(String, nullable=False)
    comissao = Column(String, nullable=False)
    vendedor_id = Column(Integer, ForeignKey("vendedores.id"))

    vendedor = relationship("Vendedor", back_populates="vendas")   # corrigido


# Criar tabelas no banco
Base.metadata.create_all(engine)
