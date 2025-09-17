import os
os.system("cls")

print("Crie um programa que solicite ao usuário seu login e uma senha." \
"O programa de continuar pedindo o login e a senha até que ambos estejam corretos")
usuario_salvo = "Ariane"
senha_salva = 301108

while True:

 login = input("Digite seu login: ")
 senha = input("Digite sua senha: ")

if login == login_salvo and senha == senha_salva: 
    print("Bem-vindo! ")
    

else: 
     print("Login ou senha inválidos")