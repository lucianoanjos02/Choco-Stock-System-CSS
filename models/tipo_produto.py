from database import Base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, String, Integer, Date, ForeignKey, Numeric, DateTime

class TipoProduto(Base):
    '''

    CLASSE TIPO_PRODUTO - MAPEIA TABELA TTp_Produto NO BANCO DE DADOS

    @autor: Gabriel Oliveira Gonçalves -
    @data: 29/08/2020 -
    @versao: 1.0.0
    '''
    __tablename__ = 'TTipo_Produto'
    id = Column(Integer, primary_key=True, autoincrement=True)
    tipo = Column(String(100), nullable=False)

    def __init__(self, tipo):
        self.tipo = tipo