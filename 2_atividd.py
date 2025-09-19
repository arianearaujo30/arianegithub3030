import os 
os.system("cls")

while True: 
    nota = float(input("Digite uma nota: "))
    # quantidade_notas = quantidade_notas + 1
    # soma = soma + nota 
    quantidade_notas += 1
    soma += nota
    resposta = input("Deseja inserir mais uma nota? \nuse S ou N: ").lower()
    if resposta == "n": 
        break

media = soma / quantidade_notas

print(f"\nMédia: {media}")
