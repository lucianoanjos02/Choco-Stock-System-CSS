from database import Base
from flask_login import UserMixin
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, String, Integer, Date, ForeignKey, Float

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
    permissao = relationship('Permissao', backref=backref('TUsuario', lazy='dynamic'))
    loja = relationship("UsuarioLoja", backref=backref('TUsuario', lazy='dynamic'))

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


class Loja(Base):
    '''

    CLASSE LOJA - MAPEIA TABELA TLoja NO BANCO DE DADOS

    @autor: Gabriel Oliveira Gonçalves -
    @data: 29/08/2020 -
    @versao: 1.0.0
    '''    
    __tablename__ = 'TLoja'
    id_loja = Column(Integer, primary_key=True, autoincrement=True)
    razao_social = Column(String(100), nullable=False, unique=True)
    nome_fantasia = Column(String(100), nullable=False, unique=True)
    cnpj = Column(String(11), nullable=False, unique=True)
    logradouro = Column(String(100), nullable=False)
    numero_logradouro = Column(String(10), nullable=False)
    cep = Column(String(8), nullable=False)
    inscricao_estadual = Column(String(20), nullable=False, unique=True)
    email = Column(String(50), nullable=False, unique=True)
    usuarios = relationship('UsuarioLoja', backref=backref('TLoja', lazy='dynamic'))
    estoque = relationship('Estoque', backref=backref('TLoja', lazy='dymanic'))

    def __init__(self, razao_social, nome_fantasia, cnpj, logradouro, numero_logradouro, cep, inscricao_estadual, email, id_usuario, usuario):
        self.razao_social = razao_social
        self.nome_fantasia = nome_fantasia
        self.cnpj = cnpj
        self.logradouro = logradouro
        self.numero_logradouro = numero_logradouro
        self.cep = cep
        self.inscricao_estadual = inscricao_estadual
        self.email = email
        self.id_usuario = id_usuario
        self.usuario = usuario


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
    id_loja = Column(Integer, ForeignKey('TLoja.id_loja'))
    id_usuario = Column(Integer, ForeignKey('TUsuario.id_usuario'))

    def __init__(self, id_loja, id_usuario):
        self.id_loja = id_loja
        self.id_usuario = id_usuario


class Estoque(Base):
    '''

    CLASSE ESTOQUE - MAPEIA TABELA TEstoque NO BANCO DE DADOS

    @autor: Gabriel Oliveira Gonçalves -
    @data: 29/08/2020 -
    @versao: 1.0.0
    '''
    __tablename__ = 'TEstoque'
    id_estoque = Column(Integer, primary_key=True, autoincrement=True)
    codigo_lote = Column(String(10), nullable=False)
    quantidade = Column(Integer, nullable=False)
    data_fabricacao = Column(Date, nullable=False)
    data_validade = Column(Date, nullable=False)
    total_item = Column(Integer, nullable=False)
    id_loja = Column(Integer, ForeignKey('TLoja.id_loja'))
    produtos = relationship("EstoqueProduto", backref=backref('TEstoque', lazy='dynamic'))

    def __init__(self, numero_lote, quantidade, data_fabricacao, data_validade, total_item):
        self.numero_lote = numero_lote
        self.quantidade = quantidade
        self.data_fabricacao = data_fabricacao
        self.data_validade = data_validade
        self.total_item = total_item


class Produto(Base):
    '''
    CLASSE PRODUTO - MAPEIA TABELA TProduto NO BANCO DE DADOS

    @autor: Gabriel Oliveira Gonçalves -
    @data: 29/08/2020 -
    @versao: 1.0.0
    '''
    __tablename__ = 'TProduto'
    id_produto  = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    codigo_barras = Column(String(100), nullable=False)
    preco = Column(Float, nullable=False)
    id_tipo = Column(Integer, ForeignKey('TTipo_Produto.id'))
    id_loja = Column(Integer, ForeignKey('TLoja.id_loja'))
    id_estoque = Column(Integer, ForeignKey('TEstoque.id_estoque'))
    tipo = relationship('TipoProduto', backref=backref('TProduto', lazy='dynamic'))
    estoque = relationship('EstoqueProduto', backref=backref('TProduto', lazy='dynamic'))
    kit = relationship('Kit', backref=backref('TProduto', lazy='dynamic'))

    def __init__(self, nome_produto, codigo_barras, preco_produto, id_tipo, id_loja, id_estoque):
        self.nome_produto = nome_produto
        self.codigo_barras = codigo_barras
        self.preco_produto = preco_produto
        self.id_tipo = id_tipo
        self.id_loja = id_loja
        self.id_estoque = id_estoque


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
    id_estoque = Column(Integer, ForeignKey('TEstoque.id_estoque'))
    id_produto = Column(Integer, ForeignKey('TProduto.id_produto'))

    def __init__(self, id_loja, id_produto):
        self.id_loja = id_loja
        self.id_produto = id_produto


class TipoProduto(Base):
    '''

    CLASSE TIPO_PRODUTO - MAPEIA TABELA TTp_Produto NO BANCO DE DADOS

    @autor: Gabriel Oliveira Gonçalves -
    @data: 29/08/2020 -
    @versao: 1.0.0
    '''
    __tablename__ = 'TTipo_Produto'
    id = Column(Integer, primary_key=True, autoincrement=True)
    tipo = Column(String(100), nullable=False)

    def __init__(self, tipo):
        self.tipo = tipo
    

class Kit(Base):
    '''

    CLASSE KIT - MAPEIA TABELA Kit NO BANCO DE DADOS

    @autor: Gabriel Oliveira Gonçalves -
    @data: 29/08/2020 -
    @versao: 1.0.0
    '''
    __tablename__ = 'TKit'
    id_kit = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    quantidade = Column(Integer, nullable=False)
    preco = Column(Float, nullable=False)
    data_validade = Column(Date, nullable=False)
    id_produto = Column(Integer, ForeignKey('TProduto.id_produto'))

    def __init__(self, nome, quantidade, preco, data_validade, id_produto):
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco
        self.data_validade = data_validade
        self.id_produto = id_produto
