from controller.cadastrarProvas import listaGabaritos
from controller.criarAlunos import listaAlunos
from utils.verificaGabarito import verificaGabarito
from models.alunos import Aluno
from models.alunosNotas import Notas


def validaNotaAluno (cpf, prova, idProva):
    aluno = 0
    for idx, val in enumerate(listaAlunos):
        if val.cpf == cpf:
            aluno = idx
            value = val
            break;

    verificaGabarito(prova,idProva,aluno)
    listaAlunos[aluno].respostas.append(prova)
    media = 0
    cont = 0
    for k, i in enumerate(listaAlunos[aluno].respostas):
        media +=  listaAlunos[aluno].respostas[k].nota
        cont = cont + 1
    listaAlunos[aluno].media = (media/cont)
    if  listaAlunos[aluno].media > 7:
        listaAlunos[aluno].aprovado = True
    else:
        listaAlunos[aluno].aprovado = False
    print("Media: ",listaAlunos[aluno].media)
    print("Situação: ", listaAlunos[aluno].aprovado)
    print(aluno)


