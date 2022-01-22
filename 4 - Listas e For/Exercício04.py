# Exercício 4
# Faça um programa que olhe todos os itens de uma lista e diga quantos deles são pares.

numeros = [22, 34, 25, 41, 52, 45, 89, 20, 62]
pares = 0

print(numeros)
print("\n")

for contador in range(len(numeros)):
    if numeros[contador] % 2 == 0:
        print(numeros[contador])
        pares += 1

print(f"\nDa lista {pares} números são pares")