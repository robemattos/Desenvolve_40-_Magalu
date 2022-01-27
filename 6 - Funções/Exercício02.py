# Exercício 2
# Faça uma função que recebe o valor do raio de um círculo e retorna
# o valor do comprimento de sua circunferência: C = 2*pi*r.

def circunferencia(raio):
    comp_circunf = 0
    pi = 3.14
    comp_circunf = 2 * pi * raio
    
    return comp_circunf

valor_raio = float(input("Digite o valor do raio: "))
circunf = circunferencia(valor_raio)
print(circunf)
