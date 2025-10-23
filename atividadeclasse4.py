import os
from dataclasses import dataclass
os.system("cls")

@dataclass
class Pessoa1:
    nome: str
    email: str
    endereco: str

@dataclass
class Pessoa2:
    nome: str
    email: str
    endereco: str

def mostrar_dados(self):
    print(f"Nome: {self.nome}")
    print(f"E-mail: {self.email}")
    print(f"Endereço: {self.endereco}")

    def mostrar_somente_nome(self):
        print(f"Nome: {self.nome}")

print("Solicitado os dados da pessoa.")
pessoa1 = Pessoa1(nome=input("Digite seu nome: "),
                 email=input("Digite seu e-mail":),
                 endereco=input("Digite seu endereço"))    

pessoa2 = Pessoa2(nome=input("Digite seu nome: "),
                 email=input("Digite seu e-mail":),
                 endereco=input("Digite seu endereço"))  

print("\n= Exibindo dados =")
pessoa1.mostrar_dados()
pessoa1.mostrar_somente_nome

pessoa2.mostrar_dados()
pessoa2.mostrar_somente_nome
