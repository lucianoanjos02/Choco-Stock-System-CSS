// ------------------------------------------------------------------------------------------------------
// ------------------  IMPLEMENTAÇÃO DO EVENTO DE CLICK NOS BOTÃO DE NOTIFICAÇÕES  ----------------------
// ------------------------------------------------------------------------------------------------------
// -------- @autor: Luciano Gomes Vieira dos Anjos
// -------- @data: 01/10/2020
// -------- @versao: 1.0.0

var botaoAdicionarProduto = document.querySelector(".notification-button");
botaoAdicionarProduto.addEventListener("click", resetarDisplayNotificacoes);

// ------------------------------------------------------------------------------------------------------
// -----  IMPLEMENTAÇÃO DA FUNÇÃO resetarDisplayNotificacoes QUE É ACIONADA AO CLICAR NO BOTÃO ----------
// -----  DE NOTIFICAÇÕES, "LIMPANDO" A QUANTIDADE DE NOTIFICAÇÕES NOVAS DO USUÁRIO NA VIEW -------------
// ------------------------------------------------------------------------------------------------------
// -------- @autor: Luciano Gomes Vieira dos Anjos
// -------- @data: 01/10/2020
// -------- @versao: 1.0.0


function resetarDisplayNotificacoes() {
    event.preventDefault();
    document.querySelector('.counter').remove();
}
