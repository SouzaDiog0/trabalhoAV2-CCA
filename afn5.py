#Criar um autômato finito não determinístico (AFN) que aceite strings sobre o alfabeto {0, 1} onde a sequência "101" aparece pelo menos uma vez.

class AFNSequencia101:
    def __init__(self):
        self.estado_inicial = 'q0'  # Estado inicial
        self.estados_aceitacao = {'q3'}  
        self.estado_atual = {self.estado_inicial}  # Conjunto de estados atuais

    def transicao(self, char):
        novos_estados = set()
        for estado in self.estado_atual:
            if estado == 'q0':  # Inicial, esperando o início da sequência
                if char == '1':
                    novos_estados.add('q1')  # Primeiro '1'
                # Se char == '0', permanece em q0, já que '0' não pode iniciar a sequência "101"
                novos_estados.add('q0')  

            elif estado == 'q1':  # Já leu "1", esperando o próximo '0'
                if char == '0':
                    novos_estados.add('q2') #"10" foi lido
                elif char == '1':
                    novos_estados.add('q1') #Se '1' for lido, permanece em q1 (não completou a sequência "101")

            elif estado == 'q2': #Já leu "10", esperando o próximo '1'
                if char == '1':
                    novos_estados.add('q3')  #"101" foi lido, aceita a string

            elif estado == 'q3':  #Já leu "101", permanece aceitando qualquer coisa
                novos_estados.add('q3')  # Permanece em q3, aceitando qualquer sequência após "101"
        
        self.estado_atual = novos_estados

    def reconhece(self, string):
        self.estado_atual = {self.estado_inicial}  # Reinicia para cada string
        for char in string:
            self.transicao(char)
        
        return any(estado in self.estados_aceitacao for estado in self.estado_atual)


# Teste
afn = AFNSequencia101()
strings = ['101', '1101', '1001', '111', '10101', '000101']
for string in strings:
    resultado = afn.reconhece(string)
    print(f"A string '{string}' e aceita? {resultado}")
