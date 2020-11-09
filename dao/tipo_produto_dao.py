from database import db_session
from models.tipo_produto import TipoProduto

class TipoProdutoDAO:
    '''
        CLASSE TipoProdutoDAO - IMPLEMENTA O ACESSO AO BANCO RELACIONADO A CLASSE 
        TipoProduto DO MÓDULO models.py QUE MAPEIA A TABELA TTipoProduto
        @autor: Luciano Gomes Vieira dos Anjos -
        @data: 15/09/2020 -
        @versao: 1.0.0
    '''
    def __init__(self, db):
        self.__db = db_session
    
    def get_tipos_produto(self):
        '''
            METODO QUE RETORNA OS TIPOS DE PRODUTO REGISTRADAS NO BANCO
            @autor: Luciano Gomes Vieira dos Anjos -
            @data: 15/09/2020 -
            @versao: 1.0.0
        '''
        info_tipos_produto = self.__db.query(TipoProduto).all()
        tipos_produto = []
        for tipo in info_tipos_produto:
            tipos_produto.append(tipo.tipo)
        self.__db.expunge_all()
        self.__db.close()
        return tipos_produto
    
    def get_tipo_produto(self, id_tipo):
        '''
            METODO QUE RETORNA O TIPO DE UM PRODUTO REGISTRADO NO BANCO.
            ESSE MÉTODO RECEBE O ID DO PRODUTO COMO PARÂMETRO.
            @autor: Luciano Gomes Vieira dos Anjos -
            @data: 03/10/2020 -
            @versao: 1.0.0
        '''
        tipo_produto = self.__db.query(TipoProduto.tipo).filter(TipoProduto.id == id_tipo).first()
        return tipo_produto
    
    def get_id_tipo(self, tipo):
        id_tipo = self.__db.query(TipoProduto.id).filter(TipoProduto.tipo == tipo).first()
        self.__db.expunge_all()
        self.__db.close()
        return id_tipo