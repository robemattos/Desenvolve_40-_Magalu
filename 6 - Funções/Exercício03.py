# Exercício 3
# Faça uma função para cada operação matemática básica
# (soma, subtração, multiplicação e divisão). 
# As funções devem receber dois números e retornar o resultado da operação.

def soma(a,b):
    resultado = a + b
    return resultado

def subtrai(a,b):
    resultado = a - b
    return resultado

def multiplica(a,b):
    resultado = a * b
    return resultado

def divide(a,b):
    resultado = a / b
    return resultado

num1 = float(input("Entre com o primeiro número: "))
num2 = float(input("Entre com o primeiro número: "))

result = soma(num1, num2)
print(result)
result = subtrai(num1, num2)
print(result)
result = multiplica(num1, num2)
print(result)
result = divide(num1, num2)
print(result)
