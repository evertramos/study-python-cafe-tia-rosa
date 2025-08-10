
# Writen by Evert Ramos

# Import print functions
from utils.print import sucesso, aviso, padrao, erro, pergunta

# Escrever suas funções aqui
def main():
    sucesso('Sua função principal')

# Menu da aplicação
while True:
    print()
    padrao('Menu Principal:')
    padrao('1. Opção 1')
    padrao('2. Opção 2')
    padrao('0. Sair')
    print()
    padrao('00. Para sair em qualquer tela!')
    print()

    try:
        escolha = int(pergunta('Escolha uma opção: '))
        print('<fim [Menu]')
        print() 
    except ValueError:
        erro('Entrada inválida, por favor insira um número.')
        continue

    if escolha == 0:
        break
    elif escolha == 1:
        main()
    elif escolha == 2:
        print('Você escolheu a Opção 2.')
    else:
        print('Opção inválida, tente novamente.')

print('Programa encerrado.')