from database import Base
from flask_login import UserMixin
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, String, Integer, Date, ForeignKey

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

    def __repr__(self):
        return f'<Permissao: {self.permissao}>'


class Loja(Base):
    '''

    CLASSE LOJA - MAPEIA TABELA Tloja NO BANCO DE DADOS

    '''    
    __tablename__ = 'TLoja'
    id_loja = Column(Integer, primary_key=True, autoincrement=True)
    razao_social = Column(String(100), nullable=False, unique=True)
    nome_fantasia = Column(String(100), nullable=False, unique=True)
    cnpj = Column(String(11), nullable=False, unique=True)
    endereco = Column(String(100), nullable=False)
    inscricao_estadual = Column(String(20), nullable=False, unique=True)
    email = Column(String(50), nullable=False, unique=True)
    id_usuario = Column(Integer, ForeignKey('TUsuraio.id_usuario'))
    usuario = relationship('Usuario', backref=backref('TLoja', lazy='dynamic'))

    def __repr__(self):
        return f'<Loja:{self.razao_social, self.nome_fantasia, self.cnpj, self.endereco, self.inscricao_estadual, self.cnpj}>'


class Estoque(Base):
    '''

    CLASSE ESTOQUE - MAPEIA TABELA TEstoque NO BANCO DE DADOS

    '''
    __tablename__ = 'TEstoque'
    id_estoque = Column(Integer, primary_key=True, autoincrement=True)
    numero_lote = Column(String(10), nullable=False)
    quantidade = Column(Integer, nullable=False)
    data_fabricacao = Column(Date, nullable=False)
    data_validade = Column(Date, nullable=False)
    total_item = Column(Integer, nullable=False)
    id_loja = Column(Integer, ForeignKey('TLoja.id_loja'))
    loja = relationship('Loja', backref=backref('TEstoque', lazy='dymanic'))

    def __repr__(self):
        return f'<Estoque:{self.numero_lote, self.quantidade, self.data_fabricacao, self.data_validade, self.total_item}>'

class Produto(Base):
    '''

    CLASSE PRODUTO - MAPEIA TABELA TProduto NO BANCO DE DADOS

    '''
    __tablename__ = 'TProduto'
    id_produto = Column(Integer, primary_key=True, autoincrement=True)
    codigo_barras = Column(String(100), nullable=False)
    nome_produto = Column(String(100), nullable=False)
    preco_produto = Column(Integer, nullable=False)
    id_loja = Column(Integer, ForeignKey('TLoja.id_loja'))
    id_estoque = Column(Integer, ForeignKey('TEstoque.id_estoque'))
    store = relationship('Loja', backref=backref('TProduto', lazy='dynamic'))
    estoque = relationship('Estoque', backref=backref('TProduto', lazy='dynamic'))

    def __repr__(self):
        return f'<Produto:{self.codigo_barras, self.nome_produto, self.preco_produto}>'


class Tipo_Produto(Base):
    '''

    CLASSE TIPO_PRODUTO - MAPEIA TABELA TTp_Produto NO BANCO DE DADOS

    '''
    __tablename__ = 'TTp_Produto'
    id_tp_produto = Column(Integer, primary_key=True, autoincrement=True)
    nome_tp_produto = Column(String(100), nullable=False)
    id_produto = Column(Integer, ForeignKey('TProduto.id_produto'))
    produto = relationship('Produto', backref=backref('TTp_Produto', lazy='dynamic'))

    def __repr__(self):
        return f'<Tipo_Produto:{self.nome_tp_produto}>'
    

class Kit(Base):
    '''

    CLASSE KIT - MAPEIA TABELA Kit NO BANCO DE DADOS

    '''
    __tablename__ = 'TKit'
    id_kit = Column(Integer, primary_key=True, autoincrement=True)
    nome_kit = Column(String(100), nullable=False)
    qtd_kit = Column(Integer, nullable=False)
    preco_kit = Column(Integer, nullable=False)
    validade_kit = Column(Date, nullable=False)
    id_produto = Column(Integer, ForeignKey('TProduto.id_produto'))
    produto_2 = relationship('Produto', backref=backref('TKit', lazy='dynamic'))

    def __repr__(self):
        return f'<Kit:{self.nome_kit, self.qtd_kit, self.preco_kit, self.validade_kit}>'