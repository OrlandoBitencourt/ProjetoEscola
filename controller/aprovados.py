from flask_restful import Resource
from flask import Flask, jsonify, request
from models.alunos import Aluno
from controller.criarAlunos import listaAlunos

listaAprovados = []

#Lista e valida os alunos (apenas traz os aprovados)
class Aprovado(Resource):
    def get(self):
        result = {}
        listaAprovados = []
        for aluno in listaAlunos:
            if aluno.aprovado == True:
                print(aluno.nome)
                listaAprovados.append([aluno.id,aluno.nome, aluno.cpf, aluno.media, aluno.aprovado])
        result = {
            "Aprovados": listaAprovados
        }
        return jsonify(result)