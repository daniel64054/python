
# criação da classe dog que dara origem a varios dogs(cachorros)
class Dog:
    """criação da função __initi__ que e resposavel por iniciar o objeto sera criado  esta sendo pededido nome  e idade em que eie é criado
    uasamos  o termo  self para fazer a propria classe  portato quando criar o dog e passar o nome e a idades que eles pertecem a classe dog"""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def data_dog(self):
        print(self.name)
        print(self.age)

    def sit(self):
        print("sento")

    def roll_over(self):
        print("rolou")
        
