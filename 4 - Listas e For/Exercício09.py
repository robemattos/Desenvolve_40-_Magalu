# Exercício 9

# Pegue a lista gerada no exercício anterior e transforme cada um dos itens
# dessa lista em um float.

# OBS: Não é para alterar o programa anterior, mas sim a lista gerada por ele.

contador = 0
lista_numeros = []

while contador < 5:
    numero = input(f"Digite o {contador+1}o. número: ")
    lista_numeros.append(numero)
    contador += 1

print("\n")

lista_float = [float(item) for item in lista_numeros]
print(lista_float)