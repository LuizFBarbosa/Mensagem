import flask
from flask import Flask, request, jsonify, render_template
import sqlite3
from dao import MensagemDao

app = Flask(__name__)
app.config["DEBUG"] = True

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

mensamgem_dao = MensagemDao()

@app.route('/', methods=['GET'])
def home():
    lista = mensamgem_dao.listar()
    return render_template('listaN1.html', titulo='Mensagens', mensagens=lista)


@app.route('/api/v1/mensagem/msgluz/all', methods=['GET'])
def msgluz_all():
    conn = sqlite3.connect('mensagens.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_msgs = cur.execute('SELECT NR,DESCRICAO FROM MENSAGEM WHERE CATEGORIA = 1;').fetchall()

    return jsonify(all_msgs)


@app.route('/api/v1/mensagem/minuto/all', methods=['GET'])
def msgminuto_all():
    conn = sqlite3.connect('mensagens.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_msgs = cur.execute('SELECT NR,DESCRICAO FROM MENSAGEM WHERE CATEGORIA = 2;').fetchall()

    return jsonify(all_msgs)


@app.route('/api/v1/mensagem/jesus/all', methods=['GET'])
def msgjesus_all():
    conn = sqlite3.connect('mensagens.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_msgs = cur.execute('SELECT NR,DESCRICAO FROM MENSAGEM WHERE CATEGORIA = 3;').fetchall()

    return jsonify(all_msgs)


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>Página não encontrada.</p>", 404


@app.route('/api/v1/mensagem/msg', methods=['GET'])
def msg_filter():
    query_parameters = request.args

    nr = query_parameters.get('nr')
    tipo = query_parameters.get('tipo')

    query = "SELECT DESCRICAO FROM MENSAGEM WHERE "
    to_filter = []

    if nr:
        query += ' NR=? AND '
        to_filter.append(nr)
    if tipo:
        query += ' CATEGORIA=? '
        to_filter.append(tipo)
    if not (nr or tipo):
        return page_not_found(404)

    #query = query[:-4] + ';'

    conn = sqlite3.connect('mensagens.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()

    results = cur.execute(query, to_filter).fetchall()

    return jsonify(results)

#app.run()

#http://127.0.0.1:5000/api/v1/mensagem/msgluz/all
#obs: quando for criar o arquivo voce deve no terminal fazer: set FLASK_APP=msgDB.py e para rodar flask run
#no browser digite http://127.0.0.1:5000/api/v1/mensagem/msg?nr=12&categoria=1
#https://stackoverflow.com/questions/51119495/how-to-setup-environment-variables-for-flask-run-on-windows