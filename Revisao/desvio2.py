"""
esse programa pega o ultimo numero da placa e diz o dia do rodizio
"""
placa =input("coloque seu ultimo numero da placa do veículo:")


if( placa == "1" or placa == "2"):
 print("seu carro  está em rodizio - segunda-feira")
elif(placa == "3" or placa == "4"):
 print("seu carro  está em rodizio - terça-feira")
elif(placa == "5" or placa == "6"):
 print("seu carro  está em rodizio - quarta-feira")
elif(placa == "7" or placa == "8"):
 print("seu carro  está em rodizio - quinta-feira")
elif(placa == "9" or placa == "0"):
 print("seu carro  está em rodizio - sexta-feira")
else:
 print("tente de novo :( \nesse numero de placa não existe")
 