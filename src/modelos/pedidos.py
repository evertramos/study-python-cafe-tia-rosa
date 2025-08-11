# Writen by Evert Ramos > copieie de clientes
import os
import json

from utils.print import sucesso, erro

# Raiz do projeto
RAIZ_PROJETO = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Arquivo de pedidos
ARQUIVO_PEDIDOS = os.path.join(RAIZ_PROJETO, 'dados', 'pedidos.json')

# Classe para tratar dos pedidos
class Pedido:
    # Para usar os campos como proriedade (pedido.produto)
    def __init__(self, cliente, produto, qtd):
        self.cliente = cliente
        self.produto = produto
        self.qtd = qtd

    @classmethod
    def listar_todos_pedidos(cls):

        # Se não achar o arquivo cria um vazio
        if not os.path.exists(ARQUIVO_PEDIDOS):
            arquivo = open(ARQUIVO_PEDIDOS, 'w')
            # adicionar '[]' no arquivo:
            json.dump([], arquivo)
            arquivo.close()

        try:
            with open(ARQUIVO_PEDIDOS, 'r') as arquivo:
                dados = json.load(arquivo)
                # Pesquisei aqui tb pra conseguir gerar o retorno como queria
                return [Pedido(d['cliente'], d['produto'], d['qtd']) for d in dados]
        except json.JSONDecodeError as e:
            erro('Erro ao abrir arquivo: ' + ARQUIVO_PEDIDOS)
            erro(f'Erro: {e}')
            return []

    # Prof.... simplifiquei ao máximo aqui ... desculpe se não ficou a contento!
    # de fato fiz de última hora.
    @classmethod
    def cadastrar_pedido(cls, cliente, produto, qtd):
        # Como não temos banco de dados, precisamos carregar tudo em memória
        # Isso não aconteceria em um sistema padrão... 
        pedidos = cls.listar_todos_pedidos()
        novo_pedido = Pedido(cliente, produto, qtd)
        pedidos.append(novo_pedido)

        # Depois de carregar e adicionar, salva arquivo do zero... 'w'
        with open(ARQUIVO_PEDIDOS, 'w') as arquivo:
            # Aqui usando esse __dict__ funcionou... 
            json.dump([pedido.__dict__ for pedido in pedidos], arquivo, indent=2, ensure_ascii=False)

        return True


    # @TODO:
    # - cancelar pedido
    # - id por pedido
    # - buscar pedido
    # - total to pedido
    # - somar pedidos
    # - criar data de pedido
    # - etc... (faltou muita coisa... )