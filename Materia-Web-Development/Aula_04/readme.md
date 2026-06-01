Aula Teórica sobre Controle de Fluxos

Condicionais

 SE (condição)
 ENTÃO  (o que o programa deve fazer)
 SENÃO  (caso a condição não seja atendida)

 Códigos de exemplo:




 <!-- let num = 5

if (num == 5){
    console.log('Variável é igual a cinco')
}
if (num == 6){
    console.log('A Variável não tem esse valor')
} -->






<!-- let umaCor = prompt('Digite uma cor: ')

if(umaCor == 'Vermelho'){
    alert('A cor é Vermelho')
}
else {
    alert('A cor não é Vermelho')
} -->




<!-- let nomeUsuario = prompt ('Digite seu nome:')

if((nomeUsuario == '') || (nomeUsuario == null)){ 
    alert('Nome não inserido')
    nomeUsuario = prompt('Por favor, insira seu nome: ')
    alert(`Nome inserido: ${nomeUsuario}`)
}
else {
    alert(`Nome inserido: ${nomeUsuario}`)
} -->







<!-- let combustivel = prompt('Digite o tipo de combustível')
if(combustivel == 'gnv'){
    alert('O veículo é movido à gás')
}
else if(combustivel == 'diesel'){
    alert('O veículo se move à diesel')
}
else if(combustivel == 'gasolina'){
    alert('O veiculo se move à gasolina')
}
else if(combustivel == 'alcool'){
    alert('O veiculo se move à alcool')
}
else {
    alert('O veiculo só pode ser elétrico')
} -->






<!-- let num = prompt('Digite número de 1 a 5')
if(num == 1){
    alert('O número é um')
}
else if(num == 2){
    alert('O número é dois')
}
else if(num == 3){
    alert('O número é três')
}
else if(num == 4){
    alert('O número é quatro')
}
else if(num == 5){
    alert('O número é cinco')
}
else {
    alert('O número é maior que o solicitado')
} -->





<!-- let numeroInserido = parseInt(prompt('Digite um num entre 1 e 10'))
if (numeroInserido <= 10){
    alert(`O número inserido: ${numeroInserido} está entre 1 e 10`)
}
else if(numeroInserido <= 20){
    alert(`O número inserido: ${numeroInserido} é maior que 11 e menor que 20`)
}
else if(numeroInserido <= 30){
    alert(`O número inserido: ${numeroInserido} é maior que 21 e menor que 30`)
}
else if(numeroInserido <= 40){
    alert(`O número inserido: ${numeroInserido} é maior que 31 e menor que 40`)
}
else if(numeroInserido <= 50){
    alert(`O número inserido: ${numeroInserido} é maior que 41 e menor que 50`)
}
else if(numeroInserido <= 60){
    alert(`O número inserido: ${numeroInserido} é maior que 51 e menor que 60`)
}
else if(numeroInserido <= 70){
    alert(`O número inserido: ${numeroInserido} é maior que 61 e menor que 70`)
}
else if(numeroInserido <= 80){
    alert(`O número inserido: ${numeroInserido} é maior que 71 e menor que 80`)
}
else if(numeroInserido <= 90){
    alert(`O número inserido: ${numeroInserido} é maior que 81 e menor que 90`)
}
else if(numeroInserido <= 100){
    alert(`O número inserido: ${numeroInserido} é maior que 91 e menor que 100`)
}
else {
    alert('O número é maior que 100')
} -->