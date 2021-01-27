from controller.cadastrarProvas import listaGabaritos
from controller.criarAlunos import listaAlunos
from utils.verificaGabarito import verificaGabarito

def validaNotaAluno (cpf, prova, idProva):
    aluno = 0
    for idx, val in enumerate(listaAlunos):
        if val.cpf == cpf:
            aluno = idx
            break;


    verificaGabarito(prova,idProva,aluno)
    print(aluno)

