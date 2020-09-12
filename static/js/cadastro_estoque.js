// ------------------------------------------------------------------------------------------------------
// --------  IMPLEMENTAÇÃO DO EVENTO DE CLICK NOS BOTÕES DE ADICIONAR PRODUTO E REMOVER PRODUTO  --------
// ------------------------------------------------------------------------------------------------------
// -------- @autor: Luciano Gomes Vieira dos Anjos
// -------- @data: 11/09/2020
// -------- @versao: 1.0.0

var botaoAdicionarProduto = document.querySelector("#adicionar-produto");
botaoAdicionarProduto.addEventListener("click", adicionarProduto);

var botaoRemoverProduto = document.querySelector("#remover-produto");
botaoRemoverProduto.addEventListener("click", removerProduto);


// ------------------------------------------------------------------------------------------------------
// --------  IMPLEMENTAÇÃO DA FUNÇÃO DE ADICIONAR PRODUTO AO CADASTRO DE ESTOQUE  -----------------------
// --------  ACIONADA AO EVENTO DE CLIQUE IMPLEMENTADO ANTERIORMENTE  -----------------------------------
// ------------------------------------------------------------------------------------------------------
// -------- @autor: Luciano Gomes Vieira dos Anjos
// -------- @data: 11/09/2020
// -------- @versao: 1.0.0

function adicionarProduto() {
    event.preventDefault();
    document.querySelector("#produtos").innerHTML += document.querySelector("#info-produto").outerHTML;
}


// ------------------------------------------------------------------------------------------------------
// --------  IMPLEMENTAÇÃO DA FUNÇÃO DE REMOVER PRODUTO DO CADASTRO DE ESTOQUE  -------------------------
// --------  ACIONADA AO EVENTO DE CLIQUE IMPLEMENTADO ANTERIORMENTE  -----------------------------------
// ------------------------------------------------------------------------------------------------------
// -------- @autor: Luciano Gomes Vieira dos Anjos
// -------- @data: 11/09/2020
// -------- @versao: 1.0.0

function removerProduto() {
    event.preventDefault();
    var produtos = document.querySelector('#produtos');
    var infoProduto = produtos.getElementsByTagName('div');

    if (infoProduto.length > 9) {
        produtos.removeChild(infoProduto[0]);
    } else {
        console.log("Não foi possível remover este produto.");
    } 
}
