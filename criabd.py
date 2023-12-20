# Importando sqlite
import sqlite3 as lite

# Criando a conexão com o banco de dados
con = lite.connect('orcamento.db')

# Criando tabela Usuários
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE usuario(id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(20) NOT NULL)")

# Criando tabela Categoria de despesas
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE categoriaDespesa(id INTEGER PRIMARY KEY AUTOINCREMENT, descricao VARCHAR(20) NOT NULL)")

# Criando tabela Categoria de receitas
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE categoriaReceita(id INTEGER PRIMARY KEY AUTOINCREMENT, descricao VARCHAR(20) NOT NULL)")

# Criando tabela Tipo de Pagamento
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE tipoPagamento(id INTEGER PRIMARY KEY AUTOINCREMENT, descricao VARCHAR(20) NOT NULL)")

# Criando tabela Tipo de Depesa
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE tipoDespesa(id INTEGER PRIMARY KEY AUTOINCREMENT, descricao VARCHAR(20) NOT NULL)")

# Criando tabela Receitas
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE receitas(id INTEGER PRIMARY KEY AUTOINCREMENT, categoria INTEGER NOT NULL, valor DECIMAL NOT NULL, dataReceita DATE NOT NULL, usuario INTEGER NOT NULL, observacao VARCHAR(50), FOREIGN KEY (categoria) REFERENCES categoriaReceita(id), FOREIGN KEY (usuario) REFERENCES usuario(id))")

# Criando tabela Depesas
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE despesas(id INTEGER PRIMARY KEY AUTOINCREMENT, categoria INTEGER NOT NULL, valor DECIMAL NOT NULL, dataDespesa DATE NOT NULL, tipoPagamento INTEGER NOT NULL, tipoDespesa INTEGER NOT NULL, usuario INTEGER NOT NULL, observacao VARCHAR(50), FOREIGN KEY (categoria) REFERENCES categoriaDespesa(id), FOREIGN KEY (tipoPagamento) REFERENCES tipoPagamento(id), FOREIGN KEY (tipoDespesa) REFERENCES tipoDespesa(id), FOREIGN KEY (usuario) REFERENCES usuario(id))")
