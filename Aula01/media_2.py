
media = 0
nota1= input ("digite a nota do aluno:")
nota2= input ("digite a nota do aluno:")
nota3= input ("digite a nota do aluno:")
nota4= input ("digite a nota do aluno:")


nota1= float(nota1)
nota2= float(nota2)
nota3= float(nota3)
nota4= float(nota4)

media = float(nota1) + float(nota2) + float(nota3) +float(nota4) / 4

    
if media>= 7:
    print("aluno  aprovado")
elif media<= 4:
    print("aluno reprovou ")
else:
    print("recuperar")

print(media)