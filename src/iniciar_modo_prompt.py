from src.models import model

def interface():
    print("======================================================================\n")
    print("Isto e o Clanker da f1 ... \n so tem dois comandos \n insere o nome, pontos, vitorias, podios e nivel dos upgrades(3-excelente, 2- bom, 1-medio) com espaco\n ou apenas escreve: calcular para calcular com os pilotes que inseriste.\n")
    print("======================================================================\n")

    dados = []
    pilot_names = []

    while True:
        prompt= input("Tu (>): ")
    
        if(prompt == "calcular"):
            if(len(pilot_names)==0):
                print("Nao foi inserido piloto nenhum!")
                continue
    
            champion = model.calc_champion(dados, pilot_names)
            print(f"====================\n E o provavel vencedor será -> {champion}\n ====================\n")
            break
    
        prompt_separada = prompt.split()
    
        if(len(prompt_separada)<5):
            print("ERRO: tens de inserir o nome, pontos, vitorias, podios e upgrades...\n")
            continue
            
        #tirar o nome da prompt e mete lo isolado pq depois o array com os dados
        #vai ser usado nas matrizes 
        nome_removido = prompt_separada.pop(0)           
        pilot_names.append(nome_removido)
        valores_numericos = list(map(int, prompt_separada))
        dados.append(valores_numericos)
                
        print("Os seguintes pilotos foram processados: \n")
        for names in pilot_names:
            print(f"--- {names} ---\n")
    
    
           
