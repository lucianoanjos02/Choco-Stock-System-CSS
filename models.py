from database import Base
from flask_login import UserMixin
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, String, Integer, ForeignKey

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
    role = relationship('Permissao', backref=backref('TUsuario', lazy='dynamic'))

    def __init__(self, nome, sobrenome, email, login, senha):
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.login = login
        self.senha = senha
    
    # -------------------------------------------------------------------------------------
    # ------ METODOS PROPERTY PARA IMPLEMENTAÇÃO DO FLASK-LOGIN COM A CLASSE USUARIO ------
    # -------------------------------------------------------------------------------------
    # @autor: Luciano Gomes Vieira dos Anjos
    # @data: 26/08/2020

    @property
    def is_authenticated(self):
        return True
    
    @property
    def is_active(self):
        return True
    
    @property
    def is_anonymous(self):
        return False


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

    def __init__(self, nome):
        self.nome = nome

