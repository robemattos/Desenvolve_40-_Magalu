numero1 = int(input("Informe um número inteiro: "))
numero2 = int(input("Informe outro número inteiro: "))
numero3 = float(input("Informe um número real: "))

op1 = (numero1 * 2) + (numero2 / 2)
op2 = (numero1 * 3) + numero3
op3 = numero3**3

print(f"O produto do dobro do primeiro com a metade do segundo é {op1:.2f}")
print(f"A soma do triplo do primeiro com o terceiro é {op2:.2f}")
print(f"O terceiro elevado ao cubo é {op3:.2f}")