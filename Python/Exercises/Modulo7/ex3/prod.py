class Produtorio:
    def __init__(self):
        self._prod = 1.0
        self._quantos = 0.0
    def calcular(self, value):
        self._prod = value * self._prod
        self._quantos +=1
    
    @property
    def valor(self):
        return self._prod
    @property
    def termos(self):
        return self._quantos