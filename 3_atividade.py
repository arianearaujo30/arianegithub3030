import os 
os.system("cls")

print("Crie um programa que solicite ao usuário seu login e uma senha" \
"O programa deve continua pedindo o login e a senha até que ambos estejam corretos" \
"O programa deve solicitar o login e senha apenas três vezes" \
"Caso ultrapasse o número de tentativas, o  programa deve ser finalizado")

tentativas = 1
usuario_salvo = "Ariane"
senha_salva = 301108

for i in range(3):
    while True:
        if tentativas >= 3:
            break
        print(f"\nTentativas: {tentativas}")
        login = input("Digite seu login: ")
        senha = input("Digite sua senha: ")

if login == login_salvo and senha == senha_salva: 
    print("Bem-vindo! ")

else: 
     print("Login ou senha inválidos") 
     tentativas += 1

