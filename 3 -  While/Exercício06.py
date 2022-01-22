# Exercícios
# Faça um programa que sorteia um número N e peça para o usuário adivinhar o número sorteado.
# A cada resposta errada, o seu programa deve imprimir um aviso dizendo que a resposta está errada
# e pedir novamente uma resposta ao usuário.

# Para a realização desse exercício, utilize alguma função da biblioteca random (e.g. randint()).

import random

num_sorteado = random.randint(0,5)

#print(num_sorteado)

resposta = int(input("Adivinhe o número sorteado: "))
qtd_tentativas = int(input("Informe a quantidade de tentativas: "))
tentativas = 0

while tentativas < qtd_tentativas and resposta != num_sorteado:
    print("Número errado!")
    resposta = int(input("Tente novamente: "))
    tentativas = tentativas + 1

if tentativas >= qtd_tentativas:
    print("Acabaram as tentativas")
elif resposta == num_sorteado:
    print("Você acertou!!!")
