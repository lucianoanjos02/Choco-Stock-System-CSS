from database import Base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, String, Integer, Date, ForeignKey, Numeric, DateTime

class Estoque(Base):
    '''

    CLASSE ESTOQUE - MAPEIA TABELA TEstoque NO BANCO DE DADOS

    @autor: Gabriel Oliveira Gonçalves -
    @data: 29/08/2020 -
    @versao: 1.0.0
    '''
    __tablename__ = 'TEstoque'
    id_estoque = Column(Integer, primary_key=True, autoincrement=True)
    codigo_lote = Column(String(10), nullable=False)
    total_item = Column(Integer, nullable=False)
    id_loja = Column(Integer, ForeignKey('TLoja.id_loja'))
    produtos = relationship("EstoqueProduto", backref=backref('TEstoque'))

    def __init__(self, codigo_lote, total_item, id_loja):
        self.codigo_lote = codigo_lote
        self.total_item = total_item
        self.id_loja = id_loja