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
    var element = document.querySelector(`#info-produto${count}`);
    var copy = element;

    document.querySelector("#produtos").innerHTML += copy.outerHTML;

    count++; 
    document.getElementsByClassName("info-produto")[0].id = "info-produto"+count;

    document.querySelector(`#info-produto${count}`).getElementsByTagName("label")[0].htmlFor= 'produto'+count;
    document.querySelector(`#info-produto${count}`).getElementsByTagName("select")[0].name= 'produto'+count;

    document.querySelector(`#info-produto${count}`).getElementsByTagName("label")[1].htmlFor= 'quantidade'+count;
    document.querySelector(`#info-produto${count}`).getElementsByTagName("input")[0].name= 'quantidade'+count;

    document.querySelector(`#info-produto${count}`).getElementsByTagName("label")[2].htmlFor= 'data_fabricacao'+count;
    document.querySelector(`#info-produto${count}`).getElementsByTagName("input")[1].name= 'data_fabricacao'+count;

    document.querySelector(`#info-produto${count}`).getElementsByTagName("label")[3].htmlFor= 'data_validade'+count;
    document.querySelector(`#info-produto${count}`).getElementsByTagName("input")[2].name= 'data_validade'+count;

    document.querySelector(`#info-produto${count}`).getElementsByTagName("select")[0].id= 'produto'+count;
    document.querySelector(`#info-produto${count}`).getElementsByTagName("input")[0].id= 'quantidade'+count;
    document.querySelector(`#info-produto${count}`).getElementsByTagName("input")[1].id= 'data_fabricacao'+count;
    document.querySelector(`#info-produto${count}`).getElementsByTagName("input")[2].id= 'data_validade'+count;

    

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
