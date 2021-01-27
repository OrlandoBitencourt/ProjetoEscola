from flask_restful import Resource
from flask import Flask, jsonify, request
from models.alunos import Aluno
from controller.criarAlunos import listaAlunos

listaAprovados = []

class Aprovado(Resource):
    def get(self):
        result = {}
        listaAprovados = []
        for aluno in listaAlunos:
            if aluno.aprovado == True:
                print(aluno.nome)
                listaAprovados.append(aluno)
        result = {
            "Aprovados": listaAprovados
        }
        return jsonify(result)