from flask_login import current_user
import smtplib
from email.message import EmailMessage
from database import db_session
from models.notificacao import Notificacao
from models.notificacao_usuario import NotificacaoUsuario
from dao.estoque_produto_dao import EstoqueProdutoDAO
from dao.estoque_dao import EstoqueDAO
from dao.produto_dao import ProdutoDAO
from dao.usuario_dao import UsuarioDAO
from dao.notificacao_dao import NotificacaoDAO
from dao.notificacao_usuario_dao import NotificacaoUsuarioDAO
from dao.kit_dao import KitDAO
from datetime import datetime, timedelta

usuario_dao = UsuarioDAO(db_session)
estoque_dao = EstoqueDAO(db_session)
estoque_produto_dao = EstoqueProdutoDAO(db_session)
produto_dao = ProdutoDAO(db_session)
notificacao_dao = NotificacaoDAO(db_session)
notificacao_usuario_dao = NotificacaoUsuarioDAO(db_session)
kit_dao = KitDAO(db_session)

'''
----------------------------------------------------------------
---- MÓDULO DE IMPLEMENTAÇÃO DE MÉTODOS AUXILIARES (HELPERS)----
----------------------------------------------------------------
@autor: Luciano Gomes Vieira dos Anjos -
@data: 27/08/2020 -
@versao: 1.0.0
'''

def is_admin(usuario):
    '''
    FUNÇÃO HELPER is_admin
    - Recebe como parâmetro um usuário, que utilizamos para 
    verificar se esse usuário é Administrador ou não, baseado
    no id_permissao do usuário cadastrado no banco.

    -Caso o usuário logado tenha o id_permissão diferente de 1
    (1 = Administrador, 2 = Operador), o método retorna False,
    caso contrário, o método retorna True.

    @autor: Luciano Gomes Vieira dos Anjos -
    @data: 26/08/2020 -
    @versao: 1.0.0
    '''
    if usuario.id_permissao != 1:
        return False
    return True


def atualiza_notificacoes_data_validade_produto():
    '''
    FUNÇÃO HELPER atualiza_notificacoes_data_validade_produto

    - Função responsável por popular as informações de notificações relacionadas
    à data de validade dos produtos em estoque no sistema, para cada
    usuário cadastrado.

    - As informações/notificações só são registradas para os usuários caso o vencimento de
    determinado produto em determinado lote no estoque, esteja a 60 dias ou menos.

    @autor: Luciano Gomes Vieira dos Anjos -
    @data: 01/11/2020 -
    @versao: 1.0.0
    '''
    produtos_notificacao = []
    usuarios = usuario_dao.get_ids_usuarios()
    produtos = estoque_produto_dao.get_estoque_produtos()
    for produto in produtos:
        data_produto = produto.data_validade
        dias_validade = datetime(data_produto.year, data_produto.month, data_produto.day) - datetime.now()
        if dias_validade.days <= 60:
            produtos_notificacao.append(produto)
    for produto in produtos_notificacao:
        notificacao = Notificacao("Alerta de Data de Validade - Produto",
                                  f"Produto: {produto_dao.get_produto(produto.fk_id_produto)[0]} - Lote: {estoque_dao.get_codigo_lote(produto.fk_id_estoque)[0]} - Data de Validade: {produto.data_validade.day}/{produto.data_validade.month}/{produto.data_validade.year}",
                                  datetime.now(),
                                  produto.fk_id_estoque,
                                  None,
                                  1)
        info_notificacoes = notificacao_dao.get_info_notificacoes_data_validade(notificacao.info_notificacao)
        if info_notificacoes == None or notificacao.info_notificacao not in info_notificacoes:
            notificacao_dao.registra_notificacao(notificacao)
    notificacoes = notificacao_dao.get_notificacoes_data_validade()
    ids_notificacoes_usuario = notificacao_usuario_dao.get_fk_id_notificacoes()
    for usuario in usuarios:
        for notificacao in notificacoes:
            if notificacao.id_notificacao not in ids_notificacoes_usuario:
                notificacao_usuario = NotificacaoUsuario(notificacao.id_notificacao,
                                                         usuario[0],
                                                         0,
                                                         0)
                notificacao_usuario_dao.registra_notificacao_usuario(notificacao_usuario)


