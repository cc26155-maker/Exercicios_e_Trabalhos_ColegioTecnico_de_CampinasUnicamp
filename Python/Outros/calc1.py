import os   # import traz o pacote indicado (os) para uso na classe
            # os é o pacote de funções prontas que permite ao python
            # executar comandos de linha de comando do sistema operacional
import time
import subprocess

class Calculadora:
    # toda classe deve ter um método __init__()
    # onde seus atributos (variáveis membro) são
    # declarados

    # método padrão de toda classe que instancia um objeto dessa classe
    def __init__(self):
        self.pri_numero = 0.0   # declara atributo (variável) pri_numero nesse objeto
        self.seg_numero = 0.0   # declara atributo (variável) seg_numero nesse objeto
        self.result     = 0.0   # declara atributo (variável) result nesse objeto

    def ligar(self):
        self.limpar_visor() 
        self.priNumero = 0.0 
        self.segNumero = 0.0
        print("\nCalculadora ligada!\n")

    def desligar(self):
        print("\nCalculadora desligada.\nAté breve!\n")

    def obter_numeros(self):
        # comando input lê um texto, e não valores numéricos
        # a variável dado_digitado receberá o que for digitado, mas
        # como um texto, que é o que o input lê.
        dado_digitado = input("Digite o primeiro valor (real): ")

        # converter para float (real do python) o texto digitado antes
        # e armazenamos no atributo self.pri_numero

        self.pri_numero = float(dado_digitado)

        self.seg_numero = float(input("Digite o segundo valor (real): "))

    def somar(self):
        self.result = self.pri_numero + self.seg_numero

    def exibir_resultado(self):
        print(f"\n{self.pri_numero} + {self.seg_numero} = {self.result}\n")

    def limpar_visor(self):
        #   os.system('cls') or None    --> modo antigo
        time.sleep(4)
        subprocess.run('cls', shell=True)   # modo recomendado para apagar a tela
    
        self.result = 0.0
def main():
    ...



if __name__== "__main__":
    try:
        main()
    except KeyboardInterrupt:
        raise TypeError("\nPrograma encerrado pelo usuario.\n")
        
