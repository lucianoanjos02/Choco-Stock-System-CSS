from flask_login import UserMixin
from database import Base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, String, Integer, Date, ForeignKey, Numeric, DateTime

class Usuario(Base, UserMixin):
    '''

    CLASSE USUARIO - MAPEIA TABELA TUsuario NO BANCO DE DADOS
  
    @autor: Luciano Gomes Vieira dos Anjos -
    @data: 26/08/2020 -
    @versao: 1.0.0
    '''
    __tablename__ = 'TUsuario'
    id_usuario = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(25), nullable=False)
    sobrenome = Column(String(25), nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    login = Column(String(20), unique=True, nullable=False)
    senha = Column(String(10), nullable=False)
    id_permissao = Column(Integer, ForeignKey('TPermissao.id_permissao'))
    permissao = relationship('Permissao', backref=backref('TUsuario'))
    loja = relationship("UsuarioLoja", backref=backref('TUsuario'))
    usuario_notificacao = relationship('NotificacaoUsuario', backref=backref('Usuario'))

    def __init__(self, nome, sobrenome, email, login, senha, id_permissao):
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.login = login
        self.senha = senha
        self.id_permissao = id_permissao
    
    # -------------------------------------------------------------------------------------
    # ------ METODOS PROPERTY PARA IMPLEMENTAÇÃO DO FLASK-LOGIN COM A CLASSE USUARIO ------
    # -------------------------------------------------------------------------------------
    # @autor: Luciano Gomes Vieira dos Anjos
    # @data: 26/08/2020
    # @versao: 1.0.0

    @property
    def is_authenticated(self):
        return True
    
    @property
    def is_active(self):
        return True
    
    @property
    def is_anonymous(self):
        return False
    
    def get_id(self):
        return str(self.id_usuario)