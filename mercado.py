class Produto:
    def __init__(self, nome, preco, quantidade_estoque):
        self.nome = nome
        self.preco = preco
        self.quantidade_estoque = quantidade_estoque
class Carrinho:
    def __init__(self):
        self.itens = []
    def adicionar_produto(self, produto):
        self.itens.append(produto)
    def listar_itens(self):
        for item in self.itens:
            print(f'Produto: {item.nome} - Preço: R${item.preco:.2f}')
    def calcular_total(self):
        total = sum(item.preco for item in self.itens)
        print(f'Total: R${total:.2f}')

produto1 = Produto('Milho', 4, 12)
produto2 = Produto('Ervilha', 2, 17)
produto3 = Produto('Café', 15, 25)

carro = Carrinho()
carro.adicionar_produto(produto1)
carro.adicionar_produto(produto2)
carro.adicionar_produto(produto3)
carro.listar_itens()
carro.calcular_total()
