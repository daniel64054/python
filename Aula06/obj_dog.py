from classe_dog  import Dog 
 
"""" para criar  o objeto  utilizamos o variavel pastor o  projeto de intanciação para classe dog foi passasado o  nome e idade  """
pastor = Dog("Bob",8)
"""acessamos o metodo data_dog que mostra os dados do dog"""
pastor.data_dog()

pastor.sit()
pastor.roll_over()
print(pastor.__class__)
print(pastor.__dict__)