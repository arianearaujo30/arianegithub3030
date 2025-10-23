import os 
from dataclasses import dataclass
os.system

@dataclass
class Pessoa:
    nome: str
    idade: int
    peso: float
    altura: float

pessoa1 = Pessoa(nome="Ariane",idade=16,peso=64.00,altura=1.58)

print(f"Nome: {pessoa1.nome}\nIdade: {pessoa1.idade}\nPeso: {pessoa1.peso}\nAltura: {pessoa1.altura}")