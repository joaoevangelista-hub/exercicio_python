idade = int(input("Digite a sua idade:  "))

if idade < 16:
    print("Não pode votar")

elif idade == 16 or idade == 17:
    print("Voto opcional")

elif idade == 18 or idade <= 69:
    print("Voto obrigatório")

else:
    print("Voto opcional")