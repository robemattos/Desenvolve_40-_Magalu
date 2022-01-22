# Exercício 7
# Faça um programa que peça para o usuário digitar a idade, o salário e o sexo de uma pessoa
# até que as entradas digitadas sejam válidas.

# a. Idade: entre 0 e 150;
# b. Salário: maior que 0;
# c. Sexo: M, F ou Outro.

nome = input("Digite o nome: ")
idade = int(input("Digite a idade (entre 0 e 150 anos): "))
salario = float(input("Digite o salário (maior que 0.00): "))
sexo = input("Digite o sexo (M / F / Outro): ")

while (idade < 0 and idade > 150) or (salario < 0) or (sexo != "M" and sexo != "F" and sexo != "Outro"):
    idade = int(input("Digite a idade (entre 0 e 150 anos: "))
    salario = float(input("Digite o salário (maior que 0.00: "))
    sexo = input("Digite o sexo (M / F / Outro): ")

print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Salário: {salario}")
print(f"Sexo: {sexo}")