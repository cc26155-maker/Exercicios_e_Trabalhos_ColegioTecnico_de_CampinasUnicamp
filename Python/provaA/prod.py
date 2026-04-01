import math

class Produtorio:
    def __init__(self):
        self._produto = 1
        self._quantosMultiplicados = 0

    def multiplicar(self, valor_a_multiplicar):
        self._produto *= valor_a_multiplicar
        self._quantosMultiplicados += 1


    def mediaGeometrica(self) ->float:
        if self._quantosMultiplicados < 0:
            raise ValueError("Impossível calcular média geométrica.")
        return math.pow(self._produto,
                        1.0/self._quantosMultiplicados)

    def taxa_geometrica_media(self) -> float:
        result = math.exp(math.log(self._produto)/self._quantosMultiplicados)
        return result

    def reset(self):
        self._produto = 1
        self._quantosMultiplicados = 0

    def produto_normalizado(self):
        return self._produto / self._quantosMultiplicados
    
    def multiplicar_ignorando_zero(self, valor_a_multiplicar : float) -> float:
        if valor_a_multiplicar != 0:
            self._produto *= valor_a_multiplicar
            self._quantosMultiplicados += 1
            
        



    @property
    def valor(self):
        return self._produto


    @property
    def quantos(self):
        return self._quantosMultiplicados
