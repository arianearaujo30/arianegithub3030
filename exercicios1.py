import os 
os.system("cls")

print("""
Código \t Prato \t Valor
 1 \t Picanha \t R$ 25,00
 2 \t Lazanha \t R$ 20,00 
 3 \t Strogonoff \t R$ 18,00
 4 \t Bife Acebolado \t R$ 15,00
 5 \t Pão com ovo \t R$ 5,00     
""")

cod = int(input("Digite o código do prato desejado: "))

match cod:   
   case 1:
    prato = "Picanha"
    preco = 25 
   case 2:
    prato = "Lazanha"
    preco = 20 
   case 3:
    prato = "Strogonoff"
    preco = 18
   case 4:
    prato = "Bife Acebolado"
    preco = 15
   case 5:
    prato = "Pão com ovo"
    preco = 5
case
print("Opção inválida")

print(f"Prato: {prato}")
print(f"Preço: {preco}")

print("Volte sempre!")