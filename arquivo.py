import pandas as pd
import matplotlib.pyplot as plt

posicao= []
totalPontos=[]

infos={
    "Nome":["P. Wehrlein", "M. Evans", "N. Cassidy", "O. Rowland", "J. Vergne", "A. Felix da Costa", "J. Dennis",
            "M. Gunther", "R. Frinjs", "S. Vandoorne", "S. Buemi", "N. Muller", "S. Bird", "J. Hughes", "N. Nato", "E. Mortara" , "S. Fenestraz",
            "N. de Vries", "D. Ticktum", "S. Camara", "J. Daruvala", "T. Bernard", "J. Eriksson", "L. Di Grassi",
            "K. van der Linde", "J. King", "P. Aron", "C. Collet"],
    "Pais":["Alemanha", "Austrália", "Austrália", "Grã-Bretanha", "França", "Portugal", "Grã-Bretanha", "Alemanha", "Holanda", "Belgica", "Suiça",
            "Suiça", "Grã-Bretanha", "Grã-Bretanha", "França", "Suiça", "França", "Holanda", "Grã-Bretanha", "Brasil", "India", "Grã-Bretanha", "Brasil", "Suecia",
            "Africa do Sul", "Grã-Bretanha", "Estonia", "Brasil",],
    "Mexico":[28, 10, 16, 0, 8, 0, 2, 12, 0, 4, 18, 0, 0, 6, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "Arabia Saudita 1":[4, 10, 15, 0, 21, 0, 26, 6, 1, 0, 0, 0, 12, 0, 8, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0],
    "Arabia Saudita 2":[6, 1, 26, 18, 4, 0, 0, 2, 18, 10, 0, 0, 0, 12, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
}

for i in range (1, 29):
    posicao.append(i)


dados_classificacao= pd.DataFrame(infos)

dados_classificacao.index = posicao

#Somar os pontos
for i in range(1, 29):
    soma= dados_classificacao.loc[i, "Mexico"] + dados_classificacao.loc[i, "Arabia Saudita 1"] + dados_classificacao.loc[i, "Arabia Saudita 2"]
    totalPontos.append(soma)



dados_classificacao["Pontuação total"]= totalPontos

print(pd.DataFrame(dados_classificacao))

#ver pontuação de um piloto específico
#
