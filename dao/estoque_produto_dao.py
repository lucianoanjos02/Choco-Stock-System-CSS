from database import db_session
from models.estoque_produto import EstoqueProduto

class EstoqueProdutoDAO:
    '''
        CLASSE EstoqueProdutoDAO - IMPLEMENTA O ACESSO AO BANCO RELACIONADO A CLASSE 
        EstoqueProduto DO MÓDULO models.py QUE MAPEIA A TABELA TEstoque_Produto
        @autor: Luciano Gomes Vieira dos Anjos -
        @data: 12/09/2020 -
        @versao: 1.0.0
    '''
    def __init__(self, db):
        self.__db = db_session

    def get_estoque_produtos(self):
        '''
            METODO QUE RETORNA AS INFORMAÇÕES DE PRODUTOS CADASTRADOS
            EM ESTOQUE
            @autor: Luciano Gomes Vieira dos Anjos -
            @data: 27/09/2020 -
            @versao: 1.0.0
        '''
        estoque_produtos = self.__db.query(EstoqueProduto).all()
        self.__db.expunge_all()
        self.__db.close()
        return estoque_produtos

    def get_fk_ids_estoque_por_produto(self, id_produto):
        '''
            METODO QUE RETORNA OS IDS DOS ESTOQUES CADASTRADOS NOS LOTES,
            DE ACORDO COM UM DETERMINADO PRODUTO

            @autor: Luciano Gomes Vieira dos Anjos -
            @data: 30/10/2020 -
            @versao: 1.0.0
        '''
        ids_estoque = self.__db.query(EstoqueProduto.fk_id_estoque).filter(EstoqueProduto.fk_id_produto == id_produto).all()
        self.__db.expunge_all()
        self.__db.close()
        return ids_estoque

    def get_quantidade_produtos(self, id_estoque):
        '''
            METODO QUE RETORNA AS QUANTIDADES DOS PRODUTOS CADASTRADOS
            EM UM DETERMINADO LOTE (id_estoque)
            @autor: Luciano Gomes Vieira dos Anjos -
            @data: 14/09/2020 -
            @versao: 1.0.0
        '''
        quantidades_estoque = self.__db.query(EstoqueProduto.quantidade_produto).filter(EstoqueProduto.fk_id_estoque == id_estoque).all()
        self.__db.expunge_all()
        self.__db.close()
        return quantidades_estoque
    
    def cadastrar_estoque_produto(self, estoque_produto):
        '''
            METODO QUE PERSISTE AS INFORMAÇÕES DOS PRODUTOS/ESTOQUE NO BANCO
            @autor: Luciano Gomes Vieira dos Anjos -
            @data: 12/09/2020 -
            @versao: 1.0.0
        '''
        try:
            self.__db.add(estoque_produto)
            self.__db.commit()
        except:
            print("Erro ao cadastrar produto(s) no estoque")
            self.__db.rollback()
        finally:
            self.__db.close()
        return 'Produto(s) cadastrado(s) no estoque com sucesso'
    
    def update_quantidade_produto(self, nova_quantidade, id_produto, id_estoque):
        '''
            METODO QUE ATUALIZA A QUANTIDADE DE UM PRODUTO DE UM LOTE REGISTRADO
            EM ESTOQUE NO BANCO
           
            @autor: Luciano Gomes Vieira dos Anjos -
            @data: 30/10/2020 -
            @versao: 1.0.0
        '''
        try:
            self.__db.query(EstoqueProduto).filter(EstoqueProduto.fk_id_estoque == id_estoque, EstoqueProduto.fk_id_produto == id_produto).update({EstoqueProduto.quantidade_produto: nova_quantidade})
            self.__db.commit()
        except:
            print("Erro ao atualizar quantidade_produto")
            self.__db.rollback()
        finally:
            self.__db.close()
        return 'quantidade_produto atualizada com sucesso'