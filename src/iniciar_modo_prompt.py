
from re import A


def interface():
    print("======================================================================\n")
    print("Isto e o Clanker da f1 ... \n so tem dois comandos \n insere o nome, pontos, vitorias, podios e nivel dos upgrades(3-excelente, 2- bom, 1-medio) com espaco\n ou apenas escreve: calcular para calcular com os pilotes que inseriste.\n")
    print("======================================================================\n")

    while True: 
        prompt_junta= input("Tu (>): ")

        prompt_separada = prompt_junta.split()

        PILOTO = prompt_separada[0]
        PONTOS = int(prompt_separada[1])
        VITORIAS = int(prompt_separada[2])
        PODIOS = int(prompt_separada[3])
        UPGRADES = int(prompt_separada[4])
        
        print(f"\nModelo: {PILOTO} processado! (Pontos: {PONTOS}, Vitorias: {VITORIAS}...)\n")


