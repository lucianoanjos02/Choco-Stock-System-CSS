from database import db_session
from models import Usuario, Permissao, Loja, Produto, Estoque, EstoqueProduto, TipoProduto, Kit, KitProduto, Notificacao, NotificacaoUsuario

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


class PermissaoDAO:
    '''
        CLASSE PermissaoDAO - IMPLEMENTA O ACESSO AO BANCO RELACIONADO A CLASSE 
        Permisssao DO MÓDULO models.py QUE MAPEIA A TABELA TPermissao
        @autor: Luciano Gomes Vieira dos Anjos -
        @data: 07/08/2020 -
        @versao: 1.0.0
    '''
    def __init__(self, db):
        self.__db = db_session
    
    def get_permissoes(self):
        '''
            METODO QUE RETORNA AS PERMISSÕES DE USUÁRIO REGISTRADAS NO BANCO
            @autor: Luciano Gomes Vieira dos Anjos -
            @data: 09/08/2020 -
            @versao: 1.0.0
        '''
        dados_permissoes = self.__db.query(Permissao).all()
        permissoes = []
        for permissao in dados_permissoes:
            permissoes.append(permissao.permissao)
        self.__db.expunge_all()
        self.__db.close()
        return permissoes
    
    def get_id_permissao(self, permissao):
        id_permissao = self.__db.query(Permissao.id_permissao).filter(Permissao.permissao == permissao).first()
        self.__db.expunge_all()
        self.__db.close()
        return id_permissao


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
    
    def get_id_tipo(self, tipo):
        id_tipo = self.__db.query(TipoProduto.id).filter(TipoProduto.tipo == tipo).first()
        self.__db.expunge_all()
        self.__db.close()
        return id_tipo


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
        id_produto = self.__db.query(Produto).filter(Produto.nome == nome_produto).first()
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
