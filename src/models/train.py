import os
import pandas as pd
import torch
from . import model
import torch.nn as nn



pasta_model = os.path.dirname(__file__)
csv_path = os.path.abspath(os.path.join(pasta_model, "..", "..", "data", "champs_data.csv"))

df = pd.read_csv(csv_path, sep=";", encoding="latin1")

colunas_X = ["PONTOS", "VITORIAS", "PODIOS", "UPGRADES"]
X = torch.tensor(df[colunas_X].values, dtype = torch.float32)

champs_Y = ["foi_campeao"]
Y = torch.tensor(df[champs_Y].values, dtype = torch.float32)
 
modelo = model.F1Predictor()
optimizer = torch.optim.SGD(modelo.parameters(), lr = 0.1, momentum = 0.9)

grupos_corridas = df.groupby(["ano", "ronda"])

loss = nn.CrossEntropyLoss()

num_epocas = 300
for EPOCAS in range(num_epocas):
    for key, grupo in grupos_corridas:



    

