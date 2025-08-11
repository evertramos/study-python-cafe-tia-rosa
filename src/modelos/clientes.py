# Writen by Evert Ramos
import os
import json

from utils.print import sucesso, erro

# Raiz do projeto
RAIZ_PROJETO = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Arquivo de Clientes
ARQUIVO_CLIENTES = os.path.join(RAIZ_PROJETO, 'dados', 'clientes.json')

# Classe para tratar dos clientes
class Cliente:
    # Prof. aqui pesquisei tbm pra saber como fazia pra usar cliente.nome fora da classe,
    # como usei no balcao.py
    def __init__(self, nome, cpf, telefone=None):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone

    @classmethod
    def listar_todos_clientes(cls, retornar_dict=False):
        # Se não achar o arquivo cria um vazio
        if not os.path.exists(ARQUIVO_CLIENTES):
            arquivo = open(ARQUIVO_CLIENTES, 'w')
            # adicionar '{}' no arquivo:
            json.dump({}, arquivo)
            arquivo.close()

        try:
            with open(ARQUIVO_CLIENTES, 'r') as arquivo:
                if retornar_dict:
                    return json.load(arquivo)
                dados = json.load(arquivo)
                # Pesquisei aqui tb pra conseguir gerar o retorno como queria 
                return [Cliente(d['nome'], cpf, d.get('telefone')) for cpf, d in dados.items()]
        except json.JSONDecodeError:
            erro('Erro ao abrir arquivo: ' + ARQUIVO_CLIENTES)
            return {}

    # Buscar Cliente pelo cpf (key)
    @classmethod
    def buscar_cliente(cls, cpf):
        todos_clientes = cls.listar_todos_clientes(True)
        # verificar cpf nas chaves do json 
        if cpf in todos_clientes:
            cliente = todos_clientes[cpf]
            return Cliente(cliente['nome'], cliente['cpf'], cliente['telefone'])
        return None
    

    # Para simplificar o sistema vamos considerar que todos os clientes possuem CPF
    @classmethod
    def cadastrar_cliente(cls, nome, cpf, telefone=None):
        
        # Como não temos banco de dados, precisamos carregar tudo em memória
        # Isso não aconteceria em um sistema padrão... 
        clientes = cls.listar_todos_clientes(True)

        if cpf in clientes:
            erro('Cliente já cadastrado.')
            return False

        novo_cliente = {
            'nome': nome,
            'cpf': cpf,
            'telefone': telefone
        }

        clientes[cpf] = novo_cliente

        # Depois de carregar e adicionar, salva arquivo do zero... 'w'
        with open(ARQUIVO_CLIENTES, 'w') as arquivo:
            # Pesquisei aqui pra ficar identado pra facilitar a leitura prof.
            json.dump(clientes, arquivo, indent=2, ensure_ascii=False)

        sucesso('Cliente cadastrado com sucesso.')
        return True

