import mysql.connector
import os
import bcrypt
from dotenv import load_dotenv

load_dotenv()

class UserModel:

    def criar_usuario(self, nome, email, senha, nome_usuario):
        try:
            hashed_senha = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())

            conn = mysql.connector.connect(
                host = os.getenv("DATABASE_HOST"),
                user = os.getenv("DATABASE_USER"),
                password= os.getenv("DATABASE_PASSWORD"),
                database= os.getenv("DATABASE")
            )
            cursor = conn.cursor()

            query = "INSERT INTO tb_USUARIO (nome, email, senha, nome_usuario) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (nome, email, hashed_senha.decode('utf-8'), nome_usuario))
            conn.commit()

            cursor.close()
            conn.close()
            return "Usuário criado com sucesso!"
        except mysql.connector.Error as err:
            return f"Erro ao criar usuário: {err}"

    def autenticar_usuario(self,email, senha):
        try:
            conn = mysql.connector.connect(
                host = os.getenv("DATABASE_HOST"),
                user = os.getenv("DATABASE_USER"),
                password= os.getenv("DATABASE_PASSWORD"),
                database= os.getenv("DATABASE")
            )
            cursor = conn.cursor()

            query = "SELECT senha FROM tb_USUARIO WHERE email = %s"
            cursor.execute(query, (email,))
            row = cursor.fetchone()

            if row:
                hashed_senha = row[0].encode('utf-8')
                if bcrypt.checkpw(senha.encode('utf-8'), hashed_senha):
                    return "Login bem-sucedido!"
                else:
                    return "Senha incorreta."
            else:
                return "Usuário não encontrado."

        except mysql.connector.Error as err:
            return f"Erro ao autenticar usuário: {err}"
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def excluir_usuario(self, id_usuario):
            try:
                conn = mysql.connector.connect(
                host = os.getenv("DATABASE_HOST"),
                user = os.getenv("DATABASE_USER"),
                password= os.getenv("DATABASE_PASSWORD"),
                database= os.getenv("DATABASE")
                )
                cursor = conn.cursor()

                query = "DELETE FROM tb_USUARIO WHERE id_usuario = %s"
                cursor.execute(query, (id_usuario,))
                conn.commit()
                return "Usuário excluído com sucesso."
            except Exception as err:
                return f"Erro ao excluir usuário: {err}"
# Exemplo de utilização
if __name__ == "__main__":
    model = UserModel()
    
