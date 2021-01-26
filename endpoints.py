from flask_restful import Api
from controller.healthCheck import HealthCheck
from controller.criarAlunos import CriarAluno
from controller.cadastrarProvas import CadastrarProvas

def init_api(app):
    api = Api()

    api.add_resource(HealthCheck, "/health-check")
    api.add_resource(CriarAluno, "/aluno")
    api.add_resource(CadastrarProvas, "/gabaritos")

    api.init_app(app)