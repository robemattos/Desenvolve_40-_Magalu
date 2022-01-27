#Exercício 5

#Faça uma função que recebe um nome e um horário e imprime “Bom dia, [nome]”,
#caso seja antes de 12h, “Boa Tarde, [nome]”, caso seja entre 12h e 18h e
#“Boa noite, [nome]” se for após às 18h.

def nome_hora(nome, hora):
    if hora < "12:00h":
        print(f"Bom dia {nome}")
    elif hora > "12:00h" and hora < "18:00h":
        print(f"Boa tarde {nome}")
    else:
        print(f"Boa noite {nome}")

usuario = input("Digite o seu nome: ")
hora_usuario = input("Digite a hora (HH:MM): ")

nome_hora(usuario, hora_usuario)