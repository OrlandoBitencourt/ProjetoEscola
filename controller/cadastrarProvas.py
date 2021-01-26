from flask_restful import Resource
from models.provas import Prova
from flask import Flask, jsonify, request

listaGabaritos = []

class CadastrarProvas(Resource):
    @staticmethod
    def post():
        prova = request.json['prova']
        provasCadastradas = Prova(prova['id'],
                    prova['q1'], prova['r1'],
                    prova['q2'], prova['r2'],
                    prova['q3'], prova['r3'],
                    prova['q4'], prova['r4'],
                    prova['q5'], prova['r5'],
                    prova['q6'], prova['r6'],
                    prova['q7'], prova['r7'],
                    prova['q8'], prova['r8'],
                    prova['q9'], prova['r9'],
                    prova['q10'], prova['r10'])
        provas = {'id': provasCadastradas.id,
                  'q1': provasCadastradas.q1, 'r1': provasCadastradas.r1,
                  'q2': provasCadastradas.q2, 'r2': provasCadastradas.r2,
                  'q3': provasCadastradas.q3, 'r3': provasCadastradas.r3,
                  'q4': provasCadastradas.q4, 'r4': provasCadastradas.r4,
                  'q5': provasCadastradas.q5, 'r5': provasCadastradas.r5,
                  'q6': provasCadastradas.q6, 'r6': provasCadastradas.r6,
                  'q7': provasCadastradas.q7, 'r7': provasCadastradas.r7,
                  'q8': provasCadastradas.q8, 'r8': provasCadastradas.r8,
                  'q9': provasCadastradas.q9, 'r9': provasCadastradas.r9,
                  'q10': provasCadastradas.q10, 'r10': provasCadastradas.r10}
        listaGabaritos.append(provasCadastradas)
        return f'Prova {provas["id"]} cadastrada com sucesso'

    def get(self):
        for i in listaGabaritos:
            print("Prova: ",i.id)
            print(i.q1, " - ", i.r1)
            print(i.q2, " - ", i.r2)
            print(i.q3, " - ", i.r3)
            print(i.q4, " - ", i.r4)
            print(i.q5, " - ", i.r5)
            print(i.q6, " - ", i.r6)
            print(i.q7, " - ", i.r7)
            print(i.q8, " - ", i.r8)
            print(i.q9, " - ", i.r9)
            print(i.q10, " - ", i.r10)
        return 'lista de gabaritos'