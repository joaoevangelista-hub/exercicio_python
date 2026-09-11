def calcular_media(lista_de_numeros):
    total = sum(lista_de_numeros)
    quantidade = len(lista_de_numeros)

    if quantidade == 0:
        return 0

    media = total / quantidade
    return media 

aluno1 = [6.5, 7.0, 8.0, 9.5, 9.5]
mediaaluno1 = calcular_media(aluno1)

print("A média é:", mediaaluno1)
