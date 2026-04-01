class Somatoria:

    def __init__(self):
        self._soma = 0.0                  # totalizador
        self._quantos_foram_somados = 0   # contador

    def somar(self, valor_a_somar : float):
        self._soma = self._soma + valor_a_somar
        self._quantos_foram_somados += 1

    @property   # para get --> obter o valor do atributo
    def valor(self) -> float:
        return self._soma
    
    @property
    def quantos(self) -> int:
        return self._quantos_foram_somados
    
    def media_aritmetica(self):
        if self._quantos_foram_somados == 0:
            raise Exception("Divisão por zero!")  # fluxo retorna
        
        # o fluxo somente vem para esse comando se _quantos_... != 0
        # nesse caso, a divisão pode ser feita sem erros
        return self._soma / self._quantos_foram_somados
    
    
