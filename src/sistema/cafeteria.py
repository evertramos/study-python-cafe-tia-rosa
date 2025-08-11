# Writen by Evert Ramos

from utils.print import sucesso, erro, padrao, aviso, pergunta

class Cafeteria:
    def __init__(self):
        self.produtos = []
        self.clientes = []
        self.pedidos = []

    def buscar_cliente(self, cpf: int):
        return next((c for c in self.clientes if c.cpf == cpf), None)


    def cadastrar_produto(self, codigo, nome, preco):
        self.produtos.append(Produto(codigo, nome, preco))

    def cadastrar_cliente(self, nome, cpf):
        self.clientes.append(Cliente(nome, cpf))

    # -------------------- BUSCA -----------------------

    def buscar_produto(self, codigo):
        return next((p for p in self.produtos if p.codigo == codigo), None)

    def buscar_cliente(self, cpf):
        return next((c for c in self.clientes if c.cpf == cpf), None)

    # -------------------- PEDIDOS ---------------------

    def novo_pedido(self, cpf, itens):
        cliente = self.buscar_cliente(cpf)
        if not cliente:
            erro('Cliente não encontrado.')
            return

        pedido = Pedido(cliente)
        for codigo_prod, qtd in itens:
            produto = self.buscar_produto(codigo_prod)
            if produto:
                pedido.adicionar_item(produto, qtd)
            else:
                erro(f'Produto código {codigo_prod} não encontrado.')

        self.pedidos.append(pedido)
        sucesso('Pedido registrado com sucesso!')
        pedido.resumo()

    # -------------------- EXIBIÇÕES -------------------

    def listar_produtos(self):
        padrao('Produtos disponíveis:')
        for p in self.produtos:
            print(f'  {p}')

    def listar_pedidos(self):
        if not self.pedidos:
            aviso('Nenhum pedido registrado.')
            return
        padrao('Histórico de pedidos:')
        for i, p in enumerate(self.pedidos, 1):
            print(f'\nPedido #{i}')
            p.resumo()

    def listar_clientes(self):
        padrao('Clientes cadastrados:')
        for c in self.clientes:
            print(f'  {c}')

    # ------------------ MODO BALCÃO --------------------

    def modo_balcao(self):
        while True:
            print()
            padrao('[MODO BALCÃO] - Atendimento ao Cliente')
            padrao('1. Cadastrar Cliente')
            padrao('2. Fazer Pedido')
            padrao('0. Voltar ao Menu Principal')
            print()

            try:
                opcao = int(pergunta('Escolha uma opção: '))
            except ValueError:
                erro('Entrada inválida. Digite um número.')
                continue

            if opcao == 0:
                break

            elif opcao == 1:
                nome = pergunta('Nome do cliente: ')
                cpf = pergunta('CPF do cliente: ')
                if self.buscar_cliente(cpf):
                    aviso('Cliente já cadastrado.')
                else:
                    self.cadastrar_cliente(nome, cpf)
                    sucesso('Cliente cadastrado com sucesso!')

            elif opcao == 2:
                cpf = pergunta('CPF do cliente: ')
                cliente = self.buscar_cliente(cpf)
                if not cliente:
                    erro('Cliente não encontrado. Cadastre-o primeiro.')
                    continue

                self.listar_produtos()
                itens = []
                while True:
                    codigo = pergunta('Código do produto (0 para finalizar): ')
                    if codigo == '0':
                        break
                    try:
                        codigo = int(codigo)
                        produto = self.buscar_produto(codigo)
                        if not produto:
                            erro('Produto não encontrado.')
                            continue
                        qtd = int(pergunta(f'Quantidade de {produto.nome}: '))
                        itens.append((codigo, qtd))
                    except ValueError:
                        erro('Entrada inválida.')
                if itens:
                    self.novo_pedido(cpf, itens)
                else:
                    aviso('Nenhum item foi adicionado ao pedido.')

            else:
                erro('Opção inválida. Tente novamente.')
