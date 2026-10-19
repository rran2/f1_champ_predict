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



