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

var count = 1;
function adicionarProduto() {
    event.preventDefault();
    var element = document.querySelector(`.produtos`);
    var copy = element;

    document.querySelector("#produtos").innerHTML += copy.outerHTML;

    count++; 
    document.getElementsByClassName("produto")[0].id = "produto"+count;

    document.querySelector(`.produtos`).getElementsByTagName("label")[0].htmlFor= 'produto'+count;
    document.querySelector(`.produtos`).getElementsByTagName("select")[0].name= 'produto'+count;

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
    var produto = produtos.getElementsByTagName('div');

    if (produto.length > 1) {
        produtos.removeChild(produto[0]);
    } else {
        console.log("Não foi possível remover este produto.");
    } 
}
