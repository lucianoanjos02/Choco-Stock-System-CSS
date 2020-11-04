from database import db_session
from models.usuario import Usuario

class UsuarioDAO:
    '''
        CLASSE UsuarioDAO - IMPLEMENTA O ACESSO AO BANCO RELACIONADO A CLASSE 
        Usuario DO MÓDULO models.py QUE MAPEIA A TABELA TUsuario
        @autor: Luciano Gomes Vieira dos Anjos -
        @data: 26/08/2020 -
        @versao: 1.0.0
    '''
    def __init__(self, db):
        self.__db = db_session
    
    def get_usuarios(self):
        '''
            METODO QUE RETORNA AS INFORMAÇÕES DE TODOS OS USUÁRIOS CADASTRADOS
            @autor: Luciano Gomes Vieira dos Anjos -
            @data: 01/11/2020 -
            @versao: 1.0.0
        '''
        usuarios = self.__db.query(Usuario).all()
        self.__db.expunge_all()
        self.__db.close()
        return usuarios
    
    def get_id_usuario(self, id_usuario):
        '''
            METODO QUE RETORNA AS INFORMAÇÕES DE UM USUÁRIO DO BANCO PELO ID DO USUÁRIO
            @autor: Luciano Gomes Vieira dos Anjos -
            @data: 26/08/2020 -
            @versao: 1.0.0
        '''
        usuario = self.__db.query(Usuario).filter(Usuario.id_usuario == id_usuario).first()
        self.__db.expunge_all()
        self.__db.close()
        return usuario
    
    def get_usuario_id(self, login):
        '''
            METODO QUE RETORNA AS INFORMAÇÕES DE UM USUÁRIO DO BANCO PELO ID DO USUÁRIO
            @autor: Luciano Gomes Vieira dos Anjos -
            @data: 26/08/2020 -
            @versao: 1.0.0
        '''
        usuario = self.__db.query(Usuario.id_usuario).filter(Usuario.login == login).first()
        self.__db.expunge_all()
        self.__db.close()
        return usuario

    def get_ids_usuarios(self):
        '''
            METODO QUE RETORNA AS INFORMAÇÕES DE UM USUÁRIO DO BANCO PELO ID DO USUÁRIO
            @autor: Luciano Gomes Vieira dos Anjos -
            @data: 26/08/2020 -
            @versao: 1.0.0
        '''
        usuarios = self.__db.query(Usuario.id_usuario).all()
        self.__db.expunge_all()
        self.__db.close()
        return usuarios
    
    def get_login_usuario(self, login):
        '''
            METODO QUE RETORNA AS INFORMAÇÕES DE UM USUÁRIO DO BANCO PELO LOGIN DO USUÁRIO
            @autor: Luciano Gomes Vieira dos Anjos -
            @data: 26/08/2020 -
            @versao: 1.0.0
        '''
        usuario = self.__db.query(Usuario).filter(Usuario.login == login).first()
        self.__db.expunge_all()
        self.__db.close()
        return usuario
    
    def get_emails(self):
        '''
            METODO QUE RETORNA UMA LISTA DE E-MAILS DOS USUÁRIOS CADASTRADOS NO BANCO
            @autor: Luciano Gomes Vieira dos Anjos -
            @data: 27/09/2020 -
            @versao: 1.0.0
        '''
        emails = self.__db.query(Usuario.email).all()
        lista_emails = []
        for email in emails:
            lista_emails.append(email.email)
        self.__db.expunge_all()
        self.__db.close()
        return lista_emails

    def cadastrar_usuario(self, usuario):
        '''
            METODO QUE PERSISTE AS INFORMAÇÕES DO USUÁRIO NO BANCO
            @autor: Luciano Gomes Vieira dos Anjos -
            @data: 26/08/2020 -
            @versao: 1.0.0
        '''
        try:
            self.__db.add(usuario)
            self.__db.commit()
        except:
            print("Erro ao cadastrar usuário")
            self.__db.rollback()
        finally:
            self.__db.close()
        return 'Usuário cadastrado com sucesso'
    
    def update_infos_usuario(self, id_usuario, nome, sobrenome, email, senha, permissao):
        '''
            METODO QUE ATUALIZA AS INFORMAÇÕES DE UM DETERMINADO USUÁRIO NO SISTEMA

            @autor: Luciano Gomes Vieira dos Anjos -
            @data: 14/09/2020 -
            @versao: 1.0.0
        '''
        try:
            self.__db.query(Usuario).filter(Usuario.id_usuario == id_usuario).update({Usuario.nome: nome, 
                                                                                      Usuario.sobrenome: sobrenome, 
                                                                                      Usuario.email: email,
                                                                                      Usuario.senha: senha,
                                                                                      Usuario.permissao: permissao})
            self.__db.commit()
        except:
            print("Erro ao atualizar as informações do usuário")
            self.__db.rollback()
        finally:
            self.__db.close()
        return 'Informações do usuário atualizadas com sucesso'