# Exercício 7

# Desafio 3 - Um hospital quer fazer o diagnóstico de gripe ou dengue a partir
# de um questionário de sintomas, tendo as perguntas abaixo,
# faça um programa que faça o diagnóstico deste hospital:

# a. Sente dor no corpo?
# b. Você tem febre?
# c. Você tem tosse?
# d. Está com congestão nasal?
# e. Tem manchas pelo corpo?

# Para o diagnóstico ele tem a seguinte tabela:

# A	    B	C	D	E	Resultado
# Sim	Sim	Não	Não	Sim	Dengue
# Sim	Sim	Sim	Sim	Não	Gripe
# Não	Sim	Sim	Sim	Não	Gripe
# Sim	Não	Não	Não	Não	Sem doenças
# Não	Não	Não	Não	Não	Sem doenças

result_dor = "N"
result_febre = "N"
result_tosse = "N"
result_cong = "N"
result_manchas = "N"

dor = input("Sente dor no corpo? (S?N): ")
febre = input("Você tem frebre? (S?N): ")
tosse = input("Você tem tosse? (S?N): ")
cong = input("Está com congestão nasal? (S?N): ")
manchas = input("Tem manchas pelo corpo? (S?N): ")

if dor == "s" or dor == "S":
    result_dor = "S"
if febre == "s" or febre == "S":
    result_febre = "S"
if tosse == "s" or tosse == "S":
    result_tosse = "S"
if cong == "s" or cong == "S":
    result_cong = "S"
if manchas == "s" or manchas == "S":
    result_manchas = "S"

if (result_dor == "S") and (result_febre == "S") and (result_manchas == "S"):
    print("Diagnóstico: Dengue")
elif (result_dor == "S" or result_dor == "N") and (result_febre == "S") and (result_tosse == "S") and (result_cong == "S"):
    print("Diagnóstio: Gripe")
elif (result_dor == "S"): # or result_dor == "N"):
    print("Diagnóstico: Sem doenças")
else:
    print("Diagnóstico: Inconclusivo")