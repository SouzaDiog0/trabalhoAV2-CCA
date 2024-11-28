def comparar_palavras(a, b):
    fita_a = list(a)
    fita_b = list(b)

    for char_a, char_b in zip(fita_a, fita_b):
        if char_a < char_b:
            return b
        elif char_a > char_b:
            return a

    if len(fita_a) < len(fita_b):
        return b
    elif len(fita_a) > len(fita_b):
        return a

    return "iguais"


entrada_a = "apple"
entrada_b = "banana"
print(f"Entrada: {entrada_a}, {entrada_b}")
print(f"Maior lexicograficamente: {comparar_palavras(entrada_a, entrada_b)}") 