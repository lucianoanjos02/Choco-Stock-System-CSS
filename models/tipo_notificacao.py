from database import Base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, String, Integer, Date, ForeignKey, Numeric, DateTime

class TipoNotificacao(Base):
    '''

    CLASSE TipoNotificacao - MAPEIA TABELA TTipo_Notificacao NO BANCO DE DADOS,
    QUE RELACIONA AS NOTIFICAÇÕES DA TABELA TNotificacao COM OS TIPOS DE NOTIFICAÇÃO
  
    @autor: Luciano Gomes Vieira dos Anjos -
    @data: 15/10/2020 -
    @versao: 1.0.0
    '''
    __tablename__ = 'TTipo_Notificacao'
    id = Column(Integer, primary_key=True, autoincrement=True)
    tipo = Column(String(30), nullable=False, unique=True)

    def __init__(self, tipo):
        self.tipo = tipo