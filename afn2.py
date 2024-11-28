#Desenvolver um AFN que aceite strings sobre o alfabeto {a, b} que comecem com 'a' e terminem com 'b'

class AFNStartAEndB:
    def __init__(self):
        self.estado_inicial = 'q0'
        self.estados_aceitacao = {'q2'}
        self.estado_atual = {self.estado_inicial}

    def transicao(self, char):
        novos_estados = set()
        for estado in self.estado_atual:
            if estado == 'q0' and char == 'a':  # Começa com 'a'
                novos_estados.add('q1')
            elif estado == 'q1':
                if char == 'b':  # Termina com 'b'
                    novos_estados.add('q2')
                else:  # Continua no estado intermediário
                    novos_estados.add('q1')
            elif estado == 'q2':  # Mantém o estado de aceitação
                if char == 'b':  # Continua aceitando enquanto termina com 'b'
                    novos_estados.add('q2')
        self.estado_atual = novos_estados

    def reconhece(self, string):
        self.estado_atual = {self.estado_inicial}
        for char in string:
            self.transicao(char)
        return any(estado in self.estados_aceitacao for estado in self.estado_atual)


# Teste
afn = AFNStartAEndB()
strings = ["ab", "aabb", "baba", "b", "a", "bb"]
for string in strings:
    print(f"A string '{string}' e aceita? {afn.reconhece(string)}")
