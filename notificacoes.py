import smtplib
from email.message import EmailMessage
from database import db_session
from models import Notificacao
from dao import EstoqueProdutoDAO, EstoqueDAO, ProdutoDAO, UsuarioDAO, NotificacaoDAO
from datetime import datetime, timedelta

usuario_dao = UsuarioDAO(db_session)
estoque_dao = EstoqueDAO(db_session)
estoque_produto_dao = EstoqueProdutoDAO(db_session)
produto_dao = ProdutoDAO(db_session)
notificacao_dao = NotificacaoDAO(db_session)


def atualiza_notificacoes_data_validade():
    produtos_notificacao = []
    produtos = estoque_produto_dao.get_estoque_produtos()
    for produto in produtos:
        data_produto = produto.data_validade
        dias_validade = datetime(data_produto.year, data_produto.month, data_produto.day) - datetime.now()
        if dias_validade.days <= 60:
            produtos_notificacao.append(produto)
    for produto in produtos_notificacao:
        notificacao = Notificacao(f"Alerta de Data de Validade",
                                  f"Produto: {produto_dao.get_produto(produto.fk_id_produto)[0]} - Lote: {estoque_dao.get_codigo_lote(produto.fk_id_estoque)[0]} - Data de Validade: {produto.data_validade.day}/{produto.data_validade.month}/{produto.data_validade.year}",
                                  datetime.now(),
                                  produto.id,
                                  1)
        notificacao_dao.registra_notificacao(notificacao)


def atualiza_notificacoes_quantidade_produto():
    produtos_notificacao = []
    produtos = estoque_produto_dao.get_estoque_produtos()
    for produto in produtos:
        if produto.quantidade_produto <= 60:
            produtos_notificacao.append(produto)
    for produto in produtos_notificacao:
        notificacao = Notificacao(f"Alerta de Quantidade de Produto",
                                  f"""Produto: {produto_dao.get_produto(produto.fk_id_produto)[0]} - 
                                  Lote: {estoque_dao.get_codigo_lote(produto.fk_id_estoque)[0]} - 
                                  Quantidade: {produto.quantidade_produto}""",
                                  datetime.now(),
                                  produto.id,
                                  2)
        notificacao_dao.registra_notificacao(notificacao)


def notificacao_email_data_validade():
    produtos_alerta = []
    produtos = estoque_produto_dao.get_estoque_produtos()
    for produto in produtos:
        data_produto = produto.data_validade
        dias_validade = datetime(data_produto.year, data_produto.month, data_produto.day) - datetime.now()
        if dias_validade.days <= 60:
            produtos_alerta.append(produto)

    for produto in produtos_alerta:
        msg = EmailMessage()
        msg['Subject'] = f'ALERTA DE VENCIMENTO DE PRODUTOS - LOTE {estoque_dao.get_codigo_lote(produto.fk_id_estoque)[0]}'
        msg['From'] = 'lucianogvda02@gmail.com'
        msg['To'] = ', '.join(usuario_dao.get_emails())
        msg.set_content(f"""\
        Lote: {estoque_dao.get_codigo_lote(produto.fk_id_estoque)[0]}
        Produto: {produto_dao.get_produto(produto.fk_id_produto)[0]}
        Data de Validadde: {f"{produto.data_validade.day}/{produto.data_validade.month}/{produto.data_validade.year}"}
        """)

        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()

            smtp.login('lucianogvda02@gmail.com', 'kax7iktv')
            smtp.send_message(msg)
            smtp.quit()
