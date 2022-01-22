peso = float(input("Informe o seu peso: "))
alt = float(input("Informe a sua altura: "))

imc = peso * (alt**2)

print(f"O seu IMC é: {imc:.2f}")