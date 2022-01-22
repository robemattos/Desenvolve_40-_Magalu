# Exercício 2
# Imprima as chaves seguidas dos seus valores para dicionário criado no
# exercício anterior.

ano = {"janeiro" : "31",
"fevereiro" :"28",
"março" : "31",
"abril" : "30",
"maio" : "31",
"junho" : "30",
"julho" : "31",
"agosto" : "31",
"setembro" : "30",
"outubro" : "31",
"novembro" : "30",
"dezembro" : "31"}



for meses in ano:
    print(meses,"-",ano[meses])