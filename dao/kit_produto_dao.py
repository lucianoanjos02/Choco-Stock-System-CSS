from database import db_session
from models.kit_produto import KitProduto

class KitProdutoDAO:
    '''
        CLASSE KitProdutoDAO - IMPLEMENTA O ACESSO AO BANCO RELACIONADO A CLASSE 
        KitProduto DO MÓDULO models.py QUE MAPEIA A TABELA TKit_Produto
        @autor: Luciano Gomes Vieira dos Anjos -
        @data: 15/09/2020 -
        @versao: 1.0.0
    '''
    def __init__(self, db):
        self.__db = db_session
    
    def get_kit_produtos(self, id_kit):
        '''
            METODO QUE RETORNA OS PRODUTOS CADASTRADOS
            EM UM DETERMINADO KIT, PASSANDO O ID DO KIT 
            COMO PARÂMETRO

            @autor: Luciano Gomes Vieira dos Anjos -
            @data: 05/11/2020 -
            @versao: 1.0.0
        '''
        produtos_kit = self.__db.query(KitProduto.fk_id_produto).filter(KitProduto.fk_id_kit == id_kit).all()
        self.__db.expunge_all()
        self.__db.close()
        return produtos_kit

    def cadastrar_kit_produtos(self, kit_produto):
        '''
            METODO QUE PERSISTE AS INFORMAÇÕES DOS PRODUTOS/KITS NO BANCO
            @autor: Luciano Gomes Vieira dos Anjos -
            @data: 15/09/2020 -
            @versao: 1.0.0
        '''
        try:
            self.__db.add(kit_produto)
            self.__db.commit()
        except:
            print("Erro ao cadastrar produto(s) do kit")
            self.__db.rollback()
        finally:
            self.__db.close()
        return 'Produto(s) do kit cadastrado(s) com sucesso'