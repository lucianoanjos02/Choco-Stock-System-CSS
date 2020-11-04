from database import db_session
from models.loja import Loja

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
        self.__db.expunge_all()
        self.__db.close()
        return lojas

    def cadastrar_loja(self, loja):
        '''
            METODO QUE PERSISTE AS INFORMAÇÕES DA LOJA NO BANCO
            @autor: Luciano Gomes Vieira dos Anjos -
            @data: 15/09/2020 -
            @versao: 1.0.0
        '''
        try:
            self.__db.add(loja)
            self.__db.commit()
        except:
            print("Erro ao cadastrar loja")
            self.__db.rollback()
        finally:
            self.__db.close()
        return 'Loja cadastrada com sucesso'