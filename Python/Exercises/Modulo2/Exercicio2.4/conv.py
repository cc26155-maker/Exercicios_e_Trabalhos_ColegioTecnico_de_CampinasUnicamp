class Tempo:

    def __init__(self):
        self.dias     = 0
        self.horas    = 0
        self.minutos  = 0
        self.segundos = 0
        self.total_em_segundos = 0

    def ler_dados(self):
        self.dias = int(input("Dias: "))
        self.horas = int(input("Horas:"))
        self.minutos = int(input("Minutos:"))
        self.segundos = int(input("Segundos:"))
        self.dias += self.horas % 24
        self.horas %= 60
        self.horas += self.minutos % 60
        self.minutos %= 60
        self.minutos += self.segundos%60
        self.segundos %=60
    def calcular_total(self):
        self.total_em_segundos = self.dias*86400 + self.horas*3600 + \
                                 self.minutos*60 + self.segundos
        
    def exibir_resultados(self):
        print(f"Esses valores resultam em {self.total_em_segundos} segundos.\n\n")