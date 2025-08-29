import os 
os.system

dia = input("Digite dia da semana")

match dia: 
    case 1:
        print("Domingo")
    case 2: 
        print("Segunda-feira.")
    case 3:
        print("Terça-feira.")
    case 4:
        print("Quarta-feira")
    case 5:
        print("Quinta-feira")
    case 6:
        print("Sexta-frira")
    case 7:
        print("Sábado")
    case _: 
        print("Opção inválido")

print("FIM")