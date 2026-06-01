class Aluno {
    constructor(nome, idade, curso){
        this.nome = nome;
        this.idade = idade;
        this.curso = curso;
    }
};

const alunos = [

    new Aluno('Ana', 17, 'Front-End'),
    new Aluno('Carlos', 17, 'JavaScript'),
    new Aluno('Marina', 17, 'HTML e CSS')
];

const inputNome = document.querySelector('#nome');
const inputIdade = document.querySelector('#idade');
const inputCurso = document.querySelector('#curso');
const inputBusca = document.querySelector('#busca');




const listaAlunos = document.querySelector('#listaAlunos');
const total = document.querySelector('#total');
const mensagem = document.querySelector('#mensagem');

const btnAdicionarFinal = document.querySelector('#btnAdicionarFinal');
const btnAdicionarInicio = document.querySelector('#btnAdicionarInicio');
const btnRemoverPrimeiro = document.querySelector('#btnRemoverPrimeiro');
const btnRemoverUltimo = document.querySelector('#btnRemoverUltimo');
const btnBuscar = document.querySelector('#btnBuscar');
const btnRemoverNome = document.querySelector('#btnRemoverNome');
const btnMostrarParte = document.querySelector('#btnMostrarParte');

function limparCampos() {
    inputNome.value = '';
    inputIdade.value = '';
    inputCurso.value = '';
    inputCurso.value = '';
}

function criarAlunoPelosInputs() {
    const nome = inputNome.value;
    const idade = inputIdade.value;
    const curso = inputCurso.value;

    if(nome == '' || idade == '' || curso == ''){
        mensagem.innerHTML = 'Preencha todos os campos...';
        return null;
    }

    return new Aluno(nome, idade, curso);
}

function mostrarAlunos(lista){
    listaAlunos.innerHTML = '';

    for(let i = 0; i < lista.lenght; i++){
        const aluno = lista[i];

        const {nome, idade, curso} = aluno;

        listaAlunos.innerHTML += `
        <li>
            <strong>${nome}</strong><br>
            Idade: ${idade}<br>
            Curso: ${curso}
        </li>
        `;
    }
    total.innerHTML = alunos.length;
}

btnAdicionarFinal.addEventListener('click', () => {
const novoAluno = criarAlunosPelosInputs();

if(novoAluno !== null){
    alunos.push(NovoAluno);
    mensagem.innerHTML = 'Aluno adicionado no final da lista.';
    limparCampos();
    mostrarAlunos(alunos);
}

});

btnAdicionarInicio.addEventListener('click', () => {
const novoAluno = criarAlunosPelosInputs();

if(novoAluno !== null){
    alunos.unshift(NovoAluno);
    mensagem.innerHTML = 'Aluno adicionado no final da lista.';
    limparCampos();
    mostrarAlunos(alunos);
}

});

btnRemoverPrimeiro.addEventListener('click', () => {
    if(alunos.length > 0){
        alunos.shift();
        mensagem.innerHTML = 'Primeiro aluno removido'
    }else{
        mensagem.innerHTML = 'A lista já está vazia'
    }

    mostrarAlunos(alunos)
})

btnRemoverUltimo.addEventListener('click', () => {
    if(alunos.length > 0){
        alunos.pop();
        mensagem.innerHTML = 'Último aluno removido'
    }else{
        mensagem.innerHTML = 'A lista já está vazia'
    }

    mostrarAlunos(alunos)
})

btnBuscar.addEventListener('click', () => {
    const nomeBuscado = inputBusca.value;
    const nomes = [];

    for(let i = 0; i < alunos.length; i++){
        nomes.push(alunos[i].nome)
    }

    const posicao = nomes.indexOf(nomeBuscado)

    if(posicao === -1){
        mensagem.innerHTML = 'Aluno não encontrado.';
    }else{
        mensagem.innerHTML = `Aluno encontrado na posição: ${posicao}`;
    }
})

btnRemoverNome.addEventListener('click', () => {
    const nomeBuscado = inputBusca.value;
    const nomes = [];

    let contador = 0;

    while(contador < alunos.lenght) {
        nomes.push(alunos[contador].nome);
        contador++
    }

    const posicao = nomes.indexOf(nomeBuscado);

    if(posicao === -1){
         mensagem.innerHTML = 'Não foi possível remover. Aluno não encontrado.';
    }else{
        alunos.splice(posicao, 1);
        mensagem.innerHTML = 'Aluno removido com sucesso.';
        mostrarAlunos(alunos);
    }
});

btnMostrarParte.addEventListener('click', () =>{
    const primeirosAlunos = alunos.slice(0, 2);

    mensagem.innerHTML = 'Mostrando apenas os 2 primeiros alunos.';
    mostrarAlunos(primeirosAlunos);
});

mostrarAlunos(alunos);