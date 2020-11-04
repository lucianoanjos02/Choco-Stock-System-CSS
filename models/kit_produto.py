from database import Base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, String, Integer, Date, ForeignKey, Numeric, DateTime

class KitProduto(Base):
    '''

    CLASSE KitProduto - MAPEIA TABELA TKit_Produto NO BANCO DE DADOS 
    QUE FAZ A ASSOCIAÇÃO ENTRE Kit E Produto
  
    @autor: Luciano Gomes Vieira dos Anjos -
    @data: 08/09/2020 -
    @versao: 1.0.0
    '''
    __tablename__ = 'TKit_Produto'
    id = Column(Integer, primary_key=True, autoincrement=True)
    fk_id_kit = Column(Integer, ForeignKey('TKit.id_kit'))
    fk_id_produto = Column(Integer, ForeignKey('TProduto.id_produto'))

    def __init__(self, fk_id_kit, fk_id_produto):
        self.fk_id_kit = fk_id_kit
        self.fk_id_produto = fk_id_produto