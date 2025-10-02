import os 
os.system("cls")

# Criando um vetor
lista_numeros = []

QUANTIDADE_NUMEROS = 6

# Lendo 6 números do úsuario 
for i in range(QUANTIDADE_NUMEROS):
    num = float(input("Digite o {i+1}ª número: "))
    lista_numeros.append(num)

    # Contadores 
    pares = 0
    impares = 0

    # Verificando pares e ímpares
    for n in lista_numeros: 
        if n % 2 == 0:
            pares += 1
        else: 
             impares += 1 

# Mostrando os resultados 
for i in range(QUANTIDADE_NUMEROS):
    print("\nNúmerero: {lista_numeros[i]}")
print("Quantidade de pares: {pares}")
print("Quantidade de impares: {impares}")