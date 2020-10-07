import smtplib
from email.message import EmailMessage
from database import db_session
from dao import EstoqueProdutoDAO, EstoqueDAO, ProdutoDAO, UsuarioDAO
from datetime import datetime, timedelta

def notificacao_email():
    usuario_dao = UsuarioDAO(db_session)
    estoque_dao = EstoqueDAO(db_session)
    estoque_produto_dao = EstoqueProdutoDAO(db_session)
    produto_dao = ProdutoDAO(db_session)

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
