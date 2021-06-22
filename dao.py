import sqlite3

from models import Mensagem

SQL_BUSCA_MENSAGENS = '''SELECT ID,NR,CATEGORIA,DESCRICAO  FROM MENSAGEM WHERE CATEGORIA = 1 AND NR = CASE WHEN IFNULL((SELECT ABS(RANDOM()) % (SELECT MAX(NR) FROM MENSAGEM WHERE CATEGORIA = 1)),1)  = 0 THEN 1 ELSE  IFNULL((SELECT ABS(RANDOM()) % (SELECT MAX(NR) FROM MENSAGEM WHERE CATEGORIA = 1)),1) END 
UNION 
SELECT ID,NR,CATEGORIA,DESCRICAO FROM MENSAGEM WHERE CATEGORIA = 2 AND NR = CASE WHEN IFNULL((SELECT ABS(RANDOM()) % (SELECT MAX(NR) FROM MENSAGEM WHERE CATEGORIA = 2)),1) = 0 THEN 1 ELSE IFNULL((SELECT ABS(RANDOM()) % (SELECT MAX(NR) FROM MENSAGEM WHERE CATEGORIA = 2)),1) END
UNION 
SELECT ID,NR,CATEGORIA,DESCRICAO FROM MENSAGEM WHERE CATEGORIA = 3 AND NR = CASE WHEN IFNULL((SELECT ABS(RANDOM()) % (SELECT MAX(NR) FROM MENSAGEM WHERE CATEGORIA = 3)),1) = 0 THEN 1 ELSE IFNULL((SELECT ABS(RANDOM()) % (SELECT MAX(NR) FROM MENSAGEM WHERE CATEGORIA = 3)),1) END '''

class MensagemDao:

    def listar(self):
        conn = sqlite3.connect('mensagens.db')
        cursor = conn.cursor()
        cursor.execute(SQL_BUSCA_MENSAGENS);
        mensagens = traduz_mensagens(cursor.fetchall())
        return mensagens


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def traduz_mensagens(mensagens):
    def cria_mensagem_com_tupla(tupla):
        return Mensagem(tupla[1], tupla[2], tupla[3], id=tupla[0])
    return list(map(cria_mensagem_com_tupla, mensagens))
