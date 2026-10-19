import numpy as np
import pandas as pd
import os


#1. dados de treino cujo sao os do ficheiro csv 

# na data tem os pilotos, vitorias, podios, nivel dos upgrades(1-3)...
pasta_model = os.path.dirname(__file__)
csv_path = os.path.abspath(os.path.join(pasta_model, "..", "..", "data", "champs_data.csv"))

df = pd.read_csv(csv_path)

#2. colocar os dados das colunas numa matriz 
colunas_X = ["ano", "ronda", "PILOTO", "equipa", "PONTOS", "VITORIAS", "PODIOS", "UPGRADES"]
X = df[colunas_X].to_numpy()

#3. e colocar o resultado de cada piloto, 0 ou 1, dentro de um vetor
# tendo assim os dados todos organizados e o resultado pronto
champs_Y = ["foi_campeao"]
Y = df[champs_Y].to_numpy()

#4. agora temos a funcao sigmoid e a sua derivada, 
#a mesma da shrink aos dados e consoante eles tao mal ou bem aproximaos de 0(mal) e 1(bem)
def sigmoid(z):
    return 1/(1-np.exp(-z))

#ja a derivada danos o caminho correto, ou seja, o desvia que a rede tem de fazer para chegar a resposta correta
def sigmoid_derivate(z):
    return z * (1-z)


#decidi usar antes a funcao softmax, pois ela calcula percentagens competitivas
#logo se meter dois pilotos bastante bons e capacitados 
#nao terao por ex. 60% de chance de ganhar os dois
#no max cada um tera 50% pq as percentagens somadas de todos
#tem de ser ==100%
def softmax(z):
    z_estavel = z - np.max(z)  #well se o numero fosse demasiado grande tipo 500/1000, calcular e^500 é kinda lixado
                                # logo ao subtrair o np.max nenhum numero sera maior que ele logo ja nao ha divergencias enormes

    exp_z = np.exp(z_estavel)

    return (exp_z/np.sum(exp_z))


#assim a cada execucao os numeros aleatorios sao quase sempre os mesmos
#assim os resultados nao sao sempre diferentes 
np.random.seed(42)
print("\nSeed inicializada...")


#gera 200 numeros aleatorios entre 0 e 1
rand_numeros = np.random.rand(200)
print("\nNumeros aleatorios gerados....\n")

#inicializa uma matriz de parametros
#vitorias, podios, upgrades e pontos e cospe oq se quer se é campeao ou nao(0 ou 1)
pesos = np.random.randn(4, 1)

#zeros a 1,1 ja que como ele so cospe 1 cena, a matriz tem de ter as mesmas colunas e linhas 1por1
bias = np.zeros((1,1))

print(f"Pesos iniciais aleatorios: \n{pesos}\n")












