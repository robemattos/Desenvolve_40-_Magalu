# Exercício 2
# Peça ao usuário para digitar um número e imprima o fatorial de n.

numero = int(input("Digite um número: "))

for contador in range(numero,1,-1):
    resultado = numero * (contador - 1)
    print(f"{numero} X {contador-1} = {resultado}")