from controller.cadastrarProvas import listaGabaritos



def verificaGabarito (prova, idProva, aluno):
    nota = 0
    idProva = int(idProva)
    idAluno = int(idAluno)
    prova.idProva = idProva
    prova.idAluno = idAluno

    #VALIDA QUESTOES E ATRIBUI NOTA
    if prova.q1 == listaGabaritos[idProva].r1:
        nota = nota+1
    if prova.q2 == listaGabaritos[idProva].r2:
        nota = nota+1
    if prova.q3 == listaGabaritos[idProva].r3:
        nota = nota+1
    if prova.q4 == listaGabaritos[idProva].r4:
        nota = nota+1
    if prova.q5 == listaGabaritos[idProva].r5:
        nota = nota+1
    if prova.q6 == listaGabaritos[idProva].r6:
        nota = nota+1
    if prova.q7 == listaGabaritos[idProva].r7:
        nota = nota+1
    if prova.q8 == listaGabaritos[idProva].r8:
        nota = nota+1
    if prova.q9 == listaGabaritos[idProva].r9:
        nota = nota+1
    if prova.q10 == listaGabaritos[idProva].r10:
        nota = nota+1
    if nota < 0:
        nota = 0
    elif nota > 10:
        nota = 10
    prova.nota = nota
    print(prova)
    print(f'Nota: {nota}')

