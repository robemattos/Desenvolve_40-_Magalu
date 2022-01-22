# Exercício 8
# Faça um programa que pede para o usuário digitar 5 números e, ao final,
# imprime uma lista com os 5 números digitados pelo usuário
# (sem converter os números para int ou float).

# Exemplo: Se o usuário digitar 1, 5, 2, 3, 6, o programa deve imprimir
# a lista ['1','5','2','3','6']

contador = 0
lista_numeros = []

while contador < 5:
    numero = input(f"Digite o {contador+1}o. número: ")
    lista_numeros.append(numero)
    contador += 1

print(lista_numeros)