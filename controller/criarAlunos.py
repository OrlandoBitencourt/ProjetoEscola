from flask_restful import Resource
from models.alunos import Aluno
from flask import Flask, jsonify, request

listaAlunos = []

class CriarAluno(Resource):
    @staticmethod
    def post():
        aluno = request.json['aluno']
        a1 = Aluno(aluno['id'], aluno['nome'], aluno['cpf'])
        result = {'id': a1.id, 'nome': a1.nome, 'cpf': a1.cpf}
        #VALIDA QUANTIDADE MAXIMA DE ALUNOS (MAXIMO = 100)
        if len(listaAlunos)<99:
            listaAlunos.append(a1)
            return f'Aluno {result["nome"]} cadastrado com sucesso'
        else:
            return "Numero maximo de alunos cadastrados"

    def get(self):
       # for i in listaAlunos:
          #  print(i))
       return 'Lista de Alunos'

