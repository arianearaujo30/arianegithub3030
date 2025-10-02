import os
os.system

# Criando um vetor 
lista_numeros = []

#Lendo 5 números do úsuarios
numeros_negativos = 0
numeros_positivos = 0 

for i in range(5): 
    numero = float(input("Digite o {i+1}° numero: "))
    lista_numeros.append(numero)

# Resultados 
for i in range(QUANTIDADE_NUMEROS): 
    print("\nNúmero: {lista_numero[i]}")
    print("Quantidade de negativos: {negativos}")
    print("Quantidade de positivos: {positivos}")