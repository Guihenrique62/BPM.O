CREATE TABLE IF NOT EXISTS tb_OKR (
    id_okr INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS tb_CICLO (
    id_ciclo INT AUTO_INCREMENT PRIMARY KEY,
    nome_ciclo VARCHAR(50) NOT NULL,
    id_okr INT NOT NULL,
    FOREIGN KEY (id_okr) REFERENCES tb_OKR (id_okr)
);

CREATE TABLE IF NOT EXISTS tb_EMPRESA (
    id_empresa INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(60) NOT NULL,
    cnpj VARCHAR(18) NOT NULL
);

CREATE TABLE IF NOT EXISTS tb_EMPRESA_CLIENTE (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    cnpj VARCHAR(18) NOT NULL,
    id_empresa INT NOT NULL,
    FOREIGN KEY (id_empresa) REFERENCES tb_EMPRESA (id_empresa)
);

CREATE TABLE IF NOT EXISTS tb_MACRO (
    id_macro INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    caracteristicas VARCHAR(25) NOT NULL,
    id_cliente INT NOT NULL,
    FOREIGN KEY (id_cliente) REFERENCES tb_EMPRESA_CLIENTE (id_cliente)
);

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

CREATE TABLE IF NOT EXISTS tb_DOCUMENTO (
    id_documento INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    id_processo INT NOT NULL,
    FOREIGN KEY (id_processo) REFERENCES tb_PROCESSO (id_processo)
);

CREATE TABLE IF NOT EXISTS tb_GRUPO_PROCESSO (
    id_grupo INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    id_macro INT NOT NULL,
    FOREIGN KEY (id_macro) REFERENCES tb_MACRO (id_macro)
);

CREATE TABLE IF NOT EXISTS tb_PROCESSO_GRUPO (
    id_processo_grupo INT AUTO_INCREMENT PRIMARY KEY,
    id_grupo INT NOT NULL,
    id_processo INT NOT NULL,
    FOREIGN KEY (id_grupo) REFERENCES tb_GRUPO_PROCESSO (id_grupo),
    FOREIGN KEY (id_processo) REFERENCES tb_PROCESSO (id_processo)
);

CREATE TABLE IF NOT EXISTS tb_USUARIO (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(60) NOT NULL,
    email VARCHAR(50) UNIQUE NOT NULL,
    senha VARCHAR(255) NOT NULL,
    nome_usuario VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS tb_PERMISSAO_USUARIO (
    id_permissao INT AUTO_INCREMENT PRIMARY KEY,
    tipo_permissao VARCHAR(12) NOT NULL,
    id_usuario INT NOT NULL,
    id_cliente INT NOT NULL,
    FOREIGN KEY (id_usuario) REFERENCES tb_USUARIO (id_usuario),
    FOREIGN KEY (id_cliente) REFERENCES tb_EMPRESA_CLIENTE (id_cliente)
);
