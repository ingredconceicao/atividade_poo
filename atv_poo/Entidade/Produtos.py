class Produtos:
   def __init__(self,prod_nome, custo, estoque, categoria):
       self.prod_nome = prod_nome.upper()
       self.custo = custo
       self.estoque = estoque
       self.categoria = categoria
       self.total = 0

   def __str__(self):
       return f'Produto: {self.prod_nome} / Custo: R${self.custo} ' \
              f'\n Categoria: {self.categoria} / Estoque: {self.estoque}' \
              f'\n Preço de venda: R${self.total}'

   @staticmethod
   def CadastrarProduto(lista_prod, lista_cat):
        prod_nome = input('Digite o nome do produto: ').upper()
        preco = float(input('Digite o preço do produto: '))
        categoria = input('Digite a categoria do produto: ')
        estoque = int(input('Digite a quantidade de produtos em estoque: '))
        if estoque < 0:
            print('O número de itens em estoque não pode ser negativo')
            estoque = int(input('Digite novamente a quantidade de produtos em estoque: '))

   @staticmethod
   def ExcluirProduto(lista_prod):
       remover_item = input('Digite a categoria que deseja remover').upper()
       for i, item in enumerate(lista_prod):
           if remover_item == item:
               lista_prod.remove(item)
               print(f'{item} foi removido da lista categoria')
           else:
               print('Produto não encontrado')

   @staticmethod
   def ProdutosCadastrados(lista_prod):

       print('Produtos cadastrados: ')
       for item in (lista_prod):
           print(item)

   @staticmethod
   def AdicionarEstoque(Produto):

       adicionar = int(input('Quantos itens deseja adicionar no estoque?'))
       if adicionar>=0:
           Produto.estoque += adicionar
       else:
            print('Não é possível adicionar quantidade de estoque menor que 0')

   @staticmethod
   def RemoverEstoque(Produto):

       adicionar = int(input('Quantos itens deseja adicionar no estoque?'))
       if adicionar >= 0:
           Produto.estoque -= adicionar
       else:
            print('Não é possível remover quantidade de estoque menor que 0')