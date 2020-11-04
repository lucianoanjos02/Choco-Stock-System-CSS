from database import db_session
from models.notificacao_usuario import NotificacaoUsuario

class NotificacaoUsuarioDAO:
    '''
        CLASSE NotificacaoUsuarioDAO - IMPLEMENTA O ACESSO AO BANCO RELACIONADO A CLASSE 
        NotificacaoUsuario DO MÓDULO models.py QUE MAPEIA A TABELA TNotificacaoUsuario

        @autor: Luciano Gomes Vieira dos Anjos -
        @data: 10/10/2020 -
        @versao: 1.0.0
    '''
    def __init__(self, db):
        self.__db = db_session

    def get_fk_id_notificacoes(self):
        '''
            METODO QUE RETORNA TODDOS OS IDs DAS NOTIFICAÇÕES DOS USUÁRIOS

            @autor: Luciano Gomes Vieira dos Anjos -
            @data: 10/10/2020 -
            @versao: 1.0.0
        '''
        fk_id_notificacoes = self.__db.query(NotificacaoUsuario.fk_id_notificacao).all()
        self.__db.expunge_all()
        self.__db.close()
        list_id_notificacao = []
        for id_notificacao in fk_id_notificacoes:
            list_id_notificacao.append(id_notificacao[0])
        return list_id_notificacao
    
    def get_email_enviado(self, id_notificacao):
        '''
            METODO QUE RETORNA O A FLAG email_enviado DE UMA DETERMINADA
            NOTIFICAÇÃO, PASSANDO O ID DA NOTIFICAÇÃO COMO PARÂMETRO

            @autor: Luciano Gomes Vieira dos Anjos -
            @data: 24/10/2020 -
            @versao: 1.0.0
        '''
        email_enviado_notificacao = self.__db.query(NotificacaoUsuario.email_enviado).filter(NotificacaoUsuario.fk_id_notificacao == id_notificacao).first()
        self.__db.expunge_all()
        self.__db.close()
        return email_enviado_notificacao.email_enviado
    
    def get_quantidade_notificacoes_usuario(self, id_usuario):
        '''
            METODO QUE RETORNA A QUANTIDADE DE NOTIFICAÇÕES NÃO VISUALIZADAS
            DE UM DETERMINADO USUÁRIO, UTILIZANDO COMO PARÂMETRO O ID DO USUÁRIO

            @autor: Luciano Gomes Vieira dos Anjos -
            @data: 30/10/2020 -
            @versao: 1.0.0
        '''
        quantidade_notificacoes = self.__db.query(NotificacaoUsuario.id).filter(NotificacaoUsuario.fk_id_usuario == id_usuario, NotificacaoUsuario.visualizada == 0).count()
        return quantidade_notificacoes

    def registra_notificacao_usuario(self, notificacao_usuario):
        '''
            METODO QUE PERSISTE AS INFORMAÇÕES DA NOTIFICAÇÃO DE
            CADA USUÁRIO NO BANCO

            @autor: Luciano Gomes Vieira dos Anjos -
            @data: 10/10/2020 -
            @versao: 1.0.0
        '''
        try:
            self.__db.add(notificacao_usuario)
            self.__db.commit()
        except:
            print("Erro ao registrar notificação do usuário")
            self.__db.rollback()
        finally:
            self.__db.close()
        return 'Notificação do usuário registrada com sucesso'
    
    def update_email_enviado(self, id_notificacao):
        '''
            METODO QUE ATUALIZA A FLAG email_enviado INDICANDO QUE O E-MAIL
            RELACIONADO À DATA DE VALIDADE OU QUANTIDADE PRODUTO FOI ENVIADO

            @autor: Luciano Gomes Vieira dos Anjos -
            @data: 24/10/2020 -
            @versao: 1.0.0
        '''
        try:
            self.__db.query(NotificacaoUsuario).filter(NotificacaoUsuario.fk_id_notificacao == id_notificacao).update({NotificacaoUsuario.email_enviado: 1})
            self.__db.commit()
        except:
            print("Erro ao atualizar email_enviado")
            self.__db.rollback()
        finally:
            self.__db.close()
        return 'email_enviado atualizado com sucesso'
    
    def update_notificacao_visualizada(self, id_usuario):
        '''
            METODO QUE ATUALIZA A FLAG visualizada INDICANDO QUE AS NOTIFICAÇÕES
            JÁ FORAM VISUALIZADAS POR DETERMINADO USUÁRIO DENTRO DO SISTEMA, UTILIZANDO
            O ID DO USUÁRIO COMO PARÂMETRO

            @autor: Luciano Gomes Vieira dos Anjos -
            @data: 31/10/2020 -
            @versao: 1.0.0
        '''
        try:
            self.__db.query(NotificacaoUsuario).filter(NotificacaoUsuario.fk_id_usuario == id_usuario, NotificacaoUsuario.visualizada == 0).update({NotificacaoUsuario.visualizada: 1})
            self.__db.commit()
        except:
            print("Erro ao atualizar que a notificação foi atualizada")
            self.__db.rollback()
        finally:
            self.__db.close()
        return 'Notificação visualizada atualizada com sucesso'