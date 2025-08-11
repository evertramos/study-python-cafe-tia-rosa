# Writen by Evert Ramos > copieie de clientes
import os
import json

from utils.print import sucesso, erro

# Raiz do projeto
RAIZ_PROJETO = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Arquivo de produtos
ARQUIVO_PRODUTOS = os.path.join(RAIZ_PROJETO, 'dados', 'produtos.json')

# Classe para tratar dos produtos
class Produto:
    # Para usar como atributos da classe
    def __init__(self, id, nome, preco):
        self.id = id
        self.nome = nome
        self.preco = preco

    @classmethod
    def listar_todos_produtos(cls, retornar_dict=False):

        # Se não achar o arquivo cria um vazio
        if not os.path.exists(ARQUIVO_PRODUTOS):
            arquivo = open(ARQUIVO_PRODUTOS, 'w')
            # adicionar '{}' no arquivo:
            json.dump({}, arquivo)
            arquivo.close()

        try:
            with open(ARQUIVO_PRODUTOS, 'r') as arquivo:
                dados = json.load(arquivo)
                if retornar_dict:
                    return dados
                # copiei de Clientes...
                return [Produto(id, d['nome'], d['preco']) for id, d in dados.items()]
        except json.JSONDecodeError:
            erro('Erro ao abrir arquivo: ' + ARQUIVO_PRODUTOS)
            return {}

    # Buscar Produto pelo id (key)
    @classmethod
    def buscar_produto(cls, id):
        todos_produtos = cls.listar_todos_produtos()
        # verificar id nas chaves do json
        if id in todos_produtos:
            produto = todos_produtos[id]
            return Produto(produto['id'], produto['nome'], produto['preco'])
        return None

    # Para simplificar o sistema vamos considerar que todos os produtos possuem ID
    @classmethod
    def cadastrar_produto(cls, id, nome, preco):
        
        # prof... id seria sequencial.. mas deixei aqui pra facilitar!

        # Como não temos banco de dados, precisamos carregar tudo em memória
        # Isso não aconteceria em um sistema padrão... 
        produtos = cls.listar_todos_produtos(True)

        if id in produtos:
            erro('Produto já cadastrado.')
            return False

        novo_produto = {
            'id': id,
            'nome': nome,
            'preco': preco
        }

        produtos[id] = novo_produto

        # Depois de carregar e adicionar, salva arquivo do zero... 'w'

        novo_produto = {
            'nome': nome,
            'preco': preco
        }

        produtos[id] = novo_produto

        # Depois de carregar e adicionar, salva arquivo do zero... 'w'
        with open(ARQUIVO_PRODUTOS, 'w') as arquivo:
            # Pesquisei aqui pra ficar identado pra facilitar a leitura prof.
            json.dump(produtos, arquivo, indent=2, ensure_ascii=False)

        sucesso('Produto cadastrado com sucesso.')
        return True

