
# Writen by Evert Ramos

# Import print functions
from modos.balcao import modo_balcao
from modos.cozinha import modo_cozinha
from modos.gestao import modo_gestao
from utils.print import limpar_tela, sucesso, aviso, padrao, erro, pergunta, espaco

# Escrever suas funções aqui
def main():
    sucesso('Sua função principal')

# Menu da aplicação
while True:
    limpar_tela()
    print()
    espaco()
    print()
    sucesso('\t\t\tSeja bem vindo ao Café Tia Rosa\n')
    print()
    aviso('Avisos:')
    aviso('- Poderá ter mais de uma instância do sistema rodando.')
    aviso('- Este sistema deve ser usado somente pelos funcionários do café.')
    espaco()
    print()
    padrao('Modos de operações do sistema:')
    padrao('1. [BALCÃO]\t- Atendimento de Clientes')
    padrao('2. [COZINHA]\t- Lista de Pedidos')
    padrao('3. [GESTÃO]\t- CadastroS')
    padrao('0. Sair')
    print()
    padrao('00. Para sair em qualquer tela!')
    print()
    
    try:
        escolha = int(pergunta('Escolha o modo de operação (inserir somente um número): '))
        print('<fim [ModoOp]>')
        print() 
    except ValueError:
        erro('Entrada inválida, por favor insira um número.')
        continue

    if escolha == 0:
        break
    elif escolha == 1:
        modo_balcao()
    elif escolha == 2:
        modo_cozinha()
    elif escolha == 3:
        modo_gestao()
    else:
        print('Opção inválida, tente novamente.')

print('Programa encerrado.')