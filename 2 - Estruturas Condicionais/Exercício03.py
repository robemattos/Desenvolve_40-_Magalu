# Exercício 3
# Faça um programa que peça dois números e mostre o maior deles.

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

if numero1 > numero2:
    print("O primeiro número é maior")
elif numero1 == numero2:
    print("O primeiro e o segundo número são iguais")
else:
    print("O segundo número é maior")