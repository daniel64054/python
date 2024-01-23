import os

class  Cliente:
    def _init_(self):
        self.__nome = ""
        self.__email = ""
        self.__cpf = ""
        self.__idade = 0
        self.__telefone = ""
    def gravarcliente(self,nome ="",email = "",cpf ="",idade = 0 ,telefone = ""):
      
      if(nome ==""or email =="" or cpf =="" or idade < 18 or telefone == "" ):
          print("Digite todos os dados !")
      else:  
        self.__nome =nome
        self.__email =email
        self.__cpf =cpf
        self.__idade =idade
        self.__telefone =telefone
        self.__gravar()


    def __gravar(self): 
        arquivo = open("dados/infoclientes.csv","a")
        arquivo.write("Nome:"+self.__nome+";\n")
        arquivo.write("Email:"+self.__email+";\n")
        arquivo.write("Cpf:"+self.__cpf+";\n")
        arquivo.write("Idade:"+self.__idade+";\n")
        arquivo.write("Telefone:"+self.__telefone+";\n")
        arquivo.close()
        print("Cliente salvo com sucesso :)")