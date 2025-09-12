import os 
os.system("cls")

print("Laço de Repetição - While")

while True: 
    nota = float(input("Digite uma nota: "))
    if nota >= 0 or nota <= 10:
        print("Nota inválida! Digite uma nota ente 0 e 10.")

    else: 
        print(f"nota: {nota}")
        break 
