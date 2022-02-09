import json
import os.path
import sys

def obter_dados():
    '''
    Essa função carrega os dados dos produtos e retorna uma lista de dicionários, onde cada dicionário representa um produto.
    NÃO MODIFIQUE essa função.
    '''
    with open(os.path.join(sys.path[0], 'dados.json'), 'r') as arq:
        dados = json.loads(arq.read())
    return dados

def listar_categorias(dados):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá retornar uma lista contendo todas as categorias dos diferentes produtos.
    Cuidado para não retornar categorias repetidas.    
    '''
    ...
    
    lista_categorias = []
    lista_dados = dados[:]
    for categ in lista_dados:
        if categ["categoria"] not in lista_categorias:
            lista_categorias.append(categ["categoria"])

    return [print(categ) for categ in lista_categorias]    

def listar_por_categoria(dados, categoria):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    O parâmetro "categoria" é uma string contendo o nome de uma categoria.
    Essa função deverá retornar uma lista contendo todos os produtos pertencentes à categoria dada.
    '''
    ...
    
    lista_categoria = []
    lista_dados = dados[:]
    for categ in lista_dados:
        if categ["categoria"] == categoria:
                lista_categoria.append(categ)

    return [print(categ) for categ in lista_categoria]
    

def produto_mais_caro(dados, categoria):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    O parâmetro "categoria" é uma string contendo o nome de uma categoria.
    Essa função deverá retornar um dicionário representando o produto mais caro da categoria dada.
    '''
    ...

    lista_categoria = []
    lista_dados = dados[:]
    maior_preco = []
    
    for categ in lista_dados:
        if categ["categoria"] == categoria:
            lista_categoria.append(categ)

    for lista_auxiliar in lista_categoria:
        if maior_preco == []:
            maior_preco = lista_auxiliar
        else:
            if float(maior_preco["preco"]) < float(lista_auxiliar["preco"]):
                maior_preco = lista_auxiliar
    
    return print(maior_preco)

def produto_mais_barato(dados, categoria):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    O parâmetro "categoria" é uma string contendo o nome de uma categoria.
    Essa função deverá retornar um dicionário representando o produto mais caro da categoria dada.
    '''
    ...

    lista_categoria = []
    menor_preco = []

    for categ in dados:
        if categ["categoria"] == categoria:
            lista_categoria.append(categ)

    for lista_auxiliar in lista_categoria:
        if menor_preco == []:
            menor_preco = lista_auxiliar
        else:
            if float(menor_preco["preco"]) > float(lista_auxiliar["preco"]):
                menor_preco = lista_auxiliar
    
    return print(menor_preco)

def top_10_caros(dados):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá retornar uma lista de dicionários representando os 10 produtos mais caros.
    '''
    ...

    lista_produtos = dados[:]
    lista_auxiliar = []
    lista_10_mais = []
    contador = 0
    indice = 0
    
    while contador < 10:
        lista_auxiliar = []
        for produto in lista_produtos:
            if lista_auxiliar == []:
                lista_auxiliar = produto
            else:
                if float(lista_auxiliar["preco"]) < float(produto["preco"]):
                    lista_auxiliar = produto
                    indice = lista_produtos.index(produto)
        lista_10_mais.append(lista_produtos[indice])
        lista_produtos.pop(indice)
        contador += 1
    
    return [print(mais_caros) for mais_caros in lista_10_mais]

def top_10_baratos(dados):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá retornar uma lista de dicionários representando os 10 produtos mais caros.
    '''
    ...

    lista_produtos = dados[:] # A lista produtos recebe uma cópia dos dados originais
    lista_auxiliar = [] # A lista auxiliar será manipulada para chegarmos ao resultado desejado
    lista_10_menos = [] # Essa lista guardará os 10 produtos mais baratos
    contador = 0 # Essa variável fará o controle do loop que pegará os 10 produtos mais baratos
    indice = 0 # Essa variável guardará o índice do dicionário com o produto mais ddcaro que será excluído

    while contador < 10:
        lista_auxiliar = []
        for produto in lista_produtos:
            if lista_auxiliar == []:
                lista_auxiliar = produto
            else:
                if float(lista_auxiliar["preco"]) > float(produto["preco"]):
                    lista_auxiliar = produto
                    indice = lista_produtos.index(produto)
        lista_10_menos.append(lista_produtos[indice])
        lista_produtos.pop(indice)
        contador += 1
    
    return [print(mais_baratos) for mais_baratos in lista_10_menos]

def menu(dados):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá, em loop, realizar as seguintes ações:
    - Exibir as seguintes opções:
        1. Listar categorias
        2. Listar produtos de uma categoria
        3. Produto mais caro por categoria
        4. Produto mais barato por categoria
        5. Top 10 produtos mais caros
        6. Top 10 produtos mais baratos
        0. Sair
    - Ler a opção do usuário.
    - No caso de opção inválida, imprima uma mensagem de erro.
    - No caso das opções 2, 3 ou 4, pedir para o usuário digitar a categoria desejada.
    - Chamar a função adequada para tratar o pedido do usuário e salvar seu retorno.
    - Imprimir o retorno salvo. 
    O loop encerra quando a opção do usuário for 0.
    '''
    ...

    mensagem = print("1 - Listar Categorias: \n2 - Listar produtos de uma categoria\n3 - Produto mais caro por categoria\n4 - Produto mais barato por categoria\n5 - Top 10 produtos mais caros\n6 - Top 10 produtos mais baratos\n0 - Sair\n")
    opcao = input(mensagem)
    verifica = ""

    while opcao != "0":
        if opcao == "1":
            listar_categorias(dados)
        elif opcao == "2":
            sub_opcao = input("Digite a categoria: ")
            listar_por_categoria(dados, sub_opcao)
        elif opcao == "3":
            sub_opcao = input("Digite a categoria: ")
            produto_mais_caro(dados, sub_opcao)
        elif opcao == "4":
            sub_opcao = input("Digite a categoria: ")
            produto_mais_barato(dados, sub_opcao)
        elif opcao == "5":
            top_10_caros(dados)
        elif opcao == "6":
            top_10_baratos(dados)
        else:
            print("Opção inválida! Tente novamente.")
        
        mensagem = print("\n1 - Listar Categorias: \n2 - Listar produtos de uma categoria\n3 - Produto mais caro por categoria\n4 - Produto mais barato por categoria\n5 - Top 10 produtos mais caros\n6 - Top 10 produtos mais baratos\n0 - Sair\n")
        opcao = input(mensagem)


# Programa Principal - não modificar!
d = obter_dados()
menu(d)
