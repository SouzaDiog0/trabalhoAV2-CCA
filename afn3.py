#Construir um AFN que aceite strings sobre o alfabeto {a, b} que contenham 'aaa' como subsequência

class AFNaaa:
    def __init__(self):
        self.estado_inicial = 'q0'
        self.estados_aceitacao = {'q3'}
        self.estado_atual = {self.estado_inicial}

    def transicao(self, char):
        novos_estados = set()
        for estado in self.estado_atual:
            if estado == 'q0' and char == 'a':
                novos_estados.add('q1')
            elif estado == 'q1' and char == 'a':
                novos_estados.add('q2')
            elif estado == 'q2' and char == 'a':
                novos_estados.add('q3')
            elif estado in {'q0', 'q1', 'q2'} and char == 'b':
                novos_estados.add(estado)
        self.estado_atual = novos_estados

    def reconhece(self, string):
        self.estado_atual = {self.estado_inicial}
        for char in string:
            self.transicao(char)
        return any(estado in self.estados_aceitacao for estado in self.estado_atual)


# Teste
afn = AFNaaa()
strings = ["aaa", "baaa", "bbaaa", "aa", "aab", "abab"]
for string in strings:
    print(f"A string '{string}' e aceita? {afn.reconhece(string)}")