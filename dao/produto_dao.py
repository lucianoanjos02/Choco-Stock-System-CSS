from database import db_session
from models.produto import Produto

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
    
    def get_produto(self, id_produto):
        '''
            METODO QUE RETORNA O NOME DO PRODUTO REGISTRADAS NO BANCO.
            ESSE MÉTODO UTILIZA O ID DO PRODUTO COMO PARÂMETRO
            @autor: Luciano Gomes Vieira dos Anjos -
            @data: 09/08/2020 -
            @versao: 1.0.0
        '''
        produto = self.__db.query(Produto.nome).filter(Produto.id_produto == id_produto).first()
        self.__db.expunge_all()
        self.__db.close()
        return produto
    
    def get_produtos(self):
        '''
            METODO QUE RETORNA UMA LISTA DE NOMES DOS PRODUTOS REGISTRADAS NO BANCO
            @autor: Luciano Gomes Vieira dos Anjos -
            @data: 09/08/2020 -
            @versao: 1.0.0
        '''
        dados_produtos = self.__db.query(Produto).all()
        produtos = []
        for produto in dados_produtos:
            produtos.append(produto.nome)
        self.__db.expunge_all()
        self.__db.close()
        return produtos
    
    def get_id_produto(self, nome_produto):
        '''
            METODO QUE RETORNA O ID DO PRODUTO REGISTRADO NO BANCO
            @autor: Luciano Gomes Vieira dos Anjos -
            @data: 12/09/2020 -
            @versao: 1.0.0
        '''
        id_produto = self.__db.query(Produto.id_produto).filter(Produto.nome == nome_produto).first()
        self.__db.expunge_all()
        self.__db.close()
        return id_produto.id_produto
    
    def cadastrar_produto(self, produto):
        '''
            METODO QUE PERSISTE AS INFORMAÇÕES DO PRODUTO NO BANCO
            @autor: Luciano Gomes Vieira dos Anjos -
            @data: 15/09/2020 -
            @versao: 1.0.0
        '''
        try:
            self.__db.add(produto)
            self.__db.commit()
        except:
            print("Erro ao cadastrar produto")
            self.__db.rollback()
        finally:
            self.__db.close()
        return 'Produto cadastrado com sucesso'