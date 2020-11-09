from database import Base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, String, Integer, Date, ForeignKey, Numeric, DateTime

class Produto(Base):
    '''
    CLASSE PRODUTO - MAPEIA TABELA TProduto NO BANCO DE DADOS

    @autor: Gabriel Oliveira Gonçalves -
    @data: 29/08/2020 -
    @versao: 1.0.0
    '''
    __tablename__ = 'TProduto'
    id_produto  = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    id_tipo = Column(Integer, ForeignKey('TTipo_Produto.id'))
    tipo = relationship('TipoProduto', backref=backref('TProduto'))
    estoque = relationship('EstoqueProduto', backref=backref('TProduto'))
    kit = relationship('KitProduto', backref=backref('TProduto'))

    def __init__(self, nome_produto, id_tipo):
        self.nome = nome_produto
        self.id_tipo = id_tipo