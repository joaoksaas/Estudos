class Produto:
    produtos = []

    def __init__(self, codigo, nome, preco, quantidade, garantia, estado):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        self.garantia = garantia
        self.estado = estado
        Produto.produtos.append(self)

    def __str__(self):
        return f"Código: {self.codigo}, Nome: {self.nome}, Preço: {self.preco}, Quantidade: {self.quantidade}, Garantia: {self.garantia}, Estado: {self.estado}"

