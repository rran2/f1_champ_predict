import numpy as np
import csv

#1. dados de treino cujo sao os do ficheiro csv 
#2. dar open com o csv reader e with open aos dados do ficheiro champs
with open("data/champs_data.csv", "r") as D:
    X = csv.reader(D)

