class Categoria:
   def __init__(self, cat_nome, porc_lucro):

       self.cat_nome = cat_nome.upper()
       self.porc_lucro = porc_lucro

   @property
   def __str__(self):

       return f'Categoria: {self.cat_nome} / Lucro da categoria: {self.porc_lucro}'

   @staticmethod
   def CadastrarCategoria(lista_cat):

       if len(lista_cat)<=5:
           cat_nome = input('Digite a categoria: ').upper()
           porc_lucro = float(input('Digite a porcentagem de lucro: '))
           categoria = Categoria(cat_nome,porc_lucro)
           lista_cat.append(categoria)
       else:
           print('O limite de 5 categorias cadastradas já foi atingido')

   @staticmethod
   def ExcluirCategoria(lista_cat):

       remover_item = input('Digite a categoria que deseja remover').upper()
       for i,item in enumerate(lista_cat):
           if remover_item == item:
               lista_cat.remove(item)
               print(f'{item} foi removido da lista categoria')
           else:
               print('Item não encontrado')