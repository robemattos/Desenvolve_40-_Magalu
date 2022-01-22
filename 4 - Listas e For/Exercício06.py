# Enunciado
# Agora usando a função max() faça um programa que imprima os três maiores números de uma lista.

# Dica: Use o método próprio de listas .remove().

lista_numeros = [22, 34, 25, 41, 52, 45, 89, 20, 62]
lista_auxiliar = lista_numeros[:]
lista_numeros_maiores = []


for contador in range(3):
    lista_numeros_maiores.append(max(lista_auxiliar))
    lista_auxiliar.remove(max(lista_auxiliar))

print(lista_numeros)
print(lista_numeros_maiores)


