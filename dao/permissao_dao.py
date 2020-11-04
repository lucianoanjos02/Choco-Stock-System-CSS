from database import db_session
from models.permissao import Permissao

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
        self.__db.expunge_all()
        self.__db.close()
        return permissoes
    
    def get_permissao(self, id_permissao):
        permissao = self.__db.query(Permissao.permissao).filter(Permissao.id_permissao == id_permissao).first()
        self.__db.expunge_all()
        self.__db.close()
        return permissao
    
    def get_id_permissao(self, permissao):
        id_permissao = self.__db.query(Permissao.id_permissao).filter(Permissao.permissao == permissao).first()
        self.__db.expunge_all()
        self.__db.close()
        return id_permissao