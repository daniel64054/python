from classs_cliente import Cliente

nome =input("Digite o nome do cliente: ")
email =input("Digite o email do cliente: ")
cpf =input("Digite o cpf do cliente: ")
idade =input("Digite o idade do cliente: ")
telefone =input("Digite o telefone do cliente: ")

# vamos instaciar a classe cliente gerar um objeto apatir  da classe  cliente passando todas de propriedade
#para o objeto criado

cli = Cliente()
cli.gravarcliente(nome,email,cpf,int(idade),telefone)
