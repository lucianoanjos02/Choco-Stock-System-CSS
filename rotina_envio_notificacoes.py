import schedule
import time
from notificacoes import notificacao_email

def envia_notificao_email():
    schedule.every().sunday.at("12:00").do(notificacao_email)

    while True:
        schedule.run_pending()
        time.sleep(86400)
