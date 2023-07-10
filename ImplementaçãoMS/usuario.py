from produto import Produto
class Usuario:
    clientes = []

    def __init__(self, nome, telefone, email, cpf, dataNascimento, senha, endereco):
        self._nome = nome
        self._telefone = telefone
        self._email = email
        self._cpf = cpf
        self._dataNascimento = dataNascimento
        self._senha = senha
        self._endereco = endereco
        self._carrinho = []
        self._estado = False
        Usuario.clientes.append(self)
    @property
    def nome(self):
        return self._nome

    @property
    def telefone(self):
        return self._telefone

    @property
    def email(self):
        return self._email

    @property
    def cpf(self):
        return self._cpf

    @property
    def dataNascimento(self):
        return self._dataNascimento

    @property
    def senha(self):
        return self._senha

    @property
    def estado(self):
        return self._estado

    @nome.setter
    def nome(self, nome):
        _nome = nome

    @telefone.setter
    def telefone(self, telefone):
        _telefone = telefone

    @email.setter
    def nome(self, email):
        _email = email

    @cpf.setter
    def nome(self, cpf):
        _cpf = cpf

    @dataNascimento.setter
    def nome(self, dataNascimento):
        _dataNascimento = dataNascimento

    @senha.setter
    def senha(self, senha):
        _senha = senha

    @estado.setter
    def senha(self, estado):
        _estado = estado

    def logarUsuario(self, email, senha):
        for cliente in Usuario.clientes:
            if senha == cliente._senha and email == cliente._email:
                print('\nLogin efetuado com sucesso.')
                self._estado = True
                return cliente, True
        print('\nEmail ou senha incorretos.')
        return None, False

    def deslogarUsuario(self):
        self._estado = False

    def adicionarProdutoCarrinho(self, codigo_produto, qnt):
        if not self.estado:
            print('\nVocê deve fazer login para poder colocar produtos em seu carrinho.')
            return
        produto = next((p for p in Produto.produtos if p.codigo == codigo_produto), None)
        if produto:
            if produto.quantidade >= qnt:
                self._carrinho.append((produto, qnt))
                print(f"\nProduto '{produto.nome}' ({qnt}) adicionado ao carrinho.")
            else:
                print(f"\nProduto '{produto.nome}' não pode ser inserido, pois a quantidade em estoque ({produto.quantidade}) é menor que a quantidade desejada ({qnt}).")
        else:
            print("\nProduto não encontrado.")

    def removerProdutoCarrinho(self, codigo_produto, qnt):
        for i, item in enumerate(self._carrinho):
            produto, quantidade = item
            if produto.codigo == codigo_produto:
                if quantidade >= qnt:
                    quantidade -= qnt
                    self._carrinho[i] = (produto, quantidade)
                    print(f"\nProduto '{produto.nome}' ({qnt}) removido do carrinho.")
                    if quantidade == 0:
                        self._carrinho.pop(i)
                else:
                    print(f"\nA quantidade informada ({qnt}) é maior do que a quantidade disponível ({quantidade}) do produto '{produto.nome}' no carrinho.")
                return
        print("\nProduto não encontrado no carrinho.")
    def realizarCompra(self):
        total = 0
        for item in self._carrinho:
            produto, quantidade = item
            total += produto.preco * quantidade
            produto.quantidade -= quantidade
        self.emitirNotaFiscal()
        self.esvaziarCarrinho()
        return total

    def esvaziarCarrinho(self):
        self._carrinho = []
    def emitirNotaFiscal(self, recebeNome=None):
        print("----- Nota Fiscal -----")
        subtotal = 0

        if recebeNome is None:
            recebeNome = self._nome  # Acessa o nome do cliente na classe Usuario
            print(f"Nome: {recebeNome}")
            print(f"CPF: {self._cpf}")
            print("-----------------------------")
        else:
            print(f"Nome: {recebeNome}")
            print("-----------------------------")
        for item in self._carrinho:
            produto, quantidade = item
            print(f"Produto: {produto.nome}")
            print(f"Quantidade: {quantidade}")
            print(f"Preço Unitário: R${produto.preco}")
            subtotal += produto.preco * quantidade
            print("-----------------------------")

        print(f"Subtotal: R${subtotal}\n")

    def imprimirCarrinho(self):
        print("----- Carrinho de Compras -----")
        for item in self._carrinho:
            produto, quantidade = item
            print(f"Código: {produto.codigo}")
            print(f"Produto: {produto.nome}")
            print(f"Quantidade: {quantidade}")
            print(f"Preço Unitário: R${produto.preco}")
            print(f"Subtotal: R${produto.preco * quantidade}")
            print("-----------------------------\n")

    def cadastrarCliente(self):
        nome = input("\nDigite o nome do cliente: ")
        telefone = input("Digite telefone do cliente: ")
        email = input("Digite o email do cliente: ")
        cpf = input("Digite o CPF do cliente: ")
        dataNascimento = input("Digite a data de nascimento do cliente: ")
        senha = input("Digite a senha do cliente: ")
        endereco = input("Digite o endereço do cliente: ")

        cliente = Usuario(nome, telefone, email, cpf, dataNascimento, senha, endereco)
        print("\nCliente cadastrado com sucesso.")

        return cliente