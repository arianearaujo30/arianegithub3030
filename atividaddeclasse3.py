import os
from dataclasses import dataclass
os.system("cls")

@dataclass
class Pessoa:
    nome: str
    email: str
    endereco: str

def mostrar_dados(self):
    print(f"Nome: {self.nome}")
    print(f"Endereço: {self.endereco}")

def dados_email_marketing(self):
    print(f"Nome: {self.nome}")
    print(f"E-mail: {self.email}")

print("Solicitado os dados da pessoa.")
pessoa1= Pessoa(nome=input("Digite seu nome: "),
                 email=input("Digite seu e-mail":),
                 endereco=input("Digite seu endereço")) 

print("\n= Exibindo dados =")
pessoa1.dados_entrega()
pessoa1.dados_email_marketing