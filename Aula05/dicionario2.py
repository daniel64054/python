import os
os.system("clear")

capitais = { "Acre":"Rio blanco","Alagoas":"maceio","amapá":"macapa","Amazonas":"manaus","Bahia":"salvador","Ceara":"fortaleza","Espirito santo":"vitoria",
"Mato grosso":"campo grande","minas gerais":"Belo horizonte","Para":"belem","paraiba":"joão pessoa","parana":"curitiba","pernabeco":"recife","piaui":"teresina",
"rio de janeiro":"rio de janeiro","rio grande":"natal","rio drande do sul":"porto alegre", "rondonia":"boa vista","santa catarina":"florinopolis","Sao paulo"
:"Sao paulo","sergipe":"aracaju","Tocantins":"palmas","distrito federal":"Brasilia"}

# for i in capitais:
#     print(i)

# pegar os primaeiros 6 numeros
ps= 1
for i in capitais:
 if ps < 6:
  print(i + " a capitais é "+capitais[i])
 else:
  break
 ps += 1