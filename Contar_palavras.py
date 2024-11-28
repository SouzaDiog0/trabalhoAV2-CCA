def contar_palavras(frase):
    fita = list(frase) + [' ']  
    palavras = 0
    dentro_palavra = False

    for char in fita:
        if char != ' ' and not dentro_palavra:
            palavras += 1
            dentro_palavra = True
        elif char == ' ':
            dentro_palavra = False

    return palavras


entrada = "O curso do professor ricardo de ciencia de dados e inteligencia artificial e muito bom" 
print(f"Entrada: {entrada}")
print(f"Número de palavras: {contar_palavras(entrada)}") 