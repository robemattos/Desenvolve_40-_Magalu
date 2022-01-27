# Exercício 11
# Crie uma lista de 10 números e imprima:

# a. uma lista com os 4 primeiros números;
# b. uma lista com os 5 últimos números;
# c. uma lista contendo apenas os elementos das posições pares;
# d. uma lista contendo apenas os elementos das posições ímpares;
# e. a lista inversa da lista sorteada (isto é, uma lista que começa com o último
#    elemento da lista sorteada e termina com o primeiro);
# f. uma lista inversa dos 5 primeiros números;
# g. uma lista inversa dos 5 últimos números.

lista_numeros = []

for indice in range(10):
    numero = int(input("Digite um número: "))
    lista_numeros.append(numero)

lista_inversa = lista_numeros[:]
lista_inversa.sort()
lista_inversa.sort(reverse = True)
lista_reversa = lista_numeros[:]
lista_reversa.reverse()

print(lista_numeros[:4])
print(lista_numeros[-5:])
print(lista_numeros[::2])
print(lista_numeros[1::2])
print(lista_inversa)
print(lista_reversa[5:])
print(lista_reversa[:-5])