# Writen by Evert Ramos

# importar limpar_tela
from modelos.clientes import Cliente
from modelos.produtos import Produto
from utils.print import limpar_tela, espaco, sucesso, aviso, padrao, pergunta, erro

# Modo Gestão
def modo_gestao():

    limpar_tela()
    
    while True:
        print('')
        espaco()
        sucesso('\t\t\tCafé Tia Rosa - MODO GESTÃO')
        espaco()
        print()
        padrao('Opções:')
        padrao('1. Cadastrar Cliente')
        padrao('2. Cadastrar Produto')
        print()
        padrao('3. Listar Clientes')
        padrao('4. Listar Produtos')
        padrao('0. Voltar ao menu principal')
        print()
        padrao('00. Sair do sistema')
        print()
        
        try:
            escolha = int(pergunta('Escolha o modo de operação (inserir somente um número): '))
            print() 
        except ValueError:
            erro('Entrada inválida, por favor insira um número.')
            continue

        if escolha == 0:
            break
        elif escolha == 1:
            padrao('Insira os dados do Cliente.')
            nome = pergunta('Nome: ')
            cpf = pergunta('CPF (somente números): ')
            telefone = pergunta('Telefone (somente números): ')
            Cliente.cadastrar_cliente(nome, cpf, telefone)
            cliente = Cliente.buscar_cliente(cpf)
            sucesso(f'Cliente: {cliente.nome}')

        elif escolha == 2:
            try:
                padrao('Insira os dados do Produto.')
                id = pergunta('ID: ')
                nome = pergunta('Nome: ')
                preco = float(pergunta('Preço (somente número): '))
                Produto.cadastrar_produto(id, nome, preco)
            except ValueError:
                erro('Entrada inválida, por favor tente novamente, insira o preço somente como um número.')
                continue
        elif escolha == 3:
            clientes = Cliente.listar_todos_clientes()
            # Loop em clientes para mostrar como tabela formatada
            # prof. pesquisei aqui para deixar a tabela mais bonita!! =)
            padrao(f"{'NOME':<20}{'CPF':<15}{'Telefone':<15}")
            padrao('-' * 50)
            for cliente in clientes:
                padrao(f'{cliente.nome:<20}{cliente.cpf:<15}{cliente.telefone:<15}')
        elif escolha == 4:
            produtos = Produto.listar_todos_produtos()
            # Loop em produtos para mostrar como tabela formatada
            padrao(f"{'ID':<5}{'NOME':<20}{'PREÇO':<15}")
            padrao('-' * 50)
            for produto in produtos:
                padrao(f'{produto.id:<5}{produto.nome:<20}{produto.preco:<15}')
        else:
            print('Opção inválida, tente novamente.')



