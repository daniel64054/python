import os
os.system("cls")

#mensagems
print ("temos dois arquivos: bloco_texto.txt e dado.txt")
print("qual delaes voce deseja apagar")

#perguntas
res = input("Digite:\n 1-dados.txt\n 2-bloco_texto.txt: ")
com = input("tem certeza \n [s] [n]\n")

#computação das respostas
if com == "s":
    if  res == "1" :
        os.remove("dados.txt")
    else :
        os.remove("bloco_texto.txt")
        print("O arquivo foi apagado com sucesso")
else:
   print("Nada foi feito")
         