class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"{self.nome} - R${self.preco:.2f}"


class Carrinho:
    def __init__(self):
        self.itens = []

    def adicionar_produto(self, produto, quantidade=1):
        self.itens.append((produto, quantidade))

    def calcular_total(self):
        total = 0
        for produto, quantidade in self.itens:
            total += produto.preco * quantidade
        return total

    def mostrar_itens(self):
        if not self.itens:
            print("Carrinho vazio.")
        else:
            for produto, quantidade in self.itens:
                print(f"{produto.nome} (x{quantidade}) - R${produto.preco * quantidade:.2f}")


class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.carrinho = Carrinho()

    def adicionar_ao_carrinho(self, produto, quantidade=1):
        self.carrinho.adicionar_produto(produto, quantidade)
        print(f"{quantidade}x {produto.nome} adicionado(s) ao carrinho.")

    def finalizar_compra(self):
        print(f"\nCliente: {self.nome}")
        print("Itens no carrinho:")
        self.carrinho.mostrar_itens()
        print(f"Total da compra: R${self.carrinho.calcular_total():.2f}")


# Programa principal
if __name__ == "__main__":
    print("=== Sistema de Compras ===")
    nome_cliente = input("Digite o nome do cliente: ")
    cliente = Cliente(nome_cliente)

    while True:
        print("\n1 - Adicionar produto")
        print("2 - Ver carrinho")
        print("3 - Finalizar compra")
        print("4 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome_produto = input("Nome do produto: ")
            preco_produto = float(input("Preço do produto: R$"))
            quantidade = int(input("Quantidade: "))
            produto = Produto(nome_produto, preco_produto)
            cliente.adicionar_ao_carrinho(produto, quantidade)

        elif opcao == "2":
            print("\n--- Itens no carrinho ---")
            cliente.carrinho.mostrar_itens()
            print(f"Total parcial: R${cliente.carrinho.calcular_total():.2f}")

        elif opcao == "3":
            cliente.finalizar_compra()
            break

        elif opcao == "4":
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida! Tente novamente.")
