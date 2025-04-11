usuario = senha = ""

while (usuario == senha):
    usuario = input("Informe o usuário: ")
    senha = input("Informe a senha: ")
    if (usuario == senha):
        print("Senha Inválida")
        print("A senha não pode ser igual ao nome de usuário.")