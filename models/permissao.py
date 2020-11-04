from database import Base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, String, Integer, Date, ForeignKey, Numeric, DateTime

class Permissao(Base):
    '''

    CLASSE PERMISSAO - MAPEIA TABELA TPermissao NO BANCO DE DADOS
  
    @autor: Luciano Gomes Vieira dos Anjos -
    @data: 26/08/2020 -
    @versao: 1.0.0
    '''
    __tablename__ = 'TPermissao'
    id_permissao = Column(Integer, primary_key=True, autoincrement=True)
    permissao = Column(String(25), unique=True, nullable=False)

    def __init__(self, permissao):
        self.permissao = permissao