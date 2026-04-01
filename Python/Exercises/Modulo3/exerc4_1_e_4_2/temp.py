class Temp_Agua:

    def __init__(self):
        self.temp_agua = 0.0 # declarar atributo da classe

    def ler_dados(self):
        self.temp_agua = float(input("Qual a temperatura da água? "))

    def exibir_estado_da_agua(self):
        if self.temp_agua < 0.0:
            print("Congelada!")
        elif self.temp_agua < 100.0:
            print("Líquida!")
        else:
            print("Gasosa (vapor)!")