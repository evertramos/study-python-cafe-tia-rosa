# Writen by Evert Ramos > copiado de balcao

import json
from modelos.pedidos import Pedido
from utils.print import limpar_tela, espaco, sucesso, aviso, padrao, pergunta, erro

# Modo Cozinha
def modo_cozinha():

    limpar_tela()
    
    while True:
        print('')
        espaco()
        sucesso('\t\t\tCafé Tia Rosa - MODO COZINHA')
        espaco()
        print()
        padrao('Opções:')
        padrao('1. Listar Pedidos')
        # padrao('2. Entregar Pedidos') # @TODO - fazer entregar pedidos
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
            # @TODO - Implementar timer pra ficar lendo os pedidos
            pedidos = Pedido.listar_todos_pedidos()
            # print(pedidos)
            padrao(f"{'CLIENTE':<20}{'PRODUTO':<15}{'QTD':<15}{'STATUS':<15}")
            padrao('-' * 50)
            for pedido in pedidos:
                padrao(f'{pedido.cliente:<20}{pedido.produto:<15}{pedido.qtd:<15}{pedido.status:<15}')
        else:
            print('Opção inválida, tente novamente.')



