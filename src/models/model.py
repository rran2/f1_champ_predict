import numpy as np
import torch
import torch.nn

class F1Predictor(torch.nn.Module):
    def softmax(z):
        z_estavel = z - torch.max(z)
        exp_z = np.exp(z_estavel)
        return exp_z / np.sum(exp_z)
    
    
    torch.random.seed()
    print("\nSeed inicializada...")
    
    
    #gera 200 numeros aleatorios entre 0 e 1
    rand_numeros = torch.randn(200)
    print("\nNumeros aleatorios gerados....\n")
    
    #inicializa uma matriz de parametros
    #vitorias, podios, upgrades e pontos e cospe oq se quer se é campeao ou nao(0 ou 1)
    W = torch.nn.Linear(4, 1)
    
    #zeros a 1,1 ja que como ele so cospe 1 cena, a matriz tem de ter as mesmas colunas e linhas 1por1
    bias = np.zeros((1,1))
    
    print("E com isso o favorito e provavel vencedor")
    
    def calc_champion(dados_input, nomes_pilotos):
        X = np.array(dados_input, dtype=float)
    
        #multiplicacao de matrizes bueda fixe
        logits = np.dot(X, W)
        #inves de ficar em (N,1) fica (N,)
        #logits = np.squeeze(logits)
            
        #softmax doing da job
        probabilidades = softmax(logits)
        
        print("As probablidades de cada piloto: ")
        
        #enumerate vai retornar o index dos pilotos e os valores, vitorias ans shyt
        for index, valores in enumerate(dados_input):
            print(f"\n -> {nomes_pilotos[index]} : {probabilidades[index]*100}% \n")
    
        winner_idx = (np.argmax(probabilidades, axis=-1))
        idx = winner_idx[0]
    
        return nomes_pilotos[idx]
    


    