def atualiza_notificacoes_data_validade_kit():
    '''
    FUNÇÃO HELPER atualiza_notificacoes_data_validade_kit

    - Função responsável por popular as informações de notificações relacionadas
    à data de validade dos kits em estoque no sistema, para cada
    usuário cadastrado.

    - As informações/notificações só são registradas para os usuários caso o vencimento de
    determinado kit no estoque, esteja a 30 dias ou menos.

    @autor: Luciano Gomes Vieira dos Anjos -
    @data: 01/11/2020 -
    @versao: 1.0.0
    '''
    kits_notificacao = []
    usuarios = usuario_dao.get_ids_usuarios()
    kits = kit_dao.get_kits()
    for kit in kits:
        data_kit = kit.data_validade
        dias_validade = datetime(data_kit.year, data_kit.month, data_kit.day) - datetime.now()
        if dias_validade.days <= 30:
            kits_notificacao.append(kit)
    for kit in kits_notificacao:
        notificacao = Notificacao("Alerta de Data de Validade - Kit",
                                  f"Kit: {kit.nome} - Código: {kit.codigo} - Data de Validade: {kit.data_validade.day}/{kit.data_validade.month}/{kit.data_validade.year}",
                                  datetime.now(),
                                  None,
                                  kit.id_kit,
                                  3)
        info_notificacoes = notificacao_dao.get_info_notificacoes_data_validade_kit(notificacao.info_notificacao)
        if info_notificacoes == None or notificacao.info_notificacao not in info_notificacoes:
            notificacao_dao.registra_notificacao(notificacao)
    notificacoes = notificacao_dao.get_notificacoes_data_validade_kit()
    ids_notificacoes_usuario = notificacao_usuario_dao.get_fk_id_notificacoes()
    for usuario in usuarios:
        for notificacao in notificacoes:
            if notificacao.id_notificacao not in ids_notificacoes_usuario:
                notificacao_usuario = NotificacaoUsuario(notificacao.id_notificacao,
                                                         usuario[0],
                                                         0,
                                                         0)
                notificacao_usuario_dao.registra_notificacao_usuario(notificacao_usuario)


def atualiza_notificacoes_quantidade_produto():
    '''
    FUNÇÃO HELPER atualiza_notificacoes_quantidade_produto

    - Função responsável por popular as informações de notificações relacionadas
    à quantidade de produto em estoque no sistema, para cada
    usuário cadastrado.

    - As informações/notificações só são registradas para os usuários caso a quantidade atual do produto
    no lote esteja em 30% ou menos da quantidade total inicial de quando o lote desse produto foi cadastrado.

    @autor: Luciano Gomes Vieira dos Anjos -
    @data: 01/11/2020 -
    @versao: 1.0.0
    '''
    produtos_notificacao = []
    usuarios = usuario_dao.get_ids_usuarios()
    produtos = estoque_produto_dao.get_estoque_produtos()
    for produto in produtos:
        if produto.quantidade_produto <= produto.total_produto * 0.3:
            produtos_notificacao.append(produto)
    for produto in produtos_notificacao:
        notificacao = Notificacao(f"Alerta de Quantidade de Produto",
                                  f"""Produto: {produto_dao.get_produto(produto.fk_id_produto)[0]} - Lote: {estoque_dao.get_codigo_lote(produto.fk_id_estoque)[0]} - Quantidade: {produto.quantidade_produto}""",
                                  datetime.now(),
                                  produto.fk_id_estoque,
                                  None,
                                  2)
        info_notificacoes = notificacao_dao.get_info_notificacoes_quantidade(notificacao.info_notificacao)
        if info_notificacoes == None or notificacao.info_notificacao not in info_notificacoes:
            notificacao_dao.registra_notificacao(notificacao)
    notificacoes = notificacao_dao.get_notificacoes_quantidade()
    ids_notificacoes_usuario = notificacao_usuario_dao.get_fk_id_notificacoes()
    for usuario in usuarios:
        for notificacao in notificacoes:
            if notificacao.id_notificacao not in ids_notificacoes_usuario:
                notificacao_usuario = NotificacaoUsuario(notificacao.id_notificacao,
                                                         usuario[0],
                                                         0,
                                                         0)
                notificacao_usuario_dao.registra_notificacao_usuario(notificacao_usuario)


