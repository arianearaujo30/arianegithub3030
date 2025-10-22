import os 
os.system("cls")

lista_notas = []

def calcular_media(lista_notas):
    resultado = sum(lista_notas) / 3
    return resultado

for i in range(3):
    while True:
      nota = float(input("Digite uma nota: "))
      if nota >= 0 and nota <= 10:
          lista_notas.append(nota)
          break
      else:
          print("Nota inválida! Tente novamente...")
          time.sleep(2) # espera 2 segundos.


    media = calcular_media(lista_notas)

    print(f"Média: {media:.2f}")
    resultado_final(media)
