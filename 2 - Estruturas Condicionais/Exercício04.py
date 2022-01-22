# Exercicio 4

# Faça um programa que leia a validade das informações:

# a. Idade: entre 0 e 150;
# b. Salário: maior que 0;
# c. Sexo: M, F ou Outro;

# O programa deve imprimir uma mensagem de erro para cada informação inválida.

idade = int(input("Digite a idade entre 0 e 150: "))
if idade < 0 or idade > 150:
    print("A idade tem que estar entre 0 e 150 anos")
else:
    print(f"A idade é {idade}")

salario = float(input("Digite o salario maior que 0: "))
if salario < 0:
    print("O salário tem que ser maior que R$ 0,00")
else:
    print(f"O salário é {salario}")

sexo = input("Entre com o sexo (M / F / Outro: ")
if (sexo == "M") or (sexo == "F") or (sexo == "Outro"):
    print(f"Sexo: {sexo}")
else:
    print("Sexo inválido")