

function trocarElementoDeColuna(colunaAtual, proximaColuna) {
    const tabela = document.getElementById('minhaTabela');
    const elementosColunaAtual = tabela.rows[1].cells[colunaAtual].querySelectorAll('li');
            
    // Verifica se há pelo menos um elemento na coluna atual
    if (elementosColunaAtual.length > 0) {
        const ultimoIndice = elementosColunaAtual.length - 1;
        const elementoMovido = elementosColunaAtual[ultimoIndice].outerHTML;
        tabela.rows[1].cells[colunaAtual].querySelector('ul').removeChild(elementosColunaAtual[ultimoIndice]);
        tabela.rows[1].cells[proximaColuna].querySelector('ul').innerHTML = elementoMovido + tabela.rows[1].cells[proximaColuna].querySelector('ul').innerHTML;
    }
}
    
setInterval(function () {
    // Troca apenas um elemento de cada vez
    trocarElementoDeColuna(0, 1); // Troca da coluna 0 (CRIADOS) para a coluna 1 (INICIADOS)
    trocarElementoDeColuna(1, 2); // Troca da coluna 1 (INICIADOS) para a coluna 2 (CONCLUÍDOS)
     // Adicione mais chamadas de função conforme necessário para outras colunas
}, 60000); // 60000 milissegundos = 1 minuto
    