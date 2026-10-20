import numpy as np

# agora temos a funcao sigmoid e a sua derivada, 
#a mesma da shrink aos dados e consoante eles tao mal ou bem aproximaos de 0(mal) e 1(bem)
def sigmoid(z):
    return 1/(1+np.exp(-z))

#ja a derivada danos o caminho correto, ou seja, o desvia que a rede tem de fazer para chegar a resposta correta
def sigmoid_derivate(z):
    return z * (1-z)


#decidi usar antes a funcao softmax, pois ela calcula percentagens competitivas
#logo se meter dois pilotos bastante bons e capacitados 
#nao terao por ex. 60% de chance de ganhar os dois
#no max cada um tera 50% pq as percentagens somadas de todos
#tem de ser ==100%
def softmax(z):
    z_estavel = z - np.max(z, axis=-1, keepdims=True) #well se o numero fosse demasiado grande tipo 500/1000, calcular e^500 é kinda lixado
                                # logo ao subtrair o np.max nenhum numero sera maior que ele logo ja nao ha divergencias enormes

    exp_z = np.exp(z_estavel)

    return (exp_z/np.sum(exp_z, axis=-1, keepdims=True))
                                #axis=-1 e para prevenir q o clanker nao some coluna a coluna
                                #o keepdims e para ela nao apagar a tabela depois da soma

#assim a cada execucao os numeros aleatorios sao quase sempre os mesmos
#assim os resultados nao sao sempre diferentes 
np.random.seed(42)
print("\nSeed inicializada...")


#gera 200 numeros aleatorios entre 0 e 1
rand_numeros = np.random.rand(200)
print("\nNumeros aleatorios gerados....\n")

#inicializa uma matriz de parametros
#vitorias, podios, upgrades e pontos e cospe oq se quer se é campeao ou nao(0 ou 1)
W = np.random.randn(4, 1)

#zeros a 1,1 ja que como ele so cospe 1 cena, a matriz tem de ter as mesmas colunas e linhas 1por1
bias = np.zeros((1,1))

print("E com isso o favorito e provavel vencedor")

def calc_champion(dados_input, nomes_pilotos):
    X = np.array(dados_input, dtype=float)

    #multiplicacao de matrizes bueda fixe
    logits = np.dot(X, W)

    #softmax doing da job
    probabilidades = softmax(logits)
    
    print("As probablidades de cada piloto: ")
    
    #enumerate vai retornar o index dos pilotos e os valores, vitorias ans shyt
    for index, valores in enumerate(dados_input):
        print(f"\n -> {nomes_pilotos[index]} : {probabilidades[index]} \n")

    winner_idx = np.argmax(probabilidades, axis=-1)
    idx = winner_idx[0]

    return nomes_pilotos[idx]
    


    












