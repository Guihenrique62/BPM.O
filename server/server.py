from flask import Flask, request, jsonify
from Controllers.user_controller import UserController

app = Flask(__name__)
controller = UserController()

@app.route('/api/registrar-usuario', methods=['POST'])
def registrar_usuario():
    dados_usuario = request.json
    resposta, status_code = controller.registrar_usuario(dados_usuario)
    return jsonify(resposta), status_code

@app.route('/api/autenticar-usuario', methods=['POST'])
def autenticar_usuario():
    dados_login = request.json
    resposta, status_code = controller.autenticar_usuario(dados_login)
    return jsonify(resposta), status_code

@app.route('/api/excluir-usuario/<int:id_usuario>', methods=['DELETE'])
def excluir_usuario(id_usuario):
    resposta, status_code = controller.excluir_usuario(id_usuario)
    return jsonify(resposta), status_code

if __name__ == '__main__':
    app.run(debug=True)
