import os 
os.system("cls")

print("""
"Pratos \t Valor"
Picanha \t R$ 25.00
Lasanha \t R$ 20.00
Strogonoff \t R$ 18.00
Bife Acebolado \t 15.00
Pão com ovo \t 5.00 """)

soma = 0 

while True: 
    escolha = int(input("Escolha o prato desejado: "))

    if escolha in precos: 
        total += precos[escolha]
        print(f"Prato adicional! Valor parcial: R$ {total:.2f}")
    else: 
        print("Opção inválida! Tente novamente.")

    continuar = input("Deseja escolher outro prato? ")
    if continuar != "S": 
        break
    
    print(f"\nValor total a pagar: R$ {total:.2f}")
