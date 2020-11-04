from database import db_session
from models.estoque import Estoque

class EstoqueDAO:
    '''
        CLASSE EstoqueDAO - IMPLEMENTA O ACESSO AO BANCO RELACIONADO A CLASSE 
        Estoque DO MÓDULO models.py QUE MAPEIA A TABELA TEstoque
        @autor: Luciano Gomes Vieira dos Anjos -
        @data: 09/08/2020 -
        @versao: 1.0.0
    '''
    def __init__(self, db):
        self.__db = db_session
    
    def cadastrar_estoque(self, estoque):
        '''
            METODO QUE PERSISTE AS INFORMAÇÕES DO ESTOQUE NO BANCO
            @autor: Luciano Gomes Vieira dos Anjos -
            @data: 12/09/2020 -
            @versao: 1.0.0
        '''
        try:
            self.__db.add(estoque)
            self.__db.commit()
        except:
            print("Erro ao cadastrar estoque")
            self.__db.rollback()
        finally:
            self.__db.close()
        return 'Estoque cadastrado com sucesso'
    
    def get_estoques(self):
        '''
            METODO QUE RETORNA AS INFORMAÇÕES LOTES CADASTRADOS
            EM ESTOQUE
            @autor: Luciano Gomes Vieira dos Anjos -
            @data: 01/10/2020 -
            @versao: 1.0.0
        '''
        estoque = self.__db.query(Estoque).all()
        self.__db.expunge_all()
        self.__db.close()
        return estoque
    
    def get_estoques_por_codigo_lote(self, codigo_lote):
        '''
            METODO QUE RETORNA AS INFORMAÇÕES LOTES CADASTRADOS
            EM ESTOQUE COM UM NÚMERO DE LOTE ESPECÍFICO, PASSADO
            COMO PARÂMETRO DO MÉTODO
            @autor: Luciano Gomes Vieira dos Anjos -
            @data: 30/10/2020 -
            @versao: 1.0.0
        '''
        estoque = self.__db.query(Estoque).filter(Estoque.codigo_lote == codigo_lote).all()
        self.__db.expunge_all()
        self.__db.close()
        return estoque
    
    def get_estoques_por_loja(self, id_loja):
        '''
            METODO QUE RETORNA AS INFORMAÇÕES LOTES CADASTRADOS
            EM ESTOQUE DE UMA LOJA ESPECÍFICA, PASSADA
            COMO PARÂMETRO DO MÉTODO
            @autor: Luciano Gomes Vieira dos Anjos -
            @data: 30/10/2020 -
            @versao: 1.0.0
        '''
        estoque = self.__db.query(Estoque).filter(Estoque.id_loja == id_loja).all()
        self.__db.expunge_all()
        self.__db.close()
        return estoque
    
    def get_estoques_por_id_estoque(self, id_estoque):
        '''
            METODO QUE RETORNA AS INFORMAÇÕES LOTES CADASTRADOS
            EM ESTOQUE, PASSANDO UM DETERMINADO ID DE ESTQOUE CADASTRADO
            COMO PARÂMETRO DO MÉTODO
            @autor: Luciano Gomes Vieira dos Anjos -
            @data: 30/10/2020 -
            @versao: 1.0.0
        '''
        estoque = self.__db.query(Estoque).filter(Estoque.id_estoque == id_estoque).all()
        self.__db.expunge_all()
        self.__db.close()
        return estoque
    
    def get_id_estoque(self, codigo_lote):
        '''
            METODO QUE RETORNA O ID DO ESTOQUE.
            ESSE MÉTODO RECEBE O CÓDIGO DO LOTE CADASTRADO NO SISTEMA
            COMO PARÂMETRO
            @autor: Luciano Gomes Vieira dos Anjos -
            @data: 30/10/2020 -
            @versao: 1.0.0
        '''
        codigo_lote = self.__db.query(Estoque.id_estoque).filter(Estoque.codigo_lote == codigo_lote).first()
        self.__db.expunge_all()
        self.__db.close()
        return codigo_lote
    
    def get_codigo_lote(self, id_estoque):
        '''
            METODO QUE RETORNA O CÓDIGO DO LOTE.
            ESSE MÉTODO RECEBE O ID DO ESTOQUE CADASTRADO NO SISTEMA
            COMO PARÂMETRO
            @autor: Luciano Gomes Vieira dos Anjos -
            @data: 27/09/2020 -
            @versao: 1.0.0
        '''
        codigo_lote = self.__db.query(Estoque.codigo_lote).filter(Estoque.id_estoque == id_estoque).first()
        self.__db.expunge_all()
        self.__db.close()
        return codigo_lote
    
    def get_ultimo_estoque_id(self):
        '''
            METODO QUE RETORNA O ID DO ÚLTIMO LOTE DO ESTOQUE CADASTRADO NO SISTEMA
            @autor: Luciano Gomes Vieira dos Anjos -
            @data: 14/09/2020 -
            @versao: 1.0.0
        '''
        estoque = self.__db.query(Estoque).order_by(Estoque.id_estoque.desc()).first()
        self.__db.expunge_all()
        self.__db.close()
        return estoque.id_estoque
    
    def update_total_item(self, novo_total, id_estoque):
        '''
            METODO QUE ATUALIZA A QUANTIDADE TOTAL DE PRODUTOS DO ESTOQUE NO BANCO
            DE ACORDO COM A QUANTIDADE REGISTRADA DE CADA PRODUTO, APÓS FEITO O CADASTRO
            DO LOTE
            @autor: Luciano Gomes Vieira dos Anjos -
            @data: 14/09/2020 -
            @versao: 1.0.0
        '''
        try:
            self.__db.query(Estoque).filter(Estoque.id_estoque == id_estoque).update({Estoque.total_item: novo_total})
            self.__db.commit()
        except:
            print("Erro ao atualizar total_item")
            self.__db.rollback()
        finally:
            self.__db.close()
        return 'total_item atualizado com sucesso'