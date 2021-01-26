from flask_restful import Api
from controller.healthCheck import HealthCheck
from controller.criarAlunos import CriarAluno

def init_api(app):
    api = Api()

    api.add_resource(HealthCheck, "/health-check")
    api.add_resource(CriarAluno, "/aluno")

    api.init_app(app)