from flask_restful import Api
from controller.healthCheck import HealthCheck
from controller.criarAlunos import CriarAluno
from controller.cadastrarProvas import CadastrarProvas
from controller.cadastrarRespostas import CadastrarRespostas

def init_api(app):
    api = Api()

    api.add_resource(HealthCheck, "/health-check")
    api.add_resource(CriarAluno, "/aluno")
    api.add_resource(CadastrarProvas, "/gabaritos")
    api.add_resource(CadastrarRespostas, "/respostas")

    api.init_app(app)