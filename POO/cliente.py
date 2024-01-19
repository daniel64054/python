#Declarando a Classe cliente. Esta classe que seja 

#obj podem ter modificadores
#classes devem ter sua primeira letra em maiculo
#self para olhar a si mesmo
# __ deixa privado

class Cliente:
    #Metodo __init__  reprssenta acontrução do metodo contrutor  da classe reposavel por inilizar o objeto  é criado E ste método possui um argumeto self
    #que faz referencia a propria classe deve-se  utilizar o comando self para refencia a propria estrutura  de classe a qual ele pertance
    #note que o metodo __init __(contrutor) foram iniciado os atributos  da classes , representa  as caracteristicas do cliente Os atributos
    #todos eles pertencem a classe cliente . Os atributos foram declarados como privados.para utilizar  2 undercores
    
    '''
    A classe cliente gera novos clientes e pede alguns dados pessoais e pode salvar o cliente
    '''
    def __init__(self):
     self.__nome =""
     self.__idade =0
     self.__genero =""
     self.__email =""

    def dados(self,nome="",idade=0,genero="",email=""):
     """
    pede daos para o cliente para ser passado para o sistema
      """
     #Metodos  dados  é utilizado para relizar passagen de dados  do cliente para dentro da classe cliente
     self.__nome = nome
     self.__idade =idade
     self.__genero=genero
     self.__email =email    

    #metodo gravar exibe auma mensagen de com o do nome do cliente dizendo que foi salvo
    def gravar(self):
        print("O cliente "+self.__nome+" foi gravado com sucesso")