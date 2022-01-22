# Faça um programa que sorteie 10 números entre 0 e 100 e imprima:
# a. o maior número sorteado;
# b. o menor número sorteado;
# c. a média dos números sorteados;
# d. a soma dos números sorteados.
# Obs.: Precisa usar a biblioteca random

import random

numeros = []

for x in range(10):
    numeros.append(random.randint(0, 100))

print(numeros)
print(f"a. O maior número sorteado é {max(numeros)}")
print(f"b. O menor número sorteado é {min(numeros)}")
print(f"c. A média dos números sorteados é {sum(numeros) / len(numeros)}")
print(f"d. A soma dos números sorteados é {sum(numeros)}")

