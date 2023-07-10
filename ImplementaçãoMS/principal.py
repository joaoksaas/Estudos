from produto import Produto
from usuario import Usuario
from atendente import Atendente
from servico import Servico
from empresa import Empresa

class Principal:

    a = Usuario('teste', 'teste', 'teste', 'teste', 'teste', 'teste', 'teste')
    b = Atendente('testea', 'testea', 'testea', 'testea', 'testea', 'testea', 'testea', 'testea', 'testea')
    produto = Produto(1, "Camiseta", 29.99, 10, 5, 'usado')
    produto = Produto(2, "Calça", 49.99, 5, 10, 'novo')
    produto = Produto(3, "Tênis", 99.99, 3, 12, 'novo')

    servico = Servico(1, "formatacao", 29.99, '10/10/2010')
    servico = Servico(2, "Limpar", 49.99, '5/05/2055')
    servico = Servico(3, "instalaçao de hardware", 99.99, '3/06/1998')

    empresa = Empresa('nome', 'telefone', 'email', 'cnph', 'endereço')
    empresa = Empresa('nome1', 'telefone', 'email', '111', 'endereço')
    empresa = Empresa('nome2', 'telefone', 'email', '2222', 'endereço')
#--------------------------------------------------------------------------------------------------

    while (True):
        print("\n============================= MENU =============================")
        print("  1 - Entrar.    2 - Cadastrar.    3 - Atendente")
        print("============================= MENU =============================")

        valor = input('\nescolha uma opção: ')
        match valor:
            case '1':
                email = input("\nDigite o email do cliente: ")
                senha = input("Digite a senha do cliente: ")
                a, status = a.logarUsuario(email, senha)
                if status == True:
                    while(True):
                        print("\n============================= MENU =============================")
                        print("  1 - Ver produtos. 2 - Adicionar produto no carrinho. 3 - Ver carrinho.")
                        print("  4 - Remover produto do carrinho. 5 - Comprar. 6 - Sair")
                        print("============================= MENU =============================")
                        valor2 = input('escolha uma opção: ')
                        match valor2:
                            case '1':
                                for produto in Produto.produtos:
                                    print(produto)

                            case '2':
                                cod = int(input('\ndigite o codigo do produto para ser adicionado'))
                                quant = int(input('digite a quantidade do produto para ser adicionado'))
                                a.adicionarProdutoCarrinho(cod, quant)

                            case '3':
                                print('seu carrinho :\n')
                                a.imprimirCarrinho()

                            case '4':
                                print('\nRemover produto do carrinho\n')
                                cod = int(input('digite o codigo do produto para ser removido'))
                                quant = int(input('digite a quantidade do produto para ser removido'))
                                a.removerProdutoCarrinho(cod, quant)

                            case '5':
                                print('Comprar\n')
                                a.realizarCompra()

                            case '6':
                                a.deslogarUsuario()
                                break
            case '2':
                print('cadastre-se :\n')
                a = a.cadastrarCliente()

            case '3':
                while(True):
                    print("\n============================= MENU =============================")
                    print("========= 1 - Cadastrar Empresa. 2 - Cadastrar Produto. =========")
                    print("========= 3 - Cadastrar Serviço. 4 - Deletar Empresa. ===========")
                    print("========= 5 - Deletar Serviço. 6 - Deletar Produto. =============")
                    print("========= 7 - Listar Produtos. 8 - Listar Empresas. =============")
                    print("========= 9 - Listar Serviços. 0 - Sair do Atendente. ===========")
                    print("============================= MENU =============================")
                    valor3 = input('\nescolha uma opção: ')
                    match valor3:
                        case '1':
                            b.cadastrarEmpresa()
                        case '2':
                            b.cadastrarProduto()
                        case '3':
                            b.cadastrarServico()
                        case '4':
                            cod = int(input('\ndigite o CNPJ da empresa para ser removida'))
                            b.deletarEmpresa(cod)
                        case '5':
                            cod = int(input('\ndigite o codigo do serviço para ser removido'))
                            b.deletarServico(cod)
                        case '6':
                            cod = int(input('\ndigite o codigo do produto para ser removido'))
                            b.deletarProduto(2)
                        case '7':
                            for produto in Produto.produtos:
                                print(produto)
                        case '8':
                            for empresa in Empresa.empresas:
                                print(empresa)
                        case '9':
                            for servico in Servico.servicos:
                                print(servico)
                        case '0':
                            break
    
