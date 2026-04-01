class Somatorio:
    
    def __init__(self):
        self._soma = 0
        self._valores_somados = 0
    
    def calcular(self, valor_somar) -> int | float:
        self._valores_somados += 1
        self._soma = self._soma + valor_somar
    

    @property
    def somados(self):
        return self._valores_somados
    @property
    def valor(self):
        return self._soma