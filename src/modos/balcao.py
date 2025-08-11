# Writen by Evert Ramos

# importar limpar_tela
from modelos.clientes import Cliente
from modelos.pedidos import Pedido
from utils.print import limpar_tela, espaco, sucesso, aviso, padrao, pergunta, erro

# Modeo Balcão
def modo_balcao():

    limpar_tela()
    
    while True:
        print('')
        espaco()
        sucesso('\t\t\tCafé Tia Rosa - MODO BALCÃO')
        espaco()
        print()
        padrao('Opções:')
        padrao('1. Fazer Pedido')
        print()
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
            # Para facilitar presumimos que todo cliente tenha CPF
            cpf = pergunta('CPF do cliente (somente números): ')
            
            # print(Cliente.carregar_clientes())

            cliente = Cliente.buscar_cliente(cpf)
            if not cliente:
                erro('Cliente não encontrado.')
                padrao('Por favor, cadastre o cliente primeiro.')
                nome = pergunta('Nome: ')
                cpf = pergunta('CPF (somente números): ')
                telefone = pergunta('Telefone (somente números): ')
                Cliente.cadastrar_cliente(nome, cpf, telefone)
                cliente = Cliente.buscar_cliente(cpf)
            sucesso(f'Cliente: {cliente.nome}')

            produto = pergunta('Produto: ')
            try:
                qtd = int(pergunta('Quantidade: '))
            except ValueError:
                erro('Quantidade inválida, por favor insira um número para quantidade.')
                continue

            # Pra facilitar coloquei aqui apenas o cpf-nome do cliente
            Pedido.cadastrar_pedido(cliente.cpf + '-' + cliente.nome, produto, qtd, 'pendente')

            sucesso('Pedido cadastrado com sucesso.')
        else:
            print('Opção inválida, tente novamente.')



