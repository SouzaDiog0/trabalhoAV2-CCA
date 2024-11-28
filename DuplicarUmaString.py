def duplicar_string(string):
    fita = list(string) + [' '] * len(string)  
    head = len(fita) // 2  

    for char in string:
        fita[head] = char  
        head += 1

    return ''.join(fita).strip()


entrada = "abc"
print(f"Entrada: {entrada}")
print(f"Saída: {duplicar_string(entrada)}") 