# Exercício 6
# 
# Vamos fazer um programa para verificar quem é o assassino de um crime.
# Para descobrir o assassino, a polícia faz um pequeno questionário com 5 perguntas onde a resposta só pode ser sim ou não:

# a. Mora perto da vítima?
# b. Já trabalhou com a vítima?
# c. Telefonou para a vítima?
# d. Esteve no local do crime?
# e. Devia para a vítima?

# Cada resposta sim dá um ponto para o suspeito. A polícia considera
# que os suspeitos com 5 pontos são os assassinos, com 4 a 3 pontos são cúmplices
# e 2 pontos são apenas suspeitos, necessitando outras investigações.
# Valores iguais ou abaixo de 1 são liberados.

pontos = 0

resposta_a = input("Mora perto da vítima? ")
if resposta_a == "s" or resposta_a == "S":
    pontos += 1
resposta_b = input("Já trabalhou com a vítima? ")
if resposta_b == "s" or resposta_b == "S":
    pontos += 1
resposta_c = input("Telefonou para a vítima? ")
if resposta_c == "s" or resposta_c == "S":
    pontos += 1
resposta_d = input("Esteve no local do crime? ")
if resposta_d == "s" or resposta_d == "S":
    pontos += 1
resposta_e = input("Devia para a vítima? ")
if resposta_e == "s" or resposta_e == "S":
    pontos += 1

if pontos == 5:
    print("O elemento é o criminoso.")
elif pontos > 2:
    print("O elemento é cúmplice.")
elif pontos > 1:
    print("O elemento é suspeito. Necessita de outras investigações.")
else:
    print("O elemento está liberado.")