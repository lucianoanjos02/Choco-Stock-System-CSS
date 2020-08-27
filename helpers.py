from flask_login import current_user

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
