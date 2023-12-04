import os
os.system("clear")

arq = open("./arquivos/dados.csv","a")
nome = input ("Digite se nome: ")
email = input ("Digite se e-mail: ")

arq.write(nome+";"+email+"\n")
arq.closed
