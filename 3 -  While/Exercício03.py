
'''
Exercício 3
Peça ao usuário para digitar um número N e some todos os números de 1 a N
utilizando o laço de repetição while.
'''

n = int(input("Digite um número inteiro: "))
contador = 1
resultado = 0
soma = 0

while contador < n:
    soma = contador + (contador + 1)
    resultado = resultado + soma
    print(f"{contador} + {contador + 1} = {soma}")
    contador += 1

print(f"Resultado final: {resultado}")

