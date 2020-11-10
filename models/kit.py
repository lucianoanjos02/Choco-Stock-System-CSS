from database import Base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, String, Integer, Date, ForeignKey, Numeric, DateTime

class Kit(Base):
    '''

    CLASSE KIT - MAPEIA TABELA Kit NO BANCO DE DADOS

    @autor: Gabriel Oliveira Gonçalves -
    @data: 29/08/2020 -
    @versao: 1.0.0
    '''
    __tablename__ = 'TKit'
    id_kit = Column(Integer, primary_key=True, autoincrement=True)
    codigo = Column(String(20), unique=True, nullable=False)
    nome = Column(String(100), nullable=False)
    quantidade = Column(Integer, nullable=False)
    data_validade = Column(Date, nullable=False)
    produtos = relationship('KitProduto', backref=backref('TKit'))
    notificacao_kit = relationship('Notificacao', backref=backref('TKit'))

    def __init__(self, codigo, nome, quantidade, data_validade):
        self.codigo = codigo
        self.nome = nome
        self.quantidade = quantidade
        self.data_validade = data_validade