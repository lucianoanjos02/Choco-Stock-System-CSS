from database import Base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, String, Integer, Date, ForeignKey, Numeric, DateTime

class UsuarioLoja(Base):
    '''

    CLASSE UsuarioLoja - MAPEIA TABELA TUsuario_Loja NO BANCO DE DADOS 
    QUE FAZ A ASSOCIAÇÃO ENTRE Usuario E Loja
  
    @autor: Luciano Gomes Vieira dos Anjos -
    @data: 02/09/2020 -
    @versao: 1.0.0
    '''
    __tablename__ = 'TUsuario_Loja'
    id = Column(Integer, primary_key=True, autoincrement=True)
    fk_id_loja = Column(Integer, ForeignKey('TLoja.id_loja'))
    fk_id_usuario = Column(Integer, ForeignKey('TUsuario.id_usuario'))

    def __init__(self, fk_id_loja, fk_id_usuario):
        self.fk_id_loja = fk_id_loja
        self.fk_id_usuario = fk_id_usuario