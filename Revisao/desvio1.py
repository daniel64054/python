"""e
ste programa pede nome,nota e media
se o aluno  tiver nota igual ou maior estara reprovado se for menor reprova
"""
nome = input("Digite o nome do alune: ")
media = input("Digite o media do alune: ")
media = float(media) 

if (media>=6):
    print("aprovado")
else:
    print("reprovado")
