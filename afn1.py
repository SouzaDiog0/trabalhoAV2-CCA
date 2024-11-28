#Construir um AFN que aceite strings sobre o alfabeto {0, 1} que contenham a sequência '01' ou '10'

class AFN01ou10:
    def __init__(self):
        self.estado_inicial = 'q0'
        self.estados_aceitacao = {'q2', 'q4'}
        self.estado_atual = {self.estado_inicial}

    def transicao(self, char):
        novos_estados = set()
        for estado in self.estado_atual:
            if estado == 'q0':
                if char == '0':
                    novos_estados.add('q1')
                elif char == '1':
                    novos_estados.add('q3')
            elif estado == 'q1' and char == '1':
                novos_estados.add('q2')
            elif estado == 'q3' and char == '0':
                novos_estados.add('q4')
            # Preservar estados de aceitação
            if estado in self.estados_aceitacao:
                novos_estados.add(estado)
        self.estado_atual = novos_estados

    def reconhece(self, string):
        self.estado_atual = {self.estado_inicial}
        for char in string:
            self.transicao(char)
        return any(estado in self.estados_aceitacao for estado in self.estado_atual)


# Teste
afn = AFN01ou10()
strings = ["0110", "1001", "000", "11", "01", "10"]
for string in strings:
    print(f"A string '{string}' e aceita? {afn.reconhece(string)}")
