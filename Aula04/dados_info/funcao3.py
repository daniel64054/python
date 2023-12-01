def soma(numeros):
    #função soma realiza a soma dos numeros  que são por paramentro 
    #e no final  retorna  o resultado da soma
    #voce deve passar por parrametros umas lista de numeros
    rs = 0
    for  n in numeros:
        rs += n
    return rs

v =[10,1,7,2,9,2,8,43]
print(soma(v))