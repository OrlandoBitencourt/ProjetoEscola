from flask_restful import Resource
from flask import Flask, jsonify, request
from controller.cadastrarProvas import listaGabaritos
from utils.validaNotaAluno import validaNotaAluno


class Prova(Resource):
    @staticmethod
    def post(cpf, idProva):
        prova = request.json['prova']
        validaNotaAluno(cpf, prova, idProva)

    def get(self, prova):
        result = {}
        if prova == 1:
            result = {
                "prova": listaGabaritos[0]
            }
        else:
            result = {
                "prova": listaGabaritos[1]
            }
        return jsonify(result)