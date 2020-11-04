from database import Base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, String, Integer, Date, ForeignKey, Numeric, DateTime

class Loja(Base):
    '''

    CLASSE LOJA - MAPEIA TABELA TLoja NO BANCO DE DADOS

    @autor: Gabriel Oliveira Gonçalves -
    @data: 29/08/2020 -
    @versao: 1.0.0
    '''    
    __tablename__ = 'TLoja'
    id_loja = Column(Integer, primary_key=True, autoincrement=True)
    razao_social = Column(String(100), nullable=False)
    nome_fantasia = Column(String(100), nullable=False)
    cnpj = Column(String(14), nullable=False)
    logradouro = Column(String(100), nullable=False)
    numero_logradouro = Column(String(10), nullable=False)
    cep = Column(String(8), nullable=False)
    inscricao_estadual = Column(String(20), nullable=False)
    email = Column(String(50), nullable=False)
    usuarios = relationship('UsuarioLoja', backref=backref('TLoja'))
    estoque = relationship('Estoque', backref=backref('TLoja'))

    def __init__(self, id_loja, razao_social, nome_fantasia, cnpj, logradouro, numero_logradouro, cep, inscricao_estadual, email):
        self.id_loja = id_loja
        self.razao_social = razao_social
        self.nome_fantasia = nome_fantasia
        self.cnpj = cnpj
        self.logradouro = logradouro
        self.numero_logradouro = numero_logradouro
        self.cep = cep
        self.inscricao_estadual = inscricao_estadual
        self.email = email