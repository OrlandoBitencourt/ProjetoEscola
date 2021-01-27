from flask_restful import Resource
from flask import Flask, jsonify, request
from controller.cadastrarProvas import listaGabaritos
from utils.validaNotaAluno import validaNotaAluno
from models.respostas import Resposta
import json


class Prova(Resource):
    @staticmethod
    def post(cpf, idProva):
        prova = request.json['prova']
        respostas = json.loads(prova, object_hook=lambda d: Resposta(**d))
        validaNotaAluno(cpf, respostas, idProva)
        return 'Respostas Salvas Com Sucesso'

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