from database import Base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, String, Integer, Date, ForeignKey, Numeric, DateTime

class Notificacao(Base):
    '''

    CLASSE Notificacao - MAPEIA TABELA TNotificacao NO BANCO DE DADOS 
  
    @autor: Luciano Gomes Vieira dos Anjos -
    @data: 15/10/2020 -
    @versao: 1.0.0
    '''
    __tablename__ = 'TNotificacao'
    id_notificacao = Column(Integer, primary_key=True, autoincrement=True)
    assunto_notificacao = Column(String(50), nullable=False)
    info_notificacao = Column(String(100), nullable=False)
    data_notificacao = Column(DateTime, nullable=False)
    fk_id_estoque_produto = Column(Integer, ForeignKey('TEstoque_Produto.id'))
    fk_id_kit = Column(Integer, ForeignKey('TKit.id_kit'))
    fk_id_tipo_notificacao = Column(Integer, ForeignKey('TTipo_Notificacao.id'))
    tipo_notificacao = relationship('TipoNotificacao', backref=backref('TNotificacao'))
    notificacao_usuario = relationship('NotificacaoUsuario', backref=backref('TNotificacao'))
    

    def __init__(self, assunto_notificacao, info_notificacao, data_notificacao, fk_id_estoque_produto, fk_id_kit, fk_id_tipo_notificacao):
        self.assunto_notificacao = assunto_notificacao
        self.info_notificacao = info_notificacao
        self.data_notificacao = data_notificacao
        self.fk_id_estoque_produto = fk_id_estoque_produto
        self.fk_id_kit = fk_id_kit
        self.fk_id_tipo_notificacao = fk_id_tipo_notificacao