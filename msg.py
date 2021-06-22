import flask
from flask import Flask,request, jsonify
import json

app = Flask(__name__)

mensagens = [
    {
        'id': 1,
        'name': "Mensagem 1",
        "description": "Esta eh a mensagem 1"
    },
    {
        "id": 2,
        "name": "Mensagem 2",
        "description": "Esta eh a mensagem 2"
    },
    {
        "id": 3,
        "name": "Mensagem 3",
        "description": "Esta eh a mensagem 3"
    }
]


@app.route('/')
def home():
    return "App esta funcionando!!!"


@app.route('/api/v1/mensagem/all', methods=['GET'])
def msg_all():
    return json.dumps(mensagens)


@app.route('/api/v1/mensagens', methods=['GET'])
def msg_id():
    ##http://127.0.0.1:5000/api/v1/mensagens?id=1
    # Verifica se ID foi fornecido como parte da URL.
    # Se ID foi fornecida, atribui a uma variável
    # Se não retorna um erro no navegador
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Erro: Informe o id da mensagem"

    # Cria uma lista vazia para nosso results
    results = []

    # Faz um um loop para encontrar o ID solicitado
    for m in mensagens:
        if m['id'] == id:
            results.append(m)

    # Usa a função jsonify  para converter nossa lista para o formato JSON.
    return jsonify(results)

#http://127.0.0.1:5000/api/v1/mensagens?id=0
#obs: quando for criar o arquivo voce deve no terminal fazer: set FLASK_APP=msg.py e para rodar flask run
#no browser digite http://127.0.0.1:5000/api/tasks
#https://stackoverflow.com/questions/51119495/how-to-setup-environment-variables-for-flask-run-on-windows