# Exercício 2
# Faça um programa que peça um número e mostre se ele é positivo ou negativo.

numero = int(input("Digite um número: "))

if numero < 0:
    print("Número negativo")
elif numero == 0:
    print("O número não é positivo e nem negativo")
else:
    print("Número positivo")