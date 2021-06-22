class Mensagem:
    def __init__(self, nr, categoria, descricao, id=None):
        self.id = id
        self.nr = nr
        self.categoria = categoria
        self.descricao = descricao