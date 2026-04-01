import math as mt

class Flow:
    def __init__(self, desafio, recomp, compr):
        self._indiceflow = 0.0
        self._tensao = 0.0
        self._desafio = desafio
        self._recompensa = recomp
        self._engajamento = 0.0
        self._comprimento = compr
        self._monotono = False
        self._punitivo = False
        self._flowmode = False
        self._flowajustado = 0.0



    def calcular_tudo(self):
        """Executa toda a cadeia de lógica estatística."""
        if self._comprimento <= 0 or self._desafio <= 0 or self._recompensa <=0:
            raise ZeroDivisionError("O comprimento do jogo deve ser maior que 0.")
        
        
        self._tensao = abs(self._desafio - self._recompensa)
        
        self._indiceflow = (self._recompensa * (100 - abs(self._desafio - 50))) / self._comprimento

        if self._recompensa > 0:
            self._engajamento = self._desafio / self._recompensa
        else:
            self._engajamento = self._desafio 

        # Classificação Estatística
        self._punitivo = self._engajamento > 1.3
        self._monotono = self._engajamento <= 0.7
        self._flowmode = 0.7 < self._engajamento <= 1.3

        media_base = (self._desafio + self._recompensa) / 2
        fator_fadiga = (1 - (self._comprimento / 200))
        self._flowajustado = media_base * max(0, fator_fadiga)
        

    def flowAjustado(self):
        self._flowajustado = ((self._desafio + self._recompensa)/2) * (1 / mt.log10(self._comprimento + 10))
        return self._flowajustado
    
    

    # Getters
    @property
    def status_formatado(self):
        if self._punitivo: return "Crítico: Punitivo (Ansiedade)"
        if self._monotono: return "Crítico: Monótono (Tédio)"
        return "Ideal: Zona de Flow"


    @property
    def flowajustado(self): return self._flowajustado

    @property
    def flowmode(self): return self._flowmode

    @property
    def floawajustado(self) -> float:
        return self._flowajustado

    @property
    def engajamento(self) -> bool:
        return self._engajamento
    
    @property 
    def flowmode(self) -> bool:
        return self._flowmode
    
    @property 
    def monotono(self) -> bool:
        return self._monotono
    
    @property
    def punitivo(self):
        return self._punitivo
    
    @property
    def indiceflow(self):
        return self._indiceflow
    @property
    def tensao(self):
        return self._tensao
