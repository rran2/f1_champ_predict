from data import ...
from models import ...

def menu():
    while True: 
        PILOTO, PONTOS, VITORIAS, PODIOS, UPGRADES = input("Tu (>): ").split()
        
        print(f"Modelo: {PILOTO} processado! (Pontos: {PONTOS}, Vitorias: {VITORIAS}...)")



