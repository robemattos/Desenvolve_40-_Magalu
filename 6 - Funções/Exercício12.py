#Exercício 12

#Faça uma função que receba duas listas e retorne o produto item a item dessas
#listas.

#Exemplo: Se a função receber as listas [1,4,3] e [3,5,1], então a função deve
#retornar [1x3, 4x5, 3x1] = [3, 20, 3].

def multiplica_listas(l1, l2):
    multiplica_listas = 0
    l3 = []
    for indice in range(len(l1)):
        multiplica_listas = l1[indice] * l2[indice]
        l3.append(multiplica_listas)
        
    return l3

lista1 = [1, 4, 3]
lista2 = [3, 5, 1]
#lista3 = []

lista3 = multiplica_listas(lista1, lista2)
print(lista3)
