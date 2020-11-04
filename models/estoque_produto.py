from database import Base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, String, Integer, Date, ForeignKey, Numeric, DateTime

class EstoqueProduto(Base):
    '''

    CLASSE EstoqueProduto - MAPEIA TABELA TEstoque_Produto NO BANCO DE DADOS
    QUE FAZ A ASSOCIAÇÃO ENTRE Estoque E Produto
  
    @autor: Luciano Gomes Vieira dos Anjos -
    @data: 02/09/2020 -
    @versao: 1.0.0
    '''
    __tablename__ = 'TEstoque_Produto'
    id = Column(Integer, primary_key=True, autoincrement=True)
    fk_id_estoque = Column(Integer, ForeignKey('TEstoque.id_estoque'))
    fk_id_produto = Column(Integer, ForeignKey('TProduto.id_produto'))
    quantidade_produto = Column(Integer, nullable=False)
    total_produto = Column(Integer, nullable=False)
    data_validade = Column(Date, nullable=False)
    estoque_produto = relationship('Notificacao', backref=backref('TEstoque_Produto'))
    

    def __init__(self, fk_id_estoque, fk_id_produto, quantidade_produto, total_produto, data_validade):
        self.fk_id_estoque = fk_id_estoque
        self.fk_id_produto = fk_id_produto
        self.quantidade_produto = quantidade_produto
        self.total_produto = total_produto
        self.data_validade = data_validade