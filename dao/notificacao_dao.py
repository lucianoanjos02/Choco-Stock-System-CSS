from database import db_session
from models.notificacao import Notificacao

class NotificacaoDAO:
    '''
        CLASSE NotificacaoDAO - IMPLEMENTA O ACESSO AO BANCO RELACIONADO A CLASSE 
        Notificacao DO MÓDULO models.py QUE MAPEIA A TABELA TNotificacao

        @autor: Luciano Gomes Vieira dos Anjos -
        @data: 01/10/2020 -
        @versao: 1.0.0
    '''
    def __init__(self, db):
        self.__db = db_session
    
    def get_notificacoes(self):
        '''
            METODO QUE RETORNA TODAS AS NOTIFICAÇÕES REGISTRADAS

            @autor: Luciano Gomes Vieira dos Anjos -
            @data: 30/10/2020 -
            @versao: 1.0.0
        '''
        notificacoes = self.__db.query(Notificacao).order_by(Notificacao.data_notificacao.desc()).all()
        self.__db.expunge_all()
        self.__db.close()
        return notificacoes

    def get_notificacoes_data_validade(self):
        '''
            METODO QUE RETORNA TODAS AS NOTIFICAÇÕES DE DATA DE VALIDADE
            REGISTRADAS

            @autor: Luciano Gomes Vieira dos Anjos -
            @data: 10/10/2020 -
            @versao: 1.0.0
        '''
        notificacoes = self.__db.query(Notificacao).filter(Notificacao.fk_id_tipo_notificacao == 1).all()
        self.__db.expunge_all()
        self.__db.close()
        return notificacoes

    def get_notificacao_data_validade(self, fk_id_estoque_produto):
        '''
            METODO QUE RETORNA A NOTIFICAÇÃO DE DATA DE VALIDADE
            REFERENTE À UM PRODUTO ESPECÍFICO

            @autor: Luciano Gomes Vieira dos Anjos -
            @data: 10/10/2020 -
            @versao: 1.0.0
        '''
        notificacoes = self.__db.query(Notificacao).filter(Notificacao.fk_id_estoque_produto, Notificacao.fk_id_tipo_notificacao == 1).first()
        self.__db.expunge_all()
        self.__db.close()
        return notificacoes
    
    def get_notificacoes_quantidade(self):
        '''
            METODO QUE RETORNA TODAS AS NOTIFICAÇÕES DE QUANTIDADE
            REGISTRADAS NO SISTEMA

            @autor: Luciano Gomes Vieira dos Anjos -
            @data: 10/10/2020 -
            @versao: 1.0.0
        '''
        notificacoes = self.__db.query(Notificacao).filter(Notificacao.fk_id_tipo_notificacao == 2).all()
        self.__db.expunge_all()
        self.__db.close()
        return notificacoes
    
    def get_notificacoes_data_validade_kit(self):
        '''
            METODO QUE RETORNA TODAS AS NOTIFICAÇÕES DE DATA DE VALIDADE
            DE KITS REGISTRADAS

            @autor: Luciano Gomes Vieira dos Anjos -
            @data: 30/10/2020 -
            @versao: 1.0.0
        '''
        notificacoes = self.__db.query(Notificacao).filter(Notificacao.fk_id_tipo_notificacao == 3).all()
        self.__db.expunge_all()
        self.__db.close()
        return notificacoes
    
    def get_info_notificacoes_data_validade(self, info_notificacao):
        '''
            METODO QUE RETORNA A INFORMAÇÃO DE NOTIFICAÇÕES
            DE DATA DE VALIDADE REGISTRADA, PASSANDO COMO PARÂMETRO
            A STRING info_notificacao

            @autor: Luciano Gomes Vieira dos Anjos -
            @data: 10/10/2020 -
            @versao: 1.0.0
        '''
        infos_notificacoes = self.__db.query(Notificacao.info_notificacao).filter(Notificacao.fk_id_tipo_notificacao == 1, Notificacao.info_notificacao == info_notificacao).all()
        self.__db.expunge_all()
        self.__db.close()
        infos_notificacoes_list = []
        for info in infos_notificacoes:
            infos_notificacoes_list.append(info[0])
        return infos_notificacoes_list
    
    def get_info_notificacoes_data_validade_kit(self, info_notificacao):
        '''
            METODO QUE RETORNA A INFORMAÇÃO DE NOTIFICAÇÕES
            DE DATA DE VALIDADE DE KITS REGISTRADAS, PASSANDO COMO PARÂMETRO
            A STRING info_notificacao

            @autor: Luciano Gomes Vieira dos Anjos -
            @data: 30/10/2020 -
            @versao: 1.0.0
        '''
        infos_notificacoes = self.__db.query(Notificacao.info_notificacao).filter(Notificacao.fk_id_tipo_notificacao == 3, Notificacao.info_notificacao == info_notificacao).all()
        self.__db.expunge_all()
        self.__db.close()
        infos_notificacoes_list = []
        for info in infos_notificacoes:
            infos_notificacoes_list.append(info[0])
        return infos_notificacoes_list

    def get_info_notificacoes_quantidade(self, info_notificacao):
        '''
            METODO QUE RETORNA A INFORMAÇÃO DE NOTIFICAÇÕES
            DE QUANTIDADE DE PRODUTO REGISTRADA, PASSANDO COMO PARÂMETRO
            A STRING info_notificacao

            @autor: Luciano Gomes Vieira dos Anjos -
            @data: 10/10/2020 -
            @versao: 1.0.0
        '''
        infos_notificacoes = self.__db.query(Notificacao.info_notificacao).filter(Notificacao.fk_id_tipo_notificacao == 2, Notificacao.info_notificacao == info_notificacao).all()
        self.__db.expunge_all()
        self.__db.close()
        infos_notificacoes_list = []
        for info in infos_notificacoes:
            infos_notificacoes_list.append(info[0])
        return infos_notificacoes_list
    
    def get_id_notificacao_email_id_estoque_produto(self, id_estoque):
        '''
            METODO QUE RETORNA O ID DA NOTIFICAÇÃO DE UM DETERMINADO
            PRODUTO EM ESTOQUE, PASSANDO O ID DELE EM ESTOQUE COMO
            PARÂMETRO

            @autor: Luciano Gomes Vieira dos Anjos -
            @data: 10/10/2020 -
            @versao: 1.0.0
        '''
        id_notificacao = self.__db.query(Notificacao.id_notificacao).filter(Notificacao.fk_id_estoque_produto == id_estoque, Notificacao.fk_id_tipo_notificacao == 1).first()
        self.__db.expunge_all()
        self.__db.close()
        return id_notificacao

    def registra_notificacao(self, notificacao):
        '''
            METODO QUE PERSISTE AS INFORMAÇÕES DA NOTIFICAÇÃO NO BANCO

            @autor: Luciano Gomes Vieira dos Anjos -
            @data: 01/10/2020 -
            @versao: 1.0.0
        '''
        try:
            self.__db.add(notificacao)
            self.__db.commit()
        except:
            print("Erro ao registrar notificação")
            self.__db.rollback()
        finally:
            self.__db.close()
        return 'Notificação registrada com sucesso'