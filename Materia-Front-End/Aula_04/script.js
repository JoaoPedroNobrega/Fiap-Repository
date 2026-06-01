// tipos primitivos
var boolean = false;
console.log(`A variável ${boolean} tem o tipo ${typeof(boolean)}`)
// template string

var numero = 1;
console.log(`A variável ${numero} tem o tipo ${typeof(numero)}`)
var num;
num = 2;

// var; // variável global ou local - valor inicial pode ser nulo 
// let; // variável local - valor inicial pode ser nulo
// const; // variável local - valor inicial é obrigatório

// usando variável global
var nome = 'Joao'
function nomeDafuncao () {

var sobrenome = 'Nobrega';
console.log(sobrenome);

}
console.log(nome);
console.log(sobrenome);

console.log(nome);
nomeDafuncao()

//operadores de comparação
var comparacao = '0' == 0;
console.log(comparacao);

var comparacaoIdentica = '0' === 0;
console.log(comparacaoIdentica);

//operaores aritméticos
//+, -, /, *, %, **

var mult = 5 * 6;
console.log(mult);

var divisao = 15 / 3; 
console.log(divisao);

//operadores relacionais
// <, >, >=, <=, !=
var maiorOuIgual = 5 >= 10;
console.log(maiorOuIgual);

var diferente = 8 != 7;
console.log(diferente);

//operadores lógicos
// && - E, || - OU, ! - NAO
var  e = true  && true;
console.log(e);

var ou = true || false;
console.log(ou)

var nao = !true;
console.log(nao);