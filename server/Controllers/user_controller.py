from Models.user_model import UserModel

class UserController:

    def registrar_usuario(self, dados_usuario):
        user_model = UserModel()
        try:
            nome = dados_usuario.get('nome')
            email = dados_usuario.get('email')
            senha = dados_usuario.get('senha')
            nome_usuario = dados_usuario.get('nome_usuario')

            mensagem = user_model.criar_usuario(nome, email, senha, nome_usuario)
            return {'mensagem': mensagem}, 200  # 200 OK
        except Exception as e:
            return {'mensagem': str(e)}, 500  # 500 Internal Server Error

    def autenticar_usuario(self, dados_login):
        user_model = UserModel()
        try:
            email = dados_login.get('email')
            senha = dados_login.get('senha')

            mensagem = user_model.autenticar_usuario(email, senha)
            return {'mensagem': mensagem}, 200  # 200 OK
        except Exception as e:
            return {'mensagem': str(e)}, 500  # 500 Internal Server Error
