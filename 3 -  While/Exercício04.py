#Exercício 4
#Faça um programa que imprima a tabuada do 9 (de 9*1 a 9*10) usando loops.

multiplicador = int(input("Digite o multiplicador: "))
resultado = 0

for multiplicando in range(1,11):
    resultado = multiplicador * multiplicando
    print(f"{multiplicador} X {multiplicando} = {resultado}")
