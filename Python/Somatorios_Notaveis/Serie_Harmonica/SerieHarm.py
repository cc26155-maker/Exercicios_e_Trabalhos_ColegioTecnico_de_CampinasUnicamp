from somatorio import Somatorio as som


class Harmonica:

    def __init__(self, down, up):
        self._up = up
        self._down = down
        self._soma = som(down, up, lambda i: 1/i**2)
        self._calculo = 0


    def func(self):
        self._soma.somar()
        self._calculo = self._soma.calcular()


    @property
    def down(self):
        return self._down
    

    @property 
    def up(self):
        return self._up
    

    @property
    def soma(self):
        return self._soma
    

    def __str__(self):
        txt = f"O somatório de 1/i para i variando de {self._down} até {self._up} é {self._calculo}"
        return txt