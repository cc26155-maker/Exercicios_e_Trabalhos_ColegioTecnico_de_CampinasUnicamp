class Produtorio:
    def __init__(self):
        self._product = 1       #Começa em 1 como elemento neutro da multiplicação
        self._factor = 0        #Quantidade de fatores sendo multiplicados

    def calculate(self, new_factor):
        self._factor += 1
        self._product*= new_factor
    
    @property
    def factor(self):
        return self._factor
    
    @property
    def product(self):
        return self._product
    