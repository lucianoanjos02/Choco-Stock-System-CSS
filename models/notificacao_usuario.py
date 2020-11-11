from database import Base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, String, Integer, Date, ForeignKey, Numeric, DateTime

class NotificacaoUsuario(Base):
    '''

    CLASSE Notificacao - MAPEIA TABELA TNotificacao_Usuario NO BANCO DE DADOS,
    QUE RELACIONA AS NOTIFICAÇÕES DA TABELA TNotificacao COM OS USUÁRIOS CADASTRADOS
    NO TABELA TUsuario
  
    @autor: Luciano Gomes Vieira dos Anjos -
    @data: 15/10/2020 -
    @versao: 1.0.0
    '''
    __tablename__ = 'TNotificacao_Usuario'
    id = Column(Integer, primary_key=True, autoincrement=True)
    fk_id_notificacao = Column(Integer, ForeignKey('TNotificacao.id_notificacao'))
    fk_id_usuario = Column(Integer, ForeignKey('TUsuario.id_usuario')) 
    visualizada = Column(Integer, nullable=False)
    email_enviado = Column(Integer, nullable=False)

    def __init__(self, fk_id_notificacao, fk_id_usuario, visualizada, email_enviado):
        self.fk_id_notificacao = fk_id_notificacao
        self.fk_id_usuario = fk_id_usuario
        self.visualizada = visualizada
        self.email_enviado = email_enviado