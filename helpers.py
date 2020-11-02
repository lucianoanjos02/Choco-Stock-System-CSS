from flask_login import current_user
import smtplib
from email.message import EmailMessage
from database import db_session
from models import Notificacao, NotificacaoUsuario
from dao import EstoqueProdutoDAO, EstoqueDAO, ProdutoDAO, UsuarioDAO, NotificacaoDAO, NotificacaoUsuarioDAO
from datetime import datetime, timedelta

usuario_dao = UsuarioDAO(db_session)
estoque_dao = EstoqueDAO(db_session)
estoque_produto_dao = EstoqueProdutoDAO(db_session)
produto_dao = ProdutoDAO(db_session)
notificacao_dao = NotificacaoDAO(db_session)
notificacao_usuario_dao = NotificacaoUsuarioDAO(db_session)

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
    MÉTODO HELPER is_admin
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


def atualiza_notificacoes_data_validade():
    produtos_notificacao = []
    usuarios = usuario_dao.get_ids_usuarios()
    produtos = estoque_produto_dao.get_estoque_produtos()
    for produto in produtos:
        data_produto = produto.data_validade
        dias_validade = datetime(data_produto.year, data_produto.month, data_produto.day) - datetime.now()
        if dias_validade.days <= 60:
            produtos_notificacao.append(produto)
    for produto in produtos_notificacao:
        notificacao = Notificacao("Alerta de Data de Validade",
                                  f"Produto: {produto_dao.get_produto(produto.fk_id_produto)[0]} - Lote: {estoque_dao.get_codigo_lote(produto.fk_id_estoque)[0]} - Data de Validade: {produto.data_validade.day}/{produto.data_validade.month}/{produto.data_validade.year}",
                                  datetime.now(),
                                  produto.fk_id_estoque,
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


def atualiza_notificacoes_quantidade_produto():
    produtos_notificacao = []
    usuarios = usuario_dao.get_ids_usuarios()
    produtos = estoque_produto_dao.get_estoque_produtos()
    for produto in produtos:
        if produto.quantidade_produto <= 60:
            produtos_notificacao.append(produto)
    for produto in produtos_notificacao:
        notificacao = Notificacao(f"Alerta de Quantidade de Produto",
                                  f"""Produto: {produto_dao.get_produto(produto.fk_id_produto)[0]} - Lote: {estoque_dao.get_codigo_lote(produto.fk_id_estoque)[0]} - Quantidade: {produto.quantidade_produto}""",
                                  datetime.now(),
                                  produto.fk_id_estoque,
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
    notificacoes = notificacao_dao.get_notificacoes_data_validade()
    for notificacao in notificacoes:
        data_validade = notificacao.info_notificacao.split()
        msg = EmailMessage()
        msg['Subject'] = f'{notificacao.assunto_notificacao} - LOTE {estoque_dao.get_codigo_lote(notificacao.fk_id_estoque_produto)[0]}'
        msg['From'] = 'lucianogvda02@gmail.com'
        msg['To'] = ', '.join(usuario_dao.get_emails())
        msg.set_content(f"{notificacao.info_notificacao}")

        if notificacao_usuario_dao.get_email_enviado(notificacao.id_notificacao) != 1:

            with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                smtp.ehlo()
                smtp.starttls()
                smtp.ehlo()

                smtp.login('lucianogvda02@gmail.com', 'kax7iktv')
                smtp.send_message(msg)
                smtp.quit()

            notificacao_usuario_dao.update_email_enviado(notificacao.id_notificacao)


def notificacao_email_quantidade():
    notificacoes = notificacao_dao.get_notificacoes_quantidade()
    for notificacao in notificacoes:
        data_validade = notificacao.info_notificacao.split()
        msg = EmailMessage()
        msg['Subject'] = f'{notificacao.assunto_notificacao} - LOTE {estoque_dao.get_codigo_lote(notificacao.fk_id_estoque_produto)[0]}'
        msg['From'] = 'lucianogvda02@gmail.com'
        msg['To'] = ', '.join(usuario_dao.get_emails())
        msg.set_content(f"{notificacao.info_notificacao}")

        if notificacao_usuario_dao.get_email_enviado(notificacao.id_notificacao) != 1:

            with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                smtp.ehlo()
                smtp.starttls()
                smtp.ehlo()

                smtp.login('lucianogvda02@gmail.com', 'kax7iktv')
                smtp.send_message(msg)
                smtp.quit()

            notificacao_usuario_dao.update_email_enviado(notificacao.id_notificacao)