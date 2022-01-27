# Exercício 14

# Super Desafio - Faça um programa que pede para o usuário digitar o CPF e verifica
# se ele é válido. Para isso, primeiramente o programa deve multiplicar cada um dos
# 9 primeiros dígitos do CPF pelos números de 10 a 2 e somar todas as respostas.
# O resultado deve ser multiplicado por 10 e dividido por 11.
# O resto dessa divisão deve ser igual ao primeiro dígito verificador (10º dígito).
# Em seguida, o programa deve multiplicar cada um dos 10 primeiros dígitos do CPF
# pelos números de 11 a 2 e repetir o procedimento anterior para verificar o segundo
# dígito verificador.

# Exemplo:
# Se o CPF for 286.255.878-87 o programa deve fazer primeiro:
# x = (2*10 + 8*9 + 6*8 + 2*7 + 5*6 + 5*5 + 8*4 + 7*3 + 8*2)
# Em seguida, o programa deve testar se x*10%11 == 8 (o décimo número do CPF). Se sim,
# o programa deve calcular:
# x = (2*11 + 8*10 + 6*9 + 2*8 + 5*7 + 5*6 + 8*5 + 7*4 + 8*3 + 8*2)
# e verificar se x*10%11 == 7 (o décimo primeiro número do CPF).

cpf_int = []
x = 0
cpf_str = list(str(input(("Digite o CPF: "))))

for cont in range(len(cpf_str)):
    cpf_int.append(int(cpf_str[cont]))

for cont in range(9):
    x += (10 - cont) * cpf_int[cont]
    
if (x * 10) % 11 == cpf_int[9]:
    x = 0
    for cont in range(10):
        x += (11 - cont) * cpf_int[cont]
        
    if (x * 10) % 11 == cpf_int[10]:
        print("CPF válido.")
else:
    print("CPF inválido.")