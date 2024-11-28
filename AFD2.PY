# Implemente um AFD que reconheça palavras que terminem com a sequência "aaa". O alfabeto utilizado deve ser 'a' e 'b'. Sua solução deve aceitar palavras que terminem exatamente com "aaa".

class AFD:
    def __init__(self):
        self.states = {'q0', 'q1', 'q2', 'q3'}
        self.alphabet = {'a', 'b'}
        self.start_state = 'q0'
        self.accept_states = {'q3'}
        self.transitions = {
            ('q0', 'a'): 'q1',
            ('q0', 'b'): 'q0',
            ('q1', 'a'): 'q2',
            ('q1', 'b'): 'q0',
            ('q2', 'a'): 'q3',
            ('q2', 'b'): 'q0',
            ('q3', 'a'): 'q3',
            ('q3', 'b'): 'q0',
        }

    def process(self, word):
        current_state = self.start_state

        for symbol in word:
            if symbol not in self.alphabet:
                raise ValueError(f"Símbolo inválido: {symbol}")

            current_state = self.transitions.get((current_state, symbol), None)
            if current_state is None:
                raise ValueError(f"Transição indefinida para o estado {current_state} com símbolo {symbol}")

        return current_state in self.accept_states

if __name__ == "__main__":
    afd = AFD()

    palavras = ["aaa", "baaa", "bbaaa", "aaaa", "a", "abaaa", "bb"]
    for palavra in palavras:
        if afd.process(palavra):
            print(f"A palavra '{palavra}' é aceita.")
        else:
            print(f"A palavra '{palavra}' não é aceita.")

