import os

# Separamos aqui para melhor organização do código

def printc(text, color_code):
    print(f'\033[{color_code}m{text}\033[0m')

def erro(text):
    printc('\n[ERRO] ' + text, '91')  # Vermelho

def sucesso(text):
    printc(text, '92')  # Verde

def aviso(text):
    printc(text, '93')  # Amarelo

def padrao(text):
    printc(text, '33')  # Amarelo padrão

# Espaçamento
def espaco():
    sucesso('#------------------------------------------------------------------------------#')

# Limpar a tela
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função de input colorido
def inputc(text, color_code):
    escolha = input(f'\033[{color_code}m{text}\033[0m')
    if escolha == '00':
        padrao('Saindo do programa...')
        exit()
    else:
        return escolha

def pergunta(text):
    return inputc(text, '94')  # Azul