def notificacao_email_data_validade():
    '''
    FUNÇÃO HELPER notificacao_email_data_validade

    - Essa função é responsável por enviar para os e-mails dos usuários cadastrados, notificações
    referente à data de validade dos produtos.

    - O envio apenas ocorre caso a flag de email_enviado do usuário na tabela TNotificao_Usuario esteja
    igual a 0.

    - Após o envio do e-mail, a flag email_enviado do usuário é alterada para 1.

    @autor: Luciano Gomes Vieira dos Anjos -
    @data: 01/11/2020 -
    @versao: 1.0.0
    '''
    notificacoes = notificacao_dao.get_notificacoes_data_validade()
    for notificacao in notificacoes:
        data_validade = notificacao.info_notificacao.split()
        msg = EmailMessage()
        msg['Subject'] = f'{notificacao.assunto_notificacao} - LOTE {estoque_dao.get_codigo_lote(notificacao.fk_id_estoque_produto)[0]}'
        msg['From'] = 'alertas.estoque.css@gmail.com'
        msg['To'] = ', '.join(usuario_dao.get_emails())
        msg.set_content(f"{notificacao.info_notificacao}")

        if notificacao_usuario_dao.get_email_enviado(notificacao.id_notificacao) != 1:

            with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                smtp.ehlo()
                smtp.starttls()
                smtp.ehlo()

                smtp.login('alertas.estoque.css@gmail.com', 'adsimpacta@2019')
                smtp.send_message(msg)
                smtp.quit()

            notificacao_usuario_dao.update_email_enviado(notificacao.id_notificacao)


def notificacao_email_data_validade_kit():
    '''
    FUNÇÃO HELPER notificacao_email_data_validade_kit

    - Essa função é responsável por enviar para os e-mails dos usuários cadastrados, notificações
    referente à data de validade dos kits.

    - O envio apenas ocorre caso a flag de email_enviado do usuário na tabela TNotificao_Usuario esteja
    igual a 0.

    - Após o envio do e-mail, a flag email_enviado do usuário é alterada para 1.

    @autor: Luciano Gomes Vieira dos Anjos -
    @data: 01/11/2020 -
    @versao: 1.0.0
    '''
    notificacoes = notificacao_dao.get_notificacoes_data_validade_kit()
    for notificacao in notificacoes:
        info_notificacao = notificacao.info_notificacao.split()
        msg = EmailMessage()
        msg['Subject'] = f'{notificacao.assunto_notificacao} - CÓDIGO {kit_dao.get_codigo_kit(notificacao.fk_id_kit)[0]}'
        msg['From'] = 'alertas.estoque.css@gmail.com'
        msg['To'] = ', '.join(usuario_dao.get_emails())
        msg.set_content(f"{notificacao.info_notificacao}")

        if notificacao_usuario_dao.get_email_enviado(notificacao.id_notificacao) != 1:

            with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                smtp.ehlo()
                smtp.starttls()
                smtp.ehlo()

                smtp.login('alertas.estoque.css@gmail.com', 'adsimpacta@2019')
                smtp.send_message(msg)
                smtp.quit()

            notificacao_usuario_dao.update_email_enviado(notificacao.id_notificacao)


def notificacao_email_quantidade():
    '''
    FUNÇÃO HELPER notificacao_email_quantidade

    - Essa função é responsável por enviar para os e-mails dos usuários cadastrados, notificações
    referente à quantidade dos produtos.

    - O envio apenas ocorre caso a flag de email_enviado do usuário na tabela TNotificao_Usuario esteja
    igual a 0.

    - Após o envio do e-mail, a flag email_enviado do usuário é alterada para 1.

    @autor: Luciano Gomes Vieira dos Anjos -
    @data: 01/11/2020 -
    @versao: 1.0.0
    '''
    notificacoes = notificacao_dao.get_notificacoes_quantidade()
    for notificacao in notificacoes:
        data_validade = notificacao.info_notificacao.split()
        msg = EmailMessage()
        msg['Subject'] = f'{notificacao.assunto_notificacao} - LOTE {estoque_dao.get_codigo_lote(notificacao.fk_id_estoque_produto)[0]}'
        msg['From'] = 'alertas.estoque.css@gmail.com'
        msg['To'] = ', '.join(usuario_dao.get_emails())
        msg.set_content(f"{notificacao.info_notificacao}")

        if notificacao_usuario_dao.get_email_enviado(notificacao.id_notificacao) != 1:

            with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                smtp.ehlo()
                smtp.starttls()
                smtp.ehlo()

                smtp.login('alertas.estoque.css@gmail.com', 'adsimpacta@2019')
                smtp.send_message(msg)
                smtp.quit()

            notificacao_usuario_dao.update_email_enviado(notificacao.id_notificacao)
