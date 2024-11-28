# Implemente um AFD que reconheça palavras que terminem com a sequência "ba". Considere que o alfabeto é composto pelos símbolos 'a' e 'b'. Sua solução deve ser capaz de identificar palavras que terminem exatamente com "ba" e rejeitar as demais.

class AFD:
    def __init__(self):
        self.states = {'q0', 'q1', 'q2'}
        self.alphabet = {'a', 'b'}
        self.start_state = 'q0'
        self.accept_states = {'q2'}
        self.transitions = {
            ('q0', 'a'): 'q0',
            ('q0', 'b'): 'q1',
            ('q1', 'a'): 'q2',
            ('q1', 'b'): 'q0',
            ('q2', 'a'): 'q0',
            ('q2', 'b'): 'q1',
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

    palavras = ["ba", "bba", "abba", "abab", "aaaa", "baab", "b"]
    for palavra in palavras:
        if afd.process(palavra):
            print(f"A palavra '{palavra}' é aceita.")
        else:
            print(f"A palavra '{palavra}' não é aceita.")

