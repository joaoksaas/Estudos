class Servico:
    servicos = []

    def __init__(self, codigo, nome, preco, data):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco
        self.data = data
        Servico.servicos.append(self)

    def __str__(self):
        return f"Código: {self.codigo}, Nome: {self.nome}, Preço: {self.preco}, Data: {self.data}"
