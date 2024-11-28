def contar_pares_impares(sequencia):
    numeros = list(map(int, sequencia.split(','))) 
    pares = sum(1 for num in numeros if num % 2 == 0)
    impares = len(numeros) - pares
    return pares, impares


entrada = "2,3,5,8,10,7"
pares, impares = contar_pares_impares(entrada)
print(f"Entrada: {entrada}")
print(f"Pares: {pares}, Ímpares: {impares}")  