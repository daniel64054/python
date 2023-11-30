import os

os.system("cls")

lst = (os.listdir("c:/"))

ps = 1

for i in lst:
    print(str(ps) + "ª-"+i)
    ps+=1

esc =input("digite o numero correspodente a arquivo que voce quer ver:") 

match esc:
    case "1":
        print(os.listdir("c:/$Recycle.bin"))
    case "2":
        print(os.listdir("c:/$WinREAgent"))
    case "3":
        print(os.listdir("c:/343E2DFBC619"))
    case "4":
        print(os.listdir("c:/adobeTemp"))
    case "5":
        print(os.listdir("c:/Arquivos de Programas"))
    case "6":
       print( os.listdir("c:/Documents and Settings"))
    case "7":
        print(os.listdir("c:/DumpStack.log.tmp"))
    case "8":
        print(os.listdir("c:/eclipse"))
    case "9":
        print(os.listdir("c:/HashiCorp"))
    case _:
        print("não a esse arquivos")
        