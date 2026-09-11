def soma_imposto(taxa_imposto: float, custo: float) -> float:

    imposto = custo * (taxa_imposto / 100)
    return custo + imposto



custo_produto = float(input("Digite o custo do produto (R$): "))
taxa = float(input("Digite a taxa de imposto (%): "))


valor_final = soma_imposto(taxa, custo_produto)


print(f"O valor final do produto com imposto é: R$ {valor_final:.2f}")