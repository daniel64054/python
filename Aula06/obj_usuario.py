from classe_usuario import Usurio

admin = Usurio("admin","P@$$w0rd","administrador")
admin.login("admin","P@$$w0rd")
admin.alterar_senha("admin",123)