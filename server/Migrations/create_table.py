# create_tables.py
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

class CreateTable:
    

    def create_tables(self):
        try:
            conn = mysql.connector.connect(
                host = os.getenv("DATABASE_HOST"),
                user = os.getenv("DATABASE_USER"),
                password= os.getenv("DATABASE_PASSWORD"),
                database= os.getenv("DATABASE")
            )
            cursor = conn.cursor()

            # Código para criar as tabelas...

            #Criar Tabela OKR
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS tb_OKR (
                    id_okr INT AUTO_INCREMENT PRIMARY KEY,
                    nome VARCHAR(50) NOT NULL
                );
            ''')
            
            #Criar Tabela CICLO
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS tb_CICLO (
                    id_ciclo INT AUTO_INCREMENT PRIMARY KEY,
                    nome_ciclo VARCHAR(50) NOT NULL,
                    id_okr INT NOT NULL,
                    FOREIGN KEY (id_okr) REFERENCES tb_OKR (id_okr)
                );
            ''')

            #Criar Tabela EMPRESA
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS tb_EMPRESA (
                    id_empresa INT AUTO_INCREMENT PRIMARY KEY,
                    nome VARCHAR(60) NOT NULL,
                    cnpj VARCHAR(18) NOT NULL
                );
            ''')

            #Criar Tabela EMPRESA CLIENTE
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS tb_EMPRESA_CLIENTE (
                    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
                    nome VARCHAR(50) NOT NULL,
                    cnpj VARCHAR(18) NOT NULL,
                    id_empresa INT NOT NULL,
                    FOREIGN KEY (id_empresa) REFERENCES tb_EMPRESA (id_empresa)
                );
            ''')

            #Criar Tabela MACRO
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS tb_MACRO (
                    id_macro INT AUTO_INCREMENT PRIMARY KEY,
                    nome VARCHAR(100) NOT NULL,
                    caracteristicas VARCHAR(25) NOT NULL,
                    id_cliente INT NOT NULL,
                    FOREIGN KEY (id_cliente) REFERENCES tb_EMPRESA_CLIENTE (id_cliente)
                );
            ''')

            #Criar Tabela PROCESSO
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS tb_PROCESSO (
                    id_processo INT AUTO_INCREMENT PRIMARY KEY,
                    nome VARCHAR(100) NOT NULL,
                    tipo VARCHAR(20) NOT NULL,
                    objetivo VARCHAR(20) NOT NULL,
                    agente VARCHAR(50) NOT NULL,
                    analista VARCHAR(50) NOT NULL,
                    lider VARCHAR(50) NOT NULL,
                    qtd_interacoes_cliente INT NOT NULL,
                    qtd_interacoes_outras INT NOT NULL,
                    link VARCHAR(255),
                    id_macro INT NOT NULL,
                    id_ciclo INT NOT NULL,
                    FOREIGN KEY (id_macro) REFERENCES tb_MACRO (id_macro),
                    FOREIGN KEY (id_ciclo) REFERENCES tb_CICLO (id_ciclo)
                );
            ''')

            #Criar Tabela DOCUMENTO
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS tb_DOCUMENTO (
                    id_documento INT AUTO_INCREMENT PRIMARY KEY,
                    nome VARCHAR(50) NOT NULL,
                    id_processo INT NOT NULL,
                    FOREIGN KEY (id_processo) REFERENCES tb_PROCESSO (id_processo)
                );
            ''')

            #Criar Tabela GRUPO PROCESSO
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS tb_GRUPO_PROCESSO (
                    id_grupo INT AUTO_INCREMENT PRIMARY KEY,
                    nome VARCHAR(100) NOT NULL,
                    id_macro INT NOT NULL,
                    FOREIGN KEY (id_macro) REFERENCES tb_MACRO (id_macro)
                );
            ''')

            #Criar Tabela PROCESSO GRUPO
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS tb_PROCESSO_GRUPO (
                    id_processo_grupo INT AUTO_INCREMENT PRIMARY KEY,
                    id_grupo INT NOT NULL,
                    id_processo INT NOT NULL,
                    FOREIGN KEY (id_grupo) REFERENCES tb_GRUPO_PROCESSO (id_grupo),
                    FOREIGN KEY (id_processo) REFERENCES tb_PROCESSO (id_processo)
                );
            ''')

            #Criar Tabela USUARIO
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS tb_USUARIO (
                    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
                    nome VARCHAR(60) NOT NULL,
                    email VARCHAR(50) NOT NULL,
                    senha VARCHAR(255) NOT NULL,
                    nome_usuario VARCHAR(50)
                );
            ''')

            #Criar Tabela PERMISSAO USUARIO
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS tb_PERMISSAO_USUARIO (
                    id_permissao INT AUTO_INCREMENT PRIMARY KEY,
                    tipo_permissao VARCHAR(12) NOT NULL,
                    id_usuario INT NOT NULL,
                    id_cliente INT NOT NULL,
                    FOREIGN KEY (id_usuario) REFERENCES tb_USUARIO (id_usuario),
                    FOREIGN KEY (id_cliente) REFERENCES tb_EMPRESA_CLIENTE (id_cliente)
                );
            ''')


            cursor.close()
            conn.close()
            print("Tabelas criadas com sucesso!")
        except mysql.connector.Error as err:
            print(f"Erro ao criar tabelas: {err}")

if __name__ == "__main__":
    create_table = CreateTable()
    create_table.create_tables()