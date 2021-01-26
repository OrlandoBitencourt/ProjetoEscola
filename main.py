from flask import Flask
import settings
from endpoints import init_api
from controller.criarGabarito import CriarGabarito

app = Flask(__name__)
init_api(app)

if __name__ == '__main__':
    CriarGabarito()
    app.run(port=8000, host="127.0.0.1")
