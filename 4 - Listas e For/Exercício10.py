# Exercício 10
# Faça um programa que peça as 4 notas bimestrais e mostre a média
# aritmética delas, usando listas.

qtd_notas = int(input("Digite a quantidade de notas: "))
notas = []
media = 0

for indice in range(qtd_notas):
    nota = float(input(f"Digite a nota no. {indice+1}: "))
    notas.append(nota)

media = sum(notas) / len(notas)

print("\n")
print(notas)

print("\n")
print(f"A soma das notas é: {sum(notas):.2f}")

print("\n")
print(f"A média das notas é: {media:.2f}")
