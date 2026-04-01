class Mdc:
    def __init__(self, factor1 : int, factor2 : int):

        self._factor1 = factor1
        self._factor2 = factor2
        self._mdc = 1
    
    def calculation(self):
            
        if(self.factor1 <0 | self.factor2 < 0):
            raise Exception('Os fatores não podem ser Negativos!\n')
        
        while self._factor1 != self._factor2:

            if self.factor1 > self.factor2:
                self.factor1 -= self._factor2

            elif self._factor1 < self._factor2:
                self._factor2 -= self._factor1

        self._mdc = self._factor2               #Qualquer um dos fatores seria valido, dado que self._factor1 = self._factor2 se verifica
        
        @property
        def factor1(self):
            return self._factor1
        
        @property
        def factor2(self):
            return self._factor2
        

    


