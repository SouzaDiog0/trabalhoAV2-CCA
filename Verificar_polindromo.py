def verificar_palindromo(palavra):
    fita = list(palavra)
    head_esq = 0
    head_dir = len(fita) - 1

    while head_esq < head_dir:
        if fita[head_esq] != fita[head_dir]:
            return "N�o"
        head_esq += 1
        head_dir -= 1

    return "Sim"


entrada = "radar"
print(f"Entrada: {entrada}")
print(f"� pal�ndromo? {verificar_palindromo(entrada)}")