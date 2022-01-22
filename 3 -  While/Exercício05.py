# Exercício 5
# Faça um programa, usando loops, que peça para um usuário digitar um número
# e que só finaliza quando o usuário digitar 0.
# Ao final imprima a soma de todos os números digitados.

soma = 0
numero = int(input("Digite um número inteiro (zero finaliza o programa): "))

while numero != 0:
    soma = soma + numero
    numero = int(input("Digite um número inteiro (zero finaliza o programa): "))

print(f"A soma dos números digitados foi: {soma}")