#Criar um AFN que aceite strings sobre o alfabeto {a, b} onde a quantidade de 'a's seja ímpar e a quantidade de 'b's seja par.

class AFNParidade:
    def __init__(self):
        self.estado_inicial = 'q0'  # Estado inicial
        self.estados_aceitacao = {'q1', 'q3'}  
        self.estado_atual = {self.estado_inicial}  # Estado atual

    def transicao(self, char):
        novos_estados = set()
        for estado in self.estado_atual:
            if estado == 'q0':  # Não foi lido nenhum caractere ainda
                if char == 'a':
                    novos_estados.add('q1')  # 1 'a', ímpar
                elif char == 'b':
                    novos_estados.add('q2')  # 1 'b', par
            elif estado == 'q1':  # Já temos 1 'a' (ímpar) e um número par de 'b's
                if char == 'a':
                    novos_estados.add('q0')  # Volta a ter quantidade par de 'a'
                elif char == 'b':
                    novos_estados.add('q3')  # 1 'a' (ímpar) e 2 'b's (par)
            elif estado == 'q2':  # Já temos 0 'a' (par) e 1 'b' (ímpar)
                if char == 'a':
                    novos_estados.add('q3')  # 1 'a' (ímpar) e 2 'b's (par)
                elif char == 'b':
                    novos_estados.add('q2')  # 0 'a' (par) e 2 'b's (par)
            elif estado == 'q3':  # Já temos 1 'a' (ímpar) e 2 'b's (par)
                if char == 'a':
                    novos_estados.add('q2')  # 0 'a' (par) e 2 'b's (par)
                elif char == 'b':
                    novos_estados.add('q1')  # 1 'a' (ímpar) e 3 'b's (ímpar)

        self.estado_atual = novos_estados

    def reconhece(self, string):
        self.estado_atual = {self.estado_inicial}  # Reinicia para cada string
        for char in string:
            self.transicao(char)
        return any(estado in self.estados_aceitacao for estado in self.estado_atual)


# Teste
afn = AFNParidade()
strings = ["abb", "aabb", "aabbb", "a", "bbb", "aaa"]

for string in strings:
    resultado = afn.reconhece(string)
    print(f"A string '{string}' e aceita? {resultado}")
