# Writen by Evert Ramos
import os
import json

from utils.print import sucesso, erro

# Raiz do projeto
RAIZ_PROJETO = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Arquivo de pedidos
ARQUIVO_PEDIDOS = os.path.join(RAIZ_PROJETO, 'dados', 'pedidos.json')

# Classe para tratar dos pedidos
class Pedido:
    # Para usar os camps como proriedade (pedido.produto)
    def __init__(self, nome, cpf, telefone=None):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone


    @classmethod
    def listar_todos_pedidos(cls):

        # Se não achar o arquivo cria um vazio
        if not os.path.exists(ARQUIVO_PEDIDOS):
            arquivo = open(ARQUIVO_PEDIDOS, 'w')
            # adicionar '{}' no arquivo:
            json.dump({}, arquivo)
            arquivo.close()

        try:
            with open(ARQUIVO_PEDIDOS, 'r') as arquivo:
                return json.load(arquivo)
        except json.JSONDecodeError:
            erro('Erro ao abrir arquivo: ' + ARQUIVO_PEDIDOS)
            return {}

    # Buscar Cliente pelo cpf (key)
    @classmethod
    def buscar_cliente(cls, cpf):
        todos_pedidos = cls.listar_todos_pedidos()
        # verificar cpf nas chaves do json 
        if cpf in todos_pedidos:
            cliente = todos_pedidos[cpf]
            return Cliente(cliente['nome'], cliente['cpf'], cliente['telefone'])
        return None
    

    # Para simplificar o sistema vamos considerar que todos os pedidos possuem CPF
    @classmethod
    def cadastrar_cliente(cls, nome, cpf, telefone=None):
        
        # Como não temos banco de dados, precisamos carregar tudo em memória
        # Isso não aconteceria em um sistema padrão... 
        pedidos = cls.listar_todos_pedidos()

        if cpf in pedidos:
            erro('Cliente já cadastrado.')
            return False

        novo_cliente = {
            'nome': nome,
            'cpf': cpf,
            'telefone': telefone
        }

        pedidos[cpf] = novo_cliente

        # Depois de carregar e adicionar, salva arquivo do zero... 'w'
        with open(ARQUIVO_PEDIDOS, 'w') as arquivo:
            # Pesquisei aqui pra ficar identado pra facilitar a leitura prof.
            json.dump(pedidos, arquivo, indent=2, ensure_ascii=False)

        sucesso('Cliente cadastrado com sucesso.')
        return True

