import os 
os.system("cls")

# Criando um vetor 
lista_notas = []

# Constante
QUANTIDADE_NOTAS = 3

# Inserindo nota
for i in range(QUANTIDADE_NOTAS):
    nota = int(input("Digite a {i+1}ª nota: "))
    lista_notas.append(nota)

    media = sum(lista_notas) / QUANTIDADE_NOTAS

    # Mostrar notas: 
    print("\nResultado:")
    for i in range(QUANTIDADE_NOTAS):
        print(f"Nota: {lista_notas[i]}")
        if lista_notas[i] >= 7:
            resultado = "Aprovado"
        elif lista_notas[i] >= 5:
            resultado = "Recuperação"
        else:
            resultado = "Recuperação"

    print(f"Média: {media}")
    print(f"Resultado: {resultado}")
    
    print("FIM")
