from typing import Callable 

class Somatorio:
    def __init__(self, liminf: int, limsup: int, funcao:Callable[[int], int]):
        self._lim_inf = liminf
        self._lim_sup = limsup
        self._function = funcao
        self._numbers = []
        self._soma = 0
        self._total = 0
    def somar(self):
        
        if self._lim_inf <= self._lim_sup:
            
            self._numbers = []
            
            for i in range(self._lim_inf, self._lim_sup + 1):
                self._numbers.append(self._function(i))
            
        else:
            raise Exception("Limite inferior maior que o limite superior")


    
    def calcular(self): 
        self._total= sum(self._numbers) 
        return self._total

    @property
    def total(self):
        return self._total
    
    
    @property
    def numbers(self):
        return self._numbers
    
    
    def __str__(self):
        return(f"\t\t\nO somatorio de {self._function} variando de {self._lim_inf} até {self._lim_sup} é {self._numbers}, com a soma resultante sendo: {self.total}\n")
    
        
            