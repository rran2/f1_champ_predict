import torch 
import torch.nn as nn

class F1Predictor(torch.nn.Module):

    def __init__(self):
        super(F1Predictor, self).__init__()

        self.linear = nn.Linear(4, 1)
    
    def forward(self, z):
        logits = self.linear(z).squeeze(-1)
        soft = nn.Softmax(dim = 0)
        return soft(logits)
    
torch.manual_seed(42)
print("\nSeed inicializada (42) ...")
    
def calc_champion(tensor_dados, nomes_pilotos):
    X = torch.tensor(tensor_dados, dtype=torch.float32)
        
    modelo = F1Predictor()
    probabilidades = modelo(X)
    
    print("As probilidades de cada piloto: \n")
    for index, valores in enumerate(tensor_dados):
        print(f"\n -> {nomes_pilotos[index]} : {probabilidades[index]*100:.2f}% \n")
    
    winner_idx  = torch.argmax(probabilidades).item()
    return nomes_pilotos[winner_idx]
    


    












