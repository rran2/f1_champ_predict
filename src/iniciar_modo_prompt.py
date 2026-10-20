from models import model

def interface():
    print("======================================================================\n")
    print("Isto e o Clanker da f1 ... \n so tem dois comandos \n insere o nome, pontos, vitorias, podios e nivel dos upgrades(3-excelente, 2- bom, 1-medio) com espaco\n ou apenas escreve: calcular para calcular com os pilotes que inseriste.\n")
    print("======================================================================\n")

dados = []
prompt_separada = []
pilot_names = []

while True:
    prompt= input("Tu (>): ")

    if(prompt == "calcular"):
        dados += list(map(int, prompt_separada))
        
        model.calc_champion(dados, pilot_names)

        print(f"====================\n E o provavel vencedor será {champ}\n ====================\n")
        
    #tirar o nome da prompt e mete lo isolado pq depois o array com os dados
    #vai ser usado nas matrizes 
    prompt_separada = prompt.split()
    nome_removido = prompt_separada.pop(0)           
    pilot_names.append(nome_removido)
            
    print("Os seguintes pilotos foram processados: \n")
    for names in pilot_names:
        print(f"--- {names} ---\n")


       
