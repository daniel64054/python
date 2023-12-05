class Usurio :
    def __init__(self, nome_usuario, senha, nivel_acesso):
        self.nome_usuario = nome_usuario
        self.senha = senha
        self.nivel_acesso = nivel_acesso 

    def login (self,nome_usuario, senha ):
        if self.nome_usuario == nome_usuario and self == senha:
            print("voce esta logado \n seja bem vindo☻")
        else:
            print("nome de usuario o senha incorreta◘")
    def alterar_senha(self,nome_usuario, senha ,nova_senha):
        if self.nome_usuario == nova_senha:
            self.senha = nova_senha
            print("Senha alterada")
        else:
            print("usuario inexitente")

    def logout (self):
        self.nome_usuario= ""
        self.senha= ""
        self.nivel_acesso= "" 
        print("Vocé saiu  do sistema ☻") 