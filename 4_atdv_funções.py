import os 
os.system("cls")

# Criando uma função.
def converter_centimetros(numero):
    return numero * 100

# Código principal. 
numero = int(input("Digite um número: "))
resposta = converter_centimetros(numero) #Chamando a função.
print(f"Resultado: {resposta} centímetros.")
