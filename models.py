from database import Base
from flask_login import UserMixin
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
    razao_social = Column(String(100), nullable=False)
    nome_fantasia = Column(String(100), nullable=False)
    cnpj = Column(String(14), nullable=False)
    logradouro = Column(String(100), nullable=False)
    numero_logradouro = Column(String(10), nullable=False)
    cep = Column(String(8), nullable=False)
    inscricao_estadual = Column(String(20), nullable=False)
    email = Column(String(50), nullable=False)
    usuarios = relationship('UsuarioLoja', backref=backref('TLoja'))
    estoque = relationship('Estoque', backref=backref('TLoja'))

    def __init__(self, id_loja, razao_social, nome_fantasia, cnpj, logradouro, numero_logradouro, cep, inscricao_estadual, email):
        self.id_loja = id_loja
        self.razao_social = razao_social
        self.nome_fantasia = nome_fantasia
        self.cnpj = cnpj
        self.logradouro = logradouro
        self.numero_logradouro = numero_logradouro
        self.cep = cep
        self.inscricao_estadual = inscricao_estadual
        self.email = email


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
    total_item = Column(Integer, nullable=False)
    id_loja = Column(Integer, ForeignKey('TLoja.id_loja'))
    produtos = relationship("EstoqueProduto", backref=backref('TEstoque'))

    def __init__(self, codigo_lote, total_item, id_loja):
        self.codigo_lote = codigo_lote
        self.total_item = total_item
        self.id_loja = id_loja


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
    preco = Column(Numeric(5,2), nullable=False)
    id_tipo = Column(Integer, ForeignKey('TTipo_Produto.id'))
    tipo = relationship('TipoProduto', backref=backref('TProduto'))
    estoque = relationship('EstoqueProduto', backref=backref('TProduto'))
    kit = relationship('KitProduto', backref=backref('TProduto'))

    def __init__(self, nome_produto, preco_produto, id_tipo):
        self.nome = nome_produto
        self.preco = preco_produto
        self.id_tipo = id_tipo


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
    codigo = Column(String(20), unique=True, nullable=False)
    nome = Column(String(100), nullable=False)
    quantidade = Column(Integer, nullable=False)
    preco = Column(Numeric(5,2), nullable=False)
    data_validade = Column(Date, nullable=False)
    produtos = relationship('KitProduto', backref=backref('TKit'))
    notificacao_kit = relationship('Notificacao', backref=backref('TKit'))

    def __init__(self, codigo, nome, quantidade, preco, data_validade):
        self.codigo = codigo
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco
        self.data_validade = data_validade


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
    fk_id_tipo_notificacao = Column(Integer, ForeignKey('TTipoNotificacao.id'))
    tipo_notificacao = relationship('TipoNotificacao', backref=backref('TNotificacao'))
    notificacao_usuario = relationship('NotificacaoUsuario', backref=backref('TNotificacao'))
    

    def __init__(self, assunto_notificacao, info_notificacao, data_notificacao, fk_id_estoque_produto, fk_id_kit, fk_id_tipo_notificacao):
        self.assunto_notificacao = assunto_notificacao
        self.info_notificacao = info_notificacao
        self.data_notificacao = data_notificacao
        self.fk_id_estoque_produto = fk_id_estoque_produto
        self.fk_id_kit = fk_id_kit
        self.fk_id_tipo_notificacao = fk_id_tipo_notificacao


class TipoNotificacao(Base):
    '''

    CLASSE TipoNotificacao - MAPEIA TABELA TTipo_Notificacao NO BANCO DE DADOS,
    QUE RELACIONA AS NOTIFICAÇÕES DA TABELA TNotificacao COM OS TIPOS DE NOTIFICAÇÃO
  
    @autor: Luciano Gomes Vieira dos Anjos -
    @data: 15/10/2020 -
    @versao: 1.0.0
    '''
    __tablename__ = 'TTipoNotificacao'
    id = Column(Integer, primary_key=True, autoincrement=True)
    tipo = Column(String(30), nullable=False, unique=True)

    def __init__(self, tipo):
        self.tipo = tipo


class NotificacaoUsuario(Base):
    '''

    CLASSE Notificacao - MAPEIA TABELA TNotificacao_Usuario NO BANCO DE DADOS,
    QUE RELACIONA AS NOTIFICAÇÕES DA TABELA TNotificacao COM OS USUÁRIOS CADASTRADOS
    NO TABELA TUsuario
  
    @autor: Luciano Gomes Vieira dos Anjos -
    @data: 15/10/2020 -
    @versao: 1.0.0
    '''
    __tablename__ = 'TNotificacaoUsuario'
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
