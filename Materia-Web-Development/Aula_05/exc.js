function verificarPar() {
    let entrada = prompt('Digite um número: ');
    let numero = parseInt(entrada);

    if (isNaN(numero)) { // isNaN significa "Is Not a Number"
        alert('Por favor, digite um número válido.');
        return; // return interrompe a função
    }
    if (numero % 2 === 0) {
        alert(numero + " é par.");
    } else {
        alert(numero + " é impar.");
    }
}
verificarPar();
verificarPar();
verificarPar();
