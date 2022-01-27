# Exercício 12
# Faça um programa que sorteia 10 números entre 0 e 100 e conte quantos números
# sorteados são maiores que 50.

# Obs.: Precisa usar a biblioteca random

import random

#num_sorteado = random.randint(0,100)

lista_sorteados = []
contador = 0

for numero in range(10):
    num_sorteado = random.randint(0,100)
    lista_sorteados.append(num_sorteado)
    if num_sorteado > 50:
        contador = contador + 1

#print(num_sorteado)
print(lista_sorteados)
print(f"{contador} numeros são maiores que 50")
