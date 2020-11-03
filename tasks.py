import schedule
import time
from helpers import atualiza_notificacoes_data_validade_produto, atualiza_notificacoes_quantidade_produto, atualiza_notificacoes_data_validade_kit, notificacao_email_data_validade, notificacao_email_quantidade, notificacao_email_data_validade_kit

def main_task():
    '''
    FUNÇÃO TASK main_task

    - Uma função que executa rotinas programadas com a biblioteca schedule, que DEVE SEMPRE estar rodando
    junto com a aplicação.

    @autor: Luciano Gomes Vieira dos Anjos -
    @data: 01/11/2020 -
    @versao: 1.0.0
    '''
    schedule.every().day.do(atualiza_notificacoes_data_validade_produto)
    schedule.every().day.do(atualiza_notificacoes_data_validade_kit)
    schedule.every().hour.do(atualiza_notificacoes_quantidade_produto)
    schedule.every().sunday.do(notificacao_email_data_validade)
    schedule.every().sunday.do(notificacao_email_quantidade)
    schedule.every().sunday.do(notificacao_email_data_validade_kit)

    while True:
        schedule.run_pending()
        time.sleep(3600)

if __name__ == '__main__':
    main_task()