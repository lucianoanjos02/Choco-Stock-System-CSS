from database import db_session
from models import Usuario, Permissao, Loja, Produto

class UsuarioDAO:
    '''
        CLASSE UsuarioDAO - IMPLEMENTA O ACESSO AO BANCO RELACIONADO A CLASSE 
        Usuario DO MÓDULO models.py QUE MAPEIA A TABELA TUsuario

        @autor: Luciano Gomes Vieira dos Anjos -
        @data: 26/08/2020 -
        @versao: 1.0.0
    '''
    def __init__(self, db):
        self.__db = db_session
    
    def get_id_usuario(self, id_usuario):
        '''
            METODO QUE RETORNA AS INFORMAÇÕES DE UM USUÁRIO DO BANCO PELO ID DO USUÁRIO

            @autor: Luciano Gomes Vieira dos Anjos -
            @data: 26/08/2020 -
            @versao: 1.0.0
        '''
        usuario = self.__db.query(Usuario).filter(Usuario.id_usuario == id_usuario).first()
        return usuario
    
    def get_login_usuario(self, login):
        '''
            METODO QUE RETORNA AS INFORMAÇÕES DE UM USUÁRIO DO BANCO PELO LOGIN DO USUÁRIO

            @autor: Luciano Gomes Vieira dos Anjos -
            @data: 26/08/2020 -
            @versao: 1.0.0
        '''
        usuario = self.__db.query(Usuario).filter(Usuario.login == login).first()
        return usuario

    def cadastrar_usuario(self, usuario):
        '''
            METODO QUE PERSISTE AS INFORMAÇÕES DO USUÁRIO NO BANCO

            @autor: Luciano Gomes Vieira dos Anjos -
            @data: 26/08/2020 -
            @versao: 1.0.0
        '''
        try:
            self.__db.add(usuario)
            self.__db.commit()
        except:
            print("Erro ao cadastrar usuário")
            self.__db.rollback()
        finally:
            self.__db.close()
        return 'Usuário cadastrado com sucesso'


class PermissaoDAO:
    '''
        CLASSE PermissaoDAO - IMPLEMENTA O ACESSO AO BANCO RELACIONADO A CLASSE 
        Permisssao DO MÓDULO models.py QUE MAPEIA A TABELA TPermissao

        @autor: Luciano Gomes Vieira dos Anjos -
        @data: 07/08/2020 -
        @versao: 1.0.0
    '''
    def __init__(self, db):
        self.__db = db_session
    
    def get_permissoes(self):
        '''
            METODO QUE RETORNA AS PERMISSÕES DE USUÁRIO REGISTRADAS NO BANCO

            @autor: Luciano Gomes Vieira dos Anjos -
            @data: 09/08/2020 -
            @versao: 1.0.0
        '''
        dados_permissoes = self.__db.query(Permissao).all()
        permissoes = []
        for permissao in dados_permissoes:
            permissoes.append(permissao.permissao)
        return permissoes


class LojaDAO:
    '''
        CLASSE LojaDAO - IMPLEMENTA O ACESSO AO BANCO RELACIONADO A CLASSE 
        Loja DO MÓDULO models.py QUE MAPEIA A TABELA TLoja

        @autor: Luciano Gomes Vieira dos Anjos -
        @data: 09/08/2020 -
        @versao: 1.0.0
    '''
    def __init__(self, db):
        self.__db = db_session
    
    def get_lojas(self):
        '''
            METODO QUE RETORNA O CÓDIGO (ID) DAS LOJAS REGISTRADAS NO BANCO

            @autor: Luciano Gomes Vieira dos Anjos -
            @data: 09/08/2020 -
            @versao: 1.0.0
        '''
        dados_lojas = self.__db.query(Loja).all()
        lojas = []
        for loja in dados_lojas:
            lojas.append(loja.id_loja)
        return lojas


class ProdutoDAO:
    '''
        CLASSE ProdutoDAO - IMPLEMENTA O ACESSO AO BANCO RELACIONADO A CLASSE 
        Produto DO MÓDULO models.py QUE MAPEIA A TABELA TProduto

        @autor: Luciano Gomes Vieira dos Anjos -
        @data: 09/08/2020 -
        @versao: 1.0.0
    '''
    def __init__(self, db):
        self.__db = db_session
    
    def get_produtos(self):
        '''
            METODO QUE RETORNA O NOME DOS PRODUTOS REGISTRADAS NO BANCO

            @autor: Luciano Gomes Vieira dos Anjos -
            @data: 09/08/2020 -
            @versao: 1.0.0
        '''
        dados_produtos = self.__db.query(Produto).all()
        produtos = []
        for produto in dados_produtos:
            produtos.append(produto.nome)
        return produtos
