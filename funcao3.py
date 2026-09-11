def valida_string(texto: str, minimo: int = 1, maximo: int = 100):
    return minimo <= len(texto) <= maximo

print(valida_string("Python"))  # Retorna True (tamanho 6)
print(valida_string(""))  # Retorna False (tamanho 0)