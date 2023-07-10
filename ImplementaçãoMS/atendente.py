from usuario import Usuario
from empresa import Empresa
from produto import Produto
from servico import Servico
class Atendente(Usuario):
    def __init__(self, nome, telefone, email, cpf, dataNascimento, senha, endereco, salario, cargo):
        super().__init__(nome, telefone, email, cpf, dataNascimento, senha, endereco)
        self.salario = salario
        self.cargo = cargo
    def cadastrarEmpresa(self):
            nome = input("\nDigite o nome da empresa: ")
            telefone = input("Digite o telefone da empresa: ")
            email = input("Digite o email da empresa: ")
            cnpj = input("Digite o cnpj da empresa: ")
            endereco = input("Digite o endereço da empresa: ")

            empresa = Empresa(nome, telefone, email, cnpj, endereco)
            print("\nEmpresa cadastrada com sucesso.")
            return Empresa.empresas

    def deletarEmpresa(self, cnpj):
        for empresa in Empresa.empresas:
            if empresa.cnpj == cnpj:
                Empresa.empresas.remove(empresa)
                print(f"\nA empresa de CNPJ {cnpj} foi removida com sucesso.")
                return
        print("\nEmpresa não encontrada.")

    def cadastrarProduto(self):
        codigo = input("\nDigite o codigo do produto: ")
        nome = input("Digite o nome do produto: ")
        preco = input("Digite o preço do produto: ")
        quantidade = input("Digite a quantidade do produto: ")
        garantia = input("Digite o tempo de garantia do produto: ")
        estado = input("Digite o estado(novo ou usado) do produto: ")

        produto = Produto(codigo, nome, preco, quantidade, garantia, estado)
        print("\nProduto cadastrado com sucesso.")
        return Produto.produtos

    def deletarProduto(self, codigo):
        for produto in Produto.produtos:
            if produto.codigo == codigo:
                Produto.produtos.remove(produto)
                print(f"\nO produto de código {codigo} foi removida com sucesso.")
                return
        print("\nProduto não encontrado.")

    def cadastrarServico(self):
        codigo = input("\nDigite o codigo do serviço: ")
        nome = input("Digite o nome do serviço: ")
        preco = input("Digite o preço do serviço: ")
        data = input("Digite a dara para qual o serviço vai ser agendado: ")

        servico = Servico(codigo, nome, preco, data)
        print("\nServiço cadastrado com sucesso.")
        return Servico.servicos

    def deletarServico(self, codigo):
        for servico in Servico.servicos:
            if servico.codigo == codigo:
                Servico.servicos.remove(servico)
                print(f"\nO serviço de código {codigo} foi removida com sucesso.")
                return
        print("\nServiço não encontrado.")
