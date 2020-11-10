from database import db_session
from models.kit import Kit

class KitDAO:
    '''
        CLASSE KitDAO - IMPLEMENTA O ACESSO AO BANCO RELACIONADO A CLASSE 
        Kit DO MÓDULO models.py QUE MAPEIA A TABELA TKit
        @autor: Luciano Gomes Vieira dos Anjos -
        @data: 15/09/2020 -
        @versao: 1.0.0
    '''
    def __init__(self, db):
        self.__db = db_session
    
    def cadastrar_kit(self, kit):
        '''
            METODO QUE PERSISTE AS INFORMAÇÕES DO KIT NO BANCO
            @autor: Luciano Gomes Vieira dos Anjos -
            @data: 15/09/2020 -
            @versao: 1.0.0
        '''
        try:
            self.__db.add(kit)
            self.__db.commit()
        except:
            print("Erro ao cadastrar kit")
            self.__db.rollback()
        finally:
            self.__db.close()
        return 'Kit cadastrado com sucesso'
    
    def get_ultimo_kit_id(self):
        '''
            METODO QUE RETORNA O ID DO ÚLTIMO KIT CADASTRADO NO SISTEMA
            @autor: Luciano Gomes Vieira dos Anjos -
            @data: 15/09/2020 -
            @versao: 1.0.0
        '''
        kit = self.__db.query(Kit).order_by(Kit.id_kit.desc()).first()
        self.__db.expunge_all()
        self.__db.close()
        return kit.id_kit
    
    def get_kits(self):
        '''
            METODO QUE RETORNA AS INFORMAÇÕES DE KITS CADASTRADOS
            EM ESTOQUE
            @autor: Luciano Gomes Vieira dos Anjos -
            @data: 27/09/2020 -
            @versao: 1.0.0
        '''
        kits = self.__db.query(Kit).all()
        self.__db.expunge_all()
        self.__db.close()
        return kits
    
    def get_codigo_kit(self, id_kit):
        '''
            METODO QUE RETORNA O CÓDIGO DO KIT.
            ESSE MÉTODO RECEBE O ID DO KIT CADASTRADO NO SISTEMA
            COMO PARÂMETRO
            @autor: Luciano Gomes Vieira dos Anjos -
            @data: 30/10/2020 -
            @versao: 1.0.0
        '''
        codigo_kit = self.__db.query(Kit.codigo).filter(Kit.id_kit == id_kit).first()
        self.__db.expunge_all()
        self.__db.close()
        return codigo_kit
    
    def get_pesquisa_codigo(self, codigo):
        '''
            METODO QUE RETORNA UM KIT, RECEBENDO COMO PARÂMETRO
            O CÓDIGO DE UM KIT

            @autor: Luciano Gomes Vieira dos Anjos -
            @data: 05/11/2020 -
            @versao: 1.0.0
        '''
        kit = self.__db.query(Kit).filter(Kit.codigo == codigo).first()
        self.__db.expunge_all()
        self.__db.close()
        return kit
    
    def get_pesquisa_nome(self, nome):
        '''
            METODO QUE RETORNA UM KIT, RECEBENDO COMO PARÂMETRO
            O NOME DE UM KIT

            @autor: Luciano Gomes Vieira dos Anjos -
            @data: 05/11/2020 -
            @versao: 1.0.0
        '''
        kit = self.__db.query(Kit).filter(Kit.nome == nome).first()
        self.__db.expunge_all()
        self.__db.close()
        return kit
    
    def update_quantidade_produto(self, id_kit, quantidade):
        '''
            METODO QUE ATUALIZA A QUANTIDADE DE UM KIT

            @autor: Luciano Gomes Vieira dos Anjos -
            @data: 05/11/2020 -
            @versao: 1.0.0
        '''
        try:
            self.__db.query(Kit).filter(Kit.id_kit == id_kit).update({Kit.quantidade: quantidade})
            self.__db.commit()
        except:
            print("Erro ao atualizar a quantidade do kit")
            self.__db.rollback()
        finally:
            self.__db.close()
        return 'Quantidade do kit atualizada com sucesso'