#Exercício 14
#Faça uma função que recebe uma lista de números e retorna a média
#aritmética dos elementos dessa lista.

def media_aritmetica(lista_num):
    media = sum(lista_num) / len(lista_num)
    
    return media

lista = []
media_num = 0
numero = 0
soma_num = 0

qtd_num = int(input("Informe a quantidade de números para a média: "))

for indice in range(qtd_num):
    numero = int(input(f"Entre com o {indice+1}o.: "))
    lista.append(numero)

soma_num = sum(lista)
media_num = media_aritmetica(lista)

print("\n")
print(f"A soma dos números é: {soma_num}\n")
print(f"A média dos {qtd_num} números é: {media_num:.2f}")