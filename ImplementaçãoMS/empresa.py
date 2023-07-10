class Empresa:
    empresas = []
    def __init__(self, nome, telefone, email, cnpj, endereco):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.cnpj = cnpj
        self.endereco = endereco
        Empresa.empresas.append(self)

    def __str__(self):
        return f"Nome: {self.nome}, Telefone: {self.telefone}, email: {self.email}, cpnj: {self.cnpj}, enderco: {self.endereco}"

