"""
 comparar duaas listas e mostras os iguais
"""

lista1 = [0,324,253,999,679,0]
lista2 = [1234,453,999,64,153,0]
iguai = ""
p = "1"

lista1 == lista2


for i in lista1:
    for o in lista2:
        if(i == o):
            print(o)
    
