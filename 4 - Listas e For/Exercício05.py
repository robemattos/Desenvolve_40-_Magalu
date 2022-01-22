# Exercício 5
# Faça um programa que imprima o maior número de uma lista,
#  sem usar a função max().

numeros = [22, 34, 25, 41, 52, 45, 89, 20, 62]

maior_numero = numeros[:]
maior_numero.sort()

print(numeros)
print(maior_numero[-1])