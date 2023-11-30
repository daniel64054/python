import os


os.system("cls")

fl = open("dados.txt","a")
texto = input("Digite algo:")
fl.white(texto+"\n")
fl.close()

rs = input("Voce deseja renomear o  arquivo?[s,n}: ")
if rs =="s":
    novo_name=input("digite o novo nome do arquivo :")
    os.rename("dados.txt",novo_name)
    print("renomeado com sulcesso")

else:
    print("Veja o resultado")