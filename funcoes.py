# Importando sqlite
import sqlite3 as lite

# Criando a conexão com o banco de dados
con = lite.connect('orcamento.db')

# Criando Inserts 
def inserirCategoriaDespesa(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO categoriaDespesa (descricao) VALUES (?)"
        cur.execute(query, i)

def inserirCategoriaReceita(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO categoriaReceita (descricao) VALUES (?)"
        cur.execute(query, i)

def inserirUsuario(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO usuario (nome) VALUES (?)"
        cur.execute(query, i)

def inserirTipoDespesa(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO tipoDespesa (descricao) VALUES (?)"
        cur.execute(query, i)

def inserirTipoPagamento(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO tipoPagamento (descricao) VALUES (?)"
        cur.execute(query, i)

def inserirDespesa(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO despesas (categoria, valor, dataDespesa, tipoPagamento, tipoDespesa, usuario, observacao) VALUES (?)"
        cur.execute(query, i)

def inserirReceita(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO receitas (categoria, valor, dataReceita, usuario, observacao) VALUES (?)"
        cur.execute(query, i)

# Criando Deletes 
def deletarCategoriaDespesa(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM categoriaDespesa WHERE id=?"
        cur.execute(query, i)

def deletarcategoriaReceita(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM categoriaReceita WHERE id=?"
        cur.execute(query, i)

def deletarUsuario(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM usuario WHERE id=?"
        cur.execute(query, i)

def deletarTipoDespesa(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM tipoDespesa WHERE id=?"
        cur.execute(query, i)

def deletarTipoPagamento(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM tipoPagamento WHERE id=?"
        cur.execute(query, i)

def deletarDespesas(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM despesas WHERE id=?"
        cur.execute(query, i)

def deletarReceitas(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM receitas WHERE id=?"
        cur.execute(query, i)

# Criando Visualizações
        
def verCategoriaDespesa():
    listaCategoriaDespesa = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT descricao FROM categoriaDespesa")
        linha = cur.fetchall()
        for l in linha:
            listaCategoriaDespesa.append(l)
    return listaCategoriaDespesa


def vercategoriaReceita(i):
    listaCategoriaReceita = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT descricao FROM categoriaReceita")
        linha = cur.fetchall()
        for l in linha:
            listaCategoriaReceita.append(l)
    return listaCategoriaReceita

def verUsuario(i):
    listaUsuario = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT nome FROM usuario")
        linha = cur.fetchall()
        for l in linha:
            listaUsuario.append(l)
    return listaUsuario

def verTipoDespesa(i):
    listaTipoDespesa = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT descricao FROM tipoDespesa")
        linha = cur.fetchall()
        for l in linha:
            listaTipoDespesa.append(l)
    return listaTipoDespesa

def verTipoPagamento(i):
    listaTipoPagamento = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT descricao FROM tipoPagamento")
        linha = cur.fetchall()
        for l in linha:
            listaTipoPagamento.append(l)
    return listaTipoPagamento

def verDespesas(i):
    listaDespesas = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM despesas")
        linha = cur.fetchall()
        for l in linha:
            listaDespesas.append(l)
    return listaDespesas

def verReceitas(i):
    listaReceitas = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM receitas")
        linha = cur.fetchall()
        for l in linha:
            listaReceitas.append(l)
    return listaReceitas