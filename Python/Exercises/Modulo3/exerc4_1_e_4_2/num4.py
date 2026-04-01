class Numero_de_4_Digitos:

    def __init__(self):
        self.numero = 0

    def ler_dados(self):
        self.numero = int(input("Digite um número de 4 dígitos: "))

    def tem_4_digitos(self):
        return 999< self.numero < 10000
        # return self.numero > 999 and self.numero < 10000
        
    def atende_a_propriedade(self):
#        8833  --> parte 1: 88   parte 2 : 33
        parte1 = self.numero // 100  # // --> retorna quociente de divisão inteira
        parte2 = self.numero % 100   # % --> calcula resto de divisão inteira

        novo_numero = parte1*parte1 + parte2*parte2

        if novo_numero == self.numero:
            return True
        else:
            return False
        
        #   return novo_numero == self.numero