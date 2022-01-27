#Exercício 7
#Faça uma função que sorteia 10 números aleatórios entre 0 e 100
#e retorna o maior entre eles.

import random

def sorteia(maior_num):
    lista_aleatorio = [] #Essa lista guardará os 10 números sorteados.
    
    for indice in range(10): #O comando for sorteia os 10 números e guarda na lista.
        aleatorio = random.randint(0, 100)
        lista_aleatorio.append(aleatorio)
    
    #O comando print abaixo é para conferir se o número a ser impresso quando a
    #função é chamada é realmente o maior.
    
    #print(lista_aleatorio)

    return(max(lista_aleatorio))

num_maior = 0
num_maior = sorteia(num_maior)

print(num_maior)

